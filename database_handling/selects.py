select_statements =[
    """UPDATE employees
        SET salary = salary * (1 + random() * 0.03 + 0.05);""",
    #------------------------------------------------------------
    """SELECT 
        employees.employee_id, 
        employees.first_name, 
        employees.last_name,
        employees.salary,
        jobs.max_salary,
        jobs.job_title,
        FROM employees
        RIGHT OUTER JOIN jobs 
            ON employees.job_id = jobs.job_id;""",
                    ]