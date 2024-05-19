from flask import Flask, jsonify, request
import mysql.connector
import time 
app = Flask(__name__)

# Database connection parameters
db_config = {
    "host": "mysql.production.svc.cluster.local",
    "user": "academixuser",
    "password": "academixpassword",
    "database": "academixdb"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/data', methods=['POST'])
def insert_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    user = request.json
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user['name'], user['email']))
    conn.commit()
    conn.close()
    return jsonify({"message": "User added successfully!"}), 201

@app.route('/data/<int:user_id>', methods=['PUT'])
def update_data(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    user = request.json
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (user['name'], user['email'], user_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated successfully!"})

@app.route('/data/<int:user_id>', methods=['DELETE'])
def delete_data(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted successfully!"})

def create_table():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """)
        conn.close()
        print("Table created successfully!")
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    time.sleep(20)
    create_table()  # Create table if it does not exist
    app.run(host='0.0.0.0', port=5000)