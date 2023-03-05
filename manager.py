import os
from file_handling.file_handler import FileHandler
from database_handling.sql_statement_creator import CreationRules
from database_handling.sql_handler import PostgresHandler
from database_handling.selects import select_statements
from calculator.calculate import calculate_salary_options
from database_handling.new_insertion import (
	data_to_insert,
	insertion_statements_for_news
)

def runtime(func):
	import time

	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()

		print("\nThe {} func. run time was: {} seconds till end".format(func.__name__.upper(), end_time - start_time))
		return result

	return wrapper

@runtime
def examination_task_manager():
	"""
	This func. responsible for the magagement of program that data have been inserted into the Postgres database.
	:return: Loaded data into the database, and a {.json} file in the {json_folder}...
	:rtype: .json file
	"""
	file_handler = FileHandler()
	postgres = PostgresHandler()
	sql_statements = CreationRules()
	sql_creation_rules = sql_statements.creation_rules()
	creation_statements = sql_statements.create_statement()
	insertation_statements = sql_statements.insert_statement()
	select_statement = select_statements
	# --------------------------------------------------------

	for idx, i in enumerate(sql_creation_rules['file_list']):

		data = file_handler.get_csv_data(file_path=sql_creation_rules['file_path'][i])

		try:
			postgres.execute_create(create_statement=creation_statements[idx])

			print(f" The '{sql_creation_rules['file_list'][idx].upper()}' table is created!")
		except Exception as e:
			print(f'Error in "sql_handler.py" during TABLE CREATING  process: {str(e)}')

		# create mapping to insertion...
		file_name = sql_creation_rules['file_list'][idx] + ".csv"
		insert_into = insertation_statements[idx]
		mapping = {file_name: insert_into}

		data_dict = data.to_dict(orient='records')

		try:
			postgres.execute_insert(
				insert_statement=mapping.get(file_name),
				d=data_dict
			)
			print(f" The data from the '{sql_creation_rules['file_list'][idx]}.csv' file has been inserted...")
		except Exception as e:
			print(f'Error in "sql_handler.py" during INSERTION  process: {str(e)}')
	print('-----------------------------------')
	# here add new employees into the database ...
	try:
		existing_data = postgres.execute_query_on_db(
			query="SELECT * FROM employees WHERE employee_id = '{}'".format(data_to_insert['employees'][0])
		)
		if not existing_data:
			postgres.execute_insert_new_data(
				creation_order=sql_creation_rules['file_list'],
				data=data_to_insert,
				insert_statement=insertion_statements_for_news
			)
	except Exception as e:
		print(str(e))


	# Modify data in database ...
	postgres.execute_query_on_db(query=select_statements[0])

	db_data = postgres.execute_get_data_from_db(select=select_statement[0])

	# create {.json} forms with requirements...
	json_data = calculate_salary_options(data=db_data)

	# create{json_folder} and write{.json} files into the folder...
	json_folder_path = os.path.join(os.path.dirname(__file__), "json_folder")

	file_handler.write_json(
		path=json_folder_path,
		data=json_data
	)


if __name__ == '__main__':
	examination_task_manager()
