/*Write the queries under each comment. Do NOT remove the comments. Leave a single blank line between the query and the next comment.*/

/*1. Create a stored procedure that counts the total number of employees in a given department number.*/
DELIMITER $$
CREATE PROCEDURE count_total_employees_by_dept(IN dept_num INT)
BEGIN
    SELECT COUNT(*) AS total_employees
    FROM employee
    WHERE Dno = dept_num;
END $$
DELIMITER ;

/*2. Create a stored procedure to get an employee full name given their SSN.*/
DELIMITER $$
CREATE PROCEDURE get_employee_full_name(IN emp_ssn CHAR(9), OUT emp_name VARCHAR(50))
BEGIN
    SELECT CONCAT(fname, ' ', minit, ' ', lname) INTO emp_name
    FROM employee
    WHERE ssn = emp_ssn;
END $$
DELIMITER ;

/*3. Create a stored procedure to get the max number of hours an employee worked on any of their projects.*/
DELIMITER $$
CREATE PROCEDURE get_total_hours_worked(IN emp_ssn CHAR(9), OUT max_hours DECIMAL(5,2))
BEGIN
    SELECT MAX(hours) INTO max_hours
    FROM works_on
    WHERE essn = emp_ssn;
END $$
DELIMITER ;

/*4. Create a function to get the name of an employee by their SSN.*/
DELIMITER $$
CREATE FUNCTION get_employee_name(emp_ssn CHAR(9))
RETURNS VARCHAR(50) DETERMINISTIC
BEGIN
    DECLARE emp_name VARCHAR(50);
    SELECT CONCAT(fname, ' ', minit, ' ', lname) INTO emp_name
    FROM employee
    WHERE ssn = emp_ssn;
    RETURN emp_name;
END $$
DELIMITER ;

/*5. Create a function to calculate the age of an employee given the date of birth.*/
DELIMITER $$
CREATE FUNCTION calculate_age(emp_bdate DATE)
RETURNS INT DETERMINISTIC
BEGIN
    RETURN TIMESTAMPDIFF(YEAR, emp_bdate, CURDATE());
END $$
DELIMITER ;


/*Submit this sql file containing the five queries to Canvas*/
