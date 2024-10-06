from tkinter import messagebox  # Import messagebox for displaying alerts
import mysql.connector  # Import MySQL connector for database interaction
import re  # Import regex library for input validation


# Function to handle the sign-up process
def sign_up():
    # Retrieve user input from entry fields
    email = EmailE.get().strip()  # Use strip() to remove leading and trailing spaces
    username = UsernameE.get().strip()
    password = PasswordE.get().strip()
    confirm_password = confirmPasswdE.get().strip()

    if email == '' or username == '' or password == '' or confirm_password == '':
        messagebox.showerror("Input Error", "All fields are required.")  # Show error if fields are empty
        return
    
    # Check for spaces in the input fields
    if ' ' in email or ' ' in username or ' ' in password or ' ' in confirm_password:
        messagebox.showerror("Input Error", "Spaces are not allowed in any field.")  # Show error if spaces are present
        return
    
    # Validate email format
    if not is_valid_email(email):
        messagebox.showerror("Input Error", "Invalid email format.")  # Show error for invalid email
        return
    

    # validate passeord and confirm password
    if password != confirm_password:
        messagebox.showerror("Input Error", "Passwords do not match.")  # Show error if passwords don't match
        return

      # Validate password complexity
    if not iS_valid_password(password):
        messagebox.showerror("Input Error", "Password must be at least 7 characters long and contain 1 alphabet and 1 special character.")  # Error if password is not complex enough
        return

    
    # Check username length
    if len(username) >= 8:
        messagebox.showerror("Input Error", "Username must be less than 10 characters.")  # Error if username is too long
        return
    
    # Check if the terms and conditions checkbox is checked
    if not termandcondition_var.get():
        messagebox.showerror("Input Error", "You must agree to the Terms and Conditions.")  # Error if terms are not agreed to
        return

    # database connection with try except and finally to check valid connection

    try:
        conn=mysql.connector.connect(
            host = 'localhost',              # mysql server host
            username  = 'your_username',              # mysql server user
            password = 'your_password',           # mysql server password
            database = 'user_registration'   # mysql database name
        )

        cursor = conn.cursor()  # Create a cursor object to interact with the database

        # Check for existing email or username
        cursor.execute("SELECT * FROM users WHERE email=%s OR username=%s", (email, username))
        if cursor.fetchone():  # If a user with that email or username exists
            messagebox.showerror("Input Error", "Email or Username already exists.")  # Show error message
            return
        
        # Insert new user into the database
        cursor.execute("INSERT INTO users (email, username, password) VALUES (%s, %s, %s)", (email, username, password))
        conn.commit()  # Commit the transaction to save the data
        messagebox.showinfo("Success", "Account created successfully!")  # Show success message
            

    except mysql.connector.Error as err:       # Catch any MySQL errors
        messagebox.showerror("Database Error", f"Error: {err}")  # Show error message for database issues

    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection



# Function to validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@gmail\.com$", email) is not None       # checks if email follows statandard pattern  


# Function to validate password
def iS_valid_password(password):
    return (len(password) <= 7 and
            re.search("[a-z]", password) and   # At least one lowercase letter
            re.search("[A-Z]", password) and   # At least one uppercase letter
            re.search("[0-9]", password) and   # At least one digit
            re.search("[@#$%^&+=-]", password)) # At least one special character



# using tkinter method we can create GUI
# we can access every method and class present in tkinter
from tkinter import *


# Create the main window 
signup = Tk()
signup.title('Sign Up Page')
signup.geometry('1050x550+50+50')  # Set the desired width and height
signup.resizable(False, False)  # Disable resizing

# Load the background image
background_image = PhotoImage(file='signUp-Bg.png')


# Create a Label widget to hold the image
background_label = Label(signup, image=background_image)
#place method allows you to position widgets at specific x and y coordinates within a parent widget.
background_label.place(x=0,y=0)  # Make the label fill the window, 

# Create a white box in the center
box_width = 300
box_height = 450
white_box = Frame(signup, width=box_width, height=box_height, bg='white')
white_box.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the box

# adding heading to page 
heading=Label(signup,text='CREATE AN ACCOUNT', font=('Comic Sans MS', 15, 'bold'),bg='white', fg='orchid3')
heading.place(x=410,y=100)


EmailE=Label(signup,text='Email', font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3')
EmailE.place(x=410,y=135)
EmailE=Entry(signup,font=('Comic Sans MS', 10, 'bold'),bg='orchid3', fg='white',bd=0,width=29)
EmailE.place(x=410, y= 165)

UsernameE=Label(signup,text='Username', font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3')
UsernameE.place(x=410,y=195)
UsernameE=Entry(signup,font=('Comic Sans MS', 10, 'bold'),bg='orchid3', fg='white',bd=0,width=29)
UsernameE.place(x=410, y= 225)

PasswordE=Label(signup,text='Password', font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3')
PasswordE.place(x=410,y=255)
PasswordE=Entry(signup,font=('Comic Sans MS', 10, 'bold'),bg='orchid3', fg='white',bd=0,width=29)
PasswordE.place(x=410, y= 285)


confirmPasswdE=Label(signup,text='Confirm Password', font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3')
confirmPasswdE.place(x=410,y=315)
confirmPasswdE=Entry(signup,font=('Comic Sans MS', 10, 'bold'),bg='orchid3', fg='white',bd=0,width=29)
confirmPasswdE.place(x=410, y=345)


termandcondition_var = BooleanVar()  # Create a BooleanVar for the checkbox
termandcondition=Checkbutton(signup,text='I agree to the Terms & Conditions', font=('Comic Sans MS', 9, 'bold'),bd=0,bg='white', cursor='hand2',activebackground='white',fg='orchid3',activeforeground="orchid3",variable=termandcondition_var)
termandcondition.place(x=410, y=380)


Signbtn=Button(signup,text='SignUp',font=('Comic Sans MS', 10, 'bold'),width=29,bd=0,bg='orchid3',cursor='hand2',activebackground='orchid3',fg='white',activeforeground="white",command=sign_up)
Signbtn.place(x=410,y=420)



# created don't have an account label
HaveaccLabel=Label(signup,text="Already have account?",font=('Comic Sans MS', 9, 'bold'),bg='white',fg='orchid3')
HaveaccLabel.place(x=410,y=465)

def signIn_page():
    signup.destroy()
    import LoginPage


# created new account button
haveaccbtn=Button(signup,text='Sign In',font=('Comic Sans MS', 9, 'underline'),bd=0,bg='white',cursor='hand2',activebackground='white',fg='blue',activeforeground="blue",command=signIn_page)
haveaccbtn.place(x=580,y=465)


# Start the Tkinter main loop
signup.mainloop()