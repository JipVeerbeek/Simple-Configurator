from dynamic_fixtures.fixtures import BaseFixture

from configurations import factories


class Fixture(BaseFixture):

    def load(self):
        factories.ConfigurationLineFactory.create()
