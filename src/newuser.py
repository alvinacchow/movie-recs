import mysql.connector
from keys import Key


def insert_user(email: str, first: str, last: str, pw: str):
    conn = mysql.connector.connect(
        host = Key.host,     
        user = Key.user,  
        password = Key.password,
        database = 'movierecs'
    )
    cursor = conn.cursor()

    # SQL query to insert a new user
    insert_user_query = """
    INSERT INTO user (email, firstName, lastName, password)
    VALUES (%s, %s, %s, %s)
    """
    user_data = (email, first, last, pw)

    try:
        # Execute the SQL query
        cursor.execute(insert_user_query, user_data)

        # Commit the transaction
        conn.commit()
        return True  # Return True if insertion is successful
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
        return False  # Return False if there is an error
    
    finally:
        cursor.close()
        conn.close()