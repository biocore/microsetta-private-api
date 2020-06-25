import inspect
from collections import defaultdict


def build_param_map(func, param_names):
    sig = inspect.signature(func)
    params = sig.parameters

    desired_set = set(param_names)

    # Argh.  OrderedDict doesn't know how to find the indexes of its keys.
    output = {}
    idx = 0
    for key in params:
        if key in desired_set:
            output[key] = (idx, params[key].default)
        idx += 1
    return output


def bind_param_map(param_map, parameter_overrides, func_args, func_kwargs):
    output = defaultdict(None)
    for key in param_map:
        idx = param_map[key][0]
        default = param_map[key][1]
        if idx < len(func_args):
            output[key] = func_args[idx]
        else:
            output[key] = func_kwargs.get(key, default)

    # TODO: We only use this to set survey_template_id on vioscreen callback
    #  would we prefer defaults instead of overrides?
    for key in parameter_overrides:
        output[key] = parameter_overrides[key]
    return output
