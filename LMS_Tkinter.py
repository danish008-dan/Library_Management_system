import tkinter as tk
from tkinter import messagebox,ttk
import pymysql




# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        # Connect to MySQL database
        connection = pymysql.connect(
            host="localhost",  # Replace with your database host
            user="root",       # Replace with your MySQL username
            password="",       # Replace with your MySQL password
            database="library_management"  # Replace with your database name
        )
        cursor = connection.cursor()

        # Query to validate login
        query = "SELECT * FROM librarian WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login Successful!")
            root.destroy()  # Close login window
            open_home_page(result)  # Pass librarian details to the home page
        else:
            messagebox.showerror("Error", "Invalid Username or Password!")

        connection.close()
    except Exception as e:
        messagebox.showerror("Error", f"Database Error: {str(e)}")

def open_issued_books_page(current_window, librarian_details):
    # current_window.destroy()  # Close the current window

    # Create the Issued Books Page
    issued_books_page = tk.Tk()
    issued_books_page.title("Issued Books")
    issued_books_page.geometry("900x600")
    issued_books_page.resizable(True, True)

    # Title Label
    label_title = tk.Label(issued_books_page, text="Issued Books", font=("Arial", 24, "bold"))
    label_title.pack(pady=20)

    # Frame for Table
    frame_table = tk.Frame(issued_books_page)
    frame_table.pack(pady=10, fill="both", expand=True)

    # Scrollbars
    scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")
    scroll_y = ttk.Scrollbar(frame_table, orient="vertical")

    # Issued Books Table
    issued_books_table = ttk.Treeview(
        frame_table,
        columns=("Roll No", "Student Name", "Serial No", "Book Title"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
        show="headings"
    )
    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")

    scroll_x.config(command=issued_books_table.xview)
    scroll_y.config(command=issued_books_table.yview)

    # Define Table Headings
    issued_books_table.heading("Roll No", text="Roll No")
    issued_books_table.heading("Student Name", text="Student Name")
    issued_books_table.heading("Serial No", text="Serial No")
    issued_books_table.heading("Book Title", text="Book Title")


    issued_books_table.column("Roll No", width=100)
    issued_books_table.column("Student Name", width=200)
    issued_books_table.column("Serial No", width=100)
    issued_books_table.column("Book Title", width=200)


    issued_books_table.pack(fill="both", expand=True)

    # Function to Fetch Issued Books
    def fetch_issued_books():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()
            query = """
                SELECT 
                    ib.roll_no, 
                    s.name AS student_name, 
                    ib.serial_no, 
                    b.title AS book_title
                FROM 
                    issued_books ib
                JOIN 
                    students s ON ib.roll_no = s.roll_no
                JOIN 
                    books b ON ib.serial_no = b.serial_no
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            for row in rows:
                issued_books_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching issued books: {e}")
        finally:
            conn.close()

    fetch_issued_books()

    # Back to Home Button
    btn_back = tk.Button(
        issued_books_page,
        text="Back to Home",
        font=("Arial", 14),
        bg="blue",
        fg="white",
        command=lambda: [issued_books_page.destroy(), open_home_page(librarian_details)]
    )
    btn_back.pack(pady=20)

    issued_books_page.mainloop()


def open_deposited_books_page(current_window, librarian_details):
    # current_window.destroy()  # Close the current window

    # Create the Deposited Books Page
    deposited_books_page = tk.Tk()
    deposited_books_page.title("Deposited Books")
    deposited_books_page.geometry("900x600")
    deposited_books_page.resizable(True, True)

    # Title Label
    label_title = tk.Label(deposited_books_page, text="Deposited Books", font=("Arial", 24, "bold"))
    label_title.pack(pady=20)

    # Frame for Table
    frame_table = tk.Frame(deposited_books_page)
    frame_table.pack(pady=10, fill="both", expand=True)

    # Scrollbars
    scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")
    scroll_y = ttk.Scrollbar(frame_table, orient="vertical")

    # Deposited Books Table
    deposited_books_table = ttk.Treeview(
        frame_table,
        columns=("Roll No", "Student Name", "Serial No", "Book Title"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
        show="headings"
    )
    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")

    scroll_x.config(command=deposited_books_table.xview)
    scroll_y.config(command=deposited_books_table.yview)

    # Define Table Headings
    deposited_books_table.heading("Roll No", text="Roll No")
    deposited_books_table.heading("Student Name", text="Student Name")
    deposited_books_table.heading("Serial No", text="Serial No")
    deposited_books_table.heading("Book Title", text="Book Title")


    deposited_books_table.column("Roll No", width=100)
    deposited_books_table.column("Student Name", width=200)
    deposited_books_table.column("Serial No", width=100)
    deposited_books_table.column("Book Title", width=200)


    deposited_books_table.pack(fill="both", expand=True)

    # Function to Fetch Deposited Books
    def fetch_deposited_books():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()
            query = """
                SELECT 
                    db.roll_no, 
                    s.name AS student_name, 
                    db.serial_no, 
                    b.title AS book_title
                FROM 
                    issued_books db
                JOIN 
                    students s ON db.roll_no = s.roll_no
                JOIN 
                    books b ON db.serial_no = b.serial_no
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            for row in rows:
                deposited_books_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching deposited books: {e}")
        finally:
            conn.close()

    fetch_deposited_books()

    # Back to Home Button
    btn_back = tk.Button(
        deposited_books_page,
        text="Back to Home",
        font=("Arial", 14),
        bg="blue",
        fg="white",
        command=lambda: [deposited_books_page.destroy(), open_home_page(librarian_details)]
    )
    btn_back.pack(pady=20)

    deposited_books_page.mainloop()


def open_fine_page(current_window, librarian_details):
    # Create the Fine Page
    fine_page = tk.Tk()
    fine_page.title("Fines to Collect")
    fine_page.geometry("800x500")
    fine_page.resizable(False, False)

    # Title Label
    label_title = tk.Label(fine_page, text="Fines to Collect", font=("Arial", 24, "bold"))
    label_title.pack(pady=20)

    # Frame for Table
    frame_table = tk.Frame(fine_page)
    frame_table.pack(pady=10, fill="both", expand=True)

    # Scrollbars
    scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")
    scroll_y = ttk.Scrollbar(frame_table, orient="vertical")

    # Fines Table
    fines_table = ttk.Treeview(
        frame_table,
        columns=("Roll No", "Student Name", "Serial No", "Book Title", "Fine Amount"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
        show="headings"
    )
    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")

    scroll_x.config(command=fines_table.xview)
    scroll_y.config(command=fines_table.yview)

    # Define Table Headings
    fines_table.heading("Roll No", text="Roll No")
    fines_table.heading("Student Name", text="Student Name")
    fines_table.heading("Serial No", text="Serial No")
    fines_table.heading("Book Title", text="Book Title")
    fines_table.heading("Fine Amount", text="Fine Amount")

    fines_table.column("Roll No", width=100)
    fines_table.column("Student Name", width=200)
    fines_table.column("Serial No", width=100)
    fines_table.column("Book Title", width=200)
    fines_table.column("Fine Amount", width=150)

    fines_table.pack(fill="both", expand=True)

    # Function to Fetch Fines
    def fetch_fines():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()

            # Fetch fines from lost_books table, including student name and book title
            query = """
                SELECT 
                    lb.roll_no, 
                    s.name AS student_name, 
                    lb.serial_no, 
                    b.title AS book_title, 
                    lb.fine
                FROM 
                    lost_books lb
                JOIN students s ON lb.roll_no = s.roll_no
                JOIN books b ON lb.serial_no = b.serial_no
                WHERE lb.fine > 0
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            # Insert rows into the fines table
            for row in rows:
                fines_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching fines: {e}")
        finally:
            conn.close()

    fetch_fines()

    # Back to Home Button
    btn_back = tk.Button(
        fine_page,
        text="Back to Home",
        font=("Arial", 14),
        bg="blue",
        fg="white",
        command=lambda: [fine_page.destroy(), open_home_page(librarian_details)]
    )
    btn_back.pack(pady=20)

    fine_page.mainloop()



def open_lost_books_page(current_window, librarian_details):
    # Create Lost Books Page
    lost_books_page = tk.Tk()
    lost_books_page.title("Lost Books")
    lost_books_page.geometry("1000x600")
    lost_books_page.resizable(False, False)

    label_title = tk.Label(lost_books_page, text="Lost Books", font=("Arial", 18, "bold"))
    label_title.pack(pady=10)

    # Frame for Table
    frame_table = tk.Frame(lost_books_page)
    frame_table.pack(pady=10, fill="both", expand=True)

    # Scrollbars
    scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")
    scroll_y = ttk.Scrollbar(frame_table, orient="vertical")

    # Lost Books Table
    lost_books_table = ttk.Treeview(
        frame_table,
        columns=("Roll No", "Student Name", "Serial No", "Book Title", "Fine"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
        show="headings"
    )
    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")

    scroll_x.config(command=lost_books_table.xview)
    scroll_y.config(command=lost_books_table.yview)

    # Define Table Headings
    lost_books_table.heading("Roll No", text="Roll No")
    lost_books_table.heading("Student Name", text="Student Name")
    lost_books_table.heading("Serial No", text="Serial No")
    lost_books_table.heading("Book Title", text="Book Title")
    lost_books_table.heading("Fine", text="Fine")

    lost_books_table.column("Roll No", width=150)
    lost_books_table.column("Student Name", width=200)
    lost_books_table.column("Serial No", width=150)
    lost_books_table.column("Book Title", width=250)
    lost_books_table.column("Fine", width=100)

    lost_books_table.pack(fill="both", expand=True)

    # Fetch and Display Lost Books
    def fetch_lost_books():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()

            # Fetch all lost books with student names and book titles
            cursor.execute("""
                SELECT lb.roll_no, s.name, lb.serial_no, b.title, lb.fine
                FROM lost_books lb
                JOIN students s ON lb.roll_no = s.roll_no
                JOIN books b ON lb.serial_no = b.serial_no
            """)
            rows = cursor.fetchall()

            # Clear existing rows in the table
            for row in lost_books_table.get_children():
                lost_books_table.delete(row)

            # Insert rows into the table
            for row in rows:
                lost_books_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching lost books: {e}")
        finally:
            conn.close()

    fetch_lost_books()

    # Function to Clear Fine for a Student
    def clear_fine():
        selected_item = lost_books_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to clear fine!")
            return

        record = lost_books_table.item(selected_item)["values"]
        roll_no, serial_no, fine = record[0], record[2], record[4]

        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()

            # Delete the record from the lost_books table
            cursor.execute("DELETE FROM lost_books WHERE roll_no = %s AND serial_no = %s", (roll_no, serial_no))
            conn.commit()

            # Update the student's fine in the students table
            cursor.execute("UPDATE students SET fine = fine - %s WHERE roll_no = %s", (fine, roll_no))
            conn.commit()

            messagebox.showinfo("Success", f"Fine of {fine} cleared for Roll No: {roll_no}")
            fetch_lost_books()  # Refresh the table

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

    # Clear Fine Button
    btn_clear_fine = tk.Button(lost_books_page, text="Clear Fine", font=("Arial", 12), bg="green", fg="white", command=clear_fine)
    btn_clear_fine.pack(pady=10)

    # Back to Home Button
    btn_back = tk.Button(lost_books_page, text="Back to Home", font=("Arial", 12), bg="blue", fg="white",
                         command=lambda: [lost_books_page.destroy(), open_home_page(librarian_details)])
    btn_back.pack(pady=10)

    lost_books_page.mainloop()




# Function to open the Home Page
def open_home_page(librarian_details):
    # Create the Home Page window
    home_page = tk.Tk()
    home_page.title("Library Management System - Home")
    home_page.geometry("600x700")
    home_page.resizable(True, True)

    # Title Label
    label_title = tk.Label(home_page, text="Library Home", font=("Arial", 24, "bold"))
    label_title.pack(pady=20)

    # Create a frame for buttons
    frame_buttons = tk.Frame(home_page)
    frame_buttons.pack(pady=10, fill="both", expand=True)

    # Add Buttons with Grid Layout
    buttons = [
        ("Profile", lambda: [home_page.destroy(), open_profile_page(home_page, librarian_details)]),
        ("Add Books", lambda: [home_page.destroy(), open_add_books_page(home_page, librarian_details)]),
        ("View Books", lambda: [home_page.destroy(), open_view_books_page(home_page, librarian_details)]),
        ("Add Student", lambda: [home_page.destroy(), open_add_student_page(home_page, librarian_details)]),
        ("Delete Student", lambda: [home_page.destroy(), open_delete_student_page(home_page, librarian_details)]),
        ("View Student", lambda: [home_page.destroy(), open_view_student_page(home_page, librarian_details)]),
        ("Delete Book", lambda: [home_page.destroy(), open_delete_book_page(home_page, librarian_details)]),
        ("Issued Books", lambda: [home_page.destroy(), open_issued_books_page(home_page, librarian_details)]),
        ("Deposited Books", lambda: [home_page.destroy(), open_deposited_books_page(home_page, librarian_details)]),
        ("Fine to Collect", lambda: [home_page.destroy(), open_fine_page(home_page, librarian_details)]),
        ("Lost Books", lambda: [home_page.destroy(), open_lost_books_page(home_page, librarian_details)]),
    ]

    # Arrange buttons in a grid
    for i, (text, command) in enumerate(buttons):
        row, col = divmod(i, 2)  # Arrange in two columns
        button = tk.Button(
            frame_buttons,
            text=text,
            font=("Arial", 14),
            width=20,
            command=command
        )
        button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    # Configure grid to expand
    for col in range(2):
        frame_buttons.columnconfigure(col, weight=1)

    # Logout Button
    btn_logout = tk.Button(
        home_page,
        text="Logout",
        font=("Arial", 14),
        bg="red",
        fg="white",
        command=lambda: home_page.destroy()
    )
    btn_logout.pack(pady=20)

    home_page.mainloop()




# Function to open the Profile Page (placeholder)
# Function to open the Profile Page
def open_profile_page(current_window, librarian_details):
    # Close the current window (Home Page)
    # current_window.destroy()

    # Create the Profile Page window
    profile_page = tk.Tk()
    profile_page.title("Library Management System - Profile")
    profile_page.geometry("400x400")
    profile_page.resizable(False, False)

    # Display Librarian Details
    label_title = tk.Label(profile_page, text="Librarian Profile", font=("Arial", 18, "bold"))
    label_title.pack(pady=20)

    # Extract librarian details
    name = librarian_details[3]  # Assuming index 3 is 'name' in result from DB
    mobile = librarian_details[4]  # Assuming index 4 is 'mobile'
    email = librarian_details[5]  # Assuming index 5 is 'email'
    address = librarian_details[6]  # Assuming index 6 is 'address'

    label_name = tk.Label(profile_page, text=f"Name: {name}", font=("Arial", 12))
    label_name.pack(pady=5)

    label_mobile = tk.Label(profile_page, text=f"Mobile: {mobile}", font=("Arial", 12))
    label_mobile.pack(pady=5)

    label_email = tk.Label(profile_page, text=f"Email: {email}", font=("Arial", 12))
    label_email.pack(pady=5)

    label_address = tk.Label(profile_page, text=f"Address: {address}", font=("Arial", 12))
    label_address.pack(pady=5)

    # Back button to return to Home Page
    btn_back = tk.Button(
        profile_page,
        text="Back to Home",
        font=("Arial", 12, "bold"),
        bg="blue",
        fg="white",
        command=lambda: [profile_page.destroy(), open_home_page(librarian_details)]
    )
    btn_back.pack(pady=20)

    profile_page.mainloop()


def open_add_student_page(current_window, librarian_details):
    # current_window.destroy()

    add_student_page = tk.Tk()
    add_student_page.title("Add Student")
    add_student_page.geometry("500x400")
    add_student_page.resizable(False, False)

    label_title = tk.Label(add_student_page, text="Add Student", font=("Arial", 18, "bold"))
    label_title.grid(row=0, column=0, columnspan=2, pady=20)

    # Student Name
    label_name = tk.Label(add_student_page, text="Student Name", font=("Arial", 12))
    label_name.grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_name = tk.Entry(add_student_page, font=("Arial", 12), width=30)
    entry_name.grid(row=1, column=1, padx=10, pady=5)

    # Student Roll No
    label_roll_no = tk.Label(add_student_page, text="Roll No", font=("Arial", 12))
    label_roll_no.grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_roll_no = tk.Entry(add_student_page, font=("Arial", 12), width=30)
    entry_roll_no.grid(row=2, column=1, padx=10, pady=5)

    # Student Email
    label_email = tk.Label(add_student_page, text="Email", font=("Arial", 12))
    label_email.grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entry_email = tk.Entry(add_student_page, font=("Arial", 12), width=30)
    entry_email.grid(row=3, column=1, padx=10, pady=5)

    # Student Mobile
    label_mobile = tk.Label(add_student_page, text="Mobile No", font=("Arial", 12))
    label_mobile.grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entry_mobile = tk.Entry(add_student_page, font=("Arial", 12), width=30)
    entry_mobile.grid(row=4, column=1, padx=10, pady=5)

    # Student Address
    label_address = tk.Label(add_student_page, text="Address", font=("Arial", 12))
    label_address.grid(row=5, column=0, sticky="e", padx=10, pady=5)
    entry_address = tk.Entry(add_student_page, font=("Arial", 12), width=30)
    entry_address.grid(row=5, column=1, padx=10, pady=5)

    def save_student():
        name = entry_name.get()
        roll_no = entry_roll_no.get()
        email = entry_email.get()
        mobile = entry_mobile.get()
        address = entry_address.get()

        if not (name and roll_no and email and mobile and address):
            messagebox.showerror("Input Error", "Please fill in all fields")
            return

        try:
            # Connect to MySQL and save data
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="library_management"
            )
            cursor = connection.cursor()
            query = "INSERT INTO students (roll_no, name, email, mobile, address) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (roll_no, name, email, mobile, address))
            connection.commit()
            connection.close()

            messagebox.showinfo("Success", "Student added successfully!")
            add_student_page.destroy()
            open_home_page(librarian_details)  # Go back to home page

        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # Save Button
    btn_save = tk.Button(add_student_page, text="Save Student", font=("Arial", 12), bg="green", fg="white", command=save_student)
    btn_save.grid(row=6, column=0, columnspan=2, pady=20)

    # Back Button
    btn_back = tk.Button(add_student_page, text="Back to Home", font=("Arial", 12), bg="blue", fg="white", command=lambda: [add_student_page.destroy(), open_home_page(librarian_details)])
    btn_back.grid(row=7, column=0, columnspan=2, pady=10)

    add_student_page.mainloop()


def open_delete_student_page(current_window, librarian_details):
    # current_window.destroy()

    delete_student_page = tk.Tk()
    delete_student_page.title("Delete Student")
    delete_student_page.geometry("400x400")
    delete_student_page.resizable(False, False)

    label_title = tk.Label(delete_student_page, text="Delete Student", font=("Arial", 18, "bold"))
    label_title.pack(pady=20)

    # Student Roll No
    label_roll_no = tk.Label(delete_student_page, text="Enter Roll No to delete:", font=("Arial", 12))
    label_roll_no.pack(pady=10)
    entry_roll_no = tk.Entry(delete_student_page, font=("Arial", 12))
    entry_roll_no.pack(pady=10)

    def delete_student():
        roll_no = entry_roll_no.get().strip()
        if roll_no == "":
            messagebox.showerror("Error", "Roll No cannot be empty.")
            return

        try:
            # Establish the database connection
            con = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cur = con.cursor()

            # Check if the student exists
            cur.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
            result = cur.fetchone()
            if not result:
                messagebox.showinfo("Not Found", f"No student found with Roll No {roll_no}.")
                return

            # Delete the student
            cur.execute("DELETE FROM students WHERE roll_no = %s", (roll_no,))
            con.commit()
            messagebox.showinfo("Success", f"Student with Roll No {roll_no} deleted successfully.")

            # Clear the input field
            entry_roll_no.delete(0, tk.END)
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
        finally:
            if con:
                con.close()

    btn_delete_student = tk.Button(delete_student_page, text="Delete Student", font=("Arial", 12),
                                   command=delete_student)
    btn_delete_student.pack(pady=20)

    btn_back = tk.Button(
        delete_student_page,
        text="Back to Home",
        font=("Arial", 12),
        bg="blue",
        fg="white",
        command=lambda: [delete_student_page.destroy(), open_home_page(librarian_details)],
    )
    btn_back.pack(pady=10)

    delete_student_page.mainloop()


def open_view_student_page(current_window, librarian_details):
    # current_window.destroy()

    view_student_page = tk.Tk()
    view_student_page.title("View Students")
    view_student_page.geometry("600x700")
    view_student_page.resizable(True, True)

    label_title = tk.Label(view_student_page, text="View Students", font=("Arial", 18, "bold"))
    label_title.pack(pady=20)

    # Frame for the Treeview and Scrollbar
    frame_treeview = tk.Frame(view_student_page)
    frame_treeview.pack(fill="both", expand=True, padx=20, pady=10)

    # Treeview (Table) to display students
    columns = ("ID", "Roll No", "Name", "Email", "Mobile", "Address")
    tree = ttk.Treeview(frame_treeview, columns=columns, show="headings")
    tree.pack(side="left", fill="both", expand=True)

    # Scrollbar for the Treeview
    scrollbar = tk.Scrollbar(frame_treeview, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    def fetch_students():
        try:
            # Connect to the MySQL database
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="library_management"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()

            # Clear the treeview before inserting new data
            for row in tree.get_children():
                tree.delete(row)

            # Insert student data into the treeview
            for student in students:
                tree.insert("", "end", values=student)

            connection.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching students: {e}")

    fetch_students()  # Initially load student data

    # Search functionality
    def search_students():
        search_query = entry_search.get().lower()
        if not search_query:
            fetch_students()
            return

        try:
            # Connect to MySQL and search data
            connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="library_management"
            )
            cursor = connection.cursor()
            query = "SELECT * FROM students WHERE LOWER(name) LIKE %s OR LOWER(roll_no) LIKE %s"
            cursor.execute(query, ('%' + search_query + '%', '%' + search_query + '%'))
            students = cursor.fetchall()

            # Clear the treeview before inserting new data
            for row in tree.get_children():
                tree.delete(row)

            # Insert the search results into the treeview
            for student in students:
                tree.insert("", "end", values=student)

            connection.close()

        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching students: {e}")

    # Search entry and button
    search_frame = tk.Frame(view_student_page)
    search_frame.pack(pady=10)

    label_search = tk.Label(search_frame, text="Search by Name or Roll No:", font=("Arial", 12))
    label_search.grid(row=0, column=0, padx=10)

    entry_search = tk.Entry(search_frame, font=("Arial", 12), width=25)
    entry_search.grid(row=0, column=1, padx=10)

    btn_search = tk.Button(search_frame, text="Search", font=("Arial", 12), command=search_students)
    btn_search.grid(row=0, column=2, padx=10)

    # Back Button to Home
    def back_to_home():
        view_student_page.destroy()
        open_home_page(librarian_details)

    btn_back = tk.Button(view_student_page, text="Back to Home", font=("Arial", 12), bg="blue", fg="white",
                         command=back_to_home)
    btn_back.pack(pady=20)

    view_student_page.mainloop()


def open_delete_book_page(current_window, librarian_details):
    # current_window.destroy()

    delete_book_page = tk.Tk()
    delete_book_page.title("Delete Book")
    delete_book_page.geometry("400x400")
    delete_book_page.resizable(False, False)

    label_title = tk.Label(delete_book_page, text="Delete Book", font=("Arial", 18, "bold"))
    label_title.pack(pady=20)

    # Book Serial No
    label_serial_no = tk.Label(delete_book_page, text="Enter Serial No to delete:", font=("Arial", 12))
    label_serial_no.pack(pady=10)
    entry_serial_no = tk.Entry(delete_book_page, font=("Arial", 12))
    entry_serial_no.pack(pady=10)

    def delete_book():
        serial_no = entry_serial_no.get().strip()
        if serial_no == "":
            messagebox.showerror("Error", "Serial No cannot be empty.")
            return

        try:
            # Establish database connection
            con = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cur = con.cursor()

            # Check if the book exists
            cur.execute("SELECT * FROM books WHERE serial_no = %s", (serial_no,))
            result = cur.fetchone()
            if not result:
                messagebox.showinfo("Not Found", f"No book found with Serial No {serial_no}.")
                return

            # Delete the book
            cur.execute("DELETE FROM books WHERE serial_no = %s", (serial_no,))
            con.commit()
            messagebox.showinfo("Success", f"Book with Serial No {serial_no} deleted successfully.")

            # Clear the input field
            entry_serial_no.delete(0, tk.END)
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
        finally:
            if con:
                con.close()

    btn_delete_book = tk.Button(delete_book_page, text="Delete Book", font=("Arial", 12), command=delete_book)
    btn_delete_book.pack(pady=20)

    btn_back = tk.Button(
        delete_book_page,
        text="Back to Home",
        font=("Arial", 12),
        bg="blue",
        fg="white",
        command=lambda: [delete_book_page.destroy(), open_home_page(librarian_details)],
    )
    btn_back.pack(pady=10)

    delete_book_page.mainloop()


def open_view_books_page(current_window, librarian_details):
    # Close the current window
    # current_window.destroy()

    # Create the View Books Page window
    view_books_page = tk.Tk()
    view_books_page.title("Library Management System - View Books")
    view_books_page.geometry("800x600")
    view_books_page.resizable(False, False)

    # Title Label
    label_title = tk.Label(view_books_page, text="View Books", font=("Arial", 18, "bold"))
    label_title.pack(pady=20)

    # Search Fields
    search_label = tk.Label(view_books_page, text="Search By Name or Type:", font=("Arial", 12))
    search_label.pack(pady=10)

    search_var = tk.StringVar()
    search_entry = tk.Entry(view_books_page, font=("Arial", 12), textvariable=search_var)
    search_entry.pack(pady=10, padx=20, fill="x")

    search_type_var = tk.StringVar()
    search_type_var.set("All")
    type_dropdown = ttk.Combobox(view_books_page, textvariable=search_type_var,
                                 values=["All", "Book", "Magazine", "Newspaper", "Journal"], font=("Arial", 12))
    type_dropdown.pack(pady=10)

    def search_books():
        search_term = search_var.get().lower()
        search_type = search_type_var.get()
        # Clear previous results in the treeview
        for row in tree.get_children():
            tree.delete(row)

        try:
            # Connect to MySQL
            connection = pymysql.connect(
                host="localhost",  # Replace with your database host
                user="root",  # Replace with your MySQL username
                password="",  # Replace with your MySQL password
                database="library_management"  # Replace with your database name
            )
            cursor = connection.cursor()

            query = "SELECT serial_no,title,price,publisher,author,book_type FROM books WHERE (LOWER(title) LIKE %s OR LOWER(author) LIKE %s)"
            params = [f"%{search_term}%", f"%{search_term}%"]

            if search_type != "All":
                query += " AND book_type = %s"
                params.append(search_type)

            cursor.execute(query, tuple(params))
            books = cursor.fetchall()
            connection.close()

            # Insert books into the table (Treeview)
            for book in books:
                tree.insert("", "end", values=book)

        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

    # Search Button
    btn_search = tk.Button(
        view_books_page,
        text="Search",
        font=("Arial", 12, "bold"),
        bg="green",
        fg="white",
        command=search_books
    )
    btn_search.pack(pady=10)

    # Create Table (Treeview) to display books
    columns = ("Serial No", "Title", "Price", "Publisher", "Author", "Type")
    tree = ttk.Treeview(view_books_page, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(pady=20, padx=20, fill="both", expand=True)

    # Back Button
    btn_back = tk.Button(
        view_books_page,
        text="Back to Home",
        font=("Arial", 12, "bold"),
        bg="blue",
        fg="white",
        command=lambda: [view_books_page.destroy(), open_home_page(librarian_details)]
    )
    btn_back.pack(pady=10)

    view_books_page.mainloop()



# Function to open the Add Books Page (placeholder)
# Function to open the Add Books Page
def open_add_books_page(current_window,librarian_details):
    # Close the current window (Home Page)
    # current_window.destroy()

    # Create the Add Books Page window
    add_books_page = tk.Tk()
    add_books_page.title("Library Management System - Add Book")
    add_books_page.geometry("500x600")
    add_books_page.resizable(False, False)

    # Title label
    label_title = tk.Label(add_books_page, text="Add a New Book", font=("Arial", 18, "bold"))
    label_title.grid(row=0, column=0, columnspan=2, pady=20)

    # Form Fields
    label_serial_no = tk.Label(add_books_page, text="Serial Number:", font=("Arial", 12))
    label_serial_no.grid(row=1, column=0, padx=20, pady=10, sticky="w")
    entry_serial_no = tk.Entry(add_books_page, font=("Arial", 12), width=30)
    entry_serial_no.grid(row=1, column=1, padx=20, pady=10)

    label_book_title = tk.Label(add_books_page, text="Book Title:", font=("Arial", 12))
    label_book_title.grid(row=2, column=0, padx=20, pady=10, sticky="w")
    entry_book_title = tk.Entry(add_books_page, font=("Arial", 12), width=30)
    entry_book_title.grid(row=2, column=1, padx=20, pady=10)

    label_price = tk.Label(add_books_page, text="Price:", font=("Arial", 12))
    label_price.grid(row=3, column=0, padx=20, pady=10, sticky="w")
    entry_price = tk.Entry(add_books_page, font=("Arial", 12), width=30)
    entry_price.grid(row=3, column=1, padx=20, pady=10)

    label_publisher = tk.Label(add_books_page, text="Publisher:", font=("Arial", 12))
    label_publisher.grid(row=4, column=0, padx=20, pady=10, sticky="w")
    entry_publisher = tk.Entry(add_books_page, font=("Arial", 12), width=30)
    entry_publisher.grid(row=4, column=1, padx=20, pady=10)

    label_author = tk.Label(add_books_page, text="Author:", font=("Arial", 12))
    label_author.grid(row=5, column=0, padx=20, pady=10, sticky="w")
    entry_author = tk.Entry(add_books_page, font=("Arial", 12), width=30)
    entry_author.grid(row=5, column=1, padx=20, pady=10)

    label_book_type = tk.Label(add_books_page, text="Book Type:", font=("Arial", 12))
    label_book_type.grid(row=6, column=0, padx=20, pady=10, sticky="w")

    # Dropdown menu for Book Type
    book_type_options = ["Book", "Magazine", "Newspaper", "Journal"]
    book_type_var = tk.StringVar()
    book_type_var.set(book_type_options[0])  # Default value
    dropdown_book_type = tk.OptionMenu(add_books_page, book_type_var, *book_type_options)
    dropdown_book_type.grid(row=6, column=1, padx=20, pady=10)

    # Function to save book details
    def save_book():
        serial_no = entry_serial_no.get()
        book_title = entry_book_title.get()
        price = entry_price.get()
        publisher = entry_publisher.get()
        author = entry_author.get()
        book_type = book_type_var.get()

        if not serial_no or not book_title or not price or not publisher or not author:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            # Connect to MySQL database
            connection = pymysql.connect(
                host="localhost",  # Replace with your database host
                user="root",       # Replace with your MySQL username
                password="",       # Replace with your MySQL password
                database="library_management"  # Replace with your database name
            )
            cursor = connection.cursor()

            # Insert book details into the database
            query = """
                INSERT INTO books (serial_no, title, price, publisher, author, book_type)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (serial_no, book_title, price, publisher, author, book_type))
            connection.commit()

            messagebox.showinfo("Success", "Book added successfully!")
            connection.close()

            # Clear the form
            entry_serial_no.delete(0, tk.END)
            entry_book_title.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            entry_publisher.delete(0, tk.END)
            entry_author.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {str(e)}")

    # Submit Button
    btn_submit = tk.Button(
        add_books_page,
        text="Add Book",
        font=("Arial", 12, "bold"),
        bg="green",
        fg="white",
        command=save_book
    )
    btn_submit.grid(row=7, column=0, columnspan=2, pady=20)

    # Back Button to return to Home Page
    btn_back = tk.Button(
        add_books_page,
        text="Back to Home",
        font=("Arial", 12, "bold"),
        bg="blue",
        fg="white",
        command=lambda: [add_books_page.destroy(), open_home_page(librarian_details)]
    )
    btn_back.grid(row=8, column=0, columnspan=2, pady=10)

    add_books_page.mainloop()


# Main Login Page
root = tk.Tk()
root.title("Library Management System - Login")
root.geometry("400x350")
root.resizable(False, False)

# Create and place labels and entry widgets
label_title = tk.Label(root, text="Librarian Login", font=("Arial", 18, "bold"))
label_title.pack(pady=20)

label_username = tk.Label(root, text="Username:", font=("Arial", 12))
label_username.pack(pady=5)
entry_username = tk.Entry(root, font=("Arial", 12), width=30)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:", font=("Arial", 12))
label_password.pack(pady=5)
entry_password = tk.Entry(root, font=("Arial", 12), show="*", width=30)
entry_password.pack(pady=5)

# Librarian Login button
btn_login = tk.Button(root, text="Login as Librarian", font=("Arial", 12, "bold"), bg="blue", fg="white", command=validate_login)
btn_login.pack(pady=10)

def open_student_home_page(student_details):
    """
    Opens the Student Home Page.
    `student_details` contains the student's data from the database.
    """
    student_home_page = tk.Toplevel(root)
    student_home_page.title("Student Home Page")
    student_home_page.geometry("600x400")
    student_home_page.resizable(False, False)

    # Display welcome message
    welcome_label = tk.Label(student_home_page, text=f"Welcome, {student_details[2]}!", font=("Arial", 16, "bold"))
    welcome_label.pack(pady=20)

    # Add buttons for various features
    btn_issue_book = tk.Button(student_home_page, text="Issue Book", font=("Arial", 12), command=lambda: open_issue_book_page(student_home_page,student_details))
    btn_issue_book.pack(pady=10)

    btn_deposit_book = tk.Button(student_home_page, text="Deposit Book", font=("Arial", 12), command=lambda: open_deposit_book_page(student_home_page,student_details))
    btn_deposit_book.pack(pady=10)

    btn_lost_book = tk.Button(student_home_page, text="Report Lost Book", font=("Arial", 12), command=lambda: open_lost_book_page(student_home_page,student_details))
    btn_lost_book.pack(pady=10)

    btn_logout = tk.Button(student_home_page, text="Logout", font=("Arial", 12), bg="red", fg="white", command=student_home_page.destroy)
    btn_logout.pack(pady=10)

# Placeholder functions for Issue, Deposit, and Lost Book functionalities
def open_issue_book_page(current_window, student_details):
    # current_window.destroy()  # Close the current window

    issue_book_page = tk.Tk()
    issue_book_page.title("Issue Book")
    issue_book_page.geometry("900x700")  # Increased width and height
    issue_book_page.resizable(True, True)

    label_title = tk.Label(issue_book_page, text="Issue Book", font=("Arial", 18, "bold"))
    label_title.pack(pady=10)

    # Frame for Book Table
    frame_table = tk.Frame(issue_book_page)
    frame_table.pack(pady=10, fill="both", expand=True)

    # Scrollbars
    scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")
    scroll_y = ttk.Scrollbar(frame_table, orient="vertical")

    # Book Table
    book_table = ttk.Treeview(
        frame_table,
        columns=("Serial No", "Title", "Price", "Publisher", "Author", "Type"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
        show="headings"
    )
    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")

    scroll_x.config(command=book_table.xview)
    scroll_y.config(command=book_table.yview)

    # Define Table Headings
    book_table.heading("Serial No", text="Serial No")
    book_table.heading("Title", text="Title")
    book_table.heading("Price", text="Price")
    book_table.heading("Publisher", text="Publisher")
    book_table.heading("Author", text="Author")
    book_table.heading("Type", text="Type")

    book_table.column("Serial No", width=100)
    book_table.column("Title", width=200)
    book_table.column("Price", width=100)
    book_table.column("Publisher", width=200)
    book_table.column("Author", width=200)
    book_table.column("Type", width=100)

    book_table.pack(fill="both", expand=True)

    # Fetch and Display Books
    def fetch_books():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()
            cursor.execute("SELECT serial_no, title, price, publisher, author, book_type FROM books")
            rows = cursor.fetchall()

            # Clear existing rows
            for row in book_table.get_children():
                book_table.delete(row)

            # Add fetched rows
            for row in rows:
                book_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching books: {e}")
        finally:
            conn.close()

    fetch_books()

    # Serial No Entry
    form_frame = tk.Frame(issue_book_page)
    form_frame.pack(pady=20)

    label_serial_no = tk.Label(form_frame, text="Enter Book Serial No:", font=("Arial", 12))
    label_serial_no.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_serial_no = tk.Entry(form_frame, font=("Arial", 12), width=30)
    entry_serial_no.grid(row=0, column=1, padx=10, pady=5)

    # Roll No Entry
    label_roll_no = tk.Label(form_frame, text="Enter Student Roll No:", font=("Arial", 12))
    label_roll_no.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_roll_no = tk.Entry(form_frame, font=("Arial", 12), width=30)
    entry_roll_no.grid(row=1, column=1, padx=10, pady=5)

    # Function to Issue Book
    def issue_book():
        serial_no = entry_serial_no.get().strip()
        roll_no = entry_roll_no.get().strip()

        if not serial_no or not roll_no:
            messagebox.showerror("Error", "Both fields are required!")
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()

            # Check if the book exists
            cursor.execute("SELECT * FROM books WHERE serial_no = %s", (serial_no,))
            book = cursor.fetchone()

            if not book:
                messagebox.showerror("Error", "Book not found!")
                return

            # Check if the student exists
            cursor.execute("SELECT * FROM students WHERE roll_no = %s", (roll_no,))
            student = cursor.fetchone()

            if not student:
                messagebox.showerror("Error", "Student not found!")
                return

            # Issue the book
            cursor.execute("INSERT INTO issued_books (roll_no, serial_no) VALUES (%s, %s)", (roll_no, serial_no))
            conn.commit()
            messagebox.showinfo("Success", "Book issued successfully!")
            fetch_books()  # Refresh the book list

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

    btn_issue = tk.Button(issue_book_page, text="Issue Book", font=("Arial", 12), bg="green", fg="white", command=issue_book)
    btn_issue.pack(pady=10)

    # Back to Home Button
    btn_back = tk.Button(issue_book_page, text="Back to Home", font=("Arial", 12), bg="blue", fg="white",
                         command=lambda: [issue_book_page.destroy(), open_student_home_page(student_details)])
    btn_back.pack(pady=10)

    issue_book_page.mainloop()


def open_deposit_book_page(current_window, student_details):
    # current_window.destroy()  # Close the current window

    deposit_book_page = tk.Tk()
    deposit_book_page.title("Deposit Book")
    deposit_book_page.geometry("800x500")
    deposit_book_page.resizable(False, False)

    label_title = tk.Label(deposit_book_page, text="Deposit Book", font=("Arial", 18, "bold"))
    label_title.pack(pady=10)

    # Frame for Book Table
    frame_table = tk.Frame(deposit_book_page)
    frame_table.pack(pady=10, fill="both", expand=True)

    # Scrollbars
    scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")
    scroll_y = ttk.Scrollbar(frame_table, orient="vertical")

    # Book Table
    book_table = ttk.Treeview(
        frame_table,
        columns=("Serial No", "Title", "Price", "Publisher", "Author", "Type"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
        show="headings"
    )
    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")

    scroll_x.config(command=book_table.xview)
    scroll_y.config(command=book_table.yview)

    # Define Table Headings
    book_table.heading("Serial No", text="Serial No")
    book_table.heading("Title", text="Title")
    book_table.heading("Price", text="Price")
    book_table.heading("Publisher", text="Publisher")
    book_table.heading("Author", text="Author")
    book_table.heading("Type", text="Type")

    book_table.column("Serial No", width=100)
    book_table.column("Title", width=200)
    book_table.column("Price", width=80)
    book_table.column("Publisher", width=150)
    book_table.column("Author", width=150)
    book_table.column("Type", width=100)

    book_table.pack(fill="both", expand=True)

    # Fetch and Display Books Issued to Student
    def fetch_issued_books():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()

            # Fetch books issued to the student based on roll_no
            cursor.execute("SELECT b.serial_no, b.title, b.price, b.publisher, b.author, b.book_type "
                           "FROM books b "
                           "JOIN issued_books ib ON b.serial_no = ib.serial_no "
                           "WHERE ib.roll_no = %s", (student_details[1],))
            rows = cursor.fetchall()

            # Clear any existing rows in the table
            for row in book_table.get_children():
                book_table.delete(row)

            # Insert new rows in the table
            for row in rows:
                book_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching issued books: {e}")
        finally:
            conn.close()

    fetch_issued_books()

    # Serial No Entry (for Book to be Deposited)
    label_serial_no = tk.Label(deposit_book_page, text="Enter Book Serial No to Deposit:", font=("Arial", 12))
    label_serial_no.pack(pady=10)
    entry_serial_no = tk.Entry(deposit_book_page, font=("Arial", 12), width=30)
    entry_serial_no.pack(pady=5)

    # Function to Deposit Book
    def deposit_book():
        serial_no = entry_serial_no.get().strip()

        if not serial_no:
            messagebox.showerror("Error", "Serial No is required!")
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()

            # Check if the book is issued to the student
            cursor.execute("SELECT * FROM issued_books WHERE serial_no = %s AND roll_no = %s", (serial_no, student_details[1]))
            issued_book = cursor.fetchone()

            if not issued_book:
                messagebox.showerror("Error", "Book not issued to this student!")
                return

            # Delete the book from the issued_books table
            cursor.execute("DELETE FROM issued_books WHERE serial_no = %s AND roll_no = %s", (serial_no, student_details[1]))
            conn.commit()

            messagebox.showinfo("Success", "Book deposited successfully!")
            fetch_issued_books()  # Refresh the list of issued books

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

    btn_deposit = tk.Button(deposit_book_page, text="Deposit Book", font=("Arial", 12), bg="green", fg="white", command=deposit_book)
    btn_deposit.pack(pady=10)

    # Back to Home Button
    btn_back = tk.Button(deposit_book_page, text="Back to Home", font=("Arial", 12), bg="blue", fg="white",
                         command=lambda: [deposit_book_page.destroy(), open_student_home_page(student_details)])
    btn_back.pack(pady=10)

    deposit_book_page.mainloop()

def open_lost_book_page(current_window, student_details):
    # Create Lost Book Page
    lost_book_page = tk.Tk()
    lost_book_page.title("Lost Book")
    lost_book_page.geometry("800x500")
    lost_book_page.resizable(False, False)

    label_title = tk.Label(lost_book_page, text="Lost Book", font=("Arial", 18, "bold"))
    label_title.pack(pady=10)

    # Frame for Book Table
    frame_table = tk.Frame(lost_book_page)
    frame_table.pack(pady=10, fill="both", expand=True)

    # Scrollbars
    scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")
    scroll_y = ttk.Scrollbar(frame_table, orient="vertical")

    # Book Table
    book_table = ttk.Treeview(
        frame_table,
        columns=("Serial No", "Title", "Price", "Publisher", "Author", "Type"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set,
        show="headings"
    )
    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")

    scroll_x.config(command=book_table.xview)
    scroll_y.config(command=book_table.yview)

    # Define Table Headings
    book_table.heading("Serial No", text="Serial No")
    book_table.heading("Title", text="Title")
    book_table.heading("Price", text="Price")
    book_table.heading("Publisher", text="Publisher")
    book_table.heading("Author", text="Author")
    book_table.heading("Type", text="Type")

    book_table.column("Serial No", width=100)
    book_table.column("Title", width=200)
    book_table.column("Price", width=80)
    book_table.column("Publisher", width=150)
    book_table.column("Author", width=150)
    book_table.column("Type", width=100)

    book_table.pack(fill="both", expand=True)

    # Fetch and Display Books Issued to Student
    def fetch_issued_books():
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()

            # Fetch books issued to the student based on roll_no
            cursor.execute("SELECT b.serial_no, b.title, b.price, b.publisher, b.author, b.book_type "
                           "FROM books b "
                           "JOIN issued_books ib ON b.serial_no = ib.serial_no "
                           "WHERE ib.roll_no = %s", (student_details[1],))
            rows = cursor.fetchall()

            # Clear any existing rows in the table
            for row in book_table.get_children():
                book_table.delete(row)

            # Insert new rows in the table
            for row in rows:
                book_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching issued books: {e}")
        finally:
            conn.close()

    fetch_issued_books()

    # Serial No Entry (for Book to be Lost)
    label_serial_no = tk.Label(lost_book_page, text="Enter Book Serial No to Mark as Lost:", font=("Arial", 12))
    label_serial_no.pack(pady=10)
    entry_serial_no = tk.Entry(lost_book_page, font=("Arial", 12), width=30)
    entry_serial_no.pack(pady=5)

    # Function to Mark Book as Lost
    def lost_book():
        serial_no = entry_serial_no.get().strip()

        if not serial_no:
            messagebox.showerror("Error", "Serial No is required!")
            return

        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cursor = conn.cursor()

            # Check if the book is issued to the student
            cursor.execute("SELECT b.price FROM books b "
                           "JOIN issued_books ib ON b.serial_no = ib.serial_no "
                           "WHERE ib.serial_no = %s AND ib.roll_no = %s", (serial_no, student_details[1]))
            book_info = cursor.fetchone()

            if not book_info:
                messagebox.showerror("Error", "Book not issued to this student!")
                return

            book_price = book_info[0]

            # Remove the book from the issued_books table
            cursor.execute("DELETE FROM issued_books WHERE serial_no = %s AND roll_no = %s", (serial_no, student_details[1]))
            conn.commit()

            # Calculate the fine (double the price of the book)
            fine = 2 * book_price

            # Update the student's fine in the students table
            cursor.execute("UPDATE students SET fine = fine + %s WHERE roll_no = %s", (fine, student_details[1]))
            conn.commit()

            # Insert data into the lost_books table
            cursor.execute("INSERT INTO lost_books (roll_no, serial_no, fine) VALUES (%s, %s, %s)",
                           (student_details[1], serial_no, fine))
            conn.commit()

            messagebox.showinfo("Success", f"Book marked as lost! Fine of {fine} has been added to your account.")
            fetch_issued_books()  # Refresh the list of issued books

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

    btn_lost = tk.Button(lost_book_page, text="Mark as Lost", font=("Arial", 12), bg="red", fg="white", command=lost_book)
    btn_lost.pack(pady=10)

    # Back to Home Button
    btn_back = tk.Button(lost_book_page, text="Back to Home", font=("Arial", 12), bg="blue", fg="white",
                         command=lambda: [lost_book_page.destroy(), open_student_home_page(student_details)])
    btn_back.pack(pady=10)

    lost_book_page.mainloop()


# Student Login button
def open_student_login():
    student_login_page = tk.Toplevel(root)
    student_login_page.title("Student Login")
    student_login_page.geometry("400x300")
    student_login_page.resizable(False, False)

    # Create labels and entries for student login
    label_title = tk.Label(student_login_page, text="Student Login", font=("Arial", 18, "bold"))
    label_title.pack(pady=20)

    label_student_id = tk.Label(student_login_page, text="Student Name:", font=("Arial", 12))
    label_student_id.pack(pady=5)
    entry_student_id = tk.Entry(student_login_page, font=("Arial", 12), width=30)
    entry_student_id.pack(pady=5)

    label_student_password = tk.Label(student_login_page, text="Password:", font=("Arial", 12))
    label_student_password.pack(pady=5)
    entry_student_password = tk.Entry(student_login_page, font=("Arial", 12), show="*", width=30)
    entry_student_password.pack(pady=5)

    # Button to validate student login
    def validate_student_login():
        student_id = entry_student_id.get().strip()
        student_password = entry_student_password.get().strip()

        if student_id == "" or student_password == "":
            messagebox.showerror("Error", "Both fields are required!")
            return

        try:
            # Database validation for student credentials
            con = pymysql.connect(host="localhost", user="root", password="", database="library_management")
            cur = con.cursor()
            cur.execute("SELECT * FROM students WHERE name = %s AND password = %s", (student_id, student_password))
            result = cur.fetchone()

            if result:
                messagebox.showinfo("Success", "Login successful!")
                # Optionally, open a student-specific home page here
                student_login_page.destroy()
                open_student_home_page(result)
            else:
                messagebox.showerror("Error", "Invalid Student ID or Password.")
        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
        finally:
            if con:
                con.close()

    btn_student_login = tk.Button(student_login_page, text="Login", font=("Arial", 12, "bold"), bg="green", fg="white", command=validate_student_login)
    btn_student_login.pack(pady=20)

# Add "Login as Student" button
btn_student_login = tk.Button(root, text="Login as Student", font=("Arial", 12, "bold"), bg="green", fg="white", command=open_student_login)
btn_student_login.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()


