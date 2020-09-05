from tkinter import *
from PIL import ImageTk,Image
import sqlite3


def update ():
    global top
    top = Tk()
    top.title("Update")
    top.iconbitmap('Coffee.ico')
    
    #create a database or connect to one 
    conn = sqlite3.connect("adressbook.db")
    record_id = delete_box.get()
    #create cursor
    c = conn.cursor()   
    #sleect a record
    c.execute( " SELECT * FROM adresses WHERE oid = "+ record_id  )
    records=c.fetchall()
    global  f_name_u,l_name_u, adresse_u,city_u,zipcode_u
    
    f_name_u= Entry(top,width= 30)
    f_name_u.grid(row=0,column =1,padx=20 ,pady = 10)

    l_name_u= Entry(top,width= 30)
    l_name_u.grid(row=1,column =1)

    adresse_u= Entry(top,width= 30)
    adresse_u.grid(row=2,column =1)

    city_u= Entry(top,width= 30)
    city_u.grid(row=3,column =1)

    zipcode_u= Entry(top,width = 30)
    zipcode_u.grid(row=4,column =1)
    #create text boxe labels
    f_name_label= Label(top,text="first name")
    f_name_label.grid(row=0,column =0,padx=20,pady = 3)

    l_name_label= Label(top,text="last name")
    l_name_label.grid(row=1,column =0)

    adresse_label= Label(top,text="adresse")
    adresse_label.grid(row=2,column =0)

    city_label= Label(top,text="city")
    city_label.grid(row=3,column =0)

    zipcode_label= Label(top,text="zipcode")
    zipcode_label.grid(row=4,column =0)
    # loop thru result
    for record in  records:
        f_name_u.insert(0 , record[0])
        l_name_u.insert(0 , record[1])
        adresse_u.insert(0 , record[2])
        city_u.insert(0 , record[3])
        zipcode_u.insert(0 , record[4])
    

    # create a save  button

    submit_btn= Button( top,text="Save record" ,command = edit)
    submit_btn.grid(row=5,column =0, columnspan = 2 , pady= 10 , padx = 10 , ipadx = 100)
    #commit changes
    conn.commit()
    #close  connuction

    conn.close()


def  edit ():
    #create a database or connect to one 
    conn = sqlite3.connect("adressbook.db")

    print (delete_box.get())
   # print (record_id)
    #create cursor
    c = conn.cursor()   
    #sleect a record
    c.execute( """ UPDATE adresses SET
             first_name = :first,
             last_name = :last,
             adresses = :adresse,
             city = :city,
             zipcode = :zipcode
             WHERE oid = 
             """ +delete_box.get() ,
               {"first":f_name_u.get(),
             "last":l_name_u.get(),
             "adresse":adresse_u.get(),
             "city":city_u.get(),
             "zipcode":zipcode_u.get(),
             }
            )

    #commit changes
    conn.commit()
    #close  connuction

    #clear text box
    #f_name_u.delete(0,END)
   # l_name_u.delete(0,END)
   # adresse_u.delete(0,END)
   # city_u.delete(0,END)
  #  zipcode_u.delete(0,END)

    conn.close()
    top.destroy()
    




def delete():
    #create a database or connect to one 
    conn = sqlite3.connect("adressbook.db")

    #create cursor
    c =conn.cursor()   
    #delete a record
    c.execute( " DELETE FROM adresses WHERE oid ="+ delete_box.get() )
    delete_box.delete(0,END)   
    #commit changes
    conn.commit()
    #close  connuction

    conn.close()


def query() :
    
    #create a database or connect to one 
    conn = sqlite3.connect("adressbook.db")

    #create cursor
    c =conn.cursor()   
    #querry the database
    c.execute(" SELECT *, oid FROM adresses ")
    records=c.fetchall()
    #print(records)
    print_records =""
    #for record in records :
    #    for r in record :
    #        print_records += str(r) + "\n"
    
    for record in records:
        print_records += str(record[0]) + "\t" + str(record[5])+"\n"    #show name

    query_label=Label(root,text= print_records )
    query_label.grid(row=12,column =0, columnspan = 2 , pady= 10 , padx = 10 , ipadx = 100)
    
    
    #commit changes
    conn.commit()
    #close  connuction

    conn.close()
def submit():

    #create a database or connect to one 
    conn = sqlite3.connect("adressbook.db")

    #create cursor
    c =conn.cursor()   
    # Insert into table
    c.execute(" INSERT INTO adresses VALUES(:f_name , :l_name , :adresse , :city , :zipcode)",
            {"f_name":f_name.get(),
             "l_name":l_name.get(),
             "adresse":adresse.get(),
             "city":city.get(),
             "zipcode":zipcode.get()
             }
              )

    #commit changes
    conn.commit()
    #close  connuction

    conn.close()

    
    #clear text box
    f_name.delete(0,END)
    l_name.delete(0,END)
    adresse.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    
root = Tk()
root.title("D_B")
root.iconbitmap('Coffee.ico')

#create a database or connect to one 
conn = sqlite3.connect("adressbook.db")


#create cursor
c =conn.cursor()

#create table  use it only one time 

#c.execute(""" CREATE TABLE adresses (
#   first_name text ,
#    last_name text ,
#    adresses text,
#    city text,
#    zipcode integer 
#    )
#    """)


f_name= Entry(root,width= 30)
f_name.grid(row=0,column =1,padx=20 ,pady = 10)

l_name= Entry(root,width= 30)
l_name.grid(row=1,column =1)

adresse= Entry(root,width= 30)
adresse.grid(row=2,column =1)

city= Entry(root,width= 30)
city.grid(row=3,column =1)

zipcode= Entry(root,width= 30)
zipcode.grid(row=4,column =1)

delete_box= Entry(root,width= 30)
delete_box.grid(row=8,column =1)

#create text boxe labels
f_name_label= Label(root,text="first name")
f_name_label.grid(row=0,column =0,padx=20,pady = 3)

l_name_label= Label(root,text="last name")
l_name_label.grid(row=1,column =0)

adresse_label= Label(root,text="adresse")
adresse_label.grid(row=2,column =0)

city_label= Label(root,text="city")
city_label.grid(row=3,column =0)

zipcode_label= Label(root,text="zipcode")
zipcode_label.grid(row=4,column =0)

delete_label= Label(root,text="SELECT ID")
delete_label.grid(row=8,column =0)

# create submut button

submit_btn= Button(root ,text="add to database" ,command = submit)
submit_btn.grid(row=5,column =0, columnspan = 2 , pady= 10 , padx = 10 , ipadx = 100)

#create a query button
query_btn =Button (root, text ="show records", command= query)
query_btn.grid(row=6,column =0, columnspan = 2 , pady= 10 , padx = 10 , ipadx = 100)


#create adelete  button

delete_btn =Button (root, text ="delete records", command= delete)
delete_btn.grid(row=9,column =0, columnspan = 2 , pady= 10 , padx = 10 , ipadx = 100)

#create adelete  button

delete_btn =Button (root, text ="Update  records", command= update)
delete_btn.grid(row=10,column =0, columnspan = 2 , pady= 10 , padx = 10 , ipadx = 100)


#commit changes
conn.commit()

#close  connuction

conn.close()
root.mainloop()
