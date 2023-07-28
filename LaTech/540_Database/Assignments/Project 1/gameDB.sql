CREATE DATABASE gameDB;
USE gameDB;

# Player table
DROP TABLE IF EXISTS player;
CREATE TABLE player(
		playerID		VARCHAR(15)		NOT NULL,
        userName		VARCHAR(15)		NOT NULL,
        password		VARCHAR(10)		NOT NULL,
        CONSTRAINT		plr_pk			PRIMARY KEY(playerID));

# Character table
DROP TABLE IF EXISTS charactr;
CREATE TABLE charactr(
		characterID		VARCHAR(15)		NOT NULL,
        playerID		VARCHAR(5)		NOT NULL,
        class			CHAR			NOT NULL,
        level			INTEGER,
        experience		INTEGER,
        strength		VARCHAR(50),
        agility			VARCHAR(50),
        intelligence	VARCHAR(50),
        armorClass		VARCHAR(50),
        hitPoints		VARCHAR(50),
        manna			VARCHAR(50),
        abilities		VARCHAR(50),
        coordinates		VARCHAR(50),
        CONSTRAINT		chr_pk			PRIMARY KEY(characterID));

# Location table
DROP TABLE IF EXISTS location;
CREATE TABLE location(
		coordinates		VARCHAR(10)		NOT NULL,
		description		VARCHAR(15)		NOT NULL,
        CONSTRAINT		loc_pk			PRIMARY KEY(coordinates)
        );
        
# Inventory table
DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory(
		itemName		VARCHAR(15)		NOT NULL,
		characterID		VARCHAR(15)		NOT NULL,
        quantity		DECIMAL(3,1)	NOT NULL		DEFAULT 1,
        damage			Integer			NOT NULL		DEFAULT 0,
        acBonus			Integer			DEFAULT 0,
        effects			VARCHAR(50),
        goldPc			INTEGER			DEFAULT 0,
        CONSTRAINT		inv_pk			PRIMARY KEY(itemName)
        );

# Quest table
DROP TABLE IF EXISTS quest;
CREATE TABLE quest(
		questName		VARCHAR(15)		NOT NULL,
        description		VARCHAR(50),
        experienceBonus	INTEGER			DEFAULT 0,
        rewards			INTEGER			DEFAULT 0,
        CONSTRAINT		qst_pk			PRIMARY KEY(questName)
        );

# Creature table
DROP TABLE IF EXISTS creature;
CREATE TABLE creature(
		creatName		VARCHAR(15)		NOT NULL,
        strength		VARCHAR(50),
		agility			VARCHAR(50),
        weakness		VARCHAR(50),
        xpWorth			DECIMAL(3,2)	DEFAULT 000.00,
        coordinates		VARCHAR(10)		NOT NULL,
        CONSTRAINT		crt_pk			PRIMARY KEY(creatName)
        );

# Ability table
DROP TABLE IF EXISTS ability;
CREATE TABLE ability(
		abilityName		VARCHAR(15)		NOT NULL,
		description		VARCHAR(50),
        characterID		VARCHAR(15)		NOT NULL,
        manaCost		INTEGER,
        CONSTRAINT		abt_pk			PRIMARY KEY(abilityName)
        );
        
# Warrior table
DROP TABLE IF EXISTS warrior;
CREATE TABLE warrior(
		characterID		VARCHAR(15)		NOT NULL,
		attackBonus		INTEGER			NOT NULL		DEFAULT 0,
		armorBonus		INTEGER			NOT NULL		DEFAULT 0
        );

# Mage table
DROP TABLE IF EXISTS mage;
CREATE TABLE mage(
		characterID		VARCHAR(15)		NOT NULL,
		spells			INTEGER			NOT NULL		DEFAULT 0,
		magicResis		INTEGER			NOT NULL		DEFAULT 0
        );

# Rouge table
DROP TABLE IF EXISTS rouge;
CREATE TABLE rouge(
		characterID		VARCHAR(15)		NOT NULL,
		agility			INTEGER			NOT NULL		DEFAULT 0,
		stealth			INTEGER			NOT NULL		DEFAULT 0
        );

# Adventure Party table
DROP TABLE IF EXISTS adven_party;
CREATE TABLE adven_party(
		partyLeaderID	VARCHAR(15)		NOT NULL,
		partyName		VARCHAR(15)		NOT NULL,
        questName		VARCHAR(5)		NOT NULL,
        CONSTRAINT		adv_prt_pk		PRIMARY KEY(partyLeaderID, partyName, questName)
        );


## Referential Integrity Constraints

# Character table
ALTER TABLE charactr
ADD CONSTRAINT char_player_fk
	FOREIGN KEY (playerID) REFERENCES player(playerID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
ADD CONSTRAINT char_coordinate_fk
    FOREIGN KEY (coordinates) REFERENCES location(coordinates)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
ADD CONSTRAINT char_ability_fk
    FOREIGN KEY (abilities) REFERENCES ability(abilityName)
    ON DELETE SET NULL
    ON UPDATE CASCADE;

# Inventory table
ALTER TABLE inventory
ADD CONSTRAINT inv_char_fk
	FOREIGN KEY (characterID) REFERENCES charactr(characterID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;

# Creature table
ALTER TABLE creature
ADD CONSTRAINT creat_coordinate_fk
    FOREIGN KEY (coordinates) REFERENCES location(coordinates)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;
        
# Warrior table
ALTER TABLE warrior
ADD CONSTRAINT warr_charID_fk
	FOREIGN KEY (characterID) REFERENCES charactr(characterID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;

# Mage table
ALTER TABLE mage
ADD CONSTRAINT mage_charID_fk
	FOREIGN KEY (characterID) REFERENCES charactr(characterID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;

# Rouge table
ALTER TABLE rouge
ADD CONSTRAINT rog_charID_fk
	FOREIGN KEY (characterID) REFERENCES charactr(characterID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;

# Party formation table
ALTER TABLE adven_party
ADD CONSTRAINT party_charID_fk
	FOREIGN KEY (partyLeaderID) REFERENCES charactr(characterID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
ADD CONSTRAINT party_quest_fk
	FOREIGN KEY (questName) REFERENCES quest(questName)
    ON DELETE RESTRICT
    ON UPDATE CASCADE;
    