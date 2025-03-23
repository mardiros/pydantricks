"""
A factory for pydantic models.
"""

import inspect
import random
from collections.abc import Callable
from enum import Enum
from types import UnionType
from typing import Any, Generic, TypeVar, get_args

from faker import Faker
from pydantic import BaseModel

from pydantricks.shared_utils.infer import is_literal, is_union

K = TypeVar("K")
F = TypeVar("F")
T = TypeVar("T", bound=BaseModel)


class ModelFactory(Generic[T]):
    """Generic Factory for Pydantic models."""

    def __new__(cls, **overrides: Any) -> T:  # type: ignore
        """Create and return an instance of the Pydantic model."""
        model_type: type[T] = cls.__orig_bases__[0].__args__[0]  # type: ignore

        field_values = overrides.copy()
        for key in model_type.model_fields:
            if key not in field_values:
                if hasattr(cls, key):
                    value = getattr(cls, key)
                    field_values[key] = value() if callable(value) else value
        field_values.update(overrides)
        return model_type(**field_values)


class _FieldFactory(Generic[F]):
    """A factory that will be called during model construction."""

    def __init__(self, faker: Faker) -> None:
        self.faker = faker

    @property
    def field(self) -> Faker:
        return self.faker

    def choice(
        self, factory: type[F] | UnionType | ModelFactory[Any]
    ) -> Callable[[], F]:
        if is_literal(factory):  # type: ignore
            choices = get_args(factory)
            return lambda: random.choice(choices)

        if is_union(factory):  # type: ignore
            choices = get_args(factory)
            return lambda: random.choice(choices)()

        if inspect.isclass(factory) and issubclass(factory, ModelFactory):
            return factory  # type: ignore

        if inspect.isclass(factory) and issubclass(factory, Enum):
            choices = list(factory)  # type: ignore
            return lambda: random.choice(choices)

        if callable(factory):  # must be done after enum
            return factory  # faker generator

        if hasattr(factory, "__iter__"):
            return lambda: random.choice(factory)  # type: ignore

        raise NotImplementedError(factory)

    def set_factory(
        self, factory: type[F], min: int, max: int | None = None
    ) -> Callable[..., set[F]]:
        def callback() -> set[F]:
            size = random.randint(min, max or min)
            ret: set[F] = set()
            while len(ret) < size:
                ret.add(self.choice(factory)())
            return ret

        return callback

    def list_factory(
        self, factory: type[F], min: int, max: int | None = None
    ) -> Callable[..., list[F]]:
        return lambda: [
            self.choice(factory)() for _ in range(random.randint(min, max or min))
        ]

    def tuple_factory(self, *factory: Any) -> Callable[..., tuple[F, ...]]:
        return lambda: tuple(self.choice(f)() for f in factory)

    def dict_factory(
        self,
        key_factory: Any,
        value_factory: Any,
        min: int,
        max: int,
    ) -> Callable[..., dict[Any, F]]:
        item_factory = self.tuple_factory(key_factory, value_factory)
        return lambda: dict(self.list_factory(item_factory, min, max)())  # type: ignore


FieldFactory = _FieldFactory[Any](Faker())
