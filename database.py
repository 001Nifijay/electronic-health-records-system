from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'

# Create a new database engine
gine = create_engine(DATABASE_URI)

# Create a configured "Session" class
tsession = sessionmaker(bind=engine)

# Create a Session
session = tsession() 

# Example usage
if __name__ == '__main__':
    try:
        # Example of querying the database
        result = session.execute('SELECT * FROM your_table')
        for row in result:
            print(row)
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        session.close()