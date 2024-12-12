import socket

#SERVER_IP = "2602:fcfb:d:1::2"  # San Diego
#SERVER_IP = "2602:fcfb:c:1::3"  # Utah
#SERVER_IP = "2602:fcfb:11:1::2" # Georgia
#SERVER_IP = "2602:fcfb:e:1::2" # Missouri
SERVER_IP = "2602:fcfb:17:1::2" # new Jersey
SERVER_PORT = 8080

with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as server:
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen(1)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    conn, addr = server.accept()
    with conn:
        print(f"Connection established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            conn.sendall(b"Game Action Acknowledged")