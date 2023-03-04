"""
This file is responsible for storing the SELECT, and UPDATE statements
"""
select_statements =[
    """UPDATE employees
        SET salary = salary * (1 + random() * 0.03 + 0.05);""",
    # ------------------------------------------------------------
    """SELECT
        AVG(salary) as avr_salary
        FROM employees;""",
    # ------------------------------------------------------------
    """SELECT
    MAX(max_salary) as maximum_salary
    FROM jobs;""",
    # ------------------------------------------------------------
    """SELECT
    MIN(min_salary) as minimum_salary
    FROM jobs;""",
    #------------------------------------------------------------
    """SELECT 
        CONCAT(first_name, ' ', last_name) AS name,
        employees.salary,
        jobs.max_salary,
        jobs.job_title
        FROM employees
        RIGHT OUTER JOIN jobs 
        ON employees.job_id = jobs.job_id;""",
    # ------------------------------------------------------------
    # here you can add more selects....
                    ]