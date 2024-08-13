import socket as sk

# Create a UDP socket
receiver_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
ip_address = "127.0.0.1"
port_number = 2525
address = (ip_address, port_number)

# Bind the socket to the address
receiver_socket.bind(address)

print("Receiver is ready to accept messages...")

# Continuously listen for incoming messages
while True:
    data = receiver_socket.recvfrom(1024)  # Receive up to 1024 bytes
    message = data[0].decode('ascii')
    sender_ip = data[1][0]
    print(f"Message from {sender_ip}: {message}")