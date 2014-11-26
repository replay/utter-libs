import unittest
import python_jsonschema_objects as pjs
from utter_libs.utils import model_mixin
from utter_libs.utils import helpers


test_object_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'type': 'object',
    'title': 'TestObject',
    'properties': {
        'str_list': {
            'type': 'array',
            'items': {'type': 'string'},
        },
        'name': {'type': 'string'},
        'number': {'type': 'number'},
    },
}

TestObjectSchema = pjs.ObjectBuilder(
    test_object_schema).build_classes().Testobject


class TestObject(model_mixin.ModelSchemaMixin):
    object_schema = TestObjectSchema
    str_list = []
    name = ''
    number = 0

    def __init__(self, str_list=None, name=None, number=None):
        self.str_list = str_list
        self.name = name
        self.number = number


class TestModelSchemaMixin(unittest.TestCase):

    def setUp(self):
        pass

    def _create_test_data(self):
        obj = TestObject(
            name = 'test object',
            number = 123,
            str_list = ['abc' + str(i) for i in range(100,200)])
        return obj

    def test_serialization(self):
        test_object1 = self._create_test_data()
        test_object1_schema = test_object1.as_schema()
        test_object1_dict = test_object1_schema.as_dict()
        test_object2_schema = TestObjectSchema(**test_object1_dict)
        test_object2 = TestObject()
        helpers.ApiSchemaHelper.fill_object_from_schema(test_object2_schema, test_object2)
        test_object2.as_schema()
        self.assertEqual(
            test_object2.as_schema().as_dict(),
            test_object1.as_schema().as_dict())
