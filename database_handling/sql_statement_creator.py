
from file_handling.file_handler import FileHandler
# -------------------------------------------------------------------------------
class CreationRules:

	file_handler    = FileHandler()
	data_properties = file_handler.file_inspector()

	@staticmethod
	def columns_name_validator(cols):
		"""
		This func. inspect the columns name in {.csv} file data
		by validation_list values.

		:param cols: From create_statement() func. take over it
		:return    : Repaired column names in cols list
		"""
		validation_list = ['!', '"', '#', '%', '&',
		                   "'", '(', "(", "*", "+",
		                   "-", "/", ":", ";", "<",
		                   "=", ">", "?", "[", "\\",
		                   "]", "^", "{", "|", "}",
		                   " ", "$", "Ł"
		                   ]
		temp = []
		for item in cols:
			temp.append(item.lower())

		wrong_col_names            = []

		for col_name in temp:
			for idx, item in enumerate(col_name):
				if item in validation_list:
					idx_wrong_col_name_in_temp = temp.index(col_name)
					wrong_col_names.append(col_name)
					idx = validation_list.index(item)
					char = validation_list[idx]
					aplhabets = []
					index = col_name.index(char)
					for i in col_name:
						aplhabets.append(i)
					aplhabets[index] = "_"
					if aplhabets[0].isnumeric() is True:
						num = "_" + aplhabets[0]
						del aplhabets[0]
						aplhabets.append(str(num))
					rep_col_name = "".join(aplhabets)
					temp[idx_wrong_col_name_in_temp] = rep_col_name
				else:
					continue
		return temp


	def creation_rules(self):
		"""
		Here you can add the Tables properties:

					- Primary keys;
					- Foreign keys;
					- creation_oreder.

		In this func. add the REQUIRED FOREIGN KEYS these keys determinated the
		running order, and it adds the PRIMARY KEYS to sessions, also.
		Finally, in this func. you can add the running order to {manager.py}
		by modifing of {self.data_properties['file_list']}
		as creation_order.

		:return: The enriched {data_properties dict} with the determinated creation rules.
		:rtype : dict
		"""
		# This list determinated the running order in {manager.py} by foreign_key connection within sessions ...
		# ['countries', 'departments', 'employees', 'jobs', 'job_history', 'locations', 'regions']

		creation_order = [
			self.data_properties['file_list'][6],  # 0 <-- 'regions.csv'
			self.data_properties['file_list'][0],  # 1 <-- 'countries.csv'
			self.data_properties['file_list'][5],  # 2 <-- 'locations.csv'
			self.data_properties['file_list'][1],  # 3 <-- 'departments.csv'
			self.data_properties['file_list'][2],  # 4 <-- 'employee.csv'
			self.data_properties['file_list'][4],  # 5 <-- 'job_history.csv'
			self.data_properties['file_list'][3],  # 6 <-- 'jobs.csv'
		]
		# ['regions', 'countries', 'locations', 'departments', 'employees', 'job_history', 'jobs']

		# Here add primary key to tables...
		primary_key_dict = {
			"regions": "region_id",
			"countries": "country_id",
			"locations": "location_id",
			"departments": "department_id",
			"employees": "employee_id",
			"job_history": "",
			"jobs": "",
		}
		# Here add Foreign keys as a table connection parametre in order to complex filtering ways...
		foreign_key_dict = {
			# "countries": {
			# 	"regions": "region_id"
			# },
			# "locations": {
			# 	"countries": "country_id"
			# },
			# "departments": {
			# 	"locations": "location_id"
			# },
			# "employees": {
			# 	"departments": "department_id",
			# },
			# "jobs": {
			# 	"departments": "department_id",
			# },
			# "job_history": {
			# 	"departments": "department_id",
			# },
		}
		if foreign_key_dict != {}:
			self.data_properties['file_list'] = creation_order
		if primary_key_dict is not None:
			self.data_properties['primary_key'] = primary_key_dict
		if foreign_key_dict is not None:
			self.data_properties['foreign_key'] = foreign_key_dict

		return self.data_properties


	def create_statement(self):
		"""
		This func. creates the CREATE TABLE statements dinamically.

		:return: A creation_statement list
		:rtype : list
		"""
		creation_statement_list = []
		foreign_key_statements  = []

		for i in self.data_properties['file_list']:

			data = self.file_handler.get_csv_data(file_path = self.data_properties['file_path'][i])
			cols = self.file_handler.get_columns_name_from_csv(df = data)
			# print(cols)

			columns_name = self.columns_name_validator(cols = cols)

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
			# Table  and foreign key create ...
			cnt = 0
			for idx, item in enumerate(columns_name):
				if self.data_properties['primary_key'] != {}:
					try:
						if cnt == len(columns_name) -1:
							if item == self.data_properties['primary_key'][i]:
								statement += f'{item} {data_types[idx]} NOT NULL PRIMARY KEY);'
							else:
								statement += f'{item} {data_types[idx]});'
						else:
							if item == self.data_properties['primary_key'][i]:
								statement += f'{item} {data_types[idx]} NOT NULL PRIMARY KEY, '
							else:
								statement += f'{item} {data_types[idx]}, '
						cnt += 1

					except Exception as e:
						print(f"{str(e)}The {i}.csv has no determinated Primary key\n")
				else:
					try:
						if cnt == len(columns_name) -1:
							statement += f'{item} {data_types[idx]});'
						else:
							statement += f'{item} {data_types[idx]}, '
						cnt += 1

					except Exception as e:
						print(f"{str(e)}The {i}.csv has no determinated Primary key\n")
			creation_statement_list.append(statement)

			# ------------------------------------------------------------------------- from this point it is also correct!
			# FOREIGN KEY appends...
			if i in self.data_properties['foreign_key']:
				# print(i)

				length = len(self.data_properties['foreign_key'])
				cnt    = 0

				for k, v in self.data_properties['foreign_key'].items():
					if k == i:
						nums = len(self.data_properties['foreign_key'][i].items())
						# print(nums)
						cnt = 0
						for item in range(nums):
							if nums ==1:
								for key, value in self.data_properties['foreign_key'][i].items():
									foreign_key = f"FOREIGN KEY ({value}) REFERENCES {key} ({value}) ON UPDATE CASCADE ON DELETE CASCADE"
									statement = foreign_key
							else:
								statement = ""
								counter = 0
								for key, value in self.data_properties['foreign_key'][i].items():
									if counter < (nums-1):
										foreign_key = f"FOREIGN KEY ({value}) REFERENCES {key} ({value}) ON UPDATE CASCADE ON DELETE CASCADE, "
										statement += foreign_key
									else:
										foreign_key = f"FOREIGN KEY ({value}) REFERENCES {key} ({value}) ON UPDATE CASCADE ON DELETE CASCADE"
										statement += foreign_key
									counter += 1

						foreign_key_statements.append(statement)

					else:
						continue
				if cnt == length:
					break
			else:
				print(f"The {i}.csv has no determinated Foreign key")
				foreign_key_statements.append("")

		creation_statement = []
		for idx, item in enumerate(creation_statement_list):
			if self.data_properties['foreign_key'] == {}:
				creation_statement.append(item + "")
			else:
				if foreign_key_statements[idx] == "":
					creation_statement.append(item)
				else:
					creation_statement.append(item[:-2] +","+ foreign_key_statements[idx] + ");")

		return creation_statement


	def insert_statement(self):
		"""
		This func. creates the INSERT statements dinamically.
		:return: A list with the insertation_statements
		:rtype : list
		"""
		insert_statement_list = []
		for i in self.data_properties['file_list']:

			data = self.file_handler.get_csv_data(file_path=self.data_properties['file_path'][i])
			cols = self.file_handler.get_columns_name_from_csv(df=data)
			cols = self.columns_name_validator(cols = cols)

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

