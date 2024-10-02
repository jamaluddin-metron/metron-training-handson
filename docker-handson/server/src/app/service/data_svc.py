from app.model import Data
from app.utils import Status, Database

# Service Class to handle CRUD operations on Data Model.
class DataService:
    def __init__(self):
        pass

    # Create a new data object and add it to the data list.
    @staticmethod
    def create(data: dict) -> tuple:
        data_object = Data(data.get("message"), data.get("timestamp"))
        db_object = Database()
        db_object.insert("logs", ", ".join(list(data_object.to_dict().keys())), 
                         f"'{data_object.data_id}', '{data_object.message}', {data_object.timestamp}, {data_object.status.value}")
        return True, 201

    # Get all data objects from the data list.
    @staticmethod
    def read_all() -> list[dict]:
        pass
        # return self.data

    # Get a data object by data_id from the data list.
    def read(data_id: str) -> Data | None:
        # for data in self.data:
        #     if str(data.data_id) == data_id:
        #         return data
        # return None
        pass

    # Update a data object by data_id from the data list.
    @staticmethod
    def update(data_id: str, message: str, timestamp: float, source_ip: str):
        # for data in self.data:
        #     if str(data.data_id) == data_id:
        #         data.message = message
        #         data.timestamp = timestamp
        #         data.source_ip = source_ip
        #         return data
        # return None
        pass

    # Delete a data object by data_id from the data list.
    @staticmethod
    def delete(self, data_id: str):
        # for data in self.data:
        #     if str(data.data_id) == data_id:
        #         self.data.remove(data)
        #         return data
        # return None
        pass

