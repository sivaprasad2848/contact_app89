import psycopg2

# Connect to PostgreSQL
con = psycopg2.connect(
    user="postgres",
    password="123654",
    host="127.0.0.1",
    port="5432",
    database="dbcontacts"
)

cr = con.cursor()

# SQL query to fetch all contacts
sql = "SELECT slno, name, email, mobile FROM contacts"
cr.execute(sql)

# Fetch all rows
rows = cr.fetchall()

# Display results
print("Contacts List:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Mobile: {row[3]}")

# Close connection
cr.close()
con.close()
