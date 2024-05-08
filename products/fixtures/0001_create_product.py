from dynamic_fixtures.fixtures import BaseFixture

from products import factories


class Fixture(BaseFixture):

    def load(self):
        factories.ProductQuestionArticleFactory.create_batch(3)
