USE gamedb;

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

DROP VIEW level_summary;
CREATE VIEW level_summary(lvl, avg_strength, avg_agility, avg_intelligence, avg_armor, avg_hitPoints, avg_manna, avg_)
	AS SELECT c.level, COUNT(w.characterID), COUNT(m.characterID), COUNT(r.characterID), AVG(c.strength, c.aligity, c.intelligence, c.armorClass, c.hitPoints, c.manna, w.attackBonus, w.armorBonus, m.spells, m.magcResist, r.agilityBonus, r.stealthBonus)
    FROM charactr c, warrior w, mage m, rouge r
    WHERE c.characterID = w.characterID AND c.characterID = w.characterID AND c.characterID = r.characterID
    GROUP BY c.level;

# TEMP 1
DROP VIEW level_summary;
CREATE VIEW level_summary
	AS SELECT c.level, COUNT(w.characterID), COUNT(m.characterID), COUNT(r.characterID)
    FROM charactr c
    JOIN warrior w on w.characterID = c.characterID
    JOIN mage m ON m.characterID = c.characterID
    JOIN rouge r ON r.characterID = c.characterID
    GROUP BY c.level;

# TEMP 2

DROP VIEW level_summary;
CREATE VIEW level_summary
AS SELECT class, COUNT(characterID) as characterNo, CAST(AVG(level) AS DECIMAL(10,2)) as avg_level, CAST(AVG(strength) AS DECIMAL(10,2)) as avg_strength, CAST(AVG(agility) AS DECIMAL(10,2)) as avg_aligity, CAST(AVG(intelligence) AS DECIMAL(10,2)) as avg_intelligence, CAST(AVG(armorCLass) AS DECIMAL(10,2)) as avg_armorClass, CAST(AVG(hitPoints) AS DECIMAL(10,2)) as avg_hitPoints, CAST(AVG(manna) AS DECIMAL(10,2)) as avg_manna, CAST(AVG(totalGold) AS DECIMAL(10,2)) as avg_totalGold
	FROM charactr c
	CROSS JOIN warrior w USING (characterID)
	GROUP BY class
	UNION SELECT class, COUNT(characterID) as characterNo, CAST(AVG(level) AS DECIMAL(10,2)) as avg_level, CAST(AVG(strength) AS DECIMAL(10,2)) as avg_strength, CAST(AVG(agility) AS DECIMAL(10,2)) as avg_aligity, CAST(AVG(intelligence) AS DECIMAL(10,2)) as avg_intelligence, CAST(AVG(armorCLass) AS DECIMAL(10,2)) as avg_armorClass, CAST(AVG(hitPoints) AS DECIMAL(10,2)) as avg_hitPoints, CAST(AVG(manna) AS DECIMAL(10,2)) as avg_manna, CAST(AVG(totalGold) AS DECIMAL(10,2)) as avg_totalGold
	FROM charactr c
	CROSS JOIN mage m USING (characterID)
	GROUP BY class
	UNION SELECT class, COUNT(characterID) as characterNo, CAST(AVG(level) AS DECIMAL(10,2)) as avg_level, CAST(AVG(strength) AS DECIMAL(10,2)) as avg_strength, CAST(AVG(agility) AS DECIMAL(10,2)) as avg_aligity, CAST(AVG(intelligence) AS DECIMAL(10,2)) as avg_intelligence, CAST(AVG(armorCLass) AS DECIMAL(10,2)) as avg_armorClass, CAST(AVG(hitPoints) AS DECIMAL(10,2)) as avg_hitPoints, CAST(AVG(manna) AS DECIMAL(10,2)) as avg_manna, CAST(AVG(totalGold) AS DECIMAL(10,2)) as avg_totalGold
	FROM charactr c
	CROSS JOIN rouge r USING (characterID)
	GROUP BY class;

# Count
(SELECT class, COUNT(characterID) as characterNo, CAST(AVG(level) AS DECIMAL(10,2)) as avg_level, CAST(AVG(strength) AS DECIMAL(10,2)) as avg_strength, CAST(AVG(agility) AS DECIMAL(10,2)) as avg_aligity, CAST(AVG(intelligence) AS DECIMAL(10,2)) as avg_intelligence, CAST(AVG(armorCLass) AS DECIMAL(10,2)) as avg_armorClass, CAST(AVG(hitPoints) AS DECIMAL(10,2)) as avg_hitPoints, CAST(AVG(manna) AS DECIMAL(10,2)) as avg_manna, CAST(AVG(totalGold) AS DECIMAL(10,2)) as avg_totalGold
FROM charactr c
CROSS JOIN warrior w USING (characterID)
GROUP BY class)
UNION ALL
(SELECT class, COUNT(characterID) as characterNo, CAST(AVG(level) AS DECIMAL(10,2)) as avg_level, CAST(AVG(strength) AS DECIMAL(10,2)) as avg_strength, CAST(AVG(agility) AS DECIMAL(10,2)) as avg_aligity, CAST(AVG(intelligence) AS DECIMAL(10,2)) as avg_intelligence, CAST(AVG(armorCLass) AS DECIMAL(10,2)) as avg_armorClass, CAST(AVG(hitPoints) AS DECIMAL(10,2)) as avg_hitPoints, CAST(AVG(manna) AS DECIMAL(10,2)) as avg_manna, CAST(AVG(totalGold) AS DECIMAL(10,2)) as avg_totalGold
FROM charactr c
CROSS JOIN mage m USING (characterID)
GROUP BY class)
UNION ALL
(SELECT class, COUNT(characterID) as characterNo, CAST(AVG(level) AS DECIMAL(10,2)) as avg_level, CAST(AVG(strength) AS DECIMAL(10,2)) as avg_strength, CAST(AVG(agility) AS DECIMAL(10,2)) as avg_aligity, CAST(AVG(intelligence) AS DECIMAL(10,2)) as avg_intelligence, CAST(AVG(armorCLass) AS DECIMAL(10,2)) as avg_armorClass, CAST(AVG(hitPoints) AS DECIMAL(10,2)) as avg_hitPoints, CAST(AVG(manna) AS DECIMAL(10,2)) as avg_manna, CAST(AVG(totalGold) AS DECIMAL(10,2)) as avg_totalGold
FROM charactr c
CROSS JOIN rouge r USING (characterID)
GROUP BY class);

(SELECT characterID, class, level, strength, agility, intelligence, armorCLass, hitPoints, manna, totalGold, attackBonus, armorBonus, 0 as MagicPwr, 0 as magicResist, 0 as agilityBonus, 0 as stealthBonus
FROM charactr c
CROSS JOIN warrior w USING (characterID))
UNION ALL
(SELECT characterID, class, level, strength, agility, intelligence, armorCLass, hitPoints, manna, totalGold, 0 as attackBonus, 0 as armorBonus, MagicPwr, magicResist, 0 as agilityBonus, 0 as stealthBonus
FROM charactr c
CROSS JOIN mage m USING (characterID))
UNION ALL
(SELECT characterID, class, level, strength, agility, intelligence, armorCLass, hitPoints, manna, totalGold, 0 as attackBonus, 0 as armorBonus, 0 as MagicPwr, 0 as magicResist, agilityBonus, stealthBonus
FROM charactr c
CROSS JOIN rouge r USING (characterID));

# Merging
SELECT COALESCE(level, 'all') as level, SUM(warrior) as warrior, SUM(mage) as mage, SUM(rouge) as rouge
FROM
	((SELECT level, COUNT(class) as warrior, 0 as mage, 0 as rouge
	FROM charactr c
	CROSS JOIN warrior w USING (characterID)
	GROUP BY level)
	UNION ALL
	(SELECT level, 0 as warrior, COUNT(class) as mage, 0 as rouge
	FROM charactr c
	CROSS JOIN mage m USING (characterID)
	GROUP BY level)
	UNION ALL
	(SELECT level, 0 as warrior, 0 as mage, COUNT(class) as rouge
	FROM charactr c
	CROSS JOIN rouge r USING (characterID)
	GROUP BY level)) t
GROUP BY level
ORDER BY level desc;

SELECT COALESCE(level, 'all') as level, SUM(warrior) as warrior, SUM(mage) as mage, SUM(rouge) as rouge
FROM
	((SELECT level, COUNT(class) as warrior, 0 as mage, 0 as rouge
	FROM charactr c
	CROSS JOIN warrior w USING (characterID)
	GROUP BY level)
	UNION ALL
	(SELECT level, 0 as warrior, COUNT(class) as mage, 0 as rouge
	FROM charactr c
	CROSS JOIN mage m USING (characterID)
	GROUP BY level)
	UNION ALL
	(SELECT level, 0 as warrior, 0 as mage, COUNT(class) as rouge
	FROM charactr c
	CROSS JOIN rouge r USING (characterID)
	GROUP BY level)) t
GROUP BY level;


SELECT * From rouge;