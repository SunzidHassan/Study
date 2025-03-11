create database newdbW22;
/*drop database newdbW22;*/

use newdbW22;

CREATE TABLE STUDENT (
SID varchar(10) not null PRIMARY KEY,
SNAME varchar (45),
SADDRESS varchar(45));

create table PROFESSOR ( 
PID varchar(10) not null, 
PName varchar(45), 
Office varchar(45), 
Age Int,
primary key (PID));

create table DEPARTMENT ( 
DeptName varchar(45) not null, 
ChairmanID varchar(45), 
primary key(`DeptName`) 
);

ALTER TABLE PROFESSOR CHANGE COLUMN Age DataOfBirth DATE NULL;
ALTER TABLE PROFESSOR ADD NewDate DATE;
ALTER TABLE PROFESSOR DROP NewDate;


create table COURSE ( 
CourseNum INTEGER not null, 
DeptName varchar(45) not null, 
CourseName varchar(45), 
ClassRoom DateTime, 
Enrollment INT, 
primary key(`CourseNum`,`DeptName`),
Foreign key (DeptName) references DEPARTMENT (DeptName)
);

/* drop table COURSE; */ 


CREATE TABLE PreReq( 
CourseNum Integer not null, 
DeptName varchar(45), 
PreReqNumber INT, 
PreReqDeptName varchar(45), 
primary key(`CourseNum`,`DeptName`)
);

drop table PreReq;

CREATE TABLE PreReq( 
CourseNum Integer not null, 
DeptName varchar(45), 
PreReqNumber INT, 
PreReqDeptName varchar(45), 
FOREIGN KEY (CourseNum) REFERENCES COURSE (CourseNum),
FOREIGN KEY (DeptName) REFERENCES DEPARTMENT (DeptName)
);

CREATE TABLE Teach ( 
PID VARCHAR(10), 
CourseNum INT, 
DeptName VARCHAR(45), 
FOREIGN KEY (PID) REFERENCES PROFESSOR (PID), 
FOREIGN KEY (CourseNum) REFERENCES COURSE (CourseNum), 
FOREIGN KEY (DeptName) REFERENCES DEPARTMENT (DeptName) 
);

CREATE TABLE Take ( 
SID VARCHAR(10), 
CourseNum INT, 
DeptName VARCHAR(45), 
Grade Decimal(4,2), 
ProfessorEval int, 
FOREIGN KEY (SID) REFERENCES STUDENT (SID), 
FOREIGN KEY (CourseNum) REFERENCES COURSE (CourseNum), 
FOREIGN KEY (DeptName) REFERENCES DEPARTMENT (DeptName) 
)






