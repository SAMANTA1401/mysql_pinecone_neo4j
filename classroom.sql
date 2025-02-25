create database temp1;
create database college;
drop database temp1;
use college;
create table student (
id int primary key,
name varchar(50),
age int not null
);
insert into student values(1,"ARPAN",26);
insert into student values(2,"souraav",25);
select * from student;