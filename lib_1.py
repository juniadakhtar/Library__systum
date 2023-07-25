import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='mdjunaid16012002@',database='Library_system')
#if mydb.is_connected():
   # print("ADjjhhjh")
def addbook():
    a=int(input("enter ISBN_Code"))
    b=input("enter Book_Title")
    c=input("Which Language")
    d=int(input("Actual book copies"))
    e=int(input("Curent Copies of No"))
    data1=(a,b,c,d,e)
    sql="insert into book_detail(ISBN_Code,Book_Title,Language,No_Copies_Actual,No_Copies_Current) values(%s,%s,%s,%s,%s)"
    cur=mydb.cursor()
    cur.execute(sql,data1)
    mydb.commit()
    print("data ensert successfully")
    main()
def Borrow_Book():
    B_I=int(input("enter Borrower_id"))
    BK=int(input("enter book_id"))
    B_D=input("enter Borrower Date")
    I_B=int(input("No of Issued_by_book"))
    data=(B_I,BK,B_D,I_B)
    a="insert into borrower_deatil(Borrower_id,Book_id,Borrower_From_Date,Issued_by) values(%s,%s,%s,%s)"
    cur=mydb.cursor()
    cur.execute(a,data)
    mydb.commit()
    print("Book Issues to:")
    bookup(BK,-1)
def submit():
    B_I=int(input("enter Borrower_id"))
    BK_I=int(input("enter book_id"))
    S_I=input("enter submiter date")
    S_B=int(input("No of submit book"))
    a="insert into submiter_detail values(%s,%s,%s,%s)"
    data=(B_I,BK_I,S_I,S_B)
    cur=mydb.cursor()
    cur.execute(a,data)
    mydb.commit()
    print("Book submit to:",B_I)
    bookup(BK_I,1)
def bookup(BK,n):
    a="select No_Copies_Current from book_detail where ISBN_Code=%s"
    data=(BK,)
    cur=mydb.cursor()
    cur.execute(a,data)#cur=10
    result=cur.fetchone()
    C=result[0]+n
    sql="update book_detail set No_Copies_Current=%s where ISBN_Code=%s"
    d=(C,BK)
    cur.execute(sql,d)
    mydb.commit()
    main()
def dispbook():
    a="select * from book_detail"
    cur=mydb.cursor()
    cur.execute(a)
    result=cur.fetchall()
    for i in result:
        print(i)
    main()
def main():
    print("LIBARY MANAGEMENT 1.ADD BOOK 2.BORROW BOOK 3.SUBMIT DETAILS 4.DISPLAY BOOK")
    choice=input("enter task No")
    if(choice=='1'):
        addbook()
    elif(choice=='2'):
        Borrow_Book()
    elif(choice=='3'):
        submit()
    elif(choice=='4'):
        dispbook()
    else:
        print("wrong choice:")
    main()
main()
    
    
