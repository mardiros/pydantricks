from tests.unittests.fixtures import (
    BobFactory,
    Permission,
    Role,
    TShirt,
    TShirtFactory,
    TSmallShirtFactory,
    User,
    UserFactory,
)


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
