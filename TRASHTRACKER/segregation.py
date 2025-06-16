from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class segregationclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+0+0")
        self.root.title("WASTE SEGREGATION")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
        self.var_type = StringVar()

        # Title
        lbl_title = Label(self.root, text="Waste Category", font=("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10, pady=20)

        # Labels and Entry Widgets
        lbl_name = Label(self.root, text="Product Name", font=("goudy old style", 30), bg="white", fg="black")
        lbl_name.place(x=50, y=100)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18), bg="lightyellow")
        txt_name.place(x=50, y=170, width=200)

        lbl_type = Label(self.root, text="Product Type", font=("goudy old style", 30), bg="white", fg="black")
        lbl_type.place(x=50, y=230)

        # ComboBox for Category Type
        self.cmb_type = ttk.Combobox(self.root, textvariable=self.var_type, font=("goudy old style", 18), state='readonly', justify=CENTER)
        self.cmb_type['values'] = ("Organic", "Recyclable", "Non-Recyclable", "Hazardous Waste", "E-Waste", "Industrial Waste")
        self.cmb_type.place(x=50, y=300, width=200)
        self.cmb_type.current(0)  # Set default value

        # Buttons
        btn_add = Button(self.root, text="ADD", command=self.add, font=("goudy old style", 15), bg="green", fg="white", cursor="hand2")
        btn_add.place(x=360, y=170, width=150, height=30)

        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="red", fg="white", cursor="hand2")
        btn_delete.place(x=520, y=170, width=150, height=30)

        btn_close = Button(self.root, text="Close", command=self.close_window, font=("goudy old style", 15), bg="grey", fg="white", cursor="hand2")
        btn_close.place(x=360, y=220, width=150, height=30)

        # Category Details Frame
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=700, y=120, width=380, height=100)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(cat_frame, columns=('cid', 'name', 'type'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.config(command=self.categoryTable.yview)
        scrollx.config(command=self.categoryTable.xview)

        self.categoryTable.heading('cid', text="C ID")
        self.categoryTable.heading('name', text="Name")
        self.categoryTable.heading('type', text="Type")

        self.categoryTable["show"] = "headings"

        self.categoryTable.column('cid', width=100)
        self.categoryTable.column('name', width=100)
        self.categoryTable.column('type', width=100)

        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>", self.get_data)

        # Image
        try:
            self.im1 = Image.open("download.png")
            self.im1 = self.im1.resize((300, 200), Image.Resampling.LANCZOS)  # Use LANCZOS for better quality
            self.im1 = ImageTk.PhotoImage(self.im1)

            self.lbl_im1 = Label(self.root, image=self.im1)
            self.lbl_im1.place(x=700, y=250)  # Adjust the y-coordinate to avoid overlap with Entry widgets
        except Exception as e:
            messagebox.showerror("Error", f"Image could not be loaded: {str(e)}", parent=self.root)

        # Show the categories in the table
        self.show()

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        # Reset category ID when closing
        self.var_cat_id.set("")
        self.root.destroy()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "" or self.var_type.get() == "":
                messagebox.showerror("Error", "Category name and type must be required", parent=self.root)
            else:
                cur.execute("SELECT * from category where name=? AND type=?", (self.var_name.get(), self.var_type.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Category is already present", parent=self.root)
                else:
                    cur.execute("INSERT into category(name,type) values(?, ?)", (
                        self.var_name.get(), self.var_type.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * from category")
            rows = cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        try:
            f = self.categoryTable.focus()
            content = self.categoryTable.item(f)
            row = content.get('values', [])

            if row:
                self.var_cat_id.set(row[0])
                self.var_name.set(row[1])
                self.var_type.set(row[2])
                self.cmb_type.set(row[2])  # Set the ComboBox to the selected type
            else:
                self.var_cat_id.set("")
                self.var_name.set("")
                self.var_type.set("")
                self.cmb_type.set("")  # Clear the ComboBox
        except IndexError as e:
            messagebox.showerror("Error", f"Data could not be retrieved: {str(e)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Category ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * from category where cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Category ID", parent=self.root)
                else:
                    op = messagebox.askyesno("CONFIRM", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE from category where cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE", "Trash Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
                        self.var_type.set("")
                        self.cmb_type.set("")  # Clear the ComboBox

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = segregationclass(root)
    root.mainloop()
