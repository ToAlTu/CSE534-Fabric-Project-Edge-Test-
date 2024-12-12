import socket
import time
import statistics

#SERVER_IP = "2602:fcfb:d:1::2"  # San Diego
#SERVER_IP = "2602:fcfb:c:1::3"  # Utah
SERVER_IP = "2602:fcfb:11:1::2" # Georgia
#SERVER_IP = "2602:fcfb:e:1::2" # Missouri
#SERVER_IP = "2602:fcfb:17:1::2" # new Jersey
SERVER_PORT = 8080
n = 1000
alatency = 0
latencies = []
try:
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as client:
        client.connect((SERVER_IP, SERVER_PORT))
        for _ in range(n):  # Simulate 100 gaming interactions
            start = time.time()
            client.sendall(b"Simulated player action")
            data = client.recv(1024)
            latency = (time.time() - start) * 1000  # in milliseconds
            latencies.append(latency)
            print(f"{latency:.2f}")
        
        avg_latency = statistics.mean(latencies)
        std_dev_latency = statistics.stdev(latencies)

        print(f"Average Latency: {avg_latency:.2f} ms")
        print(f"Standard Deviation of Latency: {std_dev_latency:.2f} ms")
except KeyboardInterrupt:
    print("Client interrupted. Exiting...")
except Exception as e:
    print(f"Error: {e}")