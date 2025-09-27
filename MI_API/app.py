from flask import Flask, jsonify, request
from pyngrok import ngrok, conf

# Configura tu authtoken de Ngrok aquí
conf.get_default().auth_token = "32yJuo37SJskir1yH7w9Sit2q1x_5LTKAFY6VnXjYnYu17Rc8"
app = Flask(__name__)

# Base de datos en memoria
users = [
    {"id": 1, "nombre": "Juan", "email": "juan@gmail.com"},
    {"id": 2, "nombre": "Ana", "email": "ana@gmail.com"}
]

# Ruta de prueba
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Bienvenido a mi API mejorada 🚀"})

# Obtener todos los usuarios
@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# Obtener usuario por ID
@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

# Crear usuario
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "nombre": data.get("nombre"),
        "email": data.get("email")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Actualizar usuario
@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    user["nombre"] = data.get("nombre", user["nombre"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200

# Eliminar usuario
@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "Usuario eliminado"}), 200

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print(f" * NGROK URL: {public_url}")
    app.run(port=5000)
