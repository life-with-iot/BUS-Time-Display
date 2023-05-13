# Import Packages
from tkinter import *
import sqlite3

# Home Window
main = Tk()
main.geometry("1920x1080")
main.title("Sathy Bus Stand")

Label(text="").pack()
Label(text="சத்தியமங்கலம் பேருந்துநிலையம் தங்களை அன்புடன் வரவேற்கிறது", bg="blue", fg="white", width="65", height="2", font=("Devanagari, Tamil", 20)).pack()
Label(text="சேரும் இடத்தை தேர்ந்தெடுக்கவும்", width="50", height="3", font=("Devanagari, Tamil", 20)).pack()

# Database Connectivity
db = sqlite3.connect('test.db')
cursor = db.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS bus(busno TEXT, start TEXT, route TEXT, end TEXT, time TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS bus1(busno TEXT, route TEXT, end TEXT, time TEXT)")
db.commit()

menu=Menu(main)
main.config(menu=menu)
menu = Menu(main)
main.config(menu=menu)

# Function Definitions
def fetch_time(desti, tims, tie):
    connt = sqlite3.connect('test.db')
    cursor = connt.cursor()
    cursor.execute("SELECT * FROM bus1 WHERE end = ? and time >= ? and time < ?", (desti, tims, tie))
    bno = []
    #strt = []
    rte = []
    end = []
    tme = []
    for row in cursor:
        bno.append(row[0])
        #strt.append(row[1])
        rte.append(row[1])
        end.append(row[2])
        tme.append(row[3])
    pt = Toplevel()
    pt.geometry("1920x1080")
    j = 0
    Label(pt, text = end[0], height="2", width="15", font=("Devanagari, Tamil", 18)).place(x=100, y=70)
    for i in range(0, len(bno)):
        Label(pt, text = bno[i], bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18)).place(x=100, y=150+j)
        Label(pt, text = rte[i], bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18)).place(x=300, y=150+j)
        Label(pt, text = tme[i], bg="lightblue", fg="red", height="2", width="15", font=("Devanagari, Tamil", 18)).place(x=500, y=150+j)
        j=j+70
    Button(pt, text="வெளியேறு", height="1", width="15", bg="lightblue", fg="red", command = pt.destroy, font=("Consolas", 30)).place(x=1100, y=600)
def fetch_dest(dest):
    # Time Display More
    def _more():
        tdm = Toplevel()
        tdm.geometry("1920x1080")
        # Left Side
        Button(tdm, text="07.00 - 08.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=80, y=100)
        Button(tdm, text="08.00 - 09.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=80, y=200)
        Button(tdm, text="09.00 - 10.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=80, y=300)
        Button(tdm, text="10.00 - 11.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=80, y=400)
        Button(tdm, text="11.00 - 12.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=80, y=500)
        Button(tdm, text="11.00 - 12.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=80, y=600)
        # Right Side
        Button(tdm, text="12.00 - 13.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=1100, y=100)
        Button(tdm, text="13.00 - 14.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=1100, y=200)
        Button(tdm, text="14.00 - 15.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=1100, y=300)
        Button(tdm, text="14.00 - 15.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=1100, y=400)
        Button(tdm, text="15.00 - 16.00", height="1", width="15", bg="lightblue", fg="red", font=("Consolas", 30)).place(x=1100, y=500)
        Button(tdm, text="வெளியேறு", height="1", width="15", bg="lightblue", fg="red", command = tdm.destroy, font=("Consolas", 30)).place(x=1100, y=600)
    # Time Display
    td = Toplevel()
    td.geometry("1920x1080")
    # Left Side
    Button(td, text="06.00 - 07.00", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "06:00", "07:00"), font=("Consolas", 30)).place(x=80, y=100)
    Button(td, text="07.00 - 08.00", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "07:00", "08:00"), font=("Consolas", 30)).place(x=80, y=200)
    Button(td, text="08.00 - 09.00", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "08:00", "09:00"), font=("Consolas", 30)).place(x=80, y=300)
    Button(td, text="09.00 - 10.00", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "09:00", "10:00"), font=("Consolas", 30)).place(x=80, y=400)
    Button(td, text="10.00 - 11.00", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "10:00", "11:00"), font=("Consolas", 30)).place(x=80, y=500)
    Button(td, text="04.00 - 05.00 pm", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "16:00", "17:00"), font=("Consolas", 30)).place(x=80, y=600)

    # Right Side
    Button(td, text="05.00 - 06.00 pm", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "17:00", "18:00"), font=("Consolas", 30)).place(x=1100, y=100)
    Button(td, text="06.00 - 07.00 pm", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "18:00", "19:00"), font=("Consolas", 30)).place(x=1100, y=200)
    Button(td, text="07.00 - 08.00 pm", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "19:00", "20:00"), font=("Consolas", 30)).place(x=1100, y=300)
    Button(td, text="08.00 - 09.00 pm", height="1", width="15", bg="lightblue", fg="red", command=lambda: fetch_time(dest, "20:00", "21:00"), font=("Consolas", 30)).place(x=1100, y=400)
    Button(td, text="மேலும்", height="1", width="15", bg="lightblue", fg="red", command = lambda: _more(), font=("Consolas", 30)).place(x=1100, y=500)
    Button(td, text="வெளியேறு", height="1", width="15", bg="lightblue", fg="red", command = td.destroy, font=("Consolas", 30)).place(x=1100, y=600)
# Home Page
# Left Side
Button(text="மைசூர்", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Mysore"), font=("Devanagari, Tamil", 30)).place(x=80, y=100)
Button(text="ஈரோடு", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Erode"), font=("Devanagari, Tamil", 30)).place(x=80, y=200)
Button(text="கோவை", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Covai"), font=("Devanagari, Tamil", 30)).place(x=80, y=300)
Button(text="திருப்பூர்", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Tiruppur"), font=("Devanagari, Tamil", 30)).place(x=80, y=400)
Button(text="கோபி", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Gobi"), font=("Devanagari, Tamil", 30)).place(x=80, y=500)
Button(text="புளியம்பட்டி", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Puliampatti"), font=("Devanagari, Tamil", 30)).place(x=80, y=600)

# Right Side
Button(text="ஊட்டி", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Ooty"), font=("Devanagari, Tamil", 30)).place(x=1150, y=100)
Button(text="அந்தியூர்", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Anthiyur"), font=("Devanagari, Tamil", 30)).place(x=1150, y=200)
Button(text="பொள்ளாச்சி", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Pollachi"), font=("Devanagari, Tamil", 30)).place(x=1150, y=300)
Button(text="சென்னை", height="1", width="12", bg="lightblue", fg="red", command=lambda: fetch_dest("Chennai"), font=("Devanagari, Tamil", 30)).place(x=1150, y=400)
Button(text="மேலும்", height="1", width="12", bg="lightblue", fg="red", font=("Devanagari, Tamil", 30)).place(x=1150, y=500)
Button(text="வெளியேறு", height="1", width="12", bg="lightblue", fg="red", command = main.destroy, font=("Devanagari, Tamil", 30)).place(x=1150, y=600)

main.mainloop()