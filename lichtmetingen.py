import serial
import time
import mysql.connector

#connectie maken met de database
connection = mysql.connector.connect(host='localhost',
                                 database='testen',
                                 user='marc',
                                 password='root') or die ("could not connect to database")
#cursor voor de database aanmaken
cursor = connection.cursor(buffered = True)

#aangeven welke seriële poort je gebruikt (wisselt tussen ACM0 en ACM1)
device = '/dev/ttyACM0' 

if __name__ == '__main__':
    #maakt een connectie met de serïele monitor van de arduino
    ser = serial.Serial(device, 9600, timeout=1)
    ser.flush()
    #time.sleep(2)
    while True:
        try:
            #query om de grenswaarde uit de database te halen
            sql = """SELECT temperature FROM domotica.users LIMIT 1"""[0][0]
            
            # uitvoeren query
            cursor.execute(sql)
            connection.commit() #commit the insert
            
            #de waarde wordt opgehaald
            data = cursor.fetchone()
            #data wordt omgezet naar bytes
            a_data = ",".join(map(str, data))
            x = int(a_data)
            y = chr(x)

            #verstuur de waarde naar de seriële monitor
            ser.write(y.encode())
        except mysql.connector.Error as error:
            print ("failed to retrieve data {}".format(error))
        try:
            #leeg de seriële monitor zodat de juiste waarde wordt gelezen
            ser.flushInput()
            time.sleep(6)
            #lees de seriële monitor en 
            line = ser.readline().rstrip()#.decode('utf-8').rstrip() #read the data from the arduino
            b_data = line#.replace(" ", "")
            print(line)
            ins = int(line)
            ins2 = str(ins)
            sql2 = """INSERT INTO domotica.light (light) VALUE ("""+ ins2 +""")"""
            val2 = (ins)
            cursor.execute(sql2, val2)
            connection.commit() #commit the insert
            print("inserted")
            time.sleep(2)
        except mysql.connector.Error as error:
            print ("failed to insert data {}".format(error))
            

