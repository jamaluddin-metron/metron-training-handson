from flask import request, jsonify, Flask
from .service import DataService
from .utils import Helper, get_logger

logger = get_logger(__name__)

def register_routes(app: Flask):
    @app.route('/health', methods=['GET'])
    def health():
        return "OK", 200
    
    @app.route('/data', methods=['GET'])
    def get_data():
        return jsonify({'data': 'GET'})
        
    @app.route('/data', methods=['POST'])
    def store_data():
        try:
            data = request.get_json()
            result, response_status = DataService.create(data) if Helper.validate_data(data) else False, 400
            if result:
                return jsonify({'message': 'Data stored successfully.'}), 201
            elif not result and response_status == 400:
                return jsonify({'message': 'Data is invalid.'}), 400
            else:
                return jsonify({'message': 'Failed to store data.'}), 500
        except Exception as error:
            logger.error(f"Error Occured while trying to store new log data:\n{error}")
            return jsonify({'error': 'Server Encountered an Error'}), 500

    @app.route('/data', methods=['PUT'])
    def update_data():
        pass

    @app.route('/data', methods=['DELETE'])
    def delete_data():
        pass
