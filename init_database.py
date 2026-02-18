import mysql.connector

# Function to initialize and set up the MySQL database

def init_database():
    try:
        # Establish the connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        cursor = connection.cursor()

        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS health_records")

        # Use the created database
        cursor.execute("USE health_records")

        # Create tables
        cursor.execute("CREATE TABLE IF NOT EXISTS patients (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            birth_date DATE,
            gender ENUM('Male', 'Female', 'Other')
        )")

        cursor.execute("CREATE TABLE IF NOT EXISTS appointments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            patient_id INT,
            appointment_date DATETIME,
            status ENUM('Scheduled', 'Completed', 'Cancelled'),
            FOREIGN KEY (patient_id) REFERENCES patients(id)
        )")

        cursor.execute("CREATE TABLE IF NOT EXISTS records (
            id INT AUTO_INCREMENT PRIMARY KEY,
            patient_id INT,
            record_date DATE,
            notes TEXT,
            FOREIGN KEY (patient_id) REFERENCES patients(id)
        )")

        # Create indexes
        cursor.execute("CREATE INDEX idx_patient_name ON patients(name)")
        cursor.execute("CREATE INDEX idx_appointment_date ON appointments(appointment_date)")

        # Commit the changes
        connection.commit()

        print('Database initialized and setup completed!')

    except mysql.connector.Error as err:
        print(f'Error: {err}')

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    init_database()