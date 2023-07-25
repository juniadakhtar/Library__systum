SELECT * FROM library_system.book_detail;
create database Library_System;
use Library_System;
create table Book_Detail(ISBN_Code int primary key,
                          Book_Title varchar(50),
						  Language varchar(10),
						  No_Copies_Actual int,
						  No_Copies_Current int
						  );
						  select * from Book_Detail
