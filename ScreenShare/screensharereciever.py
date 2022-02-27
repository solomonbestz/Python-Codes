from vidstream import StreamingServer
import threading


receiver = StreamingServer("192.168.159.86", 9999, slots=1)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()