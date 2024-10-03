from enum import Enum
# Enum for different log status values
# 1 -> ACTIVE, 0 -> INACTIVE, 2 -> INVESTIGATION, 3 -> RESOLVED

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 0
    INVESTIGATION = 2
    RESOLVED = 3

    # Define a method to get the status value from the status name
    @staticmethod
    def get_status_value(status: str) -> int:
        """
        Get the status value from the status name.

        Args:
            status (str): The status name.

        Returns:
            int: The status value.

        """
        return Status[status.upper()].value
    
    # Define a method to get the status name from the status value
    @staticmethod
    def get_status_name(status: int) -> str:
        """
        Get the status name from the status value.

        Args:
            status (int): The status value.

        Returns:
            str: The status name.

        """
        return Status(status).name
