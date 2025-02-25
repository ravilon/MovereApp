from flask import Blueprint, jsonify, request
from flasgger import swag_from
import importlib  # Used for dynamic imports

blueprint = Blueprint('api', __name__)

# Define your route for calculations
@blueprint.route('/api/calculate', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Calculation result',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {'type': 'number'}
                }
            }
        },
        400: {
            'description': 'Invalid input data'
        },
        404: {
            'description': "Calculation not found"
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'calculation': {'type': 'string'},
                    'params': {'type': 'object'}
                }
            }
        }
    ]
})
def calculate():
    global calculation_name
    try:
        # Get the calculation name and parameters from the request JSON
        data = request.get_json()
        calculation_name = data.get('calculation')
        params = data.get('params')

        if not calculation_name or not isinstance(params, dict):
            return jsonify({"error": "Invalid input data"}), 400

        # Dynamically import the correct module
        module_name = f"REST.calculations.{calculation_name}"
        module = importlib.import_module(module_name)

        # Assume that each calculation module has a `calculate` method
        result = module.calculate(params)

        return jsonify({"result": result})

    except ModuleNotFoundError:
        return jsonify({"error": f"Calculation '{calculation_name}' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

