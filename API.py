from flask import Flask, jsonify, request

app = Flask(__name__)
users = [
    {"id":1, "name":"amin", "email": "amin@gmail.com"},
    {"id":2, "name":"sara", "email": "sara@gmail.com"}
]
@app.route("/users")
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>")
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "user not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.get_json()
    new_user_id = 0
    for user in users:
        if user["id"] > new_user_id:
            new_user_id = user["id"]
    new_user_id += 1
    new_user["id"] = new_user_id
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)