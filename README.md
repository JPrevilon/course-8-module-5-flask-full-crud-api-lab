# Flask Full CRUD Event API

This project is a RESTful API built with Flask that allows users to manage events.

The API supports full CRUD functionality using JSON requests and responses.

## Routes

### GET /

Returns a welcome message.

Response Example:

{
"message": "Welcome to the Event API"
}

---

### GET /events

Returns all events.

Example Response:

[
{
"id": 1,
"title": "Tech Meetup"
},
{
"id": 2,
"title": "Python Workshop"
}
]

---

### POST /events

Creates a new event.

Example Request:

{
"title": "Hackathon"
}

Response:

{
"id": 3,
"title": "Hackathon"
}

Status Code: 201 Created

---

### PATCH /events/<id>

Updates an event title.

Example Request:

{
"title": "Hackathon 2025"
}

Example Response:

{
"id": 1,
"title": "Hackathon 2025"
}

Status Code: 200 OK

---

### DELETE /events/<id>

Deletes an event.

Status Code: 204 No Content

---

## Running the Application

Install dependencies:
pip install flask

Run the server:

python app.py

Open browser:

http://127.0.0.1:5000/events

## Screenshots

course-8-module-5-flask-full-crud-api-lab/screenshots/Screenshot1.png

course-8-module-5-flask-full-crud-api-lab/screenshots/Screenshot2.png
