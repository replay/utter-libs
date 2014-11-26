

transaction_address_schema = {
	'$schema': 'http://json-schema.org/draft-04/schema#',
	'type': 'object',
	'title': 'TransactionAddress',
	'properties': {
		'address': {
			'type': 'string'
		}
	},
}

transaction_input_schema = {
	'$schema': 'http://json-schema.org/draft-04/schema#',
	'type': 'object',
	'title': 'TransactionInput',
	'properties': {
		'value': 'number',
		'addresses': {
			'type': 'array',
			'items': transaction_address_schema
		}
	},
}

transaction_output_schema = {
	'$schema': 'http://json-schema.org/draft-04/schema#',
	'type': 'object',
	'title': 'TransactionOutput',
	'properties': {
		'value': 'number',
		'addresses': {
			'type': 'array',
			'items': transaction_address_schema
		}
	},
}

transaction_inputs_schema = {
	'$schema': 'http://json-schema.org/draft-04/schema#',
	'type': 'object',
	'title': 'TransactionInputs',
	'properties': {
		'value': 'number',
		'addresses': {
			'type': 'array',
			'items': transaction_input_schema
		}
	},
}

transaction_outputs_schema = {
	'$schema': 'http://json-schema.org/draft-04/schema#',
	'type': 'object',
	'title': 'TransactionOutputs',
	'properties': {
		'value': 'number',
		'addresses': {
			'type': 'array',
			'items': transaction_output_schema
		}
	},
}

transaction_schema = {
	'$schema': 'http://json-schema.org/draft-04/schema#',
	'type': 'object',
	'title': 'Transaction',
	'properties': {
		'hash': {'type': 'string'},
		'transaction_inputs': {
			'type': 'array',
			'items': transaction_inputs_schema,
		},
		'transaction_outputs': {
			'type': 'array',
			'items': transaction_outputs_schema,
		},
	},
}
