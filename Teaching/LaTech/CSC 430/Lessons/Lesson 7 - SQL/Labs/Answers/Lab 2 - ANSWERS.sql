/*Write the queries under each comment. Do NOT remove the comments. Leave a single blank line between the query and the next comment.*/

/*1. Query to retrieve first name and last name of employees who have a birthday in January.*/
SELECT fname, lname
FROM employee
WHERE MONTH(bdate) = 1;

/*2. Query to show the resulting salaries if every employee working on the ‘ProductX’ project with a salary between $20000 and $40000 is given a 15% raise.*/
SELECT emp.fname, emp.lname, emp.salary * 1.15 AS new_salary
FROM employee AS emp, works_on AS w, project AS p
WHERE emp.ssn = w.essn AND w.pno = p.pnumber
AND p.pname = 'ProductX' 
AND emp.salary BETWEEN 20000 AND 40000;

/*3. Query to retrieve first name, last name and SSN of employees whose salary is less than the salary of any of the employees in department 4.*/
SELECT fname, lname, ssn
FROM employee
WHERE salary < ANY (
    SELECT salary
    FROM employee
    WHERE dno = 4
);

/*4. Query to retrieve SSNs of all female employees who work on project numbers 10, 20, or 30.*/
SELECT DISTINCT emp.ssn
FROM employee AS emp, works_on AS w
WHERE emp.ssn = w.essn
AND emp.sex = 'F'
AND w.pno IN (10, 20, 30);

/*5. For each project on which less than three employees work, retrieve the project number, the project name, and the average salary of employees who work on the project.*/
SELECT p.pnumber, p.pname, AVG(emp.salary) AS avg_salary
FROM project AS p, works_on AS w, employee AS emp
WHERE p.pnumber = w.pno AND w.essn = emp.ssn
GROUP BY p.pnumber, p.pname
HAVING COUNT(w.essn) < 3;



/*Submit this sql file containing the five queries to Canvas*/
