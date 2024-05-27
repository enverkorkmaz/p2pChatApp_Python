import socket
import json
import time

peers = {}


def peer_discovery():
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver.bind(("", 6000))
    while True:
        data, addr = receiver.recvfrom(1024)
        message = json.loads(data.decode('utf-8'))
        current_time = time.time()

        # Her yeni gelen yayını al ve peers.json dosyasını güncelle
        peers[addr[0]] = {"username": message["username"], "last_seen": current_time}

        # Eski girişleri temizle
        for peer in list(peers.keys()):
            if current_time - peers[peer]["last_seen"] > 20:  # 20 saniyeden uzun süre önce görülmeyenleri temizle
                del peers[peer]

        with open('peers.json', 'w', encoding='utf-8') as f:
            json.dump(peers, f, indent=4)




if __name__ == "__main__":
    peer_discovery()
