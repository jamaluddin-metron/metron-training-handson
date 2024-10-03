
class Helper:

    @staticmethod
    def validate_post_data(data: dict) -> bool:
        if not data.get("message") or not data.get("timestamp"):
            return False
        return True
    
    @staticmethod
    def validate_put_data(data: dict) -> bool:
        if not data.get("status"):
            return False
        return True
