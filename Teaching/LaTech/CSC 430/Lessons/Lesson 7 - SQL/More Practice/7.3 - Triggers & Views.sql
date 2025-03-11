/*Trigger #1 - Write a trigger to update the salary of an employee with an average salary of the department where he/she 
works BEFORE INSERT(ing) the record in the employee table IF the salary is empty or NULL*/
DELIMITER $$
CREATE TRIGGER EMP_SALARY_TRIG
BEFORE INSERT ON EMPLOYEE
FOR EACH ROW
BEGIN
	IF (NEW.Salary = '' OR NEW.Salary IS NULL) 
    THEN 
	SET NEW.Salary = (SELECT AVG(Salary)
					  FROM EMPLOYEE E
					  WHERE E.Dno = NEW.Dno);
	END IF;
END$$
DELIMITER ;


/*Trigger #2 - Write a trigger to enforce following constraint: Dependent relationship must be either spouse, son, or 
daughter, if anything else, then display message – “Please, provide valid relationship (Spouse, Son or Daughter).”*/
DELIMITER $$
CREATE TRIGGER DEPENDENT_RELATIONSHIP
BEFORE INSERT ON DEPENDENT
FOR EACH ROW
BEGIN
	DECLARE MSG VARCHAR(255);
    IF NEW.Relationship NOT IN ('Spouse', 'Daughter', 'Son')
    THEN /* Cause Error Message */
    SET MSG = 'Please, provide correct relationship (Spouse, Son or Daughter).';
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = MSG;
    END IF;
END$$
DELIMITER ;


/*Trigger #3 - Write a trigger to create a default project for each new department inserted into database.*/
DELIMITER $$
CREATE TRIGGER NEW_DEPT
AFTER INSERT ON DEPARTMENT
FOR EACH ROW
BEGIN
	INSERT INTO PROJECT 
    VALUES(CONCAT(NEW.Dname, ' - Initialization'), CONCAT(NEW.DNumber, '1'), 'Houston', NEW.DNumber);
END$$
DELIMITER ;


/*View #1 - Create a view that provides information about the employees and the projects that they work on.*/
CREATE VIEW WORKS_ON_EXT
AS SELECT Fname, Lname, Pname, Hours
   FROM EMPLOYEE E, PROJECT P, WORKS_ON W
   WHERE E.Ssn = W.Essn AND W.Pno = P.Pnumber;


/*View #2 - Create a view that displays the number of employees and the total salary paid in each department*/
CREATE VIEW DEPT_INFO(Dept_name, No_of_emps, Total_sal)
AS SELECT Dname, COUNT(*), SUM(Salary)
   FROM DEPARTMENT D, EMPLOYEE E
   WHERE D.Dnumber = E.Dno
   GROUP BY Dname;