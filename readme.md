# P2P Chat Application

This is a peer-to-peer (P2P) chat application that allows users to discover each other on a local network and communicate securely using encryption.

## Features

- Service Announcement: Broadcasts the user's username to the local network.
- Peer Discovery: Listens for broadcast messages to discover other users on the network.
- Secure Communication: Encrypts and decrypts messages using AES encryption.
- Chat History: Logs chat history to a file.

## Prerequisites

- Python 3.x
- `pycryptodome` library

## Installation

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3. Install the required packages:

    ```bash
    pip install pycryptodome
    ```

## Usage

### Start Service Announcer

1. Open a terminal and run the Service Announcer to broadcast your username:

    ```bash
    python Service_Announcer.py
    ```

2. Enter your username when prompted.

### Start Peer Discovery and Chat Responder

1. Open another terminal and start the Peer Discovery and Chat Responder:

    ```bash
    python UI.py
    ```

### Chat with Users

1. In the UI, choose `1` to list users.
2. Choose `2` to chat with a user.
3. Choose `3` to view chat history.
4. Choose `4` to exit the application.

## File Descriptions

### Service_Announcer.py

Broadcasts the user's username to the local network.

### peer_discovery.py

Listens for broadcast messages and updates the list of peers.

### ChatInitiator.py

Initiates a chat with another user.

### ChatResponder.py

Responds to incoming chat messages.

### UI.py

Main user interface for listing users, initiating chat, and viewing chat history.
