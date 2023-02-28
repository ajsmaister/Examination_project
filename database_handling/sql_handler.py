from sqlalchemy import create_engine, text
from parameters import POSTGRES_KEY


class PostgresHandler:

	postgres_url = POSTGRES_KEY

	def __init__(self):
		self.engine = create_engine(self.postgres_url)

	def execute_create(self, create_statement):
		with self.engine.connect() as conn:
			conn.execute(create_statement)

	def execute_insert(self, insert_statement, d):
		for item in d:
			with self.engine.connect() as conn:
				conn.execute(text(insert_statement), **item)

	def execute_insert_new_employees(self, insert_statement, d):
		for item in d:
			with self.engine.connect() as conn:
				conn.execute(text(insert_statement), **item)

if __name__ == '__main__':

	# TESTING sql_handler...
	from file_handling.file_handler import FileHandler

	postgres     = PostgresHandler()
	file_handler = FileHandler()
	PATH         = "D:\PROJECTS\Examination_project\data\countries.csv"
	data         = file_handler.get_csv_data(file_path = PATH)

	# -------------------------------------------------------------------------------
	create_table = 'CREATE TABLE if not exists countries(country_id text, ' \
	               'country_name text, ' \
	               'region_id integer' \
	               ');'
	postgres.execute_create(create_statement = create_table)

	# -------------------------------------------------------------------------------
	file_name   ='countries.csv'
	insert_into = 'INSERT INTO countries(country_id , country_name , region_id)' \
	              'VALUES(:country_id, :country_name, :region_id);'
	mapping     = {file_name: insert_into}
	data_dict   = data.to_dict(orient='records')

	postgres.execute_insert(insert_statement = mapping.get(file_name), d = data_dict)