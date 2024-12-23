from flask import Flask, request

app = Flask(__name__)

contacts = [
    {"id": "1", "name": "Sarma", "phone": "123-456-7890"},
    {"id": "2", "name": "John", "phone": "234-966-1275"},
    {"id": "3", "name": "Bob", "phone": "456-789-0123"},
    {"id": "4", "name": "Charlie", "phone": "345-678-9012"},
]

next_id = 5


@app.get("/contacts")
def list_contacts():
    return contacts


@app.get("/contacts/<id>")
def read_single_contact(id):
    for contact in contacts:
        if contact["id"] == id:
            return contact

    return {"error": "That contact does not exist!"}


@app.post("/contacts")
def create_contact():
    global next_id
    new_contact = {
        "id": f"{next_id}",
        "name": request.json["name"],
        "phone": request.json["phone"],
    }
    contacts.append(new_contact)
    next_id += 1

    return new_contact


if __name__ == "__main__":
    app.run(debug=True)
