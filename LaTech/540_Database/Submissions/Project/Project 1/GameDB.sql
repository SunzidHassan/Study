-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ability`
--

DROP TABLE IF EXISTS `ability`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ability` (
  `abilityName` varchar(15) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `manaCost` int DEFAULT NULL,
  `characterID` varchar(45) NOT NULL,
  PRIMARY KEY (`abilityName`),
  KEY `ability_foreign_fk_idx` (`characterID`),
  CONSTRAINT `ability_foreign_fk` FOREIGN KEY (`characterID`) REFERENCES `charactr` (`characterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ability`
--

LOCK TABLES `ability` WRITE;
/*!40000 ALTER TABLE `ability` DISABLE KEYS */;
INSERT INTO `ability` VALUES ('Fireball','Casts a powerful fireball at the target',20,'Gandalf'),('Fog of War','Conjures a magical fog that obscures vision',15,'Merlin'),('Heal','Restores HP to a target or self',25,'Merlin'),('Power Strike','Unleashes a powerful melee attack',15,'Aragorn'),('Shadow Step','Allows the character to move quickly and avoid attacks. Provides a short burst of speed and agility, making it harder for enemies to hit the character.',10,'Legolas');
/*!40000 ALTER TABLE `ability` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adventure_party`
--

DROP TABLE IF EXISTS `adventure_party`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adventure_party` (
  `partyLeader` varchar(15) NOT NULL,
  `partyName` varchar(45) NOT NULL,
  `questName` varchar(45) NOT NULL,
  `area` varchar(10) NOT NULL,
  `characterID` varchar(45) NOT NULL,
  PRIMARY KEY (`characterID`,`questName`),
  KEY `adven_quest_idx` (`questName`),
  KEY `adven_area_fk_idx` (`area`),
  KEY `adven_leader_fk_idx` (`characterID`),
  CONSTRAINT `adven_leader_fk` FOREIGN KEY (`characterID`) REFERENCES `charactr` (`characterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adventure_party`
--

LOCK TABLES `adventure_party` WRITE;
/*!40000 ALTER TABLE `adventure_party` DISABLE KEYS */;
INSERT INTO `adventure_party` VALUES ('Gandalf','The Fellowship of the Ring','Quest for the Fellowship','Rivendell','Aragorn'),('Arthur','Knights of the Round Table','Quest for the Holy Grail','Camelot','Arthur'),('Gandalf','The Fellowship of the Ring','Quest for the Fellowship','Rivendell','Gandalf'),('Arthur','Knights of the Round Table','Quest for the Holy Grail','Camelot','Lancelot'),('Gandalf','The Fellowship of the Ring','Quest for the Fellowship','Rivendell','Legolas'),('Arthur','Knights of the Round Table','Quest for the Holy Grail','Camelot','Merlin');
/*!40000 ALTER TABLE `adventure_party` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `charactr`
--

DROP TABLE IF EXISTS `charactr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `charactr` (
  `characterID` varchar(15) NOT NULL,
  `playerID` varchar(15) NOT NULL,
  `class` varchar(15) DEFAULT NULL,
  `level` int DEFAULT NULL,
  `experience` int DEFAULT NULL,
  `strength` int DEFAULT NULL,
  `agility` int DEFAULT NULL,
  `intelligence` int DEFAULT NULL,
  `armorClass` int DEFAULT NULL,
  `hitPoints` int DEFAULT NULL,
  `manna` int DEFAULT NULL,
  `area` varchar(45) DEFAULT NULL,
  `totalGold` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`characterID`),
  KEY `char_playerID_fk_idx` (`playerID`),
  KEY `char_coord_fk_idx` (`area`),
  CONSTRAINT `char_playerID_fk` FOREIGN KEY (`playerID`) REFERENCES `player` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `charactr`
--

LOCK TABLES `charactr` WRITE;
/*!40000 ALTER TABLE `charactr` DISABLE KEYS */;
INSERT INTO `charactr` VALUES ('Aragorn','player789','Warrior',7,15000,18,14,12,14,70,50,'Gondor',75),('Arthur','player123','Warrior',5,8000,18,12,10,14,80,0,'Camelot',0),('Gandalf','player123','Mage',5,10000,10,12,18,10,50,100,'Rivendell',100),('Lancelot','player456','Warrior',7,12000,20,14,10,16,100,0,'Camelot',0),('Legolas','player789','Rogue',6,13000,12,20,16,12,60,80,'Mirkwood',65),('Merlin','player456','Mage',6,12000,12,10,20,8,45,120,'Camelot',90);
/*!40000 ALTER TABLE `charactr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creature`
--

DROP TABLE IF EXISTS `creature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `creature` (
  `creatureName` varchar(15) NOT NULL,
  `strength` varchar(45) DEFAULT NULL,
  `weakness` varchar(45) DEFAULT NULL,
  `xpWorth` int DEFAULT NULL,
  `area` varchar(100) DEFAULT NULL,
  `new_area` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`creatureName`),
  KEY `creat_coor_fk_idx` (`area`),
  KEY `creat_coor_fk` (`new_area`),
  CONSTRAINT `creat_coor_fk` FOREIGN KEY (`new_area`) REFERENCES `location` (`area`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creature`
--

LOCK TABLES `creature` WRITE;
/*!40000 ALTER TABLE `creature` DISABLE KEYS */;
INSERT INTO `creature` VALUES ('Goblin','Low','Light',100,NULL,'Misty Mountains'),('Orc','High','Sunlight',500,'Mirkwood',NULL),('Troll','Regeneration','Fire',800,'Misty Mountains',NULL);
/*!40000 ALTER TABLE `creature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `itemName` varchar(15) NOT NULL,
  `characterID` varchar(15) NOT NULL,
  `quantity` int DEFAULT NULL,
  `damage` int DEFAULT NULL,
  `acBonus` int DEFAULT NULL,
  `effects` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`itemName`,`characterID`),
  KEY `inven_charc_fk_idx` (`characterID`),
  CONSTRAINT `inven_charc_fk` FOREIGN KEY (`characterID`) REFERENCES `charactr` (`characterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('Bow','Legolas',1,6,0,'None'),('Chain Mail','Aragorn',1,NULL,6,'Light armor for warrior class'),('Excalibur','Arthur',1,15,5,'Legendary sword in the stone'),('Glamdring','Gandalf',1,20,5,'Increased damage against undead'),('Healing Potion','Merlin',3,0,0,'Heals 50 HP'),('Leather Armor','Legolas',1,NULL,4,'Allows stealth movement'),('Mage Robes','Gandalf',1,NULL,2,'Increase mana regeneration'),('Plate Mail','Arthur',1,0,8,'Heavy and sturdy plate mail armor'),('Plate Mail','Lancelot',1,0,8,'Heavy and sturdy plate mail armor'),('Staff','Gandalf',1,4,0,'None'),('Staff','Merlin',1,5,0,'A simple wooden staff'),('Sword','Aragorn',1,8,0,'None'),('Sword','Lancelot',1,10,0,'A powerful and sharp sword');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `area` varchar(100) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `temp_area` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`area`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES ('Camelot','Legendary castle and court of King Arthur',NULL),('Gondor','Kingdom in Middle-earth',NULL),('Mirkwood','Dark and dense forest in Middle-earth',NULL),('Misty Mountains','Mountain range in Middle-earth',NULL),('Rivendell','Elf kingdom in Middle-earth',NULL);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mage`
--

DROP TABLE IF EXISTS `mage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mage` (
  `characterID` varchar(15) NOT NULL,
  `MagicPwr` int DEFAULT NULL,
  `magicResist` int DEFAULT NULL,
  `spellName` varchar(50) DEFAULT NULL,
  KEY `mage_char_fk_idx` (`characterID`),
  CONSTRAINT `mage_char_fk` FOREIGN KEY (`characterID`) REFERENCES `charactr` (`characterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mage`
--

LOCK TABLES `mage` WRITE;
/*!40000 ALTER TABLE `mage` DISABLE KEYS */;
INSERT INTO `mage` VALUES ('Gandalf',15,20,'Fireball'),('Merlin',12,25,'FogOfWar');
/*!40000 ALTER TABLE `mage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `playerID` varchar(15) NOT NULL,
  `userName` varchar(15) NOT NULL,
  `password` varchar(10) NOT NULL,
  PRIMARY KEY (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES ('player123','JimiHendrix','pass123'),('player456','DavidGilmour','pass456'),('player789','JimMorrison','pass789');
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quest`
--

DROP TABLE IF EXISTS `quest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quest` (
  `description` varchar(200) DEFAULT NULL,
  `experienceBonus` int DEFAULT NULL,
  `rewards` int DEFAULT NULL,
  `questName` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quest`
--

LOCK TABLES `quest` WRITE;
/*!40000 ALTER TABLE `quest` DISABLE KEYS */;
INSERT INTO `quest` VALUES ('An epic quest to find the legendary Holy Grail',500,1000,'Quest for the Holy Grail'),('An epic quest to find the legendary Holy Grail',500,1000,'Quest for the Holy Grail');
/*!40000 ALTER TABLE `quest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rouge`
--

DROP TABLE IF EXISTS `rouge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rouge` (
  `characterID` varchar(15) NOT NULL,
  `agilityBonus` int DEFAULT NULL,
  `stealthBonus` int DEFAULT NULL,
  KEY `rog_char_fk` (`characterID`),
  CONSTRAINT `rog_char_fk` FOREIGN KEY (`characterID`) REFERENCES `charactr` (`characterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rouge`
--

LOCK TABLES `rouge` WRITE;
/*!40000 ALTER TABLE `rouge` DISABLE KEYS */;
INSERT INTO `rouge` VALUES ('Legolas',10,8);
/*!40000 ALTER TABLE `rouge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warrior`
--

DROP TABLE IF EXISTS `warrior`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warrior` (
  `characterID` varchar(15) NOT NULL,
  `attackBonus` int DEFAULT NULL,
  `armorBonus` int DEFAULT NULL,
  KEY `war_char_fk` (`characterID`),
  CONSTRAINT `war_char_fk` FOREIGN KEY (`characterID`) REFERENCES `charactr` (`characterID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warrior`
--

LOCK TABLES `warrior` WRITE;
/*!40000 ALTER TABLE `warrior` DISABLE KEYS */;
INSERT INTO `warrior` VALUES ('Aragorn',8,6),('Arthur',15,10),('Lancelot',20,12);
/*!40000 ALTER TABLE `warrior` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-25 15:21:34
