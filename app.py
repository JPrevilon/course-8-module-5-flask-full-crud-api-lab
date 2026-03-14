from flask import Flask, jsonify, request

app = Flask(__name__)


# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory "database"
events = [Event(1, "Tech Meetup"), Event(2, "Python Workshop")]


# Welcome route (required for rubric)
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Event API"})


# GET all events (required for rubric)
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])


# POST /events - Create a new event
@app.route("/events", methods=["POST"])
def create_event():

    data = request.get_json()

    # Validate input
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Generate new ID
    new_id = max([event.id for event in events], default=0) + 1

    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# PATCH /events/<id> - Update event title
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):

    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    for event in events:
        if event.id == event_id:
            event.title = data["title"]
            return jsonify(event.to_dict()), 200

    return jsonify({"error": "Event not found"}), 404


# DELETE /events/<id>
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):

    for event in events:
        if event.id == event_id:
            events.remove(event)
            return "", 204

    return jsonify({"error": "Event not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
