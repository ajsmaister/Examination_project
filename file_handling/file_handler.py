
import os
import pandas as pd
from parameters import data_path

class FileHandler:
	"""
		This class responsible for file operations, especially in connection with {.csv} files

		:param : {data} folder path from {.parameters.py}
		:return: The {data_prop} dictionary with 'data_path', 'file_list' and 'file_path',
				 finally it returns the opened the {.csv} file by
		:rtype : dict, lists and tuples from {.csv} file
		"""
	conn_properties = data_path()

	def file_inspector(self):
		"""
		This func. inspect the incomming paths, files extensions, and select {.csv} files to use.
		and determinated the TABLE CREATION RULES in order to table connection.

		:return: The selected {.csv} files properties from {datas} are collected as {data_prop} dictionary
				 together with 'folder_path' by.
		:rtype : dict
		"""
		try:
			if not os.path.exists(self.conn_properties):
				path_error = """This path: {path} \nDoes NOT exist!"""
				print(path_error.format(path = self.conn_properties))
				exit()

			if not os.path.isdir(self.conn_properties):
				path_error = """This path: {path} \nIs NOT a folder path!"""
				print(path_error.format(path = self.conn_properties))
				exit()

		except Exception as e:
			print(str(e))

		temp           = os.listdir(str(self.conn_properties))
		file_list      = []
		file_path_dict = {}

		for idx, item in enumerate(temp):
			if item[-4:] == '.csv':
				file_list.append(item[:-4])
				file_path_dict[item[:-4]] = os.path.join(self.conn_properties, str(item))

		data_prop = {
			'data_path': self.conn_properties,
			'file_list': file_list,
			'file_path': file_path_dict
		}

		return data_prop


	@staticmethod
	def get_csv_data(file_path):
		"""
		This func. open {.csv} files ONLY!
		:param file_path:
		:return: data of .csv file
		"""
		if os.path.isfile(file_path):
			try:
				if os.path.exists(file_path) :
					return pd.read_csv(file_path)
			except Exception as e:
				print(f'Error in "file_handler.py/get-data_from_csv func.: {str(e)}')
		else:
			pass

	@staticmethod
	def get_columns_name_from_csv(df):
		"""
		This func creates a colls list from the{.csv} data columns.
		:param df: dataframe from incomming data
		:return: cols
		:rtype : list
		"""
		col = list(df.columns)
		return col

	@staticmethod
	def get_rows_from_csv(df):
		"""
		This func creates a colls list from the{.csv} data columns.
		:param df: dataframe from incomming data
		:return  : rows
		:rtype   : List with tuples
		"""
		df_rows = list(df.itertuples(index = False, name  = None))
		return df_rows

	# @staticmethod
	# here comes the {.json} writer func!....

if __name__ == '__main__':

	# TESTING file_handler...
	import pprint
	PATH = data_path()
	Test = FileHandler()

	test_data_properties = Test.file_inspector() # <-- It is a dict!
	pprint.pprint(test_data_properties)
	test_path            = test_data_properties['file_path'][test_data_properties['file_list'][0]]
	# print(test_path)

	d    = Test.get_csv_data(test_path)
	cols = Test.get_columns_name_from_csv(df = d)
	rows = Test.get_rows_from_csv(df = d)

	# pprint.pprint(cols)
	# print('--------------------')
	# pprint.pprint(rows)
