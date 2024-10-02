from app import create_app, initialize_db
from app.utils import get_logger
import os

logger = get_logger(__name__)

app = create_app()

if __name__ == "__main__":
    if not initialize_db(os.getenv('DB_NAME', 'metron')):
        logger.critical("Failed to initialize the database.")
        exit("ERROR_DATABASE_INITIALIZATION_EXIT")
    else:
        logger.info("Database initialized successfully.")
    
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
