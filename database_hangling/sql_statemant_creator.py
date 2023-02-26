
from file_handling.file_handler import FileHandler

Test            = FileHandler()
data_properties = Test.file_inspector() # <-- It is a dict!

def columns_name_validator(cols):
	for item in cols:
		if " " in item:
			item.replace(" ", "_")
			item.lower()


def create_statement():
	create_statement_list = []
	for i in data_properties['file_list']:
		data = Test.get_csv_data(file_path = data_properties['file_path'][i])
		cols = Test.get_columns_name_from_csv(d = data)

		columns_name_validator(cols)

		data_types = []
		for key, val in data.dtypes.to_dict().items():
			if val == 'object':
				val = "text"
				data_types.append(val)
			elif 'int' in str(val):
				val = "integer"
				data_types.append(val)
			elif 'float' in str(val):
				val = "numeric"
				data_types.append(val)
			else:
				val = "text"
				data_types.append(val)

		statement = f'CREATE TABLE if not exists {i}('

		cnt = 0
		# this loop does the creation statement ...
		for idx, item in enumerate(cols):
			if cnt == len(cols ) -1:
				statement += f'{str(item)} {data_types[idx]});'
			else:
				statement += f'{str(item)} {data_types[idx]}, '
			cnt += 1

		create_statement_list.append(statement)

	return create_statement_list


def insert_statement():
	...

if __name__ == '__main__':
	create_statement()
