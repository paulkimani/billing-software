from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
window = Tk()
window.geometry("900x600")
window.title("Billing")
#       field listener
def quantityFieldListener(a,b,c):
    global quantityVar
    global costVar
    quantity= quantityVar.get()
    global  itemRate
    if quantity !="":
        try:
            quantity=float(quantity)
            cost = quantity*itemRate
            quantityVar.set(quantity)
            costVar.set("%.2f" %cost)
        except ValueError:
            quantity=0
            quantityVar.set("%.2f"%quantity)

def costFieldListener():
    global quantityVar
    global costVar
    global itemRate
    cost=costVar.get()
    if cost !="":
        try:
            cost = float(cost)
            quantity = cost/itemRate
            quantityVar.set("%.2f"%quantity)
            costVar.set("%.2f" % cost)
        except ValueError:
            cost= cost[:-1]
            costVar.set(cost)







#     Global variables for entreis
#       for login
usernameVar= StringVar()
passwordVar = StringVar()
#     main window variable
options= ["Shake", "Noodles", "Burger"]
itemVariable= StringVar()
quantityVar= StringVar()
quantityVar.trace('w',quantityFieldListener)
itemVariable.set(options[0])
itemRate=2
rateVar= StringVar()
rateVar.set("%.2f"%itemRate)
costVar= StringVar()
costVar.trace('w', costFieldListener)
#       mainTreeView
billsTV= ttk.Treeview(height=15, columns=('Item Name', 'Quantity', 'cost'))
#    add item variable
storedOptions= ['Freeze','Fresh']
addItemNameVar= StringVar()
addItemRateVar = StringVar()
addItemTypeVar = StringVar()
addstoredVar = StringVar()
addstoredVar.set(storedOptions[0])


#---------------admin login function
def adminLogin():
    global  usernameVar
    global  passwordVar

    username= usernameVar.get()
    password = passwordVar.get()

    conn =pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor()

    query = "select * from users where username='{}' and password='{}'".format(username, password)
    cursor.execute(query)
    data = cursor.fetchall()
    admin =False
    for row in data:
        admin = True
    conn.close()
    if admin:
        mainWindow()
    else:
        messagebox.showerror("Invalid user", "Credentials entered are invalid")
def loginWindow():
    titleLabel = Label(window, text="P&E Billing System",font="Arial 40", fg="green")
    titleLabel.grid(row=0,column=1,columnspan=4,padx=(10,0), pady=(10,0))

    loginLabel = Label(window,text="Admin Login" ,font="Arial 20")
    loginLabel.grid(row=1, column=2,padx=(50,0), pady=10)

    usernameLabel= Label(window, text="Username")
    usernameLabel.grid(row=2, column=2,padx=20, pady=5)

    passwordLabel= Label(window, text="Password")
    passwordLabel.grid(row=3, column=2,padx=20, pady=5)

    usernameEntry = Entry(window, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3,padx=20, pady=5)

    passwordEntry = Entry(window,textvariable=passwordVar,show="*")
    passwordEntry.grid(row=3, column= 3, padx=20, pady=5)

    loginButton = Button(window, text="Login", width=20, height=2, command=lambda:adminLogin() )
    loginButton.grid(row=4,column=2,columnspan=2)




def mainWindow():
    titleLabel = Label(window, text="P&E Billing System", font="Arial 40", fg="green")
    titleLabel.grid(row=0, column=1, columnspan=4, padx=(10, 0), pady=(10, 0))

    addNewItem = Button(window, text="Add Item", width=20, height=2 )
    addNewItem.grid(row=1, column=0, padx=(10,0), pady=(10,0))

    logoutBtn = Button(window, text="Logout",width=20, height=2)
    logoutBtn.grid(row=1, column=4, pady=(10,0))

    itemLabel  = Label(window, text="Select Item")
    itemLabel.grid(row=2, column=0,padx=(5,0), pady=(10,0) )

    itemDropDown = OptionMenu(window,itemVariable,*options)
    itemDropDown.grid(row=2,column=1,padx=(10,0), pady=(10,0))

    rateLabel= Label(window,text="Rate")
    rateLabel.grid(row=2, column=2, padx=(10,0), pady=(10,0))
    rateValue = Label(window,textvariable=rateVar)
    rateValue.grid(row=2, column=3,padx=(10,0), pady=(10,0))

    quantityLabel = Label(window, text="Quantity")
    quantityLabel.grid(row=3, column=0, padx=(5, 0))
    quantityEntry= Entry(window,textvariable=quantityVar)
    quantityEntry.grid(row=3,column=1,padx=(5,0), pady=(10,0))

    costLabel= Label(window,text="Cost")
    costLabel.grid(row=3, column=2, padx=(10,0), pady=(10,0))
    costEntry= Entry(window,textvariable=costVar)
    costEntry.grid(row=3,column=3,padx=(10,0), pady=(10,0))

    buttonBill = Button(window, text="Generate Bill", width=15)
    buttonBill.grid(row=3, column=4, padx=(10,0), pady=(10,0))

    billLabel= Label(window,text="Bills", font="Arial 25")
    billLabel.grid(row=4, column=2)

    billsTV.grid(row=5, column=0, columnspan=5)

    scrollBar= Scrollbar(window, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=5, column=4, sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading('#0', text = "Item Name")
    billsTV.heading('#1', text = "Rate")
    billsTV.heading('#2', text="Quantity")
    billsTV.heading('#3',text="cost")


def itemAddWindow():
    backButton = Button(window,text="Back", command=lambda:goBack())
    backButton.grid(row=0, column=0)

    titleLabel = Label(window, text="P&E Billing System",font="Arial 40", fg="green")
    titleLabel.grid(row=0, column=1, columnspan=3, pady=(10, 0))

    itemNameLabel = Label(window, text="Name")
    itemNameLabel.grid(row=1, column=1, pady=(10,0))

    itemNameEntry =Entry(window, textvariable=addItemNameVar)
    itemNameEntry.grid(row=1, column=2,pady=(10,0))

    itemRateLabel = Label(window, text="Rate")
    itemRateLabel.grid(row=1, column=3, pady=(10, 0))

    itemRateEntry = Entry(window, textvariable=addItemRateVar)
    itemRateEntry.grid(row=1, column=4, pady=(10, 0))

    itemTypeLabel = Label(window, text="Type")
    itemTypeLabel.grid(row=2, column=1, pady=(10, 0))
    #itemTypeEntry =Entry(window, textvariable=addItemRateVar)
    itemTypeEntry = Entry(window, textvariable=addItemTypeVar)
    itemTypeEntry.grid(row=2, column=2, pady=(10, 0))

    storeLabel = Label(window, text="Stored type")
    storeLabel.grid(row=2, column=3, pady=(10, 0))
    storeEntry = OptionMenu(window, addstoredVar,*storedOptions)
    storeEntry.grid(row=2, column=4, pady=(10, 0))

    AddItemButton = Button(window, text="Add Item", width=20, height=2)
    AddItemButton.grid(row=3, column=3, padx=(5, 0),pady=(10,0))


#itemAddWindow()
#mainWindow()
loginWindow()

window.mainloop()