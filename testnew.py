
# Import Packages
from tkinter import *
import sqlite3

# Home Window
main = Tk()
main.geometry("1920x1080")
main.title("Sathy Bus Stand")

Label(text="").pack()
Label(text="சத்தியமங்கலம் பேருந்துநிலையம் தங்களை அன்புடன் வரவேற்கிறது", bg="blue", fg="white", width="65", height="2", font=("Devanagari, Tamil", 20)).pack()
Label(text="Select the Place", width="20", height="3", font=("Consolas", 18)).pack()

# Database Connectivity
db = sqlite3.connect('test.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS bus(busno TEXT, dest TEXT, route TEXT, time TEXT)")
db.commit()

menu=Menu(main)
main.config(menu=menu)
menu = Menu(main)
main.config(menu=menu)

# Function Definitions

def show(destination):
    inss = Toplevel()
    inss.geometry("1920x1080")
    connt = sqlite3.connect('test.db')
    cursor = connt.cursor()
    cursor.execute("SELECT * FROM bus WHERE dest = ?", (destination,))
    busno = StringVar()
    d = StringVar()
    r = StringVar()
    t = StringVar()
    
    bno = []
    dst = []
    rte = []
    tme = []
    j=0
    for row in cursor:
        bno.append(row[0])
        dst.append(row[1])
        rte.append(row[2])
        tme.append(row[3])
    #print(bno)
    for i in range(0, len(bno)):
        print(bno[i])
        label = Label( inss, textvariable=busno, bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18)) 
        busno.set(bno[i]) 
        label.pack() 
        label.place(x=100, y=150+j)
        j=j+70
    '''

    for i in range(0, len(bno)):
        print(bno[i])
        label = Label( inss, textvariable=busno, bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18)) 
        busno.set(bno[i]) 
        label.pack() 
        label.place(x=100, y=150+j)
        i=i+1
        j=j+70
    
    
    for i in range(0, len(dst)):
        print(dst[i])
    for i in range(0, len(rte)):
        print(rte[i])
    for i in range(0, len(tme)):
        print(tme[i])
    '''

    '''
    for col in cursor.fetchall():
        ar = [[col[0]],[col[1]],[col[2]],[col[3]]]
        #print(ar[i])
    '''

            
    """     
            label = Label( inss, textvariable=d, bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18))
            d.set(dst)
            label.pack()
            #label.place(x=300, y=150)

            label = Label( inss, textvariable=r, bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18))
            r.set(rte)
            label.pack()
            #label.place(x=500 ,y=150)

            label = Label( inss, textvariable=r, bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18))
            r.set(tme)
            label.pack()
            #label.place(x=700 ,y=150)



        
        for abc in range(0,3):
            for deff in range(0,4):
                #print(row)
                ar[abc][deff]=[col[deff]]
                #ar[i] = [col[0],col[1],col[2],col[3]]
                #arr[1] = [row[0],row[1],row[2],row[3]]
                #arr[2] = [row[0],row[1],row[2],row[3]]
                print(ar[abc][deff])
        """


    j = Button(inss, text="Exit", height="2", width="15", bg="lightblue", fg="red", command = inss.destroy, font=("Devanagari, Tamil", 18))
    j.pack()
    j.place(x=1240, y=600)
    """   
        bno = row[0]
        dst = row[1]
        rte = row[2]
        tme = row[3]
        
        label = Label( inss, textvariable=busno, bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18)) 
        busno.set(row[i]) 
        label.pack() 
        label.place(x=100, y=150)
        
        label = Label( inss, textvariable=d, bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18))
        d.set(row[i+1])
        label.pack()
        label.place(x=300, y=150)

        label = Label( inss, textvariable=r, bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18))
        r.set(row[i+2])
        label.pack()
        label.place(x=500 ,y=150)

    j = Button(inss, text="Back", height="2", width="15", bg="lightblue", fg="red", command = inss.destroy, font=("Devanagari, Tamil", 18))
    j.pack()
    j.place(x=1240, y=600)
    # End show()
    """

# Home Page
# Left Side
a = Button(text="மைசூர்", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Mysore"), font=("Devanagari, Tamil", 18))
a.pack()
a.place(x=80, y=200)

b = Button(text="பண்ணாரி", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Bannari"), font=("Devanagari, Tamil", 18))
b.pack()
b.place(x=80, y=300)
    
c = Button(text="உதகமண்டலம்", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Ooty"), font=("Devanagari, Tamil", 18))
c.pack()
c.place(x=80, y=400)

d = Button(text="அந்தியூர்", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Anthiyur"), font=("Devanagari, Tamil", 18))
d.pack()
d.place(x=80, y=500)

e = Button(text="கோபி", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Gobi"), font=("Devanagari, Tamil", 18))
e.pack()
e.place(x=80, y=600)

# Right Side
f = Button(text="ஈரோடு", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Erode"), font=("Devanagari, Tamil", 18))
f.pack()
f.place(x=1240, y=200)

g = Button(text="கோவை", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Covai"), font=("Devanagari, Tamil", 18))
g.pack()
g.place(x=1240, y=300)
    
h = Button(text="திருப்பூர்", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Tirupur"), font=("Devanagari, Tamil", 18))
h.pack()
h.place(x=1240, y=400)

i = Button(text="புளியம்பட்டி", height="2", width="15", bg="lightblue", fg="red", command=lambda: show("Puliampatti"), font=("Devanagari, Tamil", 18))
i.pack()
i.place(x=1240, y=500)
        
j = Button(text="Exit", height="2", width="15", bg="lightblue", fg="red", command = main.destroy, font=("Devanagari, Tamil", 18))
j.pack()
j.place(x=1240, y=600)

main.mainloop()
