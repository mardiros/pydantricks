import random
from enum import Enum
from typing import Any, Literal

import pytest
from faker import Faker
from pydantic import BaseModel

from pydantricks import FieldFactory, ModelFactory


# we want to predict the randomness.
# by the way we can't do pure TDD here because we can't predict berore run
@pytest.fixture(autouse=True)
def kill_randomness():
    Faker.seed(0)
    random.seed(42)


class Permission(str, Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"


class Role(BaseModel):
    name: str
    permissions: set[Permission]

    def __hash__(self) -> int:
        return hash(self.name)


class User(BaseModel):
    username: str
    roles: list[Role]


class TShirt(BaseModel):
    model: str
    size: Literal["s", "m", "l"]


class RoleFactory(ModelFactory[Role]):
    name = FieldFactory.field.job
    permissions = FieldFactory.set_factory(Permission, 2)


class UserFactory(ModelFactory[User]):
    username = FieldFactory.field.user_name
    roles = FieldFactory.list_factory(RoleFactory, 0, 2)


class BobFactory(ModelFactory[User]):
    username = "bob"
    roles = FieldFactory.list_factory(RoleFactory, 0, 2)


class TSmallShirtFactory(ModelFactory[TShirt]):
    model = FieldFactory.field.company
    size = "s"


class TShirtFactory(ModelFactory[TShirt]):
    model = FieldFactory.field.company
    size = FieldFactory.choice(Literal["s", "m", "l"])


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


def test_model_example():
    assert UserFactory() == User(
        username="achang",
        roles=[
            Role(name="Architect", permissions={Permission.READ, Permission.DELETE}),
            Role(
                name="Futures trader", permissions={Permission.READ, Permission.WRITE}
            ),
        ],
    )

    assert UserFactory() == User(
        username="ysullivan",
        roles=[
            Role(name="Immunologist", permissions={Permission.ADMIN, Permission.READ}),
            Role(
                name="Publishing rights manager",
                permissions={Permission.READ, Permission.WRITE},
            ),
        ],
    )


def test_constant_value():
    assert TSmallShirtFactory() == TShirt(model="Chang-Fisher", size="s")
    assert TSmallShirtFactory() == TShirt(model="Sheppard-Tucker", size="s")

    assert BobFactory().username == "bob"


def test_choices():
    assert TShirtFactory() == TShirt(model="Chang-Fisher", size="l")
    assert TShirtFactory() == TShirt(model="Sheppard-Tucker", size="s")
