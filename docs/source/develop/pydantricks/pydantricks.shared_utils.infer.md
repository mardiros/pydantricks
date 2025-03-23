# {py:mod}`pydantricks.shared_utils.infer`

```{py:module} pydantricks.shared_utils.infer
```

```{autodoc2-docstring} pydantricks.shared_utils.infer
:parser: myst
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`is_enum <pydantricks.shared_utils.infer.is_enum>`
  - ```{autodoc2-docstring} pydantricks.shared_utils.infer.is_enum
    :parser: myst
    :summary:
    ```
* - {py:obj}`is_literal <pydantricks.shared_utils.infer.is_literal>`
  - ```{autodoc2-docstring} pydantricks.shared_utils.infer.is_literal
    :parser: myst
    :summary:
    ```
* - {py:obj}`is_sequence <pydantricks.shared_utils.infer.is_sequence>`
  - ```{autodoc2-docstring} pydantricks.shared_utils.infer.is_sequence
    :parser: myst
    :summary:
    ```
* - {py:obj}`is_union <pydantricks.shared_utils.infer.is_union>`
  - ```{autodoc2-docstring} pydantricks.shared_utils.infer.is_union
    :parser: myst
    :summary:
    ```
````

### API

````{py:function} is_enum(typ: typing.Any) -> typing.TypeGuard[enum.Enum]
:canonical: pydantricks.shared_utils.infer.is_enum

```{autodoc2-docstring} pydantricks.shared_utils.infer.is_enum
:parser: myst
```
````

````{py:function} is_literal(typ: typing.Any) -> bool
:canonical: pydantricks.shared_utils.infer.is_literal

```{autodoc2-docstring} pydantricks.shared_utils.infer.is_literal
:parser: myst
```
````

````{py:function} is_sequence(typ: typing.Any) -> typing.TypeGuard[collections.abc.Sequence[typing.Any]]
:canonical: pydantricks.shared_utils.infer.is_sequence

```{autodoc2-docstring} pydantricks.shared_utils.infer.is_sequence
:parser: myst
```
````

````{py:function} is_union(typ: typing.Any) -> typing.TypeGuard[types.UnionType]
:canonical: pydantricks.shared_utils.infer.is_union

```{autodoc2-docstring} pydantricks.shared_utils.infer.is_union
:parser: myst
```
````
