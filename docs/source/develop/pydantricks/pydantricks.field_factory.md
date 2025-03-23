# {py:mod}`pydantricks.field_factory`

```{py:module} pydantricks.field_factory
```

```{autodoc2-docstring} pydantricks.field_factory
:parser: myst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GenericFakerFieldFactory <pydantricks.field_factory.GenericFakerFieldFactory>`
  - ```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory
    :parser: myst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`is_model_factory <pydantricks.field_factory.is_model_factory>`
  - ```{autodoc2-docstring} pydantricks.field_factory.is_model_factory
    :parser: myst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`F <pydantricks.field_factory.F>`
  - ```{autodoc2-docstring} pydantricks.field_factory.F
    :parser: myst
    :summary:
    ```
* - {py:obj}`FakerFieldFactory <pydantricks.field_factory.FakerFieldFactory>`
  - ```{autodoc2-docstring} pydantricks.field_factory.FakerFieldFactory
    :parser: myst
    :summary:
    ```
* - {py:obj}`FieldFactory <pydantricks.field_factory.FieldFactory>`
  - ```{autodoc2-docstring} pydantricks.field_factory.FieldFactory
    :parser: myst
    :summary:
    ```
* - {py:obj}`K <pydantricks.field_factory.K>`
  - ```{autodoc2-docstring} pydantricks.field_factory.K
    :parser: myst
    :summary:
    ```
````

### API

````{py:data} F
:canonical: pydantricks.field_factory.F
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} pydantricks.field_factory.F
:parser: myst
```

````

````{py:data} FakerFieldFactory
:canonical: pydantricks.field_factory.FakerFieldFactory
:value: >
   None

```{autodoc2-docstring} pydantricks.field_factory.FakerFieldFactory
:parser: myst
```

````

````{py:data} FieldFactory
:canonical: pydantricks.field_factory.FieldFactory
:value: >
   'FakerFieldFactory(...)'

```{autodoc2-docstring} pydantricks.field_factory.FieldFactory
:parser: myst
```

````

`````{py:class} GenericFakerFieldFactory(faker: faker.Faker)
:canonical: pydantricks.field_factory.GenericFakerFieldFactory

Bases: {py:obj}`typing.Generic`\[{py:obj}`pydantricks.field_factory.F`\, {py:obj}`pydantricks.field_factory.K`\]

```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory
:parser: myst
```

```{rubric} Initialization
```

```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory.__init__
:parser: myst
```

````{py:method} choice(factory: type[pydantricks.field_factory.F] | types.UnionType | pydantricks.model_factory.ModelFactory[pydantricks.model_factory.T] | str) -> collections.abc.Callable[[], pydantricks.field_factory.F]
:canonical: pydantricks.field_factory.GenericFakerFieldFactory.choice

```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory.choice
:parser: myst
```

````

````{py:method} dict_factory(key_factory: pydantricks.field_factory.K, value_factory: pydantricks.field_factory.F, min: int, max: int) -> collections.abc.Callable[..., dict[pydantricks.field_factory.K, pydantricks.field_factory.F]]
:canonical: pydantricks.field_factory.GenericFakerFieldFactory.dict_factory

```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory.dict_factory
:parser: myst
```

````

````{py:property} field
:canonical: pydantricks.field_factory.GenericFakerFieldFactory.field
:type: faker.Faker

```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory.field
:parser: myst
```

````

````{py:method} list_factory(factory: type[pydantricks.field_factory.F], min: int, max: int | None = None) -> collections.abc.Callable[..., list[pydantricks.field_factory.F]]
:canonical: pydantricks.field_factory.GenericFakerFieldFactory.list_factory

```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory.list_factory
:parser: myst
```

````

````{py:method} set_factory(factory: type[pydantricks.field_factory.F], min: int, max: int | None = None) -> collections.abc.Callable[..., set[pydantricks.field_factory.F]]
:canonical: pydantricks.field_factory.GenericFakerFieldFactory.set_factory

```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory.set_factory
:parser: myst
```

````

````{py:method} tuple_factory(*factory: typing.Any) -> collections.abc.Callable[..., tuple[pydantricks.field_factory.F, ...]]
:canonical: pydantricks.field_factory.GenericFakerFieldFactory.tuple_factory

```{autodoc2-docstring} pydantricks.field_factory.GenericFakerFieldFactory.tuple_factory
:parser: myst
```

````

`````

````{py:data} K
:canonical: pydantricks.field_factory.K
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} pydantricks.field_factory.K
:parser: myst
```

````

````{py:function} is_model_factory(typ: typing.Any) -> typing.TypeGuard[pydantricks.model_factory.ModelFactory[typing.Any]]
:canonical: pydantricks.field_factory.is_model_factory

```{autodoc2-docstring} pydantricks.field_factory.is_model_factory
:parser: myst
```
````
