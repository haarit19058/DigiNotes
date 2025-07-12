


# Creating database
- create database college
- use college

# Our first table
## Create table

create table \<tablename\>(
column_name1 datatype constraint,
column_name2 datatype constraint,
column_name3 datatype constraint,
)


### Example
create table student(
roll_no int,
name varchar(30),
age int
);

insert into student 
values
(101,adam,12),
(102,bob,15);

select \* from student;     *Shows all the data from the student table*








# Database Queries

- create database \<database_name\>;
- create database if not exists \<db_name>;
- drop database db_name;
- drop database if exists db_name;
- show databases;
- show tables


# Table Queries
- create
- insert
- update
- alter
- truncate
- delete

```sql
create table table_name(
column_name1 datatype constraint,
column_name2 datatype constraint,
);




insert into table_name
(colname1,colname2);
values
(col1_v1,col2_v1),
(col1_v2,col2_v2);




update table_name
set col1=val1,col2=val2
where condition;

set sql_safe_updates=0;
--if you are using sql safe update mode




delete from table_name
where condition;


-- to change the schema

alter table table_name
add column column_name datatype constraint;

alter table table_name
drop column column_name;

alter table table_name
rename to new_table_name;

alter table table_name
change column old_name new_name new_datatype_constraint;

alter table table_name
modify col_name new_datatype new_constraint;




truncate table table_name;
-- removes all the data of the table



```




# Select Command

syntax
select col1,col2 from table_name;


select  \*  from table_name;










# Where Clause

```sql
select col1,col2 from table_name
where consditions;

select * 
from user 
where followers >=200;

```
## Operators in where
1) Arithematic :  + - \* /
2) Comparison : =   !=  >  >=  < <= 
3) Logical :  and or not in between all like any
4) Bitwise : bitwise and &     bitwise or  |

```sql
select name,age
from user 
where age>15 and follower >200;

select name,age
from user 
where age>15 or follower >200;

select name,age
from user 
where age between 15 and 17;

select name,age
from user 
where email in (email1,email2,email3);
```







# Limit Clause

- sets an upper limit on the number of tuples rows to be returned

syntax
select col1,col2 from table_name
limit number;

```sql
select name,age,email
from user 
where age>15
limit 2;
```


# Orderby Clause
- to sort ascending(ASC) or descending order(DESC)
syntax
select col1,col2 from table_name
order by col_name(s) ASC;

```sql
select name,age,followers
from user 
order by followers;

-- default is ascending and you have to specify if descending order is to be used
```



# Aggregate Functions

1) count()
2) max()
3) min()
4) sum()
5) avg()

```sql
select max(marks)
from student;

select count(age)
from user
where age=14;

-- user is the name of the table

select avg(age)
from user;

select sum(followers)
from users;

```

# Group by clause
- groups rows that have same values into summary rows.
- It collects data from multiple records and groups the results by one or more columns.

- Generally we use group by with some aggregation funcitons.

```sql
select col1,col2
from table_name
group by col_name(s);


select count(id)
from user 
group by age;
-- first it groups by age then gives the count of ids ineach group

select age,max(followers)
from user
group by age;
-- gives the maximum followers according to the age groups.


```


# Having Clause
- similar to where ie applies conditions on rows
- but it is used when we want to apply condition after grouping

syntax
select col1,col2
from table_name
group by col_name(s)
having condition;

- where is for table, having is for a group
- grouping is necessary for having

```sql
select age,max(followers)
from user
group by age
having max(followers)>200;
```

# General order to write the clauses

```sql
select columns
from table_name
where condition
group by column(s)
having condition
order by column(s) ASC;
```

# Datatypes
- char
- varchar
- blob
- int
- tinyint
- bigint
- bit
- float
- double
- boolean
- date
- year



# Constraints
- not null -- columns cannot have a null value
- unique -- all values in ccolumn are different
- default -- stes the default value of a column
- check -- it can limit the values allowed in a column

## example
salary int default 25000
constraint age_check check (age>=18 and city="Delhi")

create table user(
id int,
age int,
name varchar(30) nto null,
email varchar(50) unique,
followers int default 0,
following int,
constraint  check (age>=13)
)


# Key constraints
## Primary key constraints
- makes a column unique and not null but used only for one
- It is a column or set of columns in a table that uniquely identigies each rows.(a unique id )  There is only 1 PK & it should not be null.
```sql
create table temp(
id not null ,
	primary key(id)
)
or
create table user(
id not null primary key
);

```

- we can also make combination as primary key in sql that means that combination of both should be unique.
## Foreign key
- prevents actions that would destroy links between tables
```sql
create table temp(
cust_id int,
foreign key (cust_id) refrences customer (id)
);
```

- A foreign key is a column in a table that refers to the primary key in another table.
- FKs can have duplicate and null values
- there can be multiple FKs.

database > reverse engineer to see the connections between different tables.







# Cascading for FK
- On Delete Cascade
	- when we create a foreign key using this option , it deltes the referencing rows in the child table when the referenced row is deleted in the parent table which has a primary key.
- On update cascade
	- when we create a foreign key using updae cascade the referencing rows are updated in the chilsd table when the referenced row is updated in the parent table which has a primary key.
```sql
create table student(
id int primary key,
courseID int,
foreign key (courseID) references course(id)
on delete cascade 
on update cascade
)
```

# Joins in SQL

- used to combine rows from two or more tables, based on related column between them.

Types of Joins

- inner joins
- outer joins
	- left joins
	- right joins
	- full joins
```sql
select column(s)
from tableA
inner join tableB
on tableA.col_name = tableB.col_name


select column(s)
from tableA
left join tableB
on tableA.col_name = tableB.col_name


select column(s)
from tableA
right join tableB
on tableA.col_name = tableB.col_name


select column(s)
from tableA
full join tableB
on tableA.col_name = tableB.col_name

```


## Self join

- It is a regular join but the table is joined with itself

```sql
select column(s)
from tableA as a
join tableB as b
on a.col_name=b.col_name
```


## Natural Join
### **Features of Natural Join**

Here, we will discuss the features of natural join.
1. It will perform the Cartesian product.
2. It finds consistent tuples and deletes inconsistent tuples.
3. Then it deletes the duplicate attributes.

```sql
SELECT *
FROM TABLE1
NATURAL JOIN TABLE2;
```
# Aliases


- Instead of writing names we can use aliases like this.

```sql
select *
from student as s
inner join course as c
on s.id=c.id
```



# Union 
- It is used to combine the result -set of two or more select statements 
- Gives unique records
To use it:
- every select should have same no of columns
- columns must have similar data types
- columns in every select should be in same order

```sql
select column(s) from tableA
union
select column(s) from tableB

select column(s) from tableA
union all
select column(s) from tableB
```
- union all gives the duplicates as well


# SQL sub queries
There are three ways to write the sub queries

1) written inside select
2) written inside from
3) written inside where
- most commonly used is the third one. the following snippet is for the same.




- Query inside another query
```sql
select column(S)
from table_name
where col_name operator
(subquery)
```

*Examples*

- Get the names of all the students who scored more than the class average.

Step1: Find the avg of class
Step2: find the names of students with marks>avg

```sql
select avg(marks)
from student;

select name,marks
from student
where marks>87.6667;

-- We want a dynamic process 
-- Using sub query
select name,marks
form student
where marks>(selecct avg(marks) from students);

```


# views

- A view is a virtual table based on the result-set of an SQL statement
- A view always shows up-to-date data. The database engine recreates the view, every time a user queries it.
- Changes on virtual data doesn't reflect on the original copy.

```sql
create view view1 as
select rollno,name from student
select * from view1; 
```