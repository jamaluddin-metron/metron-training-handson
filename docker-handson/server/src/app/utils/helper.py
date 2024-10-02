
class Helper:

    @staticmethod
    def validate_data(data: dict) -> bool:
        if not data.get("message") or not data.get("timestamp"):
            return False
        return True
