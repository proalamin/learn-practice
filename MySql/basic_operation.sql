create database people;

show databases;
use people;

-- drop database people; -- delete database

-- create operation

create table people(
	id int primary key,
    name varchar(50),
    email varchar(100),
    salary float
);

drop table people;


-- insert operation
insert into people(id, name, email, salary)
values(1, "jon", "jon232@gmail.com", 32322);

insert into people
values(2, "mr. V", "v@v.v", 32234);

select * from people;



