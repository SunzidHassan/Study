-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 06, 2025 at 06:29 PM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `company`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
CREATE TABLE IF NOT EXISTS `department` (
  `dname` varchar(25) NOT NULL,
  `dnumber` int NOT NULL,
  `mgr_ssn` varchar(9) DEFAULT NULL,
  `mgr_start_date` date DEFAULT NULL,
  PRIMARY KEY (`dnumber`),
  UNIQUE KEY `dept_unique` (`dname`),
  KEY `dept_mgr_fk` (`mgr_ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`dname`, `dnumber`, `mgr_ssn`, `mgr_start_date`) VALUES
('Headquarters', 1, '888665555', '1981-06-19'),
('Administration', 4, '987654321', '1995-01-01'),
('Research', 5, '333445555', '1988-05-22');

-- --------------------------------------------------------

--
-- Table structure for table `dependent`
--

DROP TABLE IF EXISTS `dependent`;
CREATE TABLE IF NOT EXISTS `dependent` (
  `essn` varchar(9) NOT NULL,
  `dependent_name` varchar(15) NOT NULL,
  `sex` char(1) DEFAULT NULL,
  `bdate` date DEFAULT NULL,
  `relationship` enum('Spouse','Son','Daughter') NOT NULL DEFAULT 'Spouse',
  PRIMARY KEY (`essn`,`dependent_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `dependent`
--

INSERT INTO `dependent` (`essn`, `dependent_name`, `sex`, `bdate`, `relationship`) VALUES
('123456789', 'Alice', 'F', '1988-12-30', 'Daughter'),
('123456789', 'Elizabeth', 'F', '1967-05-05', 'Spouse'),
('123456789', 'Michael', 'M', '1988-01-04', 'Son'),
('333445555', 'Alice', 'F', '1986-04-05', 'Daughter'),
('333445555', 'Joy', 'F', '1958-05-03', 'Spouse'),
('333445555', 'Theodore', 'M', '1983-10-25', 'Son'),
('987654321', 'Abner', 'M', '1942-02-28', 'Spouse');

-- --------------------------------------------------------

--
-- Table structure for table `dept_locations`
--

DROP TABLE IF EXISTS `dept_locations`;
CREATE TABLE IF NOT EXISTS `dept_locations` (
  `dnumber` int NOT NULL,
  `dlocation` varchar(15) NOT NULL,
  PRIMARY KEY (`dnumber`,`dlocation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `dept_locations`
--

INSERT INTO `dept_locations` (`dnumber`, `dlocation`) VALUES
(1, 'Houston'),
(4, 'Stafford'),
(5, 'Bellaire'),
(5, 'Houston'),
(5, 'Sugarland');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `fname` varchar(15) NOT NULL,
  `minit` char(1) DEFAULT NULL,
  `lname` varchar(15) NOT NULL,
  `ssn` varchar(9) NOT NULL,
  `bdate` date DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  `super_ssn` varchar(9) DEFAULT NULL,
  `dno` int DEFAULT '1',
  PRIMARY KEY (`ssn`),
  KEY `emp_super_fk` (`super_ssn`),
  KEY `emp_dept_fk` (`dno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`fname`, `minit`, `lname`, `ssn`, `bdate`, `address`, `sex`, `salary`, `super_ssn`, `dno`) VALUES
('John', 'B', 'Smith', '123456789', '1965-01-09', '731 Fondren, Houston, TX', 'M', 30000.00, '333445555', 5),
('Franklin', 'T', 'Wong', '333445555', '1955-12-08', '638 Voss, Houston, TX', 'M', 40000.00, '888665555', 5),
('Joyce', 'A', 'English', '453453453', '1972-07-31', '5631 Rice, Houston, TX', 'F', 25000.00, '333445555', 5),
('Ramesh', 'K', 'Narayan', '666884444', '1962-09-15', '971 Fire Oak, Humble, TX', 'M', 38000.00, '333445555', 5),
('James', 'E', 'Borg', '888665555', '1937-11-10', '450 Stone, Houston, TX', 'M', 55000.00, NULL, 1),
('Jennifer', 'S', 'Wallace', '987654321', '1911-06-20', '291 Berry, Bellaire, TX', 'F', 43000.00, '888665555', 4),
('Ahmad', 'V', 'Jabbar', '987987987', '1969-03-29', '980 Dallas, Houston, TX', 'M', 25000.00, '987654321', 4),
('Alicia', 'J', 'Zelaya', '999887777', '1968-01-19', '3321 Castle, Spring, TX', 'F', 25000.00, '987654321', 4);

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
CREATE TABLE IF NOT EXISTS `project` (
  `pname` varchar(25) NOT NULL,
  `pnumber` int NOT NULL,
  `plocation` varchar(15) DEFAULT NULL,
  `dnum` int DEFAULT NULL,
  PRIMARY KEY (`pnumber`),
  UNIQUE KEY `project_unique` (`pname`),
  KEY `project_fk` (`dnum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`pname`, `pnumber`, `plocation`, `dnum`) VALUES
('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 4),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 4);

-- --------------------------------------------------------

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
CREATE TABLE IF NOT EXISTS `works_on` (
  `essn` varchar(9) NOT NULL,
  `pno` int NOT NULL,
  `hours` decimal(4,1) DEFAULT NULL,
  PRIMARY KEY (`essn`,`pno`),
  KEY `works_on_pno_fk` (`pno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `works_on`
--

INSERT INTO `works_on` (`essn`, `pno`, `hours`) VALUES
('123456789', 1, 32.5),
('123456789', 2, 7.5),
('333445555', 2, 10.0),
('333445555', 3, 10.0),
('333445555', 10, 10.0),
('333445555', 20, 10.0),
('453453453', 1, 20.0),
('453453453', 2, 20.0),
('666884444', 3, 40.0),
('888665555', 20, 0.0),
('987654321', 20, 15.0),
('987654321', 30, 20.0),
('987987987', 10, 35.0),
('987987987', 30, 5.0),
('999887777', 10, 10.0),
('999887777', 30, 30.0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `dept_mgr_fk` FOREIGN KEY (`mgr_ssn`) REFERENCES `employee` (`ssn`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `dependent`
--
ALTER TABLE `dependent`
  ADD CONSTRAINT `dependent_fk` FOREIGN KEY (`essn`) REFERENCES `employee` (`ssn`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `dept_locations`
--
ALTER TABLE `dept_locations`
  ADD CONSTRAINT `dept_loc_fk` FOREIGN KEY (`dnumber`) REFERENCES `department` (`dnumber`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `emp_dept_fk` FOREIGN KEY (`dno`) REFERENCES `department` (`dnumber`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `emp_super_fk` FOREIGN KEY (`super_ssn`) REFERENCES `employee` (`ssn`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `project`
--
ALTER TABLE `project`
  ADD CONSTRAINT `project_fk` FOREIGN KEY (`dnum`) REFERENCES `department` (`dnumber`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Constraints for table `works_on`
--
ALTER TABLE `works_on`
  ADD CONSTRAINT `works_on_pno_fk` FOREIGN KEY (`pno`) REFERENCES `project` (`pnumber`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `works_on_ssn_fk` FOREIGN KEY (`essn`) REFERENCES `employee` (`ssn`) ON DELETE RESTRICT ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
