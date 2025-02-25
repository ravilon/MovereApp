from flask import Blueprint, jsonify, request, render_template
from flasgger import swag_from
import importlib  # Used for dynamic imports

blueprint = Blueprint('api', __name__)

# Define your route for functions
@blueprint.route('/api/functions', methods=['POST'])

@swag_from({
    'responses': {
        200: {
            'description': 'Function result',
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
            'description': "Function not found"
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
                    'function': {'type': 'string'},
                    'params': {'type': 'object'}
                }
            }
        }
    ]
})

def calculate():
    global function_name
    try:
        # Get the calculation name and parameters from the request JSON
        data = request.get_json()
        function_name = data.get('function')
        params = data.get('params')

        if not function_name or not isinstance(params, dict):
            return jsonify({"error": "Invalid input data"}), 400

        # Dynamically import the correct module
        module_name = f"REST.functions.{function_name}"
        module = importlib.import_module(module_name)

        # Assume that each calculation module has a `calculate` method
        result = module.calculate(params)

        return jsonify({"result": result})

    except ModuleNotFoundError:
        return jsonify({"error": f"Function '{function_name}' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@blueprint.route('/')
def home():
    return render_template('index.html')
