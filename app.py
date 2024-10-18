from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__,
            template_folder="html",         # Specify custom HTML folder
            static_folder="assets")         # Specify custom static folder

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",               # Replace with your MySQL username
    password="yourpassword",  # Replace with your actual MySQL password
    database="user_db"
)

@app.route('/')
def index():
    return redirect(url_for('register'))  # Redirect to the registration page

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""  # Initialize the message variable
    if request.method == 'POST':
        user_id = request.form['userID']
        mobile_number = request.form['mobileNumber']
        password = request.form['password']

        cursor = db.cursor()

        # Check if the user already exists
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            message = "User already exists! Please try another User ID."  # Set error message
        else:
            # Insert new user into the database
            cursor.execute("INSERT INTO users (user_id, mobile_number, password) VALUES (%s, %s, %s)",
                           (user_id, mobile_number, password))
            db.commit()
            message = "Registration successful!"  # Set success message

    return render_template('register.html', message=message)  # Pass the message to the template

if __name__ == '__main__':
    app.run(debug=True)
