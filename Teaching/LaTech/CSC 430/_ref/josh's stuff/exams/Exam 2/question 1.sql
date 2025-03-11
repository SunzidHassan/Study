use company;

-- part a
SELECT e.fname as First_Name, e.lname as Last_Name, e.address as Employee_Address
FROM employee e, department d
WHERE e.dno = d.dnumber AND d.dname = 'Research';

-- part b
SELECT p.pnumber as Project_Number, p.pname as Project_Name, count(*) as Num_Of_Employees
FROM employee e, project p, works_on w
WHERE w.pno = p.pnumber AND w.essn = e.ssn
GROUP BY p.pnumber
ORDER BY p.pnumber;