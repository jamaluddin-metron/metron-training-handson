from app.model import Data
from app.utils import Status, Database, get_logger

logger = get_logger(__name__)

# Service Class to handle CRUD operations on Data Model.
class DataService:
    db_object = Database()
    def __init__(self):
        pass

    # Create a new data object and add it to the data list.
    @staticmethod
    def create(data: dict) -> tuple:
        data_object = Data(data.get("message"), data.get("timestamp"))
        
        transaction_status = DataService.db_object.insert("logs", ", ".join(list(data_object.to_dict().keys())), 
                         f"'{data_object.data_id}', '{data_object.message}', {data_object.timestamp}, {data_object.status.value}")
        logger.debug(f"Transaction Status: {transaction_status}")
        return (transaction_status, 201) if transaction_status else (False, 500)

    # Get all data objects from the data list.
    @staticmethod
    def read_all() -> list[dict]:
        data = DataService.db_object.select("logs")
        data_list = []
        for row in data:
            data_list.append({
                "data_id": row[0],
                "message": row[1],
                "timestamp": row[2],
                "status": Status.get_status_name(row[3])
            })
        return data_list

    # Get a data object by data_id from the data list.
    def read(data_id: str) -> Data | None:
        # for data in self.data:
        #     if str(data.data_id) == data_id:
        #         return data
        # return None
        pass

    # Update a data object by data_id from the data list.
    @staticmethod
    def update(data_id: str, status: str) -> tuple:
        check_id = True if DataService.db_object.select("logs", "data_id", f"WHERE data_id = '{data_id}'") else False
        if not check_id:
            logger.error(f"Data ID: {data_id} not found in the logs.")  
            return False, 400
        try:
            status_value = Status.get_status_value(status)
        except:
            logger.error(f"Invalid Status value: {status} supplied.")
            return False, 400
        transaction_status = DataService.db_object.update("logs", f"status = {status_value}", f"data_id = '{data_id}'")
        
        return transaction_status, 201 if transaction_status else 500

    # Delete a data object by data_id from the data list.
    @staticmethod
    def delete(data_id: str):
        row_count = DataService.db_object.delete("logs", f"data_id = '{data_id}'")
        logger.debug(f"Rows Deleted: {row_count}")
        return True if row_count > 0 else False  

