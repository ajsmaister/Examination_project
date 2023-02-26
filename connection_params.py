import os
import pprint

POSTGRES_KEY = ""

def data_path():
	"""
	This func create The data folder path.
	:return: data_path
	"""
	data_path = os.path.join(os.path.dirname(__file__), 'data')

	return data_path

if __name__ == '__main__':
	pprint.pprint(data_path())