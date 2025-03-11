# Part A - Creating Tables and defining attribute contraints

CREATE DATABASE company;

USE company;

DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
	 fname VARCHAR(15) NOT NULL, 
	 minit CHAR,
	 lname VARCHAR(15) NOT NULL,
	 ssn VARCHAR(9) NOT NULL,
	 bdate DATE,
	 address VARCHAR(50),
	 sex CHAR,
	 salary DECIMAL(10,2) CHECK (salary > 0),
	 super_ssn VARCHAR(9),
	 dno INTEGER DEFAULT 1,
CONSTRAINT emp_pk
PRIMARY KEY (ssn)
);


DROP TABLE IF EXISTS dependent;

CREATE TABLE dependent (
	 essn VARCHAR(9) NOT NULL,
	 dependent_name VARCHAR(15) NOT NULL,
	 sex CHAR,
	 bdate DATE,
	 relationship VARCHAR(8),
CONSTRAINT dependent_pk
PRIMARY KEY (essn, dependent_name)
);

DROP TABLE IF EXISTS department;

CREATE TABLE department (
	 dname VARCHAR(25) NOT NULL,
	 dnumber INTEGER NOT NULL,
	 mgr_ssn VARCHAR(9), 
	 mgr_start_date DATE,
 
 CONSTRAINT dept_pk
 PRIMARY KEY (dnumber),
 
 CONSTRAINT dept_unique
 UNIQUE (dname)
 
);

DROP TABLE IF EXISTS dept_locations;
CREATE TABLE dept_locations (
	 dnumber INTEGER NOT NULL,
	 dlocation VARCHAR(15) NOT NULL,
     
 CONSTRAINT dept_loc_pk
 PRIMARY KEY (dnumber, dlocation)
);

DROP TABLE IF EXISTS project;
CREATE TABLE project (
	 pname VARCHAR(25) NOT NULL,
	 pnumber INTEGER NOT NULL,
	 plocation VARCHAR(15),
	 dnum INTEGER, 

 CONSTRAINT project_pk
 PRIMARY KEY (pnumber),
 
 CONSTRAINT project_unique
 UNIQUE (pname)
);

DROP TABLE IF EXISTS works_on;
CREATE TABLE works_on (
	 essn VARCHAR(9) NOT NULL,
	 pno INTEGER NOT NULL,
	 hours DECIMAL(4,1),
 CONSTRAINT works_on_pk
 PRIMARY KEY (essn,pno)
);

# Part B - Adding Referential Integrity Constraints

ALTER TABLE employee
	ADD CONSTRAINT emp_super_fk
		FOREIGN KEY (super_ssn) REFERENCES employee(ssn)
			ON DELETE SET NULL
			ON UPDATE CASCADE,
	ADD CONSTRAINT emp_dept_fk
		FOREIGN KEY (Dno) REFERENCES department(dnumber)
			ON DELETE SET NULL
			ON UPDATE CASCADE;
            
ALTER TABLE dependent
	ADD CONSTRAINT dependent_fk
		FOREIGN KEY (essn) REFERENCES employee(ssn)
			ON DELETE RESTRICT
			ON UPDATE CASCADE;
            
# Department relation:
ALTER TABLE department
	ADD CONSTRAINT dept_mgr_fk
		FOREIGN KEY (mgr_ssn) REFERENCES employee(ssn)
			ON DELETE SET NULL
			ON UPDATE CASCADE;
            
# Department locations relation:
ALTER TABLE dept_locations
	ADD CONSTRAINT dept_loc_fk
		FOREIGN KEY (dnumber) REFERENCES department(dnumber)
			ON DELETE RESTRICT
			ON UPDATE CASCADE;

# Project relation:
ALTER TABLE project
	ADD CONSTRAINT project_fk
		FOREIGN KEY (dnum) REFERENCES department(dnumber)
			ON DELETE RESTRICT
			ON UPDATE CASCADE;

# Works on relation:
ALTER TABLE works_on
	ADD CONSTRAINT works_on_ssn_fk
		FOREIGN KEY (essn) REFERENCES employee(ssn)
			ON DELETE RESTRICT
			ON UPDATE CASCADE,
	ADD CONSTRAINT works_on_pno_fk
		FOREIGN KEY (pno) REFERENCES project(pnumber)
			ON DELETE RESTRICT
			ON UPDATE CASCADE;
            
            
# Day 2 (Lesson 7.1 and lab 0) - Insert
use company;

INSERT INTO employee
VALUES ('Richard', 'K', 'Marini', '656565656', '1962-12-30', '100 Main Str, Ruston, LA', 'M', 37000, '123456789', 5);

# show the whole table
SELECT * FROM employee;

# updating values
UPDATE employee
SET salary=40000
WHERE ssn = '656565656';

UPDATE employee
SET salary = salary * 1.1
WHERE dno='5';

# deleting values
DELETE FROM employee
WHERE ssn='656565656' or ssn = '777777770';

# don't every type DELETE FROM employee . This would delete all of the tuples in the table. Not the table though.

## select - the most commonly used
SELECT  *
FROM	employee
WHERE	dno='5';

SELECT bdate, address
FROM employee
WHERE fname='John' AND minit = 'B' AND lname='Smith';

# using select when trying to join two tables
# SELECT first name, lastname, and address of all employees who work for the research department.
SELECT fname, lname, address
FROM employee, department
WHERE dname='Research' AND dnumber = dno;  # note that dnumber is the PK in department and dno is the FK. The order doesn't matter. 

# we can specify the table it is coming from using aliasing
# he expects us to use this notation in the assignments (labs and projects)
SELECT e.fname, e.lname, e.address
FROM employee e, department d			# renames employee as e and department as d
WHERE d.dname='Research' AND d.dnumber = e.dno;

# we can rename stuff too
SELECT e.fname as first_name, e.lname as last_name, e.address
FROM employee e, department d			# renames employee as e and department as d
WHERE d.dname='Research' AND d.dnumber = e.dno;

# Select last_name, address, and birth date of employees who manage departments with projects located in Stafford
# step by step process of how to get to the result.
# step 1 - look at the project table
SELECT *
FROM project;

# step 2 - select only the rows where the plocation is Stafford
SELECT *
FROM project
WHERE plocation='Stafford';

# step 3 - cartesian product with department
SELECT *
FROM project, department
WHERE plocation='Stafford';

# step 4 - incorporate the equality to eliminate the non-relevent results from the cartesian product
SELECT *
FROM project p, department d
WHERE p.plocation='Stafford' AND p.dnum=d.dnumber;

# step 5 - incorporate employee and eliminate the not neccessary rows with another AND plus equality
SELECT *
FROM project p, department d, employee e
WHERE p.plocation='Stafford' AND p.dnum=d.dnumber AND e.ssn = d.mgr_ssn;

# step 6 - do the projection to narrow down the columns
SELECT lname, address, bdate
FROM project p, department d, employee e
WHERE p.plocation='Stafford' AND p.dnum=d.dnumber AND e.ssn = d.mgr_ssn;
# note that duplicates are possible.  to remove the duplicates do the following

# step 7 - do the projection
SELECT DISTINCT e.lname, e.address, e.bdate
FROM project p, department d, employee e
WHERE p.plocation='Stafford' AND p.dnum=d.dnumber AND e.ssn = d.mgr_ssn;

# note that aliasing is required when doing recursive relationships

## Another Example:
# Select first name and last name of employees and their supervisors

# cartesian product of employee with itself
SELECT *
FROM employee e, employee s;

# narrow it down
SELECT *
FROM employee e, employee s
WHERE e.super_ssn = s.ssn;

/* selecting only the first name and last name and renaming */
SELECT e.fname employee_fname, e.lname employee_lname, s.fname supervisor_fname, s.lname supervisor_lname
FROM employee e, employee s
WHERE e.super_ssn = s.ssn;


/* Example: SQL doesn't eliminate duplicates */
SELECT sex
FROM employee;

SELECT DISTINCT sex
FROM employee;

#Example of Cartesian Product
SELECT e.ssn, d.dname
FROM employee e, department d;

/* Example of giving the cartesian product meaning */
SELECT e.ssn, d.dname
FROM employee e, department d
WHERE e.ssn = d.mgr_ssn;  /* this was previously our select*/


/*Query 6. Select all attributes of employees who work in department number 5.*/
SELECT *
FROM employee
WHERE dno = 5;








