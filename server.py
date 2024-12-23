from flask import Flask

app = Flask(__name__)

contacts = [
    {"name": "Sarma", "phone": "123-456-7890"},
    {"name": "John", "phone": "234-966-1275"},
    {"name": "Bob", "phone": "456-789-0123"},
    {"name": "Charlie", "phone": "345-678-9012"},
]


@app.get("/hello")
def root():
    return {"message": "Hello from Flask!"}


@app.get("/contacts")
def list_contacts():
    return contacts


if __name__ == "__main__":
    app.run(debug=True)
