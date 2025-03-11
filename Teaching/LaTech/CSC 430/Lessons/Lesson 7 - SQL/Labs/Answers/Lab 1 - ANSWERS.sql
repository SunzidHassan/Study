/*Write the queries under each comment. Do NOT remove the comments. Leave a single blank line between the query and the next comment.*/

/*1. Query to retrieve first name and last name of all male employees with salary more than 30000.*/
SELECT fname, lname
FROM employee
WHERE sex = 'M' AND salary > 30000;

/*2. Query to retrieve locations of Research department projects.*/
SELECT plocation
FROM project AS proj, department AS dept
WHERE proj.dnum = dept.dnumber AND dept.dname = "Research";

/*3. Query to retrieve first name, last name, and SSN of all employees who work more than 9 hours on project #2.*/
SELECT emp.fname, emp.lname, emp.ssn
FROM employee AS emp, works_on AS w
WHERE emp.ssn = w.essn
AND w.pno = 2
AND w.hours > 9;

/*4. Query to retrieve name, date of birth and relationship of all female dependents of employees who work for department #5.*/
SELECT dep.dependent_name, dep.bdate, dep.relationship
FROM dependent AS dep, employee AS emp
WHERE dep.essn = emp.ssn
AND emp.dno = 5
AND dep.sex = 'F';

/*5. Query to retrieve first name, last name and salary of employees who manage departments with projects located in Houston.*/
SELECT DISTINCT emp.fname, emp.lname, emp.salary
FROM employee AS emp, department AS dept, project AS proj
WHERE emp.ssn = dept.mgr_ssn
AND dept.dnumber = proj.dnum
AND proj.plocation = 'Houston';



/*Submit this sql file containing the five queries to Canvas*/
