SELECT * FROM library_system.borrower_deatil;
Create table Borrower_Deatil(Borrower_id int primary Key,
							  Book_id int,
							  Borrower_From_Date date,
							  Issued_by int
							  );