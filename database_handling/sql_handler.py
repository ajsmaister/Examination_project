
import psycopg2
from sqlalchemy import create_engine, text
from parameters import POSTGRES_KEY


class PostgresHandler:
	"""
	This class handling the database operations like CREATE, INSERT, SELECT...
	"""
	postgres_url = POSTGRES_KEY
	conn         = psycopg2.connect(POSTGRES_KEY)

	def __init__(self):
		self.engine = create_engine(self.postgres_url)


	def execute_create(self, create_statement):
		with self.engine.connect() as conn:
			conn.execute(create_statement)


	def execute_insert(self, insert_statement, d):
		for item in d:
			with self.engine.connect() as conn:
				conn.execute(text(insert_statement), **item)


	def execute_insert_new_data(self, creation_order, data, insert_statement):
		for item in creation_order:
			with self.engine.connect() as conn:
				conn.execute(insert_statement[item], data[item])


	def execute_query_on_db(self, query):
		cursor = self.conn.cursor()
		return cursor.execute(query)


	def execute_get_data_from_db(self, select):
		cursor = self.conn.cursor()
		cursor.execute(select)

		cols = [desc[0] for desc in cursor.description]
		rows = cursor.fetchall()

		data = {'cols': cols,
		        'rows': rows}
		return data


