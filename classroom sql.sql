use world
create table holiday
(
holiday_date varchar(20),
reason_for_Holiday varchar(20)
)
select * from holiday

select holiday_date,reason from holiday

create table book
(
	subject_name varchar(20) ,
    book_name varchar(20) ,
    author_name varchar(20)
);
select * from book;
select subject_name,book_name,author_name from book

create table Teacher1
(
name varchar(20) primary key,
age int,
username varchar(20),
password varchar(20)
)

select * from Teacher1
insert into Teacher1 values('pooja',35,'pooja','pooja')

delete column qualification from Teacher1
drop table Teacher1

create table Lecture1
(
subjectid varchar(20)  ,
lecday varchar(20),
faculty_name varchar(20) ,
start_time varchar(20),
end_time varchar(20)
)
select * from Lecture1
select * from teacher1
drop table Lecture1

delete from Lecture1 where faculty_name='vidya'

select faculty_name,lecday,subjectid,start_time,end_time from Lecture1 as lo join Teacher1 as tr on lo.faculty_name=tr.name

create table student1
(
	StudentId int ,
	StudentName varchar(200),
    StudentPassword varchar(200),
    faculty_name varchar(20),
    contact bigint,
    age int,
	gender varchar(200)
)
select * from student1
select StudentName,StudentPassword,gender from student1

drop table student1

Insert into student1 values  (1,'dharkan','dharkan','pooja',989562222,20,'F')
Insert into student1 values  (2,'rishika','rishika','pooja',9856232356,20,'F')


create table class
(
class_name varchar(20),
subjectname varchar(20)
)
drop table class

select * from class
insert into class values('D10','java')
insert into class values('D10','networking')
select * from lecture1
select class_name,lecday,faculty_name,subjectid,start_time,end_time from class as c join lecture1 as lo where lo.subjectid=c.subjectname

create table marks
(
StudentId int,
python int,
ds int,
C_Prog int,
HTML_CSS int
)
select * from marks
select StudentName,python,ds,C_Prog,HTML_CSS from marks as m join student1 as s on m.StudentId=s.StudentId
select * from student1
drop table marks

create table attendance
(
StudentId int,
python int,
Ds int,
C_Prog int,
HTML_CSS int
)
drop table attendance
select * from attendance
select StudentName,python,Ds,C_Prog,HTML_CSS from attendance as a join student1 as s on a.StudentId=s.StudentId
use world

select * from student1
select * from teacher1

