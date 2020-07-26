import unittest

from parameterized import parameterized
from hermesql.clickhouse.type_conversion import ToFixedString

from hermesql import Field
from hermesql.clickhouse.nullable_arg import IfNull


class TestSearchString(unittest.TestCase):
    @parameterized.expand(
        [
            (IfNull(Field("name"), Field("login")), "ifNull(name,login)",),
            (
                IfNull(Field("builder"), ToFixedString("hermesql", 100)),
                "ifNull(builder,toFixedString('hermesql',100))",
            ),
        ]
    )
    def test_get_sql(self, func, expected):
        self.assertEqual(func.get_sql(), expected)
