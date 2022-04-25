from tkinter import *
import sqlite3
import os

root = Tk()
root.title("My Fridge")
root.geometry("500x500")

# connection to database
conn = sqlite3.connect('my_Fridge.db')

# Cursor
f = conn.cursor()

# Create Table
'''
f.execute("CREATE TABLE fridge (food_name text, f_category text, f_expiration int)")
'''
# Food text box
food_name = Entry(root, width=30)
food_name.grid(row = 0, column=1, padx=20)

# Category Text box
f_category = Entry(root, width=30)
f_category.grid(row = 1, column=1, padx=20)

# Expiration text box
f_expiration = Entry(root, width=30)
f_expiration.grid(row = 2, column=1, padx=20)

def delete_items():
    conn = sqlite3.connect('my_Fridge.db')
    f = conn.cursor()

    f.execute("DELETE FROM fridge WHERE oid= " + delete_by_id.get())
    delete_by_id.delete(0,END)
    conn.commit()
    conn.close()
    return

def updater():
    conn = sqlite3.connect('my_Fridge.db')
    f = conn.cursor()
    item_id = delete_by_id.get()
    f.execute("UPDATE fridge SET food_name = :food_name, f_category = :f_category, f_expiration = :f_expiration WHERE oid = :oid",
    {
        'food_name' : food_name_update.get(),
        'f_category' : f_category_update.get(),
        'f_expiration' : f_expiration_update.get(),
        'oid' : item_id
    })
    conn.commit()
    conn.close()

    update.destroy()
    return

def update_items():
    global update
    update = Tk()
    update.title("Update Item")
    update.geometry("400x400")

    conn = sqlite3.connect('my_Fridge.db')
    f = conn.cursor()

    item_ID = delete_by_id.get()
    f. execute('SELECT * FROM fridge WHERE oid =' + item_ID)
    update_items = f.fetchall()

    conn.commit()
    conn.close()
    global food_name_update
    global f_category_update
    global f_expiration_update

    
    food_name_label_update = Label(update, text="Food")
    food_name_label_update.grid(row=0,column=0)

    f_category_label_update = Label(update, text="Category")
    f_category_label_update.grid(row=1,column=0)

    f_expiration_label_update = Label(update, text="Expiration date")
    f_expiration_label_update.grid(row=2,column=0)


    food_name_update = Entry(update, width=30)
    food_name_update.grid(row = 0, column=1, padx=20)

    # Category Text box
    f_category_update = Entry(update, width=30)
    f_category_update.grid(row = 1, column=1, padx=20)

    # Expiration text box
    f_expiration_update = Entry(update, width=30)
    f_expiration_update.grid(row = 2, column=1, padx=20)
    
    for update_item in update_items:
        food_name_update.insert(0,update_item[0])
        f_category_update.insert(0, update_item[1])
        f_expiration_update.insert(0,update_item[2])
    

    save_button_update = Button(update, text="Save food to fridge", command=updater)
    save_button_update.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    return


# Create submit button
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

    # Delete text fields when saved
    food_name.delete(0,END)
    f_category.delete(0,END)
    f_expiration.delete(0,END)
    return

def show_items():
    conn = sqlite3.connect('my_Fridge.db')
    f = conn.cursor()

    f. execute('SELECT *, oid FROM fridge')
    items = f.fetchall()

    list_items = ''
    for item in items:
        list_items += str(item[3]) + " " + "\t" + str(item[0]) + " - Expires on: " + str(item[2]) + "\n"

    show_label = Label(root, text=list_items)
    show_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()
    return

# Create Lables
food_name_label = Label(root, text="Food")
food_name_label.grid(row=0,column=0)

f_category_label = Label(root, text="Category")
f_category_label.grid(row=1,column=0)

f_expiration_label = Label(root, text="Expiration date")
f_expiration_label.grid(row=2,column=0)


delete_by_id = Entry(root, width=30)
delete_by_id.grid(row=9, column=1)

delete_label = Label(root, text="Enter item ID")
delete_label.grid(row=9, column=0)


# Buttons
save_button = Button(root, text="Save food to fridge", command=submit)
save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


show_item = Button(root, text="Show items in my fridge", command=show_items)
show_item.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_item = Button(root, text="delete an item", command=delete_items)
delete_item.grid(row=10, column=0, columnspan=1, pady=10, padx=10, ipadx=70)

update_item = Button(root, text="Edit an item", command=update_items)
update_item.grid(row=10, column=1, columnspan=1, pady=10, padx=10, ipadx=70)

# Commit to db
conn.commit()

# Close Connection
conn.close()


root.mainloop()