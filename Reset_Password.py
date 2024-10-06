from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

# Function to connect to the database
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='user_registration'
    )

# Function to reset the password
def reset_password():
    username = UsernameE.get()
    new_password = NewPasswordE.get()
    confirm_password = confirmNewPasswdE.get()

    # Validations
    if username == '' or new_password == '' or confirm_password == '':
        messagebox.showerror("Input Error", "All fields are required.")
        return

    if new_password != confirm_password:
        messagebox.showerror("Input Error", "Passwords do not match.")
        return

    if len(new_password) < 7 or not re.search("[a-zA-Z]", new_password) or not re.search("[@#$%^&+=-_]", new_password):
        messagebox.showerror("Input Error", "Password must be at least 7 characters long, contain at least 1 alphabet, and 1 special character.")
        return

    # Update password in the database
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()

        if result is None:
            messagebox.showerror("Error", "Username not registered.")
        else:
            cursor.execute("UPDATE users SET password=%s WHERE username=%s", (new_password, username))
            connection.commit()
            messagebox.showinfo("Success", "Password updated successfully!")
            reset_window.destroy()
            import LoginPage  # Go back to login page after resetting password

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

# Create the reset password window
reset_window = Tk()
reset_window.title("Reset Password")
reset_window.geometry('1050x550+50+50')  # Set the desired width and height
reset_window.resizable(False, False)  # Disable resizing

# Load the background image
background_image = PhotoImage(file='signUp-Bg.png')

# Create a Label widget to hold the image
background_label = Label(reset_window, image=background_image)
#place method allows you to position widgets at specific x and y coordinates within a parent widget.
background_label.place(x=0,y=0)  # Make the label fill the window


# Create a white box in the center
box_width = 300
box_height = 400
white_box = Frame(reset_window, width=box_width, height=box_height, bg='white')
white_box.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the box

# adding heading to page 
heading=Label(reset_window,text='RESET PASSWORD', font=('Comic Sans MS', 15, 'bold'),bg='white', fg='orchid3')
heading.place(x=430,y=115)

UsernameE=Label(reset_window,text='USERNAME', font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3')
UsernameE.place(x=410,y=165)
UsernameE=Entry(reset_window,font=('Comic Sans MS', 10, 'bold'),bg='orchid3', fg='white',bd=0,width=29)
UsernameE.place(x=410, y=200)

NewPasswordE=Label(reset_window,text='Password', font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3')
NewPasswordE.place(x=410,y=240)
NewPasswordE=Entry(reset_window,font=('Comic Sans MS', 10, 'bold'),bg='orchid3', fg='white',bd=0,width=29)
NewPasswordE.place(x=410, y= 275)

confirmNewPasswdE=Label(reset_window,text='Confirm Password', font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3')
confirmNewPasswdE.place(x=410,y=315)
confirmNewPasswdE=Entry(reset_window,font=('Comic Sans MS', 10, 'bold'),bg='orchid3', fg='white',bd=0,width=29)
confirmNewPasswdE.place(x=410, y=345)



ResetBtn=Button(reset_window,text='SUBMIT',font=('Comic Sans MS', 10, 'bold'),width=29,bd=0,bg='orchid3',cursor='hand2',activebackground='orchid3',fg='white',activeforeground="white",command=reset_password)
ResetBtn.place(x=410,y=400)

# Start the Tkinter main loop
reset_window.mainloop()
