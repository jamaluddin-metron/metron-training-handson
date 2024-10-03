from uuid import uuid4
from app.utils import Status
# Define a model Data class with attributes like message, timestamp, and source ip address.
class Data:

    """
    A class to represent a data record.
    Attributes:
    ----------
    data_id : uuid.UUID
        A unique identifier for the data record.
    message : str
        The message content of the data record.
    timestamp : float
        The timestamp when the data record was created.
    status : Status
        The status of the data record.
    Methods:
    -------
    __str__():
        Returns a string representation of the data record.
    __repr__():
        Returns a string representation of the data record.
    to_dict():
        Converts the data record to a dictionary format.
    """
    def __init__(self, message: str, timestamp: float, status: Status = Status.ACTIVE, data_id:str = str(uuid4())):
        """
        Initializes a new instance of the Data class.
        Args:
            message (str): The message associated with the data.
            timestamp (float): The timestamp when the data was created.
            status (Status, optional): The status of the data. Defaults to Status.ACTIVE.
            data_id (str, optional): The unique identifier for the data. Defaults to a new UUID string.
        """
        self.data_id = data_id
        self.message = message
        self.timestamp = timestamp
        self.status = status

    def __str__(self):
        return f"Data(id={self.data_id}, message={self.message}, timestamp={self.timestamp}, status={self.status})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'data_id': str(self.data_id),
            'message': self.message,
            'timestamp': self.timestamp,
            'status': Status.get_status_name(self.status.value)
        }
