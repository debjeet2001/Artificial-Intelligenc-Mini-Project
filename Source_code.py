import speech_recognition as sr
import pyodbc
# Function to connect to the ACCDB file and retrieve records
def retrieve_records_from_database(uid):
# Set the path to your ACCDB file
db_path = "database path"
try:
# Connect to the database
conn_str = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=" + db_path
conn = pyodbc.connect(conn_str)
# Execute a SQL query to retrieve the records
cursor = conn.cursor()
cursor.execute("SELECT * FROM a1 WHERE [UID] = ?", uid)
# Fetch the records
records = cursor.fetchall()
if records:
# Print the records
print("Records for UID ", uid + ":")
for record in records:
print(record)
else:
print("No records found for", uid)
# Close the database connection
cursor.close()
conn.close()
except pyodbc.Error as e:
print("Error connecting to the database:", str(e))
# Function to deliver academic records
def deliver_academic_records(r):
# Use the default microphone as the audio source
with sr.Microphone() as source:
print("Please say the UID of the person")
audio = r.listen(source)
try:
# Recognize speech using Google Speech Recognition
uid = r.recognize_google(audio)
print("You said:", uid)
if uid:
# Code to deliver the academic records
print("Delivering academic records for", uid)
# Retrieve the records from the ACCDB file for the specified name
retrieve_records_from_database(uid)
else:
print("Sorry, I couldn't understand the UID.")
except sr.UnknownValueError:
print("Sorry, I couldn't understand the UID.")
except sr.RequestError as e:
print("Could not request results from Google Speech Recognition service:", str(e))
# Create an instance of the Recognizer class
r = sr.Recognizer()
# Call the function to start the voice-based delivery system
deliver_academic_records(r)
