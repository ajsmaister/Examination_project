
from file_handling.file_handler import FileHandler
from database_hangling.sql_statemant_creator import create_statement


if __name__ == '__main__':
	file_handler = FileHandler()
	data_properties = file_handler.file_inspector() # <-- It is a dict!
	create_stat = create_statement()

	# This is the main flow: ....
	for idx, i in enumerate(data_properties['file_list']):
		data = file_handler.get_csv_data(file_path=data_properties['file_path'][i])
		print(data)
		print("---------------\n")
		coll = file_handler.get_columns_name_from_csv(d=data)
		# here comes the sql handler elements...

		print(create_stat[idx])
		break