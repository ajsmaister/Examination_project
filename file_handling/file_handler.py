
import os
import pandas as pd
from connection_params import data_path

class FileHandler:
	"""
		This class responsible for file operations, especially in connection with {.csv} files
		:param : {data} folder path from {.connection_params.py}
		:return: The {data_prop} dictionary with 'data_path', 'file_list' and 'file_path',
				 finally it returns the opened the {.csv} file by
		:rtype : dict, and data from {.csv} file
		"""
	conn_properties = data_path()

	def file_inspector(self):
		"""
		This func. inspect the incomming files extensions, and select {.csv} files only
		:return:  The selected {.csv} files properties from {datas} are collected as {data_prop} dictionary
				  together with 'folder_path' by.
		"""

		temp = os.listdir(str(self.conn_properties))

		file_list = []
		file_path_dict = {}
		for idx, item in enumerate(temp):
			if item[-4:] == '.csv':
				file_list.append(item[:-4])
				file_path_dict[item[:-4]] = os.path.join(self.conn_properties, str(item))
			else:
				continue

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
		return pd.read_csv(file_path)

	@staticmethod
	def get_columns_name_from_csv(d):
		colls = list(d.columns)
		return colls

if __name__ == '__main__':
	import pprint

	Test            = FileHandler()
	data_properties = Test.file_inspector() # <-- It is a dict!
	pprint.pprint(data_properties)
	print("---------------\n")

	# This is the main flow: ....
	for i in data_properties['file_list']:
		data = Test.get_csv_data(file_path = data_properties['file_path'][i])
		print(data)
		print("---------------\n")
		coll = Test.get_columns_name_from_csv(d = data)
		print(coll)
		print("---------------\n")
		print(data.dtypes)
		print("---------------\n")
		break

