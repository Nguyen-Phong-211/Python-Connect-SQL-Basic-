CREATE DATABASE ManagementClass

USE ManagementClass

CREATE TABLE Student(
	student_id int not null PRIMARY KEY, 
	full_name nvarchar(50), 
	class_name varchar(30), 
	school_name varchar(20)
)

SELECT * FROM [ManagementClass].[dbo].[Student]
