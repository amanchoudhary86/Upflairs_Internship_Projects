import socket as sk

# Create a UDP socket
sender_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# Define target IP address and port number
target_ip = "127.0.0.1"
port_number = 2525
target_address = (target_ip, port_number)

print("Message Sender is ready...")

# Loop to send messages
while True:
    message = input("Enter a message to send: ")
    encoded_message = message.encode('ascii')
    
    # Send the encoded message to the target address
    sender_socket.sendto(encoded_message, target_address)
    print("Message sent successfully!")
    
    # Ask the user if they want to stop sending messages
    user_input = input("Do you want to stop sending messages? (Y/N): ").strip().lower()
    if user_input == 'y':
        print("Exiting the message sender...")
        break