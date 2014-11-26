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
        self.transaction_object = blockchain.BTCTransaction.from_dict(
            test_data)

    def test_from_and_to_dict(self):
        self.assertEqual(test_data, self.transaction_object.as_dict())

    def test_get_addresses(self):
        self.assertEqual(
            ['myaddress1', 'blaaddress2'],
            self.transaction_object.get_addresses('out'))
        self.assertEqual(
            ['anotheraddress1'],
            self.transaction_object.get_addresses('in'))

    def test_get_value_by_address(self):
        self.assertEqual(
            self.transaction_object.get_value_by_address('out', 'myaddress1'),
            123)
        self.assertEqual(
            self.transaction_object.get_value_by_address('in', 'anotheraddress1'),
            321)
        self.assertRaises(Exception,
            self.transaction_object.get_value_by_address, 'out', 'myaddress')
