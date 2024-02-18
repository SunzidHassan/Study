# Create a view that displays highest achieved level, total experience, total collected gold, and area exploration % of each player
DROP VIEW player_progress;
CREATE VIEW player_progress
AS SELECT p.userName, MAX(c.level) Highest_character_level, SUM(c.experience) as Total_experience, SUM(c.totalGold) AS Total_gold, CONCAT(CAST(COUNT(c.area)/(SELECT COUNT(area)FROM location)*100 as DECIMAL(10)),'%') AS Area_explored
	FROM charactr c, player p
    WHERE c.playerID = p.playerID
	GROUP BY c.playerID;
