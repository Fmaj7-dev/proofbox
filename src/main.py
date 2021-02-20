import threading

from raspberry import Raspberry
import server

r = Raspberry()

def startRaspberry():
    r.loop()

def startServer():
    server.run(r)

if __name__ == '__main__':
  rasp_thread = threading.Thread(target=startRaspberry)
  rasp_thread.start()

  server_thread = threading.Thread(target=startServer)
  server_thread.start()
  
