
import math

def calculate_salary_options(avg, data):
	"""
	This func. responsible for data selection by the requirements and collect the JSON_FORM
	:param avg  : It is an average salary
	:param data : It is comes from database
	:return     : JSON_FORM
	:rtype      : .json file
	"""
	average_salary= math.ceil(float(avg))
	rows = data['rows']

	JSON_FORM = {}
	validated_salaries = []
	best_salaries_per_positions  = []
	worst_salaries_per_positions = []
	salaries = []

	for item in rows:
		if math.ceil(float(item[1])) > int(item[2]):
			salary = item[2]
		else:
			salary = math.ceil(float(item[1]))

		salaries.append(salary)

	sorted_salary = sorted(salaries)
	sorted_salary.reverse()

	for item in rows:
		if math.ceil(float(item[1])) >= int(item[2]):
			validation = [item[0], math.ceil(float(item[2])), item[3]]
		else:
			validation = [item[0], math.ceil(float(item[1])), item[3]]
		validated_salaries.append(validation)

	JSON_FORM["differences"] = {
        "best_salary"   : max(salaries) ,
        "worst_salary"  : min(salaries),
		"average_salary": average_salary,
        "difference"    : max(salaries) - min(salaries)
    }

	for item in validated_salaries:
		if math.ceil(float(item[1])) in sorted_salary[:9]:
			best = {'name'    : item[0],
			        'salary'  : math.ceil(float(item[1])),
			        'position': item[2]
			        }
			best_salaries_per_positions.append(best)
		elif math.ceil(float(item[1])) in sorted_salary[-8:]:
			worst = {'name'   : item[0],
			        'salary'  : math.ceil(float(item[1])),
			        'position': item[2]
			         }
			worst_salaries_per_positions.append(worst)

	# collect the {.json} form ...
	JSON_FORM["best_salaries_per_positions"]  = best_salaries_per_positions
	JSON_FORM["worst_salaries_per_positions"] = worst_salaries_per_positions

	return JSON_FORM






