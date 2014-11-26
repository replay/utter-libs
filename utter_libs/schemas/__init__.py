import six
import python_jsonschema_objects as pjs

from utter_libs.schemas.instance import instance_schema
from utter_libs.schemas.instance import instance_list_schema
from utter_libs.schemas.appliance import appliance_schema
from utter_libs.schemas.flavor import flavor_schema
from utter_libs.schemas.flavor import flavor_list_schema
from utter_libs.schemas.instance_start_parameters import \
  instance_start_parameters_schema
from utter_libs.schemas.bonsho_callback import transaction_schema


schemas = {
    'InstanceSchema': (instance_schema, 'Instance'),
    'InstanceListSchema': (instance_list_schema, 'Instancelist'),
    'ApplianceSchema': (appliance_schema, 'Appliance'),
    'FlavorSchema': (flavor_schema, 'Flavor'),
    'FlavorListSchema': (flavor_list_schema, 'Flavorlist'),
    'InstanceStartParametersSchema': (
      instance_start_parameters_schema, 'Instancestartparameters'),
}

# iterate over schemas and create their according content-types
for (k, v) in six.iteritems(schemas):
    schemas[k] = getattr(pjs.ObjectBuilder(v[0]).build_classes(), v[1])
