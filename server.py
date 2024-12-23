from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def root():
    return {"message": "Hello from Flask!"}


if __name__ == "__main__":
    app.run(debug=True)
