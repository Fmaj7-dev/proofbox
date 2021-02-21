import threading

from raspberry import Raspberry
from database import Database
import server

d = Database()
r = Raspberry( d )

def startRaspberry():
    r.loop()

def startServer():
    server.run(r, d)

if __name__ == '__main__':
    #import webbrowser
    
    rasp_thread = threading.Thread(target=startRaspberry)
    rasp_thread.start()

    server_thread = threading.Thread(target=startServer)
    server_thread.start()
  
    #webbrowser.open("http://127.0.0.1:5000/")
