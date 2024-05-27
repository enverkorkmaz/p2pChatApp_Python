import threading
import time
import json
from PeerDiscovery import peer_discovery
from ChatInitiator import chat_initiator
from ChatResponder import chat_responder

peers = {}


def load_peers():
    try:
        with open('peers.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def display_menu():
    print("\n1. List users")
    print("2. Chat with user")
    print("3. View chat history")
    print("4. Exit")


def list_users():
    global peers
    peers = load_peers()

    if not peers:
        print("No users found.")
        return

    online_users = []
    away_users = []

    for peer, info in peers.items():
        if time.time() - info['last_seen'] < 10:  # 10 saniyeden kısa süre önce görüldüyse "Online" olarak göster
            online_users.append(f"{info['username']} ({peer})")
        else:
            away_users.append(f"{info['username']} ({peer})")

    print("Online users:")
    for user in online_users:
        print(user)

    print("\nAway users:")
    for user in away_users:
        print(user)


def chat_with_user():
    global peers
    if not peers:
        print("No users available. Please list users first.")
        return

    target_user = input("Enter username to chat with: ")
    ip = None
    for peer, info in peers.items():
        if info['username'] == target_user or peer == target_user:
            ip = peer
            break

    if not ip:
        print("User not found.")
        return

    chat_initiator(ip)


def view_chat_history():
    try:
        with open('chat_history.txt', 'r', encoding='utf-8') as f:
            history = f.read()
            print("Chat History:")
            print(history)
    except FileNotFoundError:
        print("No chat history found.")


def main():
    responder_thread = threading.Thread(target=chat_responder)
    responder_thread.daemon = True
    responder_thread.start()

    discovery_thread = threading.Thread(target=peer_discovery)
    discovery_thread.daemon = True
    discovery_thread.start()

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            list_users()
        elif choice == "2":
            chat_with_user()
        elif choice == "3":
            view_chat_history()
        elif choice == "4":
            print("Exiting...")

            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
