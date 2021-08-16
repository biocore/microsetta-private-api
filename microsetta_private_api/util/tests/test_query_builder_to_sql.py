from microsetta_private_api.util.query_builder_to_sql import build_condition
import unittest
import json
from microsetta_private_api.repo.transaction import Transaction


class EmailTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parameterized_sql(self):
        query_builder_example = json.loads(
            """
            {
              "condition": "AND",
              "rules": [
                {
                  "id": "price",
                  "field": "price",
                  "type": "double",
                  "input": "number",
                  "operator": "less",
                  "value": 10.25
                },
                {
                  "condition": "OR",
                  "rules": [
                    {
                      "id": "category",
                      "field": "category",
                      "type": "integer",
                      "input": "select",
                      "operator": "equal",
                      "value": 2
                    },
                    {
                      "id": "category",
                      "field": "category",
                      "type": "integer",
                      "input": "select",
                      "operator": "equal",
                      "value": 1
                    }
                  ]
                }
              ],
              "valid": true
            }
            """)

        condition, params = build_condition(query_builder_example)
        with Transaction() as t:
            self.assertEqual(
                condition.as_string(t.cursor()),
                '"price" < %s and ("category" = %s or "category" = %s)'
            )
            self.assertListEqual(
                params,
                [10.25, 2, 1]
            )
            t.rollback()

    def test_many_groups(self):
        query_builder_example = json.loads(
            """
            {
              "condition": "AND",
              "rules": [
                {
                  "id": "price",
                  "field": "price",
                  "type": "double",
                  "input": "number",
                  "operator": "less",
                  "value": 10.25
                },
                {
                  "condition": "OR",
                  "rules": [
                    {
                      "id": "category",
                      "field": "category",
                      "type": "integer",
                      "input": "select",
                      "operator": "equal",
                      "value": 2
                    },
                    {
                      "id": "category",
                      "field": "category",
                      "type": "integer",
                      "input": "select",
                      "operator": "equal",
                      "value": 1
                    },
                    {
                      "condition": "AND",
                      "rules": [
                        {
                          "id": "name",
                          "field": "name",
                          "type": "string",
                          "input": "text",
                          "operator": "equal",
                          "value": "Foobar"
                        }
                      ]
                    },
                    {
                      "condition": "AND",
                      "rules": [
                        {
                          "id": "in_stock",
                          "field": "in_stock",
                          "type": "integer",
                          "input": "radio",
                          "operator": "equal",
                          "value": 1
                        },
                        {
                          "id": "category",
                          "field": "category",
                          "type": "integer",
                          "input": "select",
                          "operator": "equal",
                          "value": 1
                        }
                      ]
                    }
                  ]
                }
              ],
              "valid": true
            }
            """)

        condition, params = build_condition(query_builder_example)
        with Transaction() as t:
            self.assertEqual(
                condition.as_string(t.cursor()),
                '"price" < %s and ("category" = %s or "category" = %s or ("name" = %s) or ("in_stock" = %s and "category" = %s))'  # noqa
            )
            self.assertListEqual(
                params,
                [10.25, 2, 1, "Foobar", 1, 1]
            )
            t.rollback()

    def test_sql_injection(self):
        query_builder_example = json.loads(
            """
            {
              "condition": "AND",
              "rules": [
                {
                  "id": "1\\"=\\"1\\" or \\"name",
                  "field": "name",
                  "type": "string",
                  "input": "text",
                  "operator": "equal",
                  "value": "bobby\\" or 1=1\\"\\\\; DROP TABLES;"
                }
              ],
              "valid": true
            }
            """)

        condition, params = build_condition(query_builder_example)
        with Transaction() as t:
            self.assertEqual(
                condition.as_string(t.cursor()),
                '"1""=""1"" or ""name" = %s'
            )
            self.assertListEqual(
                params,
                ['bobby" or 1=1"\\; DROP TABLES;']
            )
            t.rollback()
