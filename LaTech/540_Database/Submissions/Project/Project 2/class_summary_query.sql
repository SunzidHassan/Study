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