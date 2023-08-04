USE gamedb;

# a trigger to check if party leader is in existing characters
DELIMITER $$
CREATE TRIGGER adven_party_leader
BEFORE INSERT ON adven_party
FOR EACH ROW
BEGIN
	DECLARE MSG VARCHAR(255);
    IF NEW.partyLeaderID not in (
		SELECT characterID
        FROM charactr
        WHERE NEW.partyLeaderID = characterID)
    THEN /* Cause Error Message */
    SET MSG = 'Party leader needs to from existing characters';
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = MSG;
	END IF;
END$$
DELIMITER ;