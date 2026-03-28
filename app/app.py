from flask import Flask, render_template, request, redirect, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


# ===== CREATE DATABASE TABLES (RUN ONCE) =====
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    image_path TEXT,
    prediction TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()


model = load_model("../model/blood_cell_model.h5")

# Load model
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)

    class_names = ['EOSINOPHIL','LYMPHOCYTE','MONOCYTE','NEUTROPHIL']

    return class_names[np.argmax(prediction)]

# ================== DATABASE ==================
def get_db():
    return sqlite3.connect("database.db")







# ================== REGISTER ==================
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)",
                       (username, password))

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

# ================== LOGIN ==================
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                       (username, password))

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

# ================== PREDICTION ==================
@app.route("/predict", methods=["GET","POST"])
def predict():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        file = request.files["file"]
        path = os.path.join("static", file.filename)
        file.save(path)

        result = predict_image(path)

        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO history (username, image_path, prediction, time)
        VALUES (?,?,?,?)
        """, (session["user"], path, result, now))

        conn.commit()
        conn.close()

        return render_template("predict.html", result=result, img_path=path)

    return render_template("predict.html")


# ================== HOME ==================
@app.route("/")
def home():
    return redirect("/register")


# ================== HISTORY ==================
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history")
    data = cursor.fetchall()

    conn.close()

    return render_template("history.html", data=data)

# ================== LOGOUT ==================
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)