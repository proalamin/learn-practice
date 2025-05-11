create database people;

show databases;
use people;

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
select name from people;


-- update operation
update people
set name="mr. vx"
where id=2;

set sql_safe_updates =0;  -- safe update mode of

update people
set salary= 3434333
where name= "mr. vx";

set sql_safe_updates =1;


-- delete operation
delete from people
where id=3;


-- drop

-- drop database people; -- delete database
-- drop table people; -- -- delete table

