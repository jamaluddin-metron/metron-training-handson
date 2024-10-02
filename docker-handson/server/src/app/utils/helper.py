
class Helper:

    @staticmethod
    def validate_data(data: dict) -> bool:
        if not data.get("message") or not data.get("timestamp") or not data.get("status"):
            return False
        return True
