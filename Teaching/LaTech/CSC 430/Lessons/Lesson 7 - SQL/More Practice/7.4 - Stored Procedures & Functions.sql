/*Stored procedure #1 - Create a stored procedure that counts the total number of employees in the company.*/
DELIMITER $$
CREATE PROCEDURE GetEmployeeCount()
BEGIN
	SELECT COUNT(*) AS TotalEmployees FROM Employee;
END $$
DELIMITER ;

CALL GetEmployeeCount();
 
/*Stored procedure #2 - Create a stored procedure to get an employee full name given an SSN.*/
DELIMITER $$
CREATE PROCEDURE GetEmployeeName(IN empSSN INT, OUT empName VARCHAR(50))
BEGIN
	SELECT CONCAT(fname, ' ', lname) INTO empName FROM Employee WHERE Ssn = empSSN;
END $$
DELIMITER ;

CALL GetEmployeeName(123456789, @emp_name);
SELECT @emp_name;

/*Stored procedure #3 - Create a stored procedure to get the total number of hours an employee works on all projects.*/
DELIMITER $$
CREATE PROCEDURE GetEmployeeHours(IN empFname VARCHAR(20), IN empLname VARCHAR(20), OUT empHours DECIMAL(4,1))
BEGIN
  SELECT SUM(w.Hours) INTO empHours
  FROM Employee e, Works_on w
  WHERE e.Ssn = w.Essn AND e.Fname = empFname AND e.Lname = empLname;
END $$
DELIMITER ;

CALL GetEmployeeHours("John", "Smith", @emp_hrs);
SELECT @emp_hrs;

/*Function #1 - Create a function to get the name of the employee by the SSN.*/
DELIMITER $$
CREATE FUNCTION NameBySSN(empSSN VARCHAR(9))
RETURNS VARCHAR(20) DETERMINISTIC
BEGIN
	DECLARE empName VARCHAR(20);
	SELECT Fname INTO empName FROM Employee WHERE SSN = empSSN;
	RETURN empName;
END $$
DELIMITER ;

SELECT NameBySSN(123456789);

/*Function #2 - Create a function to calculate the age of an employee given the date of birth.*/
DELIMITER $$
CREATE FUNCTION GetAge(DOB DATE)
RETURNS INT DETERMINISTIC
BEGIN
    DECLARE today DATE;
    SET today = CURDATE();
    RETURN YEAR(today) - YEAR(DOB);
END $$
DELIMITER ;

SELECT GetAge((SELECT Bdate FROM Employee WHERE Ssn = 123456789));

/*Function #3 - Create a function to calculate the number of the employees for a given department.*/
DELIMITER $$
CREATE FUNCTION GetEmployeesByDepartment(deptNo INT)
RETURNS INT DETERMINISTIC
BEGIN
    RETURN (SELECT COUNT(*) FROM Employee WHERE Dno = deptNo);
END $$
DELIMITER ;

SELECT GetEmployeesByDepartment(5);