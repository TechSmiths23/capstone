import RPi.GPIO as GPIO
import netifaces as ni
import socket


#Need to Figure out what module to import based on motor drivers
#GPIO Pin set up

# Create a TCP/IP server socket
server_ip = '169.254.189.163'  # Listen on all available interfaces
port = 6000  # Match the port number used in MATLAB

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, port))
server_socket.listen(1)

def check_ethernet_status(interface="eth0"):
    try:
        ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
        return True
    except ValueError:
        return False

if check_ethernet_status():
    print("Ethernet cable is connected.")
    print(f"Listening on {server_ip}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
else:
    print("Ethernet cable is not connected.")


