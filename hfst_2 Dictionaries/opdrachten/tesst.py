import socket

import pickle

import pyautogui
 
# Create the client socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('172.16.112.44', 5000))  # Connect to the host IP address
 
def recv_data(sock, buffer_size=1024):

    """Helper function to receive the full message"""

    data = b""

    while len(data) < buffer_size:

        packet = sock.recv(buffer_size - len(data))

        if not packet:

            return None

        data += packet

    return data
 
running = True

while running:

    try:

        # First, receive the fixed-length header (10 bytes)

        header = recv_data(client_socket, 10)

        if not header:

            break

        message_length = int(header.decode('utf-8').strip())  # Extract the message length

        # Now receive the actual message based on the length in the header

        data = recv_data(client_socket, message_length)

        if not data:

            break

        event_type, mouse_pos = pickle.loads(data)  # Deserialize the event and position
 
        if event_type == 'move':  # Handle mouse movement

            pyautogui.moveTo(mouse_pos[0], mouse_pos[1])  # Move mouse to the position

        elif event_type == 'click':  # Handle left-click event

            print(f"Received left-click at: {mouse_pos}")

            pyautogui.click(mouse_pos[0], mouse_pos[1])  # Simulate a left-click

    except Exception as e:

        print(f"Error: {e}")

        running = False
 
# Close the connection

client_socket.close()

 