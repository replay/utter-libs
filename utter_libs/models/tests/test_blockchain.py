import unittest
from utter_libs.models import blockchain


test_data = {
    'hash': 'mytesthash123',
    'outputs': {
        'outputs': [{
            'addresses': [
                {'address': 'myaddress1'},
                {'address': 'blaaddress2'}],
            'value': 123}]},
    'inputs': {
        'inputs': [{
            'addresses': [{
                'address': 'anotheraddress1'}],
            'value': 321}]}}


class TestModelSchemaMixin(unittest.TestCase):

    def setUp(self):
        pass

    def test_from_and_to_dict(self):
        transaction_object = blockchain.BTCTransaction.from_dict(test_data)
        self.assertEqual(test_data, transaction_object.as_dict())

    def test_get_addresses(self):
        transaction_object = blockchain.BTCTransaction.from_dict(test_data)
        self.assertEqual(
            ['myaddress1', 'blaaddress2'],
            transaction_object.get_addresses('out'))
        self.assertEqual(
            ['anotheraddress1'],
            transaction_object.get_addresses('in'))
