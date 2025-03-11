use company;

/* Query 1 - Retrieve salary of every employee and all distinct salary values.*/
SELECT ALL Salary		/* ALL may not be necessary here, because it would select them all anyway. and include duplicates */
FROM EMPLOYEE;

SELECT DISTINCT Salary /* DISTINCT eleminates duplicates */
FROM EMPLOYEE;



/* Query 2 - Make a list of all project numbers for projects that involve an employee whose last name is ‘Smith’, 
either as a worker or as a manager of the department that controls the project.*/
(SELECT W.Pno
 FROM WORKS_ON W, EMPLOYEE E
 WHERE W.Essn = E.Ssn AND E.Lname = 'Smith')
UNION							/* UNION, INTERSECT, and EXCEPT will remove duplicates (i.e. the set operations). Using ALL with set operations will result in multisets (i.e. duplicates)*/
(SELECT P.Pnumber
 FROM PROJECT P, DEPARTMENT D, EMPLOYEE E
 WHERE P.Dnum = D.Dnumber AND D.Mgr_ssn = E.Ssn AND E.Lname = 'Smith');
 
 /* Query 2.1 - Make a list of all project numbers for projects that involve an employee whose last name is ‘Wong’, 
either as a worker or as a manager of the department that controls the project.*/
(SELECT W.Pno
 FROM WORKS_ON W, EMPLOYEE E
 WHERE W.Essn = E.Ssn AND E.Lname = 'Wong')
UNION							
(SELECT P.Pnumber
 FROM PROJECT P, DEPARTMENT D, EMPLOYEE E
 WHERE P.Dnum = D.Dnumber AND D.Mgr_ssn = E.Ssn AND E.Lname = 'Wong');
  
  
  
/* Query 3.1 - Retrieve all employees whose address is in Houston, Texas.*/
SELECT Fname, Lname 
FROM EMPLOYEE 
WHERE Address LIKE '%Houston, TX%';		/* Like is used for substring pattern matching. % replaces an arbitrary number of characters*/

/* Query 3.2 - Find all employees who were born during the 1970s.*/
SELECT Fname, Lname 
FROM EMPLOYEE 
WHERE Bdate LIKE '__7_______'; /* _ replaces exactly 1 character*/

/* Another option for 3.2 */
SELECT Fname, Lname 
FROM EMPLOYEE 
WHERE Bdate LIKE '__7%';

/* Query 4 - Show resulting salaries if every employee working on the ‘ProductX’ project is given a 10% raise.*/
SELECT E.Fname, E.Lname, 1.1 * E.Salary AS Increased_sal		/* we can use * to show what would happen if we updated, this doesn't actually update the data */
FROM EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
WHERE E.Ssn = W.Essn AND W.Pno = P.Pnumber AND P.Pname = 'ProductX';

/* Query 5 - Retrieve all employees in department 5 whose salary is between $30,000 and $40,000.*/
SELECT *
FROM EMPLOYEE
WHERE (Salary BETWEEN 30000 AND 40000) AND Dno = 5;		/* we can use between instead of and AND with > and < */

/* Query 6 - Retrieve a list of employees and projects they are working on, ordered by department and, 
within each department, ordered alphabetically by last name, then first name.*/
SELECT D.Dname, E.Lname, E.Fname, P.Pname
FROM DEPARTMENT AS D, EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
WHERE D.Dnumber = E.Dno AND E.Ssn = W.Essn AND W.Pno = P.Pnumber
ORDER BY D.Dname, E.Lname, E.Fname;		/* ORDERED BY puts the strings in alphabetical order */

/* Query 7 - Retrieve names of all employees who do not have supervisors.*/
SELECT Fname, Lname
FROM EMPLOYEE
WHERE Super_ssn='null';  /*currently we have null as a string in our data*/

SELECT Fname, Lname
FROM EMPLOYEE
WHERE Super_ssn IS NULL; /* we would use this if it was legit not a null value */

SELECT Fname, Lname 
FROM EMPLOYEE
WHERE Super_ssn IS NOT NULL;

/* Query 8 - Make a list of all project numbers for projects that involve an employee whose last name is ‘Wong’, 
either as a worker or as a manager of the department that controls the project.*/
/* this is not a correlated nested query. we do not use PROJECT in the nested queries*/
SELECT Pnumber
FROM PROJECT
WHERE Pnumber IN
				(SELECT W.Pno
				 FROM WORKS_ON W, EMPLOYEE E
				 WHERE W.Essn = E.Ssn AND E.Lname = 'Wong')
	  OR
	  Pnumber IN
	  			(SELECT P.Pnumber
				 FROM PROJECT P, DEPARTMENT D, EMPLOYEE E
				 WHERE P.Dnum = D.Dnumber AND D.Mgr_ssn = E.Ssn AND E.Lname = 'Wong');


/* Query 9 - Retrieve name of each employee who has a dependent with the same first name and same sex as the employee.*/
/* This is a correlated nested query. We use E in the nested query. */
SELECT E.Fname, E.Lname
FROM EMPLOYEE AS E
WHERE E.Ssn IN (SELECT D.Essn
				FROM DEPENDENT AS D
				WHERE E.Fname = D.Dependent_name
				AND E.Sex = D.Sex);

	/* In general, a query written with nested select-from-where blocks and using the = or IN comparison operators can always 
	be expressed as a single block query.*/
	SELECT E.Fname, E.Lname
	FROM EMPLOYEE AS E, DEPENDENT AS D
	WHERE E.Ssn = D.Essn AND E.Sex = D.Sex AND E.Fname = D.Dependent_name;

 
/* Query 10 - List names of employees whose salary is greater than the salary of all the employees in department 5.*/
SELECT Lname, Fname, Salary
FROM EMPLOYEE
WHERE Salary > ALL (SELECT Salary
					FROM EMPLOYEE
					WHERE Dno = 5);
 
/* Query 11 - Alternative to Query 9, with EXISTS.*/
	/* Query 9 - Retrieve name of each employee who has a dependent with the same sex as the employee.*/
SELECT E.Fname, E.Lname
FROM EMPLOYEE AS E
WHERE EXISTS (SELECT * 
			  FROM DEPENDENT AS D
			  WHERE E.Ssn = D.Essn AND E.Sex = D.Sex);
 
/* Query 12 - Retrieve names of employees who have no dependents.*/
SELECT Fname, Lname
FROM EMPLOYEE E
WHERE NOT EXISTS (SELECT *
				  FROM DEPENDENT D
				  WHERE E.Ssn = D.Essn);

/* Query 13 - List names of managers who have at least one dependent.*/
SELECT Fname, Lname
FROM EMPLOYEE E
WHERE EXISTS (SELECT *
			  FROM DEPARTMENT DEP
			  WHERE E.Ssn = DEP.Mgr_ssn)
	  AND 
	  EXISTS
			(SELECT *
			 FROM DEPENDENT D
			 WHERE E.Ssn = D.Essn);
 
/* Query 14 - Retrieve ssns of all employees who work on project number 1, 2, or 3.*/
SELECT DISTINCT Essn
FROM WORKS_ON
WHERE Pno IN (1, 2, 3); /* alternative to WHERE Pno = 1 OR Pno = 2 OR Pno = 3 */

/* Query 15 - Retrieve last name of each employee and his or her supervisor while renaming the resulting attribute names
as Employee_name and Supervisor_name.*/
SELECT E.Lname AS Employee_name, S.Lname AS Supervisor_name
FROM EMPLOYEE AS E, EMPLOYEE AS S
WHERE E.Super_ssn = S.Ssn;


/* JOIN and NATURAL JOIN ---------------------------------------------------------- */

/* Query 16 - Retrieve name and address of every employee who works for the ‘Research’ department.*/ 
SELECT E.Fname, E.Lname, E.Address
FROM (EMPLOYEE E JOIN DEPARTMENT D ON E.Dno = D.Dnumber)
WHERE D.Dname = 'Research';

/* Query 17 - Rename attribute name of DEPARTMENT relation and use NATURAL JOIN.*/ 
SELECT E.Fname, E.Lname, E.Address
FROM (EMPLOYEE E NATURAL JOIN (SELECT D.Dname, D.Dnumber AS Dno, D.Mgr_ssn, D.Mgr_start_date
							FROM DEPARTMENT D) AS DEPT)
WHERE DEPT.Dname = 'Research';

/* Query 18 - For every project located in ‘Stafford’, list project number, controlling department number, 
and department manager’s last name, address, and birth date.*/ 
SELECT P.Pnumber, D.Dnumber, E.Lname, E.Address, E.Bdate
FROM ((PROJECT P JOIN DEPARTMENT D ON P.Dnum = D.Dnumber) JOIN EMPLOYEE E ON D.Mgr_ssn = E.Ssn)
WHERE P.Plocation = 'Stafford';

/* AGGREGATE FUNCTIONS -----------------------------------------------------------*/
/* Note that null values are discarded. however, for COUNT, you can use COUNT(*) for count all. COUNT counts the tuples.

/* Query 19.1 - Find the sum of salaries of all employees, maximum salary, minimum salary, and average 
salary without attribute renaming.*/ 
SELECT SUM(Salary), MAX(Salary), MIN(Salary), AVG(Salary)
FROM EMPLOYEE;

/* Query 19.2 - Find the sum of salaries of all employees, maximum salary, minimum salary, and average 
salary with attribute renaming.*/
SELECT SUM(Salary) AS Total_Sal, MAX(Salary) AS Highest_Sal, MIN(Salary) AS Lowest_Sal, AVG(Salary) AS Average_Sal
FROM EMPLOYEE;

/* Query 20 - Find the sum of salaries of all employees of the ‘Research’ department, as well as maximum salary,
minimum salary, and average salary in this department.*/
SELECT SUM(E.Salary), MAX(E.Salary), MIN(E.Salary), AVG(E.Salary)
FROM (EMPLOYEE E JOIN DEPARTMENT D ON E.Dno = D.Dnumber)
WHERE D.Dname = 'Research';

/* same as above */
SELECT SUM(E.Salary), MAX(E.Salary), MIN(E.Salary), AVG(E.Salary)
FROM employee E, department D
WHERE D.Dname = 'Research' AND E.Dno = D.Dnumber;

/* Query 21 - Count the number of distinct salary values in the database.*/
SELECT COUNT(DISTINCT Salary)
FROM EMPLOYEE;

/* Query 22 - Retrieve names of all employees who have two or more dependents.*/
SELECT E.Lname, E.Fname
FROM EMPLOYEE E
WHERE (SELECT COUNT(*)
	   FROM DEPENDENT D
	   WHERE E.Ssn = D.Essn) >= 2;

/* Query 23 - For each department, retrieve department number, number of employees in the department, and their 
average salary.*/
SELECT Dno, COUNT(*) as num_of_employee, AVG(Salary) as avg_salary
FROM EMPLOYEE
GROUP BY Dno;

/* Query 24 - For each project, retrieve project number, project name, and the number of employees who work on 
that project.*/
SELECT P.Pnumber, P.Pname, COUNT(*)
FROM PROJECT P, WORKS_ON W
WHERE P.Pnumber = W.Pno
GROUP BY P.Pnumber, P.Pname;

/* Query 25 - For each project on which more than two employees work, retrieve project number, project name, and 
the number of employees who work on the project.*/
SELECT P.Pnumber, P.Pname, COUNT(*)
FROM PROJECT P, WORKS_ON W
WHERE P.Pnumber = W.Pno
GROUP BY P.Pnumber, P.Pname
HAVING COUNT(*) > 2; 