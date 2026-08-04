"""
Exercise: Student Directory

Description:
Demonstrates a simple student directory example using external data.
"""

import json
import requests


class Elever:
    def __init__(self, name, lastname, email, phone):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone

    def prLista():
        for elev in Eleverlista:
            print(f"Elevnamn: {elev.name}")


extern_data = requests.get("https://dummyjson.com/users")
intern_data = extern_data.text
python_data = json.loads(intern_data)

Eleverlista = []
EleverlistaUP = []

for delar in python_data["users"]:
    hitta_elever = Elever(
        name=delar["firstName"],
        lastname=delar["lastName"],
        email=delar["email"],
        phone=delar["phone"],
    )
    Eleverlista.append(hitta_elever)
    EleverlistaUP.append(hitta_elever)


# Inloggning för lärare
while True:
    lognamn = input("Namn: ").lower()
    logkod = input("Lösenord: ")
    if lognamn == "john" and logkod == "Examen2026":
        print("Välkommen lärare John")
        break
    else:
        print("Inloggning misslyckad")

for elev in Eleverlista:
    print(f"elevnamn: {elev.name} {elev.lastname}, Mail: {elev.email}, Telefon: {elev.phone}")

