import socket

# RPi Server configuration
HOST = '0.0.0.0'  # Symbolic name meaning all available interfaces
PORT = 65432  # Arbitrary non-privileged port

# Simulink command
simulink_command = "open_simulink_file"  # Replace this with your actual command

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        # Sending the command
        conn.sendall(simulink_command.encode())

    print("Command sent successfully.")

#windows client 
#import socket

# Server configuration
#HOST = '192.168.1.100'  # Replace with the Raspberry Pi's IP address
#PORT = 65432  # The same port as used by the server

# Create a socket
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   # s.connect((HOST, PORT))

    # Receive the command
  #  data = s.recv(1024)

  #  print(f"Received: {data.decode()}")

    # Use the received command to open Simulink or perform any other action
    # Example: if data.decode() == "open_simulink_file":
    #            Implement code to open Simulink here

