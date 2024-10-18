
# Question_3

Creating a user registration website that requests for
UserID, Mobile Number, and Password for registration. It stores UserID, Mobile
Number, and Password in MySQL database.




## Installation

1.Clone the repository 

```bash
git clone https://github.com/VIKAS-047/a7_question_3.git
```

```bash
cd a7_question_3
```
2.Install Required Python Libraries

```bash
pip install Flask
```

```bash
pip install mysql-connector-python
```

3.Setting Up MySQL Database

```bask
CREATE DATABASE user_db;
USE user_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid VARCHAR(50) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    password VARCHAR(100) NOT NULL
);
```

4.Update Database Credentials

```bash
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="user_registration"
)
```


## Running Tests

To run tests, run the following command

```bash
  python app.py
```


## Screenshots
![Screenshot (119)](https://github.com/user-attachments/assets/877829f2-4b2f-49f1-b6ef-2b893dceedd1)



