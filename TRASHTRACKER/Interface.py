from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from wastedisposal import wastedisposalclass
from segregation import segregationclass

class Trashtracker:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("TrashTrack - Waste Management System")
        self.root.config(bg="white")

        # Title
        title = Label(self.root, text="TrashTrack", compound=LEFT, 
                      font=("times new roman", 40, "bold"), bg="green", fg="white")
        title.place(x=0, y=0, relwidth=1, height=70)

        # Footer
        lbl_footer = Label(self.root, text="Waste Inventory Management System", 
                           font=("times new roman", 15, "bold"), bg="grey", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)

        # Left Menu Frame
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=300, height=565)

        # Menu Label
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), 
                         bg="yellow", fg="black")
        lbl_menu.pack(side=TOP, fill=X)

        # Buttons in Menu
        btn_Category = Button(LeftMenu, text="Waste Segregation", command=self.category, 
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_Category.pack(side=TOP, fill=X)

        btn_Supplier = Button(LeftMenu, text="Waste Disposal", command=self.disposal, 
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_Supplier.pack(side=TOP, fill=X)

        btn_Sanitize = Button(LeftMenu, text="Sanitize", command=self.sanitize, 
                              font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_Sanitize.pack(side=TOP, fill=X)

        btn_Exit = Button(LeftMenu, text="Exit", command=self.exit_app, 
                          font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2")
        btn_Exit.pack(side=TOP, fill=X)

        # Dashboard Label
        self.lbl_total_waste = Label(self.root, text="Total Waste Managed\n [0]", bd=5, relief=RIDGE, 
                                     bg="blue", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_total_waste.place(x=600, y=300, height=150, width=300)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = segregationclass(self.new_win)

    def disposal(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = wastedisposalclass(self.new_win)

    def sanitize(self):
        # Sanitization Confirmation Dialog
        sanitize = messagebox.askyesno("Sanitization", "Have you sanitized?", parent=self.root)
        if sanitize:
            messagebox.showinfo("Sanitization", "Thank you for sanitizing!", parent=self.root)
        else:
            messagebox.showwarning("Sanitization", "Please sanitize before proceeding.", parent=self.root)

    def exit_app(self):
        # Confirmation to Exit
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.root)
        if confirm:
            self.sanitize()  # Call the sanitize function before exiting
            self.root.quit()  # Exit the application directly after sanitizing

if __name__ == "__main__":
    root = Tk()
    obj = Trashtracker(root)
    root.mainloop()
