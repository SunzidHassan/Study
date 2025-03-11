/*Query 0. Retrieve the birth date and address of the employee(s) whose name is 'John B. Smith'.*/
SELECT Bdate, Address
FROM EMPLOYEE
WHERE Fname = 'John' AND Minit = 'B' AND Lname = 'Smith';

/*Query 1. Retrieve the name and address of all employees who work for the 'Research' department.*/
SELECT Fname, Lname, Address
FROM EMPLOYEE, DEPARTMENT
WHERE Dname = 'Research' AND Dnumber = Dno;

SELECT EMPLOYEE.Fname, EMPLOYEE.LName, EMPLOYEE.Address
FROM EMPLOYEE, DEPARTMENT
WHERE DEPARTMENT.DName = 'Research' AND DEPARTMENT.Dnumber = EMPLOYEE.Dno;

SELECT E.Fname, E.LName, E.Address
FROM EMPLOYEE AS E, DEPARTMENT AS D
WHERE D.DName = 'Research' AND D.Dnumber = E.Dno;

/*Query 2. For every project located in 'Stafford', list the project number, the controlling department number, 
and the department manager's last name, address, and birth date.*/
SELECT Pnumber, Dnum, Lname, Address, Bdate
FROM PROJECT, DEPARTMENT, EMPLOYEE
WHERE Dnum = Dnumber AND Mgr_ssn = Ssn AND Plocation = 'Stafford';

/* Query 3. For each employee, retrieve the employee's first and last name and the first and last name of his or her 
immediate supervisor.*/
SELECT E.Fname, E.Lname, S.Fname, S.Lname
FROM EMPLOYEE AS E, EMPLOYEE AS S
WHERE E.Super_ssn = S.Ssn;

/*Query 4. Select all EMPLOYEE Ssns*/
SELECT Ssn
FROM EMPLOYEE;

/*Query 5. Select all combinations of EMPLOYEE Ssn and DEPARTMENT Dname in the database.*/
SELECT Ssn, Dname
FROM EMPLOYEE, DEPARTMENT;

/*Query 6. Select all the attribute values of any EMPLOYEE who works in DEPARTMENT number 5.*/
SELECT *
FROM EMPLOYEE
WHERE Dno = 5;

/*Query 7. Select all the attributes of an EMPLOYEE and the attributes of the DEPARTMENT in which he or she works for
every employee of the 'Research' department.*/
SELECT *
FROM EMPLOYEE, DEPARTMENT
WHERE Dname = 'Research' AND Dno = Dnumber;

/*Query 8. CROSS PRODUCT of the EMPLOYEE and DEPARTMENT relations.*/
SELECT *
FROM EMPLOYEE, DEPARTMENT;