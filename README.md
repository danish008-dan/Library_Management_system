📚 Library Management System (Tkinter + MySQL)
🧩 Overview

This Library Management System is a Python-based desktop application built using Tkinter (for GUI) and MySQL (for database storage).
It allows librarians and students to manage library operations such as book issue, return, student management, and fine tracking efficiently through an interactive graphical interface.

⚙️ Features
👩‍💼 Librarian Features

Secure Login: Validates librarian credentials using MySQL.

Add Books: Add new books with details like title, author, price, publisher, and type (Book, Magazine, Journal, Newspaper).

View Books: Search and view all available books by name, author, or type.

Delete Books: Remove books from the database using their serial number.

Add Student: Register new students with personal details.

View Students: Display all students with search functionality.

Delete Student: Remove a student record by roll number.

Issued Books: View the list of all currently issued books.

Deposited Books: View all returned books.

Fine Management: Display fines for lost books and allow fine clearance.

Lost Books: Manage and clear fines for lost or damaged books.

Librarian Profile: View the logged-in librarian’s personal details.

Logout: Securely log out from the system.

🎓 Student Features

Student Login: Login using student credentials.

View Available Books: Browse available books for issue.

Issue Book: Issue a book using the book’s serial number.

Deposit Book: Return previously issued books.

Report Lost Book: Mark a book as lost and automatically calculate the fine (double the price of the book).

View Fine Details: Track fines associated with lost books.

Logout: Log out of the system.

🧮 Database Structure

The system connects to a MySQL database named library_management.
The required tables and their expected structure are as follows:

1. librarian
Column	Type	Description
id	INT (PK)	Librarian ID
username	VARCHAR(50)	Login username
password	VARCHAR(50)	Login password
name	VARCHAR(100)	Librarian name
mobile	VARCHAR(15)	Mobile number
email	VARCHAR(100)	Email address
address	VARCHAR(255)	Address
2. students
Column	Type	Description
id	INT (PK)	Student ID
roll_no	VARCHAR(20)	Student Roll No
name	VARCHAR(100)	Student Name
email	VARCHAR(100)	Email Address
mobile	VARCHAR(15)	Mobile Number
address	VARCHAR(255)	Address
password	VARCHAR(50)	Student Login Password
fine	FLOAT	Total Fine Amount
3. books
Column	Type	Description
serial_no	VARCHAR(20)	Unique Book ID
title	VARCHAR(100)	Book Title
price	FLOAT	Book Price
publisher	VARCHAR(100)	Publisher Name
author	VARCHAR(100)	Author Name
book_type	VARCHAR(50)	Book Type
4. issued_books
Column	Type	Description
roll_no	VARCHAR(20)	Student Roll No
serial_no	VARCHAR(20)	Issued Book Serial No
5. lost_books
Column	Type	Description
roll_no	VARCHAR(20)	Student Roll No
serial_no	VARCHAR(20)	Lost Book Serial No
fine	FLOAT	Fine Amount
💻 Requirements

Before running the program, make sure you have the following installed:

Python 3.8+

MySQL Server

Python Packages:

pip install pymysql


(Tkinter comes pre-installed with Python.)

🚀 How to Run

Set up MySQL Database

Create a database named library_management.

Import or manually create the tables listed above.

Update Database Credentials

Open LMS_Tkinter.py and update your MySQL credentials:

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="library_management"
)


Run the Application

python LMS_Tkinter.py


Login Options

Librarian: Use username and password from the librarian table.

Student: Use name and password from the students table.

🧠 Key Modules Used

Tkinter → GUI creation and event handling.

pymysql → MySQL database connectivity.

ttk → Styled widgets (Treeview tables, scrollbars).

messagebox → Alert dialogs and confirmations.

🪄 User Interface Structure

Login Window

Options to log in as Librarian or Student.

Home Page (Librarian)

Button grid for all library operations.

Student Dashboard

Buttons for issuing, returning, and reporting lost books.

Data Tables

Scrollable Treeviews to display book and student lists.

🧰 Future Enhancements

Add Admin Panel for librarian management.

Include due date tracking and automatic fine calculation for late returns.

Improve UI styling using customtkinter or ttkbootstrap.

Add search filters and data export options (CSV/PDF).

Implement email notifications for due dates and fines.

🏁 Conclusion

This Library Management System provides a complete solution for managing library operations with an intuitive GUI and reliable database integration. It’s a beginner-friendly project for learning Python, Tkinter, and MySQL integration.
