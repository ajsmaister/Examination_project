
from file_handling.file_handler import FileHandler

file_handler            = FileHandler()
data_properties         = file_handler.file_inspector()
print(data_properties)

foregin_key_dict = {}

def columns_name_validator(cols):
	"""
	This func. inspect the columns name in {.csv} file data
	:param cols: From create_statement() func. take over it
	:return    : Repaired column names in cols list
	"""
	for item in cols:
		if " " in item:
			item.replace(" ", "_")
			item.lower()


def create_statement():
	"""
	This func. creates the CREATE TABLE statements dinamically.
	:return: A creation_statement list
	:rtype : list
	"""
	creation_statement_list = []

	for i in data_properties['file_list']:

		data = file_handler.get_csv_data(file_path = data_properties['file_path'][i])
		cols = file_handler.get_columns_name_from_csv(df = data)

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
		for idx, item in enumerate(cols):
			try:
				if cnt == len(cols) -1:
					if item == data_properties['primary_key'][i]:
						statement += f'{item} {data_types[idx]} PRIMARY KEY);'
					else:
						statement += f'{item} {data_types[idx]});'
				else:
					if item == data_properties['primary_key'][i]:
						statement += f'{item} {data_types[idx]} PRIMARY KEY, '
					else:
						statement += f'{item} {data_types[idx]}, '
				cnt += 1
			except Exception as e:
				print(f"{str(e)}The {i}.csv has no determinated Primary key")

		creation_statement_list.append(statement)
		# break

	return creation_statement_list


def insert_statement():
	"""
	This func. creates the INSERT statements dinamically.
	:return: A list with the insertation_statements
	:rtype : list
	"""
	insert_statement_list = []
	for i in data_properties['file_list']:

		data = file_handler.get_csv_data(file_path=data_properties['file_path'][i])
		cols = file_handler.get_columns_name_from_csv(df = data)

		columns_name_validator(cols)

		statement = f'INSERT INTO {i}('

		cnt = 0
		# this loop does the insertion statement ...
		for idx, item in enumerate(cols):
			if cnt == len(cols) - 1:
				statement += f'{str(item)})VALUES('
				cnt = 0
				for i in cols:
					if cnt == len(cols)-1:
						statement += f':{i});'
					else :
						statement += f':{i}, '
					cnt += 1
			else:
				statement += f'{str(item)} , '
			cnt += 1
		insert_statement_list.append(statement)

	return insert_statement_list

if __name__ == '__main__':
	import pprint
	creation = create_statement()
	pprint.pprint(creation)
	insertion = insert_statement()
	pprint.pprint(insertion)
