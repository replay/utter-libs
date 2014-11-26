import abc
import six

from utter_libs.utils.helpers import ApiSchemaHelper


class ModelSchemaMixin:

    object_schema = None
    object_list_schema = None

    # create api schema and fill it with data from self
    def as_schema(self):
        schema = self.object_schema()
        ApiSchemaHelper.fill_schema_from_object(schema, self)
        return schema

    # render list of objects of this model
    @classmethod
    def as_schema_list(self, object_list):
        # if self.object_list_schema is not set we can't create a list
        if not hasattr(self, 'object_list_schema'):
            raise Exception("don't have self.object_list_schema property")

        schema = self.object_list_schema()

        # populate list schema with list of object schemas as dictionaries
        schema.update({'items': [
            x.as_schema().as_dict()
            for x in object_list]})

        # return schema
        return schema
