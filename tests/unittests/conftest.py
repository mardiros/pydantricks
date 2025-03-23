import random

import pytest
from faker import Faker


# we want to predict the randomness.
# by the way we can't do pure TDD here because we can't predict berore run
@pytest.fixture(autouse=True)
def kill_randomness():
    Faker.seed(0)
    random.seed(42)
