//this program tests the creation of the heat map using the Google Maps API from the given pothole coordinates

import serial
import mysql.connector
from gmplot import gmplot

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "locations"
)

mycursor = mydb.cursor()
ser = serial.Serial('COM3', 9600, timeout=1)
i = 1
a = 3
b = 3
val = []

gmap = gmplot.GoogleMapPlotter(43.663040, -79.398010,13)
gmap.apikey = "AIzaSyD2yJNOapILnfGHQrtmUfb_eATRpfHb5PY"

while True:
   line = ser.readline()
   print(line)
   if (line == "43.663040,-79.398010"):
      print("Adding pothole location to database")
      a=line.split(",")[0]
      b=line.split(",")[1]
      sql = """INSERT INTO locations_2 (ID, X, Y) VALUES (%s, %s, %s)"""
      val = val + [str(i)] + [a] + [b]
      mycursor.execute(sql,tuple(val))
      mydb.commit()
      i = i + 1
      val = []
      gmap.heatmap([43.663040],[-79.398010])
      gmap.draw("my_map.html")
