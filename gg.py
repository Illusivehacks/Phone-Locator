from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

root = Tk()
root.title("Phone Number Tracker")
root.geometry("385x594+300+200")
root.resizable(False, False)
root.configure(bg='#96BFFF')
key = "3958e45e884542e6aced273c2165ca0e"

def track():
    enter_nb = entry.get()
    try:
        number = phonenumbers.parse(enter_nb)

        location = geocoder.description_for_number(number, 'en')

        service = carrier.name_for_number(number, 'en')
        sim.config(text=service)

        query = str(location)
        geocode = OpenCageGeocode(key)
        results = geocode.geocode(query)

        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            longitude.config(text=f"Longitude: {lng}")
            latitude.config(text=f"Latitude: {lat}")

            myMap = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(myMap)
            myMap.save("myLocation.html")
        else:
            longitude.config(text="Longitude: Not found")
            latitude.config(text="Latitude: Not found")
            sim.config(text="")
    except Exception as e:
        longitude.config(text="Invalid Number")
        latitude.config(text="")
        sim.config(text="")
        print(e)

def open_map():
    try:
        webbrowser.open("myLocation.html")
    except Exception as e:
        print(e)

logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#96BFFF").place(x=135, y=40)

search = PhotoImage(file="search.png")
Label(root, image=search, bg="#96BFFF").place(x=14, y=244)

heading = Label(root, text="Track Number", font='arial 20 bold', fg="#39281E", bg="#96BFFF")
heading.place(x=90, y=190)

entry = StringVar()
enter_nb = Entry(root, textvariable=entry, width=17, justify='center', bd=0, font='arial 20', bg="#2C3541", fg="white")
enter_nb.place(x=54, y=258)

search_button = PhotoImage(file='search_icon.png')
btn = Button(root, image=search_button, cursor='hand2', bg="#96BFFF", bd=0, command=track, activebackground='#ED8051')
btn.place(x=155, y=308)

longitude = Label(root, text="Longitude", bg='#96BFFF', fg='black', font='arial 14 bold')
longitude.place(x=55, y=370)

latitude = Label(root, text="Latitude", bg='#96BFFF', fg='black', font='arial 14 bold')
latitude.place(x=255, y=370)

sim = Label(root, text="SIM", bg='#96BFFF', fg='black', font='arial 14 bold')
sim.place(x=55, y=420)

open_map_btn = Button(root, text="Location", width=10, cursor='hand2', bg="#EE8C62", bd=0, command=open_map, activebackground='#ED8051', font='arial 14 bold')
open_map_btn.place(x=125, y=470)

insta_page = Label(root, text="@Illusivehacks and @Harzadeous16", bg='#96BFFF', fg='black', font='arial 10 bold italic')
insta_page.place(x=135, y=550)

root.mainloop()
