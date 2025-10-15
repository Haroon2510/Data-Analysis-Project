import pyodbc

conn = pyodbc.connect(
"DRIVER={ODBC Driver 18 for SQL Server};"
"SERVER=Your server Name;"
"DATABASE=Database name;"
"UID=sqladmin;"
"PWD=sqladmin;"
"TrustServerCertificate=yes;"
)
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("SELECT TOP 5 name FROM sys.databases")
rows = cursor.fetchall()
for r in rows:
    print(r)
cursor.close()
conn.close()
print("Done")