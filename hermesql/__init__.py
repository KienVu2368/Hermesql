"""
hermesql is divided into a couple of modules, primarily the ``queries`` and ``terms`` modules.

hermesql.queries
--------------

This is where the ``Query`` class can be found which is the core class in hermesql.  Also, other top level classes such
as ``Table`` can be found here.  ``Query`` is a container that holds all of the ``Term`` types together and also
serializes the builder to a string.

hermesql.terms
------------

This module contains the classes which represent individual parts of queries that extend the ``Term`` base class.

hermesql.functions
----------------

Wrappers for common SQL functions are stored in this package.

hermesql.enums
------------

Enumerated values are kept in this package which are used as options for Queries and Terms.


hermesql.utils
------------

This contains all of the utility classes such as exceptions and decorators.

"""

# noinspection PyUnresolvedReferences
from hermesql.dialects import (
    ClickHouseQuery,
    Dialects,
    MSSQLQuery,
    MySQLQuery,
    OracleQuery,
    PostgreSQLQuery,
    RedshiftQuery,
    SQLLiteQuery,
    VerticaQuery,
)

# noinspection PyUnresolvedReferences
from hermesql.enums import (
    DatePart,
    JoinType,
    Order,
)

# noinspection PyUnresolvedReferences
from hermesql.queries import (
    AliasedQuery,
    Query,
    Schema,
    Table,
    Column,
    Database,
    make_tables as Tables,
    make_columns as Columns,
    model
)

# noinspection PyUnresolvedReferences
from hermesql.terms import (
    Array,
    Bracket,
    Case,
    Criterion,
    EmptyCriterion,
    Field,
    Field_piece,
    Index,
    Interval,
    JSON,
    Not,
    NullValue,
    Parameter,
    Rollup,
    Tuple,
    CustomFunction
)

# noinspection PyUnresolvedReferences
from hermesql.utils import (
    CaseException,
    GroupingException,
    JoinException,
    QueryException,
    RollupException,
    SetOperationException,
    FunctionException,
    remove_vowels
)

__author__ = "Timothy Heys"
__email__ = "theys@kayak.com"
__version__ = "0.37.16"
