from app.model import Data

# Service Class to handle CRUD operations on Data Model.
class DataService:
    def __init__(self):
        pass

    # Create a new data object and add it to the data list.
    @staticmethod
    def create(self, data: dict) -> tuple:
        data_object = Data(data.get("message"), data.get("timestamp"), data.get("source_ip"))
        # self.data.append(data_object)
        return True, 201

    # Get all data objects from the data list.
    @staticmethod
    def read_all(self) -> list[dict]:
        pass
        # return self.data

    # Get a data object by data_id from the data list.
    def read(self, data_id: str) -> Data | None:
        # for data in self.data:
        #     if str(data.data_id) == data_id:
        #         return data
        # return None
        pass

    # Update a data object by data_id from the data list.
    @staticmethod
    def update(self, data_id: str, message: str, timestamp: float, source_ip: str):
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

