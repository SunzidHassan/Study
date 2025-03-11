drop table if exists student;
create table student (
    Fn varchar(30) not null,
    Ln varchar(30) not null,
    constraint student_pk primary key(Fn, Ln)
);
drop table if exists instructor;
create table instructor (
    Fname varchar(30) not null,
    Lname varchar(30) not null,
    constraint student_pk primary key(Fname, Lname)
);
insert into student values ('Susan', 'Yao');
insert into student values ('Ramesh', 'Shah');
insert into student values ('Johnny', 'Kohler');
insert into student values ('Barbara', 'Jones');
insert into student values ('Amy', 'Ford');
insert into student values ('Jimmy', 'Wang');
insert into student values ('Ernest', 'Gilbert');

insert into instructor values ('John', 'Smith');
insert into instructor values ('Ricardo', 'Browne');
insert into instructor values ('Susan', 'Yao');
insert into instructor values ('Francis', 'Johnson');
insert into instructor values ('Ramesh', 'Shah');

SELECT * FROM student
UNION
SELECT * FROM instructor;

SELECT * FROM student
INTERSECT
SELECT * FROM instructor;

SELECT * FROM student
EXCEPT
SELECT * FROM instructor;
