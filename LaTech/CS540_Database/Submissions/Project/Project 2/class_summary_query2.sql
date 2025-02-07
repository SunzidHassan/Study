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