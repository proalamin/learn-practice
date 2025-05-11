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

