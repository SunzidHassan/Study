use company;

/* Define a trigger */
DELIMITER $$
CREATE TRIGGER EMP_SALARY_TRIG
BEFORE INSERT ON employee
FOR EACH ROW
BEGIN
	IF (NEW.Salary = '' OR NEW.Salary IS NULL)
    THEN
    SET NEW.Salary = (SELECT AVG(Salary)
					  FROM employee e
                      WHERE e.dno = NEW.dno);
	END IF;
END$$
DELIMITER ;

/* Test EMP_SALARY_TRIG*/
insert into employee(fname, minit, lname, ssn, dno)
values ('John', 'J', 'Johnson', '999999999', 5);

insert into employee(fname, minit, lname, ssn, dno, salary)
values ('John', 'J', 'Jones', '999999990', 5, 30000); /* why doesn't this work ??? */


/* Write a trigger to encforce the following constraint */
/* Dependent relationship must be either spouse, son, or daughter. 
If anything else, then display message - "Please, provide valid relationship (Spouse, son, or daughter)/*

/*Definition*/

DELIMITER $$
CREATE TRIGGER DEPENDENT_RELATIONSHIP
BEFORE INSERT ON dependent
FOR EACH ROW
BEGIN
	DECLARE MSG VARCHAR(255);
	IF (NEW.relationship NOT IN ('Spouse', 'Daughter', 'Son'))
    THEN
    SET MSG = 'Please, provide correct relationship (Spouse, Son or Daughter)';
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = MSG;
	END IF;
END$$
DELIMITER ;

/* Testing DEPENDENT_RELATIONSHIP */
insert into dependent
values ('987654321', 'John', 'M', '1990-01-01', 'Spouse'); /*replacing Spouse with something like 'horse' will cause an error */


/*Write a trigger to create a default project for each new department inserted into the database*/
/* Event - AFTER INSERT ON department */
/* Condition - No condition, just needs to always happen when a new department is inserted*/
/* Action - Create a default project */

DELIMITER $$
CREATE TRIGGER NEW_DEPT
AFTER INSERT ON department
FOR EACH ROW
BEGIN
	INSERT INTO project
    VALUES(concat(NEW.dname, '-initilization'), concat(NEW.dnumber, '1'), 'Houston', NEW.dnumber);
END $$
DELIMITER ;

/* Test Query */

insert into department
values ('R&D', 7, NULL, NULL);


/* VIEWS */
/* When you define a query and give it a name? Basically creates a virtual table that you may want to frequent, but don't want as an actual table.*/

CREATE VIEW WORKS_ON_EXT
AS SELECT e.fname, e.lname, p.pname, w.hours
FROM employee e, project p, works_on w
WHERE e.ssn = w.essn AND w.pno = p.pnumber;


/* Create a view that displays the number of employees and the total salary paid in each department */

CREATE VIEW DEPT_INFO(Dept_name, No_of_emps, Total_sal)
AS SELECT dname, count(*), sum(salary)
FROM department d, employee e
WHERE d.dnumber = e.dno
GROUP BY Dname;

/* get rid of the dept_info view*/
drop view dept_info;