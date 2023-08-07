from tkinter import *
from tkinter import messagebox
import pymysql
f = ('Times', 14)

def conn():
    return pymysql.connect(host='localhost',
                                 user='root',
                                 db='data',
                                 #password="root1234"
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)


ws = Tk()
ws.title('LOG-IN FORM')
ws.geometry('940x600')
ws.config(bg='#0B5A81')

def insert_record():
    check_counter = 0
    warn = ""
    if register_name.get() == "":
        warn = "Name can't be empty"
    else:
        check_counter += 1

    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if register_mobile.get() == "":
        warn = "Contact can't be empty"
    else:
        check_counter += 1

    if var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if variable.get() == "":
        warn = "Select Country"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 8:
        try:
            con = conn()
            cur = con.cursor()
            cur.execute(f'INSERT INTO record VALUES ("{register_name.get()}",'
                        f'"{register_email.get()}",'
                        f'{register_mobile.get()},'
                        f'"{var.get()}", '
                        f'"{str(variable.get())}",'
                        f'"{register_pwd.get()}")'
            )
            con.commit()
            messagebox.showinfo('confirmation', 'Record Submitted')

        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Error', warn)


def login_response():
    uname = email_tf.get()
    upwd = pwd_tf.get()
    try:
        con = conn()
        cur = con.cursor()
        query=f'Select register_name,register_pwd from record where register_email="{uname}" and register_pwd="{upwd}"'
        p=cur.execute(query)
        x=cur.fetchone()
        print("Sucess",x)
        if x!=None:
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
        else:
            messagebox.showerror('Login Status', 'Invalid Username or Password')
    except Exception as ep:
        print(ep,'Error')
        messagebox.showerror('', ep)

var = StringVar()
var.set('Male')

countries = []
variable = StringVar()
world = open('countries.txt', 'r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)
variable.set(countries[37])

# widgets
left_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    left_frame,
    text="Enter Email",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame,
    font=f
)
pwd_tf = Entry(
    left_frame,
    font=f,
    show='*'
)
login_btn = Button(
    left_frame,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=login_response
)

right_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    right_frame,
    text="Enter Name",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Email",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Contact Number",
    bg='#CCCCCC',
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select Gender",
    bg='#CCCCCC',
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select Country",
    bg='#CCCCCC',
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Re-Enter Password",
    bg='#CCCCCC',
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

register_name = Entry(
    right_frame,
    font=f
)

register_email = Entry(
    right_frame,
    font=f
)

register_mobile = Entry(
    right_frame,
    font=f
)

male_rb = Radiobutton(
    gender_frame,
    text='Male',
    bg='#CCCCCC',
    variable=var,
    value='male',
    font=('Times', 10),

)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='#CCCCCC',
    variable=var,
    value='female',
    font=('Times', 10),

)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='#CCCCCC',
    variable=var,
    value='others',
    font=('Times', 10)

)

register_country = OptionMenu(
    right_frame,
    variable,
    *countries)

register_country.config(
    width=15,
    font=('Times', 12)
)
register_pwd = Entry(
    right_frame,
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame,
    font=f,
    show='*'
)

register_btn = Button(
    right_frame,
    width=15,
    text='Register',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)

# widgets placement
email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20)
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)

# infinite loop
ws.mainloop()
