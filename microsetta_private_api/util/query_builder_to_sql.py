# Take model objects from the jquery query builder
# and convert them into escaped sql where clauses

from psycopg2 import sql
from microsetta_private_api.exceptions import RepoException

# If we ever implement remaining operators, be sure to
# check that parameterized arguments are generated in
# the correct order
supported_operators = {
    'equal': '=',
    'not_equal': '!=',
    # in,
    # not_in,
    'less': "<",
    'less_or_equal': "<=",
    'greater': ">",
    'greater_or_equal': ">=",
    # between,
    # not_between,
    # begins_with,
    # not_begins_with,
    # contains,
    # not_contains,
    # ends_with,
    # not_ends_with,
    # is_empty,
    # is_not_empty,
    'is_null': "is null",
    'is_not_null': "is not null",
}


def build_condition(top_level_obj):
    def build_condition_helper_group(root_obj, out_values, is_top_level=False):
        condition = root_obj['condition']
        rules = root_obj['rules']

        if condition == 'AND':
            join_str = " and "
        elif condition == 'OR':
            join_str = " or "
        else:
            raise RepoException("Unknown condition: " + str(condition))

        cond = sql.SQL(join_str)\
            .join([build_condition_helper(x, out_values) for x in rules])
        if not is_top_level:
            cond = sql.SQL('({cond})').format(cond=cond)
        return cond

    def build_condition_helper_rule(root_obj, out_values):
        id = root_obj['id']
        # field = root_obj['field']
        # type = root_obj['type']
        # input = root_obj['input']
        operator = root_obj['operator']
        value = root_obj['value']

        if operator not in supported_operators:
            raise RepoException("Unsupported query operator: " + str(operator))

        if operator in ["is_null", "is_not_null"]:
            cond = "{id}" + supported_operators[operator]
            # no need to append null to out_values
        else:
            cond = "{id} " + supported_operators[operator] + " {value}"
            out_values.append(value)

        return sql.SQL(cond).format(
            id=sql.Identifier(id),
            value=sql.Placeholder())

    def build_condition_helper(root_obj, out_values, is_top_level=False):
        if "condition" in root_obj:
            return build_condition_helper_group(
                root_obj,
                out_values,
                is_top_level=is_top_level)
        else:
            return build_condition_helper_rule(root_obj, out_values)

    valid = top_level_obj['valid']

    if not valid:
        raise RepoException("Query is invalid")

    out_values = []

    return build_condition_helper(
        top_level_obj,
        out_values,
        is_top_level=True), out_values
