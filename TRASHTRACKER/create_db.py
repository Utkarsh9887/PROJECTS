import sqlite3
def create_db():
    con=sqlite3.connect(r"ims.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit() 
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,type text NOT NULL)")
    con.commit()
        
     
create_db()