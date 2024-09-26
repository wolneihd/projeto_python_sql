import src.api_service as api_service
import src.database_create as database_create

# CREATE DATABASE
database_run = database_create.DatabaseManager()
database_run.run_sql_script()

# RUN API
api_run = api_service.App()
api_run.run()