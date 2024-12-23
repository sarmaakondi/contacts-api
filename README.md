# contacts-api

## Overview

This is a simple contacts API built with Python.

## Requirements

-   Python 3.x
-   Flask

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sarmaakondi/contacts-api.git
    ```
2. Navigate to the project directory:
    ```sh
    cd contacts-api
    ```
3. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```
4. Activate the virtual environment:

    ```sh
    # On Windows
    .venv\Scripts\activate

    # On macOS and Linux
    source .venv/bin/activate
    ```

5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the server:
    ```sh
    python server.py
    ```
2. The API will be available at `http://127.0.0.1:5000/`

## Endpoints

-   `GET /contacts` - Retrieve all contacts
-   `POST /contacts` - Add a new contact
-   `GET /contacts/<id>` - Retrieve a contact by ID
-   `PUT /contacts/<id>` - Update a contact by ID
-   `DELETE /contacts/<id>` - Delete a contact by ID

## Example

To add a new contact:

```sh
curl -X POST http://127.0.0.1:5000/contacts -H "Content-Type: application/json" -d '{"name": "John Doe", "phone": "123-456-7890"}'
```

## License

This project is licensed under the MIT License.
