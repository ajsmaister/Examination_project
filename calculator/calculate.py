
import pprint
import math
from random import randint


def calculate_salary_options(data):
	"""
	This func. responsible for data selection by the requirements and collect the JSON_FORM

	:param data : It is comes from database
	:return     : JSON_FORM
	:rtype      : .json file
	"""
	rows      = data['rows']
	JSON_FORM = {}
	best_salaries_per_positions  = []
	worst_salaries_per_positions = []
	salaries  = []
	five_perc_peersons   = []
	enhanced_salary_list = []
	maximum_enhancing_perc = 5

	# get that persons, who do NOT earn more than the minimum salary, and create a salaries list...
	for item in rows:
		if math.ceil(float(item[1])) == int(item[2]):
			five_perc_peersons.append(item[0])
			salary = item[1]
		else:
			salary = math.ceil(float(item[1]))
		salaries.append(int(salary))

	five_perc_peersons = list(set(five_perc_peersons))

	sorted_salary = sorted(salaries)
	sorted_salary.reverse()
	median_salary = int(sum(sorted_salary) /len(sorted_salary))

	# in order to clear memory...
	del sorted_salary

	# Calculate the salary enrichment by requirements...
	for item in rows:
		if (math.ceil(float(item[1])) > median_salary) and (item[1] < math.ceil(float(item[1])) * (1 + randint(3, 5) / 100)):
			ran = (1 + randint(3, 5) / 100)
			best = {'name'    : item[0],
			        'salary'  : math.ceil(float(item[1])) * ran,
			        'position': item[4],
			        'percentage of salary analysis': str(int(ran *100)-100) + ' %'
			        }
			enhanced_salary_list.append(best['salary'])
			best_salaries_per_positions.append(best)
		elif (math.ceil(float(item[1])) > median_salary) and (item[1] > math.ceil(float(item[1])) * (1 + randint(3, 5) / 100)):
			best = {'name'    : item[0],
			        'salary'  : item[3],
			        'position': item[4],
			        'percentage of salary analysis': 'no analysis'
			        }
			enhanced_salary_list.append(best['salary'])
			best_salaries_per_positions.append(best)

		elif (math.ceil(float(item[1])) < median_salary) and (item[0] in five_perc_peersons):
			worst = {'name'   : item[0],
			         'salary' : math.ceil(float(item[1])) + (math.ceil(float(item[1])) / 100) * maximum_enhancing_perc,
			         'position': item[4],
			         'percentage of salary analysis': maximum_enhancing_perc
			         }
			enhanced_salary_list.append(worst['salary'])
			worst_salaries_per_positions.append(worst)

		elif (math.ceil(float(item[1])) < median_salary) and (item[0] not in five_perc_peersons):
			ran = (1 + randint(3, 5) / 100)
			worst = {'name'    : item[0],
			         'salary'  : math.ceil(float(item[1])) * ran,
			         'position': item[4],
			         'percentage of salary analysis': str(int(ran *100)-100) + ' %'
			         }
			enhanced_salary_list.append(worst['salary'])
			worst_salaries_per_positions.append(worst)

	# in order to clear memory and avoid the duplications in {JSON_FORM}...
	del rows

	print(enhanced_salary_list)
	JSON_FORM["differences"] = {
		"best_salary": max(enhanced_salary_list),
		"worst_salary": min(enhanced_salary_list),
		"difference": max(enhanced_salary_list) - min(enhanced_salary_list)
	}
	del enhanced_salary_list
	# collect the {.json} form ...
	JSON_FORM["best_salaries_per_positions"]  = best_salaries_per_positions
	JSON_FORM["worst_salaries_per_positions"] = worst_salaries_per_positions

	pprint.pprint(JSON_FORM)
	return JSON_FORM






