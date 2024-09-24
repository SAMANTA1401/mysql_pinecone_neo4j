SHOW DATABASES;

CREATE DATABASE test_db;

USE test_db;

create table if not exists emp_info(
		first varchar(25),
        last varchar(25),
        id int not null,
        age int,
        city varchar(25),
        state varchar(25)
);

insert into emp_info (first, last, id, age, city, state) 
values 
    ('Ava', 'Garcia', 245, 24, 'Dallas', 'TX'),
    ('Ethan', 'Hall', 246, 31, 'San Jose', 'CA'),
    ('Lily', 'Patel', 247, 20, 'Austin', 'TX'),
    ('Logan', 'Brooks', 248, 38, 'Jacksonville', 'FL'),
    ('Sophia', 'Kim', 249, 23, 'San Francisco', 'CA'),
    ('Alexander', 'Walker', 250, 42, 'Indianapolis', 'IN'),
    ('Mia', 'Allen', 251, 19, 'Columbus', 'OH'),
    ('Gabriel', 'Ryan', 252, 36, 'Fort Worth', 'TX'),
    ('Isabella', 'Jackson', 253, 21, 'Charlotte', 'NC'),
    ('Julian', 'Lewis', 254, 39, 'Memphis', 'TN');

CREATE TABLE if not exists projects (
    id INT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    project_country VARCHAR(100) NOT NULL
);


INSERT INTO projects (project_name, id, project_country)
VALUES 
    ('Sustainable Energy', 245, 'United States'),
    ('Clean Water Initiative', 246, 'Canada'),
    ('Renewable Power', 247, 'Germany'),
    ('Eco-Friendly Infrastructure', 248, 'Australia'),
    ('Green Technology', 249, 'United Kingdom'),
    ('Climate Change Mitigation', 250, 'France'),
    ('Waste Management', 251, 'Japan'),
    ('Biodiversity Conservation', 252, 'Brazil'),
    ('Energy Efficiency', 253, 'China'),
    ('Disaster Relief', 254, 'India');


SELECT * FROM test_db.emp_info; --LIMIT 0, 1000

SELECT * FROM emp_info ORDER BY id DESC limit 5 ;
SELECT * FROM emp_info ORDER BY date DESC limit 5 ;

select first, last, city from emp_info;

select first, last, city from emp_info where age>30;

select * from emp_info where first like 'j%';

select * from emp_info where last like '%s';

select * from emp_info where last like '%s%n%' or last like '%o%k%';

select * from emp_info where first like 'j%' and last like '%s';

select * from emp_info where city='Dallas' and state='TX';

select * from emp_info order by age desc;

SELECT AVG(age) as average_age FROM emp_info;

SELECT COUNT(*) as total_employees FROM emp_info;

select * from emp_info where age in(24, 42);

select * from emp_info where age not in(24, 42);



SET SQL_SAFE_UPDATES = 1;

update emp_info set state = "arizona" WHERE first ="Julian" and last = "Lewis" LIMIT 1; -- without limit it throws errro

delete from  emp_info where age = 20 LIMIT 1;

delete from emp_info;

drop table emp_info;


select * from emp_info order by age;--asc

select * from emp_info order by age desc;

select count(*) from emp_info;

select first, age, count(*) from emp_info group by first, age;


select a.first , a.last, a.id, a.age, b.project_name from emp_info a left join projects b on a.id = b.id;

select a.first , a.last, a.id, a.age, b.project_name from emp_info a right join projects b on a.id = b.id;

select a.first , a.last, a.id, a.age, b.project_name from emp_info a inner join projects b on a.id = b.id;

select a.first , a.last, a.id, a.age, b.project_name from emp_info a cross join projects b;

select a.first , a.last, a.id, a.age, b.project_name from emp_info a  join projects b;


select state, count(*) from emp_info group by state;

select min(age) from emp_info;
select max(age) from emp_info;
select avg(age) from emp_info;

select * from emp_info where age=min(age); ---error

select * from emp_info where age = (select min(age) from emp_info);
select * from emp_info where age in (select max(age) from emp_info);

select * from emp_info where age > (select age from emp_info where first ='' and last='')

select * from emp_info order by first asc;

select * from emp_info order by first asc limit 3;
select * from emp_info order by age asc limit 3;

select sum(age), state from emp_info group by state;

select * from emp_info where sum(age) > 50; --error

select sum(age), state from emp_info group by state having sum(age) >50;

select sum(age) as sum_age, state from emp_info group by state having sum(age) >50;

select concat(first, ' ', last) as full_name from emp_info;

select substr(first,1,4) as first_4_chars, first from emp_info;
select substring(first,1,4) as first_4_chars, first from emp_info;

select upper(first) as up , first from emp_info;

select character_length(first) as total_chars, first from emp_info;

select reverse(first) as rev, first from emp_info;

select datediff(last_update, create_date) from customer limit 1;

select  year(create_date) , create_date from customer limit 1;

select * from customer where email REGEXP '^w'; -- start with w
select * from customer where email REGEXP '[z]'; --z inside email
select * from customer where email REGEXP '[x-z]'; 
