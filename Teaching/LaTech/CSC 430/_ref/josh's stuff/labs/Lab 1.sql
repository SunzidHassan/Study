/* Josh Coriell */
/* Lab 1 */

use company;

/*Query 1 - Retrieve first name and last name of all male employees with salary more than 30000.*/
SELECT fname, lname
FROM employee
WHERE salary > 30000 AND sex='M';

/*Query 2 - Retrieve locations of Research department projects.*/
SELECT p.plocation
FROM project p, department d
WHERE d.dname = 'Research' AND p.dnum = d.dnumber;

/*Query 3 - Retrieve first name, last name, and SSN of all employees who work more than 9 hours on project #2.*/
SELECT e.fname, e.lname, e.ssn
FROM employee e, works_on w
WHERE w.pno = 2 AND w.hours > 9 AND e.ssn = w.essn;

/*Query 4 - Retrieve name, date of birth and relationship of all female dependents of employees who work for department #5.*/
SELECT DISTINCT d.dependent_name, d.bdate, d.relationship
FROM employee e, dependent d
WHERE e.dno='5' AND d.sex='F';

/*Query 5 - Retrieve first name, last name and salary of employees who manage departments with projects located in Houston.*/
SELECT e.fname, e.lname, e.salary
FROM project p, employee e, department d
WHERE p.plocation='Houston' AND p.dnum=d.dnumber AND d.mgr_ssn=e.ssn;
