import socket
import json
import time
from EncryptDecrypt import Encryption

key = b'Sixteen byte key'
encryption = Encryption(key)


def load_peers():
    try:
        with open('peers.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def chat_initiator(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, 65001))  # Make sure the port number matches ChatResponder
        print(f"Connected to {ip}. Type 'exit' to close the connection.")

        while True:
            msg = input("Enter your message: ")
            if msg.lower() == "exit":
                s.send(json.dumps({"message": msg}).encode('utf-8'))
                print("Closing connection.")
                break

            secure = input("Should the message be secure? (yes/no): ").strip().lower()
            if secure == "yes":
                encrypted_msg = encryption.encrypt(msg)
                print(f"Encrypted message (hex): {encrypted_msg.hex()}")
                s.send(json.dumps({"encrypted_message": encrypted_msg.hex()}).encode('utf-8'))
            else:
                s.send(json.dumps({"message": msg}).encode('utf-8'))

            with open('chat_history.txt', 'a') as f:
                f.write(f"To {ip}: {msg} (Secure: {secure == 'yes'})\n")


if __name__ == "__main__":
    peers = load_peers()
    print("Available users:")
    for peer, info in peers.items():
        status = "Online" if time.time() - info['last_seen'] < 10 else "Away"
        print(f"{info['username']} ({peer}) ({status})")

    target_user = input("Enter username to chat with: ")
    ip = None
    for peer, info in peers.items():
        if info['username'] == target_user or peer == target_user:
            ip = peer
            break
    if not ip:
        print("User not found.")
    else:
        chat_initiator(ip)
