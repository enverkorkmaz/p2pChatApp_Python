import socket
import json
import time

def service_announcer(username):
    broadcaster = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcaster.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    while True:
        message = json.dumps({"username": username})
        broadcaster.sendto(message.encode('utf-8'), ('<broadcast>', 6000))
        time.sleep(5)

if __name__ == "__main__":
    username = input("Enter your username: ")
    service_announcer(username)
