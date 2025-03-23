from enum import Enum
from typing import Literal

from pydantic import BaseModel

from pydantricks import FieldFactory, ModelFactory


class Permission(Enum):
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
