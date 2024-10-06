from tkinter import messagebox
import mysql.connector


# Validate login credentials
def validate_login():
    username = UsernameE.get()
    password = PasswordE.get()

    if username == 'Username' or password == 'Password' or username == '' or password == '':
        messagebox.showerror("Input Error", "Please enter valid username and password.")
        return

    
    # Database connection
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Your MySQL server host
            user='your_username',  # Your MySQL username
            password='your_password',  # Your MySQL password
            database='user_registration'  # The database to use
        )
        cursor = connection.cursor()
        
        # Query to check if the username exists and fetch the password
        cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()

        if result is None:
            messagebox.showerror("Login Error", "Username not registered.")
        elif result[0] != password:
            messagebox.showerror("Login Error", "Incorrect password.")
        else:
            messagebox.showinfo("Login Success", "Logged in successfully!")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        cursor.close()
        connection.close()






# using tkinter method we can create GUI
# we can access every method and class present in tkinter
from tkinter import *

# Create the main window 
login = Tk()
login.title('Sign In Page')
login.geometry('1050x550+50+50')  # Set the desired width and height
login.resizable(False, False)  # Disable resizing

# Load the background image
background_image = PhotoImage(file='signUp-Bg.png')

# Create a Label widget to hold the image
background_label = Label(login, image=background_image)
#place method allows you to position widgets at specific x and y coordinates within a parent widget.
background_label.place(x=0,y=0)  # Make the label fill the window


# Create a white box in the center
box_width = 300
box_height = 400
white_box = Frame(login, width=box_width, height=box_height, bg='white')
white_box.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the box

# adding heading to page 
heading=Label(login,text='USER LOGIN', font=('Comic Sans MS', 15, 'bold'),bg='white', fg='orchid3')
heading.place(x=450,y=120)


# creating username field
# we created object just because we can use the methods of that particular class using object
UsernameE=Entry(login,font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3',bd=0,width=26)
UsernameE.place(x=400, y=180)
UsernameE.insert(0,'Username')    #inserting the username to label that will be disable while cliking on that feild

#defining function to disable the placeholder of username

def clear_userplaceholder(event):
    if UsernameE.get() == 'Username':       #if inside the place holder username is written
        UsernameE.delete(0, END)            #then delete it from 0 to end


UsernameE.bind('<FocusIn>',clear_userplaceholder)   # we created function in top that we using here to disable the username from field

frame1=Frame(login,height=2,width=240,bg='orchid3')
frame1.place(x=400,y=205)


# creating password field
# we created object just because we can use the methods of that particular class using object

# the way we created username entry in the same way we can create password entry 
PasswordE=Entry(login,font=('Comic Sans MS', 10, 'bold'),bg='white', fg='orchid3',bd=0,width=26)
PasswordE.place(x=400, y= 225)
PasswordE.insert(0,'Password')      #inserting the username to label that will be disable while cliking on that feild


#defining function to disable the placeholder of username

def clear_passplaceholder(event):
    if PasswordE.get() == 'Password':       #if inside the place holder username is written
        PasswordE.delete(0, END)            #then delete it from 0 to end


PasswordE.bind('<FocusIn>',clear_passplaceholder)   # we created function in top that we using here to disable the username from field

frame2=Frame(login,height=2,width=240,bg='orchid3')
frame2.place(x=400,y=250)

openEye=PhotoImage(file="open-eye.png")

#defining function so when we click on open eye it will change into close eye 

def hide():
    openEye.config(file='close-eye.png')    # it will change the icon
    PasswordE.config(show='*')    # it will chnage the character of password into * 
    EyeButton.config(command=show)        # calling show function

def show():
    openEye.config(file='open-eye.png') 
    PasswordE.config(show='')     #shows normal text 
    EyeButton.config(command=hide)       #calling hide function

EyeButton=Button(login,image=openEye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
EyeButton.place(x=620,y=230)

#created forgot button

def import_reset_password():
    login.destroy()  # Destroy the login window
    import Reset_Password

ForgetBtn=Button(login,text='Forgot Password?',font=('Comic Sans MS', 9, 'bold'),bd=0,bg='white',activebackground='white',cursor='hand2',fg='orchid3',activeforeground="orchid3",command=import_reset_password)
ForgetBtn.place(x=555,y=265)


# created login button
Loginbtn=Button(login,text='LOGIN',font=('Comic Sans MS', 10, 'bold'),width=30,bd=0,bg='orchid3',cursor='hand2',activebackground='orchid3',fg='white',activeforeground="white",command=validate_login)
Loginbtn.place(x=400,y=320)


# created don't have an account label
accLabel=Label(login,text="Don't have an account?",font=('Comic Sans MS', 9, 'bold'),bg='white',fg='orchid3')
accLabel.place(x=400,y=370)


def signUp_page():
    login.destroy()
    import RegisterPage
    


# created new account button     also in command giving signup page access by using fucntion that created above
newaccbtn=Button(login,text='creat new account',font=('Comic Sans MS', 9, 'underline'),bd=0,bg='white',cursor='hand2',activebackground='white',fg='blue',activeforeground="blue",command=signUp_page)
newaccbtn.place(x=550,y=369)




# Start the Tkinter main loop
login.mainloop()