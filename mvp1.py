from tkinter import *
import sqlite3
import os
from tkinter import font

root = Tk()
root.title("My Fridge")
root.geometry("325x500")

def show_items():
    conn = sqlite3.connect('my_Fridge.db')
    f = conn.cursor()

    f. execute('SELECT *, oid FROM fridge')
    items = f.fetchall()

    list_items = ''
    for item in items:
        list_items += str(item[3]) + " " + "\t" + str(item[0]) + " - Expires on: " + str(item[2]) + "\n"

    show_label = Label(root, text=list_items)
    show_label.grid(row=15, column=0, columnspan=2)

    conn.commit()
    conn.close()
    return

def submit():
    conn = sqlite3.connect('my_Fridge.db')
    f = conn.cursor()
    f.execute("INSERT INTO fridge VALUES (:food_name, :f_category, :f_expiration)",
        {
            'food_name' : food_name.get(),
            'f_category' : f_category.get(),
            'f_expiration' : f_expiration.get()
        } 
    )

    conn.commit()
    conn.close()
    add.destroy()
    return

def add_item():
    global add
    global food_name
    global f_category
    global f_expiration

    add = Tk()
    add.title("Add an item")
    add.geometry("325x500")

    conn = sqlite3.connect('my_Fridge.db')
    f = conn.cursor()

    # Create Lables
    food_name_label = Label(add, text="Food")
    food_name_label.grid(row=0,column=0)

    f_category_label = Label(add, text="Category")
    f_category_label.grid(row=1,column=0)

    f_expiration_label = Label(add, text="Expiration date")
    f_expiration_label.grid(row=2,column=0)

    # Food text box
    food_name = Entry(add, width=30)
    food_name.grid(row = 0, column=1, padx=20)

    # Category Text box
    f_category = Entry(add, width=30)
    f_category.grid(row = 1, column=1, padx=20)

    # Expiration text box
    f_expiration = Entry(add, width=30)
    f_expiration.grid(row = 2, column=1, padx=20)

    save_button = Button(add, text="Save food to fridge", command=submit)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    
    conn.commit()
    conn.close()

    # Delete text fields when saved
    food_name.delete(0,END)
    f_category.delete(0,END)
    f_expiration.delete(0,END)
    return

def delete_items():
    conn = sqlite3.connect('my_Fridge.db')
    f = conn.cursor()

    f.execute("DELETE FROM fridge WHERE oid= " + delete_by_id.get())
    delete_by_id.delete(0,END)
    conn.commit()
    conn.close()
    return

########################  Labels  ###################################
welcome = Label(root, text="Welcome to the Fridge!", font=('times new roman', 20))
welcome.grid(row = 1, column=1, padx=20, pady=15)

ask_user = Label(root, text="Please select an option below: ", font=('times new roman', 15))
ask_user.grid(row=2, column=1)




#########################  BUTTONS  #################################
fridge_inventory = Button(root, text="View your Fridge", command=show_items)
fridge_inventory.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

add_items = Button(root, text="Add an item", command=add_item)
add_items.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=102)



delete_label = Label(root, text="Delete item by ID")
delete_label.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=102)

#########################  Entries  #################################
delete_by_id = Entry(root, width=5)
delete_by_id.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=102)

delete_item = Button(root, text="delete an item", command=delete_items)
delete_item.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=102)


root.mainloop()