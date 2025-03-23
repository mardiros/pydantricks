from typing import Any, Literal

import pytest

from pydantricks import FieldFactory
from tests.unittests.fixtures import (
    Permission,
    Role,
    RoleFactory,
    TShirt,
    TShirtFactory,
    TSmallShirtFactory,
)


@pytest.mark.parametrize(
    "factory,expected_list",
    [
        pytest.param(Literal["a", "b", "c"], ["c", "a"], id="Literal"),
        pytest.param("abcdef", ["f", "a", "a"], id="Iterable"),
        pytest.param(
            Permission,
            [Permission.READ, Permission.READ, Permission.DELETE],
            id="Enum",
        ),
        pytest.param(
            RoleFactory | TSmallShirtFactory | TShirtFactory,
            [
                TShirt(model="Chang-Fisher", size="s"),
                Role(
                    name="Futures trader",
                    permissions={Permission.READ, Permission.WRITE},
                ),
            ],
            id="Union[Factory]",
        ),
    ],
)
def test_choice(factory: Any, expected_list: Any):
    for expected in expected_list:
        assert FieldFactory.choice(factory)() == expected


@pytest.mark.parametrize(
    "factory,expected_list",
    [
        pytest.param(
            (RoleFactory, TShirtFactory),
            (
                Role(name="Musician", permissions={Permission.READ, Permission.DELETE}),
                TShirt(model="Williams-Sheppard", size="s"),
            ),
            id="Factory",
        ),
        pytest.param(
            (FieldFactory.field.user_name, TShirtFactory),
            (
                "achang",
                TShirt(model="Green PLC", size="l"),
            ),
            id="item",
        ),
    ],
)
def test_tuple_factory(factory: Any, expected_list: Any):
    assert FieldFactory.tuple_factory(*factory)() == expected_list


@pytest.mark.parametrize(
    "factory,expected_list",
    [
        pytest.param(
            (FieldFactory.field.user_name, 1, 3),
            [
                "achang",
                "greenwilliam",
                "thull",
            ],
            id="str",
        ),
        pytest.param(
            (RoleFactory, 1, 2),
            [
                Role(
                    name="Musician", permissions={Permission.WRITE, Permission.DELETE}
                ),
            ],
            id="ModelFactory",
        ),
        pytest.param(
            (
                FieldFactory.tuple_factory(
                    FieldFactory.field.user_name,
                    RoleFactory,
                ),
                3,
                5,
            ),
            [
                (
                    "achang",
                    Role(
                        name="Architect",
                        permissions={Permission.READ, Permission.DELETE},
                    ),
                ),
                (
                    "tammy76",
                    Role(
                        name="Immunologist",
                        permissions={Permission.READ, Permission.WRITE},
                    ),
                ),
                (
                    "nhoward",
                    Role(
                        name="Retail merchandiser",
                        permissions={Permission.ADMIN, Permission.READ},
                    ),
                ),
                (
                    "juancampos",
                    Role(
                        name="Water engineer",
                        permissions={Permission.READ, Permission.WRITE},
                    ),
                ),
                (
                    "vanessa89",
                    Role(
                        name="Data processing manager",
                        permissions={Permission.READ, Permission.WRITE},
                    ),
                ),
            ],
            id="composite",
        ),
    ],
)
def test_list_factory(factory: Any, expected_list: Any):
    assert FieldFactory.list_factory(*factory)() == expected_list


@pytest.mark.parametrize(
    "factory,expected_list",
    [
        pytest.param((Literal["a", "b", "c"], 2), {"a", "c"}, id="literal"),
        pytest.param(
            (Literal["a", "b", "c", "d", "e", "f"], 1, 3),
            {"a", "c", "f"},
            id="literal-range",
        ),
        pytest.param(("abcdef", 2), {"a", "f"}, id="str"),
        pytest.param((Permission, 2), {Permission.READ, Permission.DELETE}, id="enum"),
    ],
)
def test_set_factory(factory: Any, expected_list: Any):
    assert FieldFactory.set_factory(*factory)() == expected_list


@pytest.mark.parametrize(
    "factory,expected_list",
    [
        pytest.param(
            FieldFactory.dict_factory(
                FieldFactory.field.user_name,
                RoleFactory,
                3,
                5,
            ),
            {
                "achang": Role(
                    name="Architect", permissions={Permission.READ, Permission.DELETE}
                ),
                "juancampos": Role(
                    name="Water engineer",
                    permissions={Permission.READ, Permission.WRITE},
                ),
                "nhoward": Role(
                    name="Retail merchandiser",
                    permissions={Permission.READ, Permission.ADMIN},
                ),
                "tammy76": Role(
                    name="Immunologist", permissions={Permission.READ, Permission.WRITE}
                ),
                "vanessa89": Role(
                    name="Data processing manager",
                    permissions={Permission.READ, Permission.WRITE},
                ),
            },
            id="dict",
        ),
    ],
)
def test_dict_factory(factory: Any, expected_list: Any):
    assert factory() == expected_list
