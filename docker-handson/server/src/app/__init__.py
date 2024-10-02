from .app import create_app
from .utils import Database
# from .service import DataService
# from .model import Data

def initialize_db(database_name: str) -> bool:
    db = Database(f"{database_name}.db")
    create_table_sql = """CREATE TABLE IF NOT EXISTS logs (
                            data_id VARCHAR(36) PRIMARY KEY,
                            message TEXT NOT NULL,
                            timestamp NUMBER,
                            status NUMBER(1) DEFAULT 1
                        )"""
    return db.create_table(create_table_sql)
