
from parameters import data_path
from file_handling.file_handler import FileHandler
from database_handling.sql_statemant_creator import create_statement, insert_statement
from database_handling.sql_handler import PostgresHandler

if __name__ == '__main__':

	# RUNNING The Main flow...
	data_folder_path       = data_path()
	file_handler           = FileHandler()
	data_properties        = file_handler.file_inspector()
	creation_statements    = create_statement()
	insertation_statements = insert_statement()
	postgres               = PostgresHandler()

	# print(data_properties) # <-- Only Debugging!

	for idx, i in enumerate(data_properties['file_list']):

		data = file_handler.get_csv_data(file_path=data_properties['file_path'][i])
		coll = file_handler.get_columns_name_from_csv(df = data)
		rows = file_handler.get_rows_from_csv(df = data)

		try:
			postgres.execute_create(create_statement = creation_statements[idx])
			print(f" The '{data_properties['file_list'][idx].upper()}' table is created!")
		except Exception as e:
			print(f'Error in "sql_handler.py" during TABLE CREATING  process: {str(e)}')

		# create mapping to insertion...
		file_name   = data_properties['file_list'][idx] +".csv"
		insert_into = insertation_statements[idx]
		mapping     = {file_name: insert_into}

		data_dict   = data.to_dict(orient = 'records')

		try:
			postgres.execute_insert(
				insert_statement = mapping.get(file_name),
				d = data_dict
			)
			print(f" The data from the '{data_properties['file_list'][idx]}.csv' file has been inserted...")
			print('--------------------------')
		except Exception as e:
			print(f'Error in "sql_handler.py" during INSERTION  process: {str(e)}')

	r = input(('Nyomj le egy betűt, hogy kilépjek!'))

