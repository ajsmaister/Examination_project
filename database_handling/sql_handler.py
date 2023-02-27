
from sqlalchemy import create_engine
from database_handling.connection_params import POSTGRES_KEY


class PostgresHandler:

	postgres_url = POSTGRES_KEY

	def __init__(self):
		self.engine = create_engine(self.postgres_url)
		self.curs = self.engine
		self.query = None

	def execute_create(self, create_statement):
		with self.engine.connect()as conn:
			try:
				conn.execute(create_statement)
			except Exception as e:
				print(str(e))

	def execute_insert(self, insert_statement, data):
		...

if __name__ == '__main__':
	...

