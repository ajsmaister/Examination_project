
"""
This file is responsible for new arrival insertion in database from UI application, or manual insertion...
"""

data_to_insert = {
    "regions"    : [5, 'Sounth America'],
    "countries"  : ['C', 'Chile', 5],
    "locations"  : [2101, '2014 Chegewara Rd', '26056', 'REd squear', 'Arapaima', 'C'],
    "departments": [280, 'joga_instructor', 2101],
    "employees"  : [207, 'Gonzales', 'Nyunyoka', 'nyunyoka@sqltutorial.org', '715.123.0000', '2007-01-17',
                   'YO_INS', 5000.00, 0.3, 101, 280],
    "job_history": [280, '1998-03-24', '1998-12-31', 'YO_INS', 280],
    "jobs"       : ['YO_INS', 'Yoga instructor', 2000, 6000]
}

d = data_to_insert

insertion_statements_for_news = {
"regions": f"INSERT INTO regions (region_id,region_name) VALUES ("
           f"{d['regions'][0]},"
           f"'{d['regions'][1]}'"
           f");",
"countries": f"INSERT INTO countries (country_id,country_name,region_id) VALUES ("
             f"'{d['countries'][0]}',"
             f"'{d['countries'][1]}',"
             f"{d['countries'][2]}"
             f");",
"locations": f"INSERT INTO locations (location_id,street_address,postal_code,city,state_province,country_id) VALUES ("
             f"{d['locations'][0]},"
             f"'{d['locations'][1]}',"
             f"'{d['locations'][2]}',"
             f"'{d['locations'][3]}',"
             f"'{d['locations'][4]}',"
             f"'{d['locations'][5]}'"
             f");",
"departments": f"INSERT INTO departments (department_id,department_name,location_id) VALUES ("
               f"{d['departments'][0]},"
               f"'{d['departments'][1]}',"
               f"{d['departments'][2]}"
               f");",
"employees": f"INSERT INTO employees ("
             f"employee_id,first_name,last_name,email,phone_number,hire_date,job_id,salary,commission_pct,manager_id,department_id)"
             f"VALUES ("
             f"{d['employees'][0]},"
             f"'{d['employees'][1]}',"
             f"'{d['employees'][2]}',"
             f"'{d['employees'][3]}',"
             f"'{d['employees'][4]}',"
             f"'{d['employees'][5]}',"
             f"'{d['employees'][6]}',"
             f"{d['employees'][7]},"
             f"{d['employees'][8]},"
             f"{d['employees'][9]},"
             f"{d['employees'][10]}"
             f");",
"job_history": f"INSERT INTO job_history (employee_id,start_date,end_date,job_id,department_id) "
               f"VALUES ("
               f"{d['job_history'][0]},"
               f"'{d['job_history'][1]}',"
               f"'{d['job_history'][2]}',"
               f"'{d['job_history'][3]}',"
               f"{d['job_history'][4]});",
"jobs": f"INSERT INTO jobs (job_id, job_title, min_salary, max_salary) "
        f"VALUES ("
        f"'{d['jobs'][0]}',"
        f"'{d['jobs'][1]}',"
        f"{d['jobs'][2]},"
        f"{d['jobs'][3]});"
}
