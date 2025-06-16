from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class Organicclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Eco-Friendly Organic Waste Management")
        self.root.geometry("1100x600+0+0")
        self.root.configure(bg="#eaf2f8")  # Light blue background for a fresh, eco-friendly feel

        # Heading
        Label(self.root, text="Manage Your Organic Waste Responsibly", font=("Arial", 16, "bold"), bg="#eaf2f8", fg="#2e8b57").pack(pady=10)

        # Educational Tip
        Label(self.root, text="Tip: Composting organic waste reduces landfill use and benefits the soil!", font=("Arial", 12), bg="#eaf2f8", fg="#2e8b57").pack(pady=5)

        # Frame to display entries
        self.frame = Frame(self.root, bg="#eaf2f8")
        self.frame.pack(pady=10)

        # Treeview to display organic waste entries
        columns = ('ID', 'Name', 'Type')
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings', height=8)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Type', text='Type')
        self.tree.column('ID', width=50, anchor=CENTER)
        self.tree.column('Name', width=150, anchor=CENTER)
        self.tree.column('Type', width=150, anchor=CENTER)
        self.tree.pack(fill=BOTH, expand=True)

        # Scrollbars for the Treeview
        scroll_y = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        scroll_x = ttk.Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=scroll_y.set, xscroll=scroll_x.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)

        # Delete Button
        Button(self.root, text="Delete Selected Waste", command=self.confirm_delete, font=("Arial", 12), bg="#e74c3c", fg="white", cursor="hand2").pack(pady=15)

        # Display existing organic waste entries from the database
        self.display_entries()

    def display_entries(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        
        # Clear the treeview
        self.tree.delete(*self.tree.get_children())

        try:
            # Fetch only entries where type is 'organic'
            cur.execute("SELECT * FROM category WHERE type = 'Organic'")
            rows = cur.fetchall()
            for row in rows:
                self.tree.insert('', 'end', values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def confirm_delete(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to delete", parent=self.root)
            return

        item_values = self.tree.item(selected_item, 'values')
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to dispose:\n\nID: {item_values[0]}\nName: {item_values[1]}?", parent=self.root):
            self.delete_entry(item_values[0])

    def delete_entry(self, entry_id):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM category WHERE cid = ?", (entry_id,))
            con.commit()
            messagebox.showinfo("Success", "Trash disposed successfully", parent=self.root)
            self.display_entries()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

# Create the main application window and run the app
if __name__ == "__main__":
    root = Tk()
    app = Organicclass(root)
    root.mainloop()
