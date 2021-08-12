from django.test import SimpleTestCase
from django.test import TransactionTestCase


class GrandparentOfSecondClass(TransactionTestCase):

    def get(self):
        return self.client.get("/some/example")


class ParentOfSecondClass(GrandparentOfSecondClass):
    pass


class ThirdBaseClass(ParentOfSecondClass):
    pass


class SecondBaseClass(ParentOfSecondClass):
    pass


class ParentOfGrandparentOfSecondClass(SimpleTestCase):
    pass


class FirstBaseClass(ParentOfGrandparentOfSecondClass):
    pass


class BuggyTestCase(
    FirstBaseClass,
    SecondBaseClass,
    ThirdBaseClass
):

    def test_example(self):
        resp = self.get()
        self.assertEqual(resp.rendered_content, "")
