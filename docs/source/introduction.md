# Pydantricks

Pydantricks is a library made for developpers that use Pydantic for their model,
and want clean faker data easily.

It use [Faker](https://github.com/joke2k/faker) under the hood in order to have
better values than just random letters.

It is very usefull while unit testing, functional testing and prototyping.

It support simple types and all kind of complex type.

The main difference between pydantricks and its alternative is that
it focus on domain models faked object made with pydantic,
it feet well with the library [messagebus](https://pypi.org/project/messagebus/).


## Alternative projects:

* [polyfactory](https://github.com/litestar-org/polyfactory)

Polyfactory supports many types but does not use faker, it create random
data for every model without caring of what they should contains.

The project was named pydantic-factories but renamed while supporting
many model library.

You don't need to configure what the data has to contains.

* [factory_boy](https://factoryboy.readthedocs.io/en/stable/)

Factory Boy is a similar project has Pydantricks and is very general,
it is widely used with ORM.
