/********************************************************************************************************************
 *                                                                                                                  *
 *                               This file containts the neccessary PostgreSQL statements...                        *
 *                                                                                                                  *
*********************************************************************************************************************/

----- TABLE CREATION STATEMENTS ----------------------------------------------------------------------------------------

CREATE TABLE if not exists regions(
region_id integer PRIMARY KEY,
region_name text
);
CREATE TABLE if not exists countries(
country_id text PRIMARY KEY,
country_name text,
region_id integer,FOREIGN KEY (region_id) REFERENCES regions (region_id) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE if not exists locations(
location_id integer PRIMARY KEY,
street_address text,
postal_code text,
city text,
state_province text,
country_id text,FOREIGN KEY (country_id) REFERENCES countries (country_id) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE if not exists departments(
department_id integer PRIMARY KEY,
department_name text,
manager_id numeric,
location_id integer,
FOREIGN KEY (location_id) REFERENCES locations (location_id) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE if not exists jobs(
job_id text PRIMARY KEY,
job_title text,
min_salary numeric,
max_salary numeric
);
CREATE TABLE if not exists employees(
employee_id integer PRIMARY KEY,
first_name text,
last_name text,
email text,
phone_number text,
hire_date text,
job_id text,
salary numeric,
commission_pct numeric,
manager_id numeric,
department_id numeric,
FOREIGN KEY (job_id) REFERENCES jobs (job_id) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (department_id) REFERENCES departments (department_id) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE if not exists job_history(
employee_id integer,
start_date text,
end_date text,
job_id text,
department_id integer,
FOREIGN KEY (employee_id) REFERENCES employees (employee_id) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (job_id) REFERENCES jobs (job_id) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (department_id) REFERENCES departments (department_id) ON UPDATE CASCADE ON DELETE CASCADE
);

----- INSERTION STATEMENTS ---------------------------------------------------------------------------------------------

INSERT INTO countries(country_id , country_name , region_id)
VALUES(
:country_id,
:country_name,
:region_id
);
INSERT INTO locations(location_id , street_address , postal_code , city , state_province , country_id)
VALUES(
:location_id,
:street_address,
:postal_code,
:city,
:state_province,
:country_id
);
INSERT INTO departments(department_id , department_name , manager_id , location_id)
VALUES(
:department_id,
:department_name,
:manager_id,
:location_id
);
INSERT INTO employees(employee_id , first_name , last_name , email , phone_number , hire_date , job_id , salary , commission_pct , manager_id , department_id)
VALUES(
:employee_id,
:first_name,
:last_name,
:email,
:phone_number,
:hire_date,
:job_id,
:salary,
:commission_pct,
:manager_id,
:department_id
);
INSERT INTO jobs(job_id , job_title , min_salary , max_salary)
VALUES(
:job_id,
:job_title,
:min_salary,
:max_salary
);
INSERT INTO job_history(employee_id , start_date , end_date , job_id , department_id)
VALUES(
:employee_id,
:start_date,
:end_date,
:job_id,
:department_id
);

INSERT INTO regions(region_id , region_name)
VALUES(
:region_id,
:region_name
);

----- SELECTION STATEMENTS ---------------------------------------------------------------------------------------------

-- This select create the growed salary of employees ...
UPDATE employees
SET salary = salary * (1 + random() * 0.03 + 0.05);

-- This select creates the avarage salary ...
SELECT
AVG(salary) as avr_salary
FROM employees;

-- This select creates the maximum salary ...
SELECT
MAX(max_salary) as maximum_salary
FROM jobs;

-- This select creates the minimum salary  ...
SELECT
MIN(min_salary) as minimum_salary
FROM jobs;

-- This select returns the information to calculate the salary of growing ...
SELECT
CONCAT(first_name, ' ', last_name) AS name,
employees.salary,
jobs.max_salary,
jobs.job_title
FROM employees
RIGHT OUTER JOIN jobs
ON employees.job_id = jobs.job_id;
