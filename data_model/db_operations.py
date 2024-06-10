import mysql.connector


db = mysql.connector.connect(
    host="localhost", user="root", password="rootpassword!", database="mengprojectdb"
)
cursor = db.cursor()

# # Check if the table exists
# cursor.execute("SHOW TABLES LIKE 'user'")
# table_exists = cursor.fetchone()

# if not table_exists:
#     # Define the CREATE TABLE statement
#     create_table_query = """
#     CREATE TABLE user (
#       user_ID int PRIMARY KEY,
#       username varchar(255),
#       email varchar(255)
#     )
#     """

#     # Execute the CREATE TABLE statement
#     cursor.execute(create_table_query)

#     # Commit changes
#     db.commit()
#     print("Table 'user' created successfully.")
# else:
#     print("Table 'user' already exists.")

# # Close the cursor and connection
# cursor.close()
# db.close()
