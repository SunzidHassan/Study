/* Josh Coriell */
/* Lab 3 */

use company;

/* Query 1 - Write a trigger to create a default department location in Houston every time new department is inserted into database. */

DELIMITER $$
CREATE TRIGGER DEFAULT_DEPT_TRIG
AFTER INSERT ON department 
FOR EACH ROW
BEGIN
    INSERT INTO dept_locations
    VALUES(NEW.dnumber, 'Houston');
END $$
DELIMITER ;

/* Query 1 Test */
-- INSERT INTO department
-- VALUES('Marketing2', 11, NULL, NULL);

/* Query 2 - Write a trigger to enforce following constraint: employee salary must not be higher than the salary of his/her direct supervisor. If it is, then display message – “Supervisee salary is higher than supervisor salary.*/

DELIMITER $$
CREATE TRIGGER EMP_MAX_SALARY_TRIG
BEFORE INSERT ON employee
FOR EACH ROW
BEGIN
    DECLARE MSG VARCHAR(255);
    IF (NEW.salary > (SELECT s.salary
                      FROM employee s
                      WHERE NEW.super_ssn = s.ssn))
    THEN
    SET MSG = 'Supervisee salary is higher than supervisor salary.';
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = MSG;
    END IF;
END$$
DELIMITER ;


/* Test Query 2 - */
-- insert into employee(fname, minit, lname, ssn, dno, super_ssn, salary)
-- values ('Josh', 'J', 'Josherson', '222334444', 5, '123456789', 99999);


/* Query 3 - Write a trigger to update supervisor SSN of an employee with the SSN of the department manager where he/she works BEFORE INSERT(ing) the record into employee table IF the supervisor SSN attribute is empty or NULL. */
DELIMITER $$
CREATE TRIGGER UPDATE_SUPER_SSN
BEFORE INSERT ON employee
FOR EACH ROW
BEGIN
	IF (NEW.super_ssn = '' OR NEW.super_ssn IS NULL)
    THEN
    SET NEW.super_ssn = (SELECT d.mgr_ssn
					  FROM department d
                      WHERE d.dnumber = NEW.dno);
	END IF;
END$$
DELIMITER ;

/* Test Query 3 */
-- insert into employee(fname, minit, lname, ssn, dno, super_ssn)
-- values ('Joosher', 'J', 'Joshman', '111223333', 5, '');


/* Query 4 - Create a view that displays first name, last name, SSN, salary, department name and department number for each department manager. */
create view mgr_info(fname, lname, ssn, salary, dname, dnumber)
as SELECT e.fname, e.lname, e.ssn, e.salary, d.dname, d.dnumber
FROM employee e, department d
WHERE e.ssn = d.mgr_ssn;

/* Query 5 - Create a view that displays project number, project name, controlling department number, controlling department name, total number of employees, total salary paid, and total hours worked for each project. */
CREATE VIEW PROJ_INFO(proj_number, proj_name, dept_number, dept_name, num_of_employees, total_salary, total_hrs)
AS SELECT  p.pnumber, p.pname, p.dnum, d.dname, COUNT(*), sum(e.salary), sum(w.hours)
FROM department d, project p, employee e, works_on w
WHERE p.dnum = d.dnumber AND p.pnumber = w.pno AND e.ssn = w.essn
GROUP BY p.pnumber;
