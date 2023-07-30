USE company;

# Retrieve last name and SSN of employees whose birthday is in June.
SELECT lname, ssn
FROM employee
WHERE bdate LIKE '____-06-__';

# List first name, last name and salary of employees whose salary is greater than the salary of any employee in department 5.
SELECT fname,lname,salary
FROM employee
WHERE salary > ANY (SELECT salary 
				FROM employee
				WHERE dno=5);

# Show the resulting salaries if every employee working on the ‘ProductY’ project with a salary between $20000 and $45000 is given a 20% raise.
SELECT e.salary * 1.2 AS Changed_salary
FROM project p, works_on w, employee e
WHERE p.pname = 'ProductY' AND p.pnumber = w.pno AND (e.salary BETWEEN 20000 AND 45000) AND w.essn = e.ssn;

# Retrieve SSNs of all male employees who work on project numbers 1, 2, or 3.
SELECT DISTINCT ssn
FROM employee e, works_on w
WHERE e.ssn=w.essn AND e.sex='M' AND w.pno IN (1,2,3);

# For each project on which more than two employees work, retrieve project number, project name, and the average salary of employees who work on the project.
SELECT p.pnumber,p.pname, AVG(e.salary) AS Avg_salary 
FROM works_on w
JOIN employee e ON e.ssn=w.essn
JOIN project p ON p.pnumber=w.pno
GROUP BY p.pnumber, p.pname 
HAVING COUNT(*) > 2;