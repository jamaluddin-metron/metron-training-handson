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
            logger.debug(f"Received Data Payload: {data}")
            result, response_status = DataService.create(data) if Helper.validate_post_data(data) else (False, 400)
            if result:
                logger.info("New Log Entry stored successfully.")
                return jsonify({'message': 'Data stored successfully.'}), 201
            elif not result and response_status == 400:
                logger.error(f"Ingest Data Payload failed validation.")
                return jsonify({'message': 'Data is invalid.'}), 400
            else:
                logger.error(f"Failed to store data. Check logs")
                return jsonify({'message': 'Failed to store data.'}), 500
        except Exception as error:
            logger.error(f"Error Occured while trying to store new log data:\n{error}")
            return jsonify({'error': 'Server Encountered an Error'}), 500

    @app.route('/data/<string:data_id>', methods=['PUT'])
    def update_data(data_id):
        try:
            data = request.get_json()
            logger.debug(f"Received Data Payload: {data}")
            logger.debug(f"Received Data ID: {data_id}")
            result, response_status = DataService.update(data_id, data.get("status")) if Helper.validate_put_data(data) else (False, 400)
            if result:
                logger.info("Log Entry updated successfully.")
                return jsonify({'message': 'Data updated successfully.'}), response_status
            elif not result and response_status == 400:
                logger.error(f"Invalid Data Id or Payload Supplied.")
                return jsonify({'message': 'Data is invalid.'}), response_status
            else:
                logger.error(f"Failed to update data. Check logs")
                return jsonify({'message': 'Failed to update data.'}), response_status
        except Exception as error:
            logger.error(f"Error Occured while trying to update log data:\n{error}")
            return jsonify({'error': 'Server Encountered an Error'}), 500

    @app.route('/data', methods=['DELETE'])
    def delete_data():
        pass
