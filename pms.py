

from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

def add_employee():
    if idEntry.get()==''or mobileEntry.get()==''or nameEntry.get()==''or projectnameEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        database.insert(idEntry.get(),nameEntry.get(),mobileEntry.get(),roleBox.get(),genderBox.get(),projectnameEntry.get())


window=CTk()
window.geometry('930x582+100+100')
window.resizable(False,False)
window.title('Project Management Systems')
window.configure(fg_color='#FFFBD4')
logo=CTkImage(Image.open('Zerone1.jpg'),size=(930,158))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0, columnspan=2)


leftFrame=CTkFrame(window)
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='Id', font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name', font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

mobileLabel=CTkLabel(leftFrame,text='Mobile number', font=('arial',18,'bold'),text_color='white')
mobileLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

mobileEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
mobileEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role', font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')

role_options=['Project Manager','Network Engineer','Project Engineer']
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Gender', font=('arial',18,'bold'),text_color='white')
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_options=['Male','Female']
genderBox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set('Male')

projectnameLabel=CTkLabel(leftFrame,text='Project Name', font=('arial',18,'bold'),text_color='white')
projectnameLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

projectnameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
projectnameEntry.grid(row=5,column=1)



rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options=['Id','Name','Mobile number','Role','Gender','Project name']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='Show All',width=100)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Mobile number','Role','Gender','Project name')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Mobile number',text='Mobile number')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Project name',text='Project name')

tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=120)
tree.column('Mobile number',width=120)
tree.column('Role',width=130)
tree.column('Gender',width=100)
tree.column('Project name',width=100)

style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',10,'bold'))

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,)
scrollbar.grid(row=1,column=4,sticky='ns')

buttonFrame=CTkFrame(window,fg_color='#FFFBD4')
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)


window.mainloop()