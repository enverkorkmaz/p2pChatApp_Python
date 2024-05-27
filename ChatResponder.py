import socket
import json
from EncryptDecrypt import Encryption

key = b'Sixteen byte key'
encryption = Encryption(key)

def chat_responder():
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("", 65001))
    listener.listen(5)

    while True:
        conn, addr = listener.accept()
        print(f"Connected to {addr}")
        while True:
            data = conn.recv(1024)

            if not data:
                print("Received empty data")
                break

            try:
                message = json.loads(data.decode('utf-8'))
            except json.JSONDecodeError:
                print("Received invalid JSON data")
                break

            if "message" in message:
                print(f"Received message from {addr}: {message['message']}")
                with open('chat_history.txt', 'a') as f:
                    f.write(f"From {addr}: {message['message']}\n")
                if message["message"].lower() == "exit":
                    print("Connection closed by client.")
                    break
            elif "encrypted_message" in message:
                try:
                    encrypted_message = bytes.fromhex(message['encrypted_message'])
                    print(f"Received encrypted message (hex): {encrypted_message.hex()}")
                    decrypted_message = encryption.decrypt(encrypted_message)
                    print(f"Received encrypted message from {addr}: {decrypted_message}")
                    with open('chat_history.txt', 'a') as f:
                        f.write(f"From {addr}: {decrypted_message}\n")
                    if decrypted_message.lower() == "exit":
                        print("Connection closed by client.")
                        break
                except ValueError as e:
                    print(f"Error decrypting message: {e}")

        conn.close()
        print(f"Connection to {addr} closed")

if __name__ == "__main__":
    chat_responder()
