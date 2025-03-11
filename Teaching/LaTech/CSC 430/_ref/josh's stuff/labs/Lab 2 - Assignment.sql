/* Josh Coriell - Lab 2 Assignment */
use company;

/* Query 1 - Retrieve first name and last name of employees whose birthday is in January.*/
SELECT fname, lname
FROM employee
WHERE bdate LIKE "_____01___";

/* Query 2 -Show the resulting salaries if every employee working on the ‘ProductX’ project with a salary between $20000 and $40000 is given a 15% raise.*/
SELECT e.fname, e.lname, e.salary * 1.15 as Increased_Sal
FROM employee e, project p, works_on w
WHERE p.pname='ProductX' AND (e.salary BETWEEN 20000 AND 40000) AND w.essn = e.ssn AND p.pnumber = w.pno;

/* Query 3 - List first name, last name and SSN of employees whose salary is less than the salary of any of the employees in department 4.*/
SELECT e.fname, e.lname, e.ssn
FROM employee e
WHERE e.salary < ANY (SELECT f.salary FROM employee f WHERE f.dno = 4);

/* Query 4 - Retrieve SSNs of all female employees who work on project numbers 10, 20, or 30.*/
SELECT DISTINCT e.ssn
FROM employee e, works_on w
WHERE e.ssn = w.essn AND e.sex = 'F' AND w.pno IN (10, 20, 30);

/* Query 5 -For each project on which less than three employees work, retrieve project number, project name, and the average salary of employees who work on the project.*/
SELECT p.pnumber, p.pname, AVG(e.salary)
FROM project p, employee e, works_on w
WHERE p.pnumber = w.pno AND w.essn = e.ssn
GROUP BY p.pnumber, p.pname
HAVING COUNT(*) < 3;

use podracing;
-- for each being that is not a slave, group by the planet, show the number of nonslaves from that plant, and the population of the planet

SELECT p.planet_name, p.planet_population, count(*)
FROM being b, is_from i, planet p
WHERE i.being_id =  b.id AND p.planet_name = i.pname
GROUP BY p.planet_name;



SELECT r.bid, b.fname
FROM racer r, droid d, being b
WHERE d.racer_bid = r.bid AND r.bid = b.id
GROUP BY b.fname
HAVING COUNT(*) >= 2; 

CREATE VIEW droid_viewers 
AS SELECT D.Droid_number, D.droid_type, V.race_name
FROM Viewer AS V, Droid AS D
WHERE V.Bid = D.racer_bid;


CREATE VIEW bidders_names_on_in_race_racers
AS SELECT concat(vb.Fname, " " ,vb.Lname) AS viewer, Bet_type, rb.Fname AS racer, Amount, i.Race_Name
FROM being rb, being vb, bet b, viewer v, is_in i
WHERE b.R_bid = rb.Id AND b.V_bid = vb.Id AND i.Racer_Bid = b.R_bid
GROUP BY viewer, racer;

DELIMITER $$
CREATE TRIGGER no_owner_on_bike
BEFORE INSERT ON POD
FOR EACH ROW
BEGIN 
    DECLARE MSG VARCHAR(500);
    IF(racer_bid = NULL or racer_bid = '' )
    THEN
        SET MSG = 'The pod has no racer_bid.';
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = MSG;
    END if;
END $$
DELIMITER ;

DROP TRIGGER no_owner_on_bike;

INSERT INTO POD(engine_type, vin, pod_weight, top_speed, modified_flag)
VALUES ('ufj', 23, 2424, 24, 0);

