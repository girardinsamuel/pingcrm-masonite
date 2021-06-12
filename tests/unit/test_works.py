from masonite.tests import TestCase


class TestUnit(TestCase):

    def test_example_assertion(self):
        self.get("/login").assertInertiaComponent("Auth/Login")
