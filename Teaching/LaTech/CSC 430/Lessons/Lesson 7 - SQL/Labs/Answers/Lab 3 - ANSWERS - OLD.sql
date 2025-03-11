/*Write the queries under each comment. Do NOT remove the comments. Leave a single blank line between the query and the next comment.*/

/*1. Write a trigger to create a default department location in Houston every time a new department is inserted into the database.*/
DELIMITER $$
CREATE TRIGGER add_default_location
AFTER INSERT ON department
FOR EACH ROW
BEGIN
    INSERT INTO dept_locations (dnumber, dlocation)
    VALUES (NEW.dnumber, 'Houston');
END $$
DELIMITER ;

/*2. Write a trigger to enforce the following constraint when updating employee salary: employee salary must not be higher than the salary of his/her direct supervisor. If it is, then display message – "Supervisee salary is higher than supervisor salary".*/
DELIMITER $$
CREATE TRIGGER check_salary_constraint
BEFORE UPDATE ON employee
FOR EACH ROW
BEGIN
    DECLARE supervisor_salary DECIMAL(10,2);
    
    SELECT salary INTO supervisor_salary
    FROM employee
    WHERE ssn = NEW.super_ssn;
    
    IF NEW.salary > supervisor_salary THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Supervisee salary is higher than supervisor salary';
    END IF;
END $$
DELIMITER ;

/*3. Write a trigger to update the supervisor SSN of an employee with the SSN of the department manager where he/she works BEFORE INSERT(ing) the record into the employee table IF the supervisor SSN attribute is empty or NULL.*/
DELIMITER $$
CREATE TRIGGER set_default_supervisor
BEFORE INSERT ON employee
FOR EACH ROW
BEGIN
    IF NEW.super_ssn IS NULL OR NEW.super_ssn = '' THEN
        SET NEW.super_ssn = (SELECT mgr_ssn
                             FROM department
                             WHERE dnumber = NEW.dno);
    END IF;
END $$
DELIMITER ;

/*4. Create a view that displays first name, last name, SSN, salary, department name, and department number for each department manager.*/
CREATE VIEW department_managers AS
SELECT emp.fname, emp.lname, emp.ssn, emp.salary, dept.dname, dept.dnumber
FROM employee AS emp, department AS dept
WHERE emp.ssn = dept.mgr_ssn;

/*5. Create a view that displays project number, project name, controlling department number, controlling department name, total number of employees, total salary paid, and total hours worked for each project.*/
CREATE VIEW project_summary AS
SELECT p.pnumber, p.pname, p.dnum, d.dname, 
       COUNT(w.essn) AS total_employees, 
       SUM(e.salary) AS total_salary, 
       SUM(w.hours) AS total_hours
FROM project AS p
JOIN department AS d ON p.dnum = d.dnumber
JOIN works_on AS w ON p.pnumber = w.pno
JOIN employee AS e ON w.essn = e.ssn
GROUP BY p.pnumber, p.pname, p.dnum, d.dname;


/*Submit this sql file containing the five queries to Canvas*/
