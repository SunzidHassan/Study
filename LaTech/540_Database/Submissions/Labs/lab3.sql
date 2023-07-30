USE company;

# Write a trigger to create a default department location in Bellaire every time new department is inserted into database.
DELIMITER $$
CREATE TRIGGER new_dept_loc
AFTER INSERT ON department
FOR EACH ROW
BEGIN 
	INSERT INTO dept_locations
    VALUES (NEW.dnumber,'Bellaire');
END $$
DELIMITER ;

# Write a trigger to enforce following constraint: employee salary must not be higher than the salary of his/her direct supervisor. If it is, then display message – “Please, provide correct value for the employee salary".
DELIMITER $$
CREATE TRIGGER emp_super_salary
BEFORE INSERT ON employee
FOR EACH ROW
BEGIN
	DECLARE MSG VARCHAR(255);
    IF NEW.salary > (SELECT e.salary AS mgr_salary
					FROM employee e
					WHERE e.ssn = NEW.mgr_ssn)
    THEN /* Cause Error Message */
    SET MSG = 'Please, provide correct value for the employee salary';
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = MSG;
	END IF;
END$$
DELIMITER ;

# Write a trigger to update supervisor SSN of an employee with the SSN of the department manager where he/she works before inserting the record into employee table if the supervisor SSN attribute is empty or NULL.
DELIMITER $$
CREATE TRIGGER super_ssn_trig
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

# Create a view that displays first name, last name, SSN, salary, department name and department number for each department manager.
DROP VIEW mgr_info;
CREATE VIEW mgr_info(mgr_fname, mgr_lname, mgr_ssn, mgr_salary, mgr_dname, mgr_dnum)
AS SELECT e.fname, e.lname, e.ssn, e.salary, d.dname, d.dnumber
	FROM department d, employee e
	WHERE d.mgr_ssn = e.ssn;

# Create a view that displays project number, project name, controlling department number, controlling department name, total number of employees, total salary paid, and total hours worked for each project.
DROP VIEW project_info;
CREATE VIEW project_info(prj_num, prj_name, dnum, dname, ttl_emp, ttl_slry, ttl_hrs)
	AS SELECT p.pname, p.pnumber, d.dnumber, d.dname, COUNT(e.ssn), SUM(e.salary), SUM(w.hours)
	FROM employee e
	JOIN works_on w ON w.essn = e.ssn
	JOIN project p ON p.pnumber = w.pno
	JOIN department d ON d.dnumber = p.dnum
    GROUP BY p.pname, p.pnumber;
