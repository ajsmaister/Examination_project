"""
This file is responsible for storing the SELECT, and UPDATE statements
"""
select_statements =[
    """SELECT 
        CONCAT(first_name, ' ', last_name) AS name,
        employees.salary,
        jobs.min_salary,
        jobs.max_salary,
        jobs.job_title
        FROM employees
        RIGHT OUTER JOIN jobs 
        ON employees.job_id = jobs.job_id;""",
    # ------------------------------------------------------------
    # here you can add more selects....
                    ]