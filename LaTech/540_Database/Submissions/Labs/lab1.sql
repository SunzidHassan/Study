USE company;

# Retrieve first name, last name, and date of birth of all male employees with salary less than 35000.
SELECT fname, lname, bdate
FROM employee
WHERE sex = 'M' AND salary < 35000;

# Retrieve project numbers and project locations of all projects that belong to the Administration department.
SELECT p.pnumber, p.plocation
FROM project p, department d
WHERE d.dnumber = p.dnum AND dname = 'Administration';

# Retrieve first name, last name, and SSN of all employees who work more than 10 hours on project 10.
SELECT fname, lname, ssn
FROM employee e, works_on w
WHERE e.ssn = w.essn AND w.pno = 10 AND w.hours > 10;

# Retrieve name, date of birth, and relationship of all male dependents of employees who work for department 5.
SELECT d.dependent_name, d.bdate, d.relationship
FROM employee e, dependent d
WHERE e.dno = 5 AND e.ssn = d.essn AND d.sex = 'M';

# Retrieve first name, last name, date of birth, and salary of employees who manage departments with projects located in Houston.
SELECT e.fname, e.lname, e.bdate, e.salary
FROM project p, department d, employee e
WHERE p.plocation = 'Houston' AND p.dnum = d.dnumber AND d.mgr_ssn = e.ssn;