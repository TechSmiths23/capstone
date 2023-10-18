#packages for power_status
import psutil
#packages for motor_status
import RPi.GPIO as GPIO
import time
import motor_functions  # Import the file containing the motor_status function
#functions for comm_status
import EthernetTest



def power_status():
    # Check voltage and current input for Raspberry Pi 3
    battery = psutil.sensors_battery()
    if battery:
        power_info = {
            "percent": battery.percent,
            "power_plugged": battery.power_plugged
        }
        print(f"Battery percentage: {power_info['percent']}%")
        print(f"Power plugged in: {power_info['power_plugged']}")
        return True  # Assuming power status is good
    else:
        print("Unable to retrieve battery information.")
        return False  # Assuming power status is not good


def comm_status():
  #checks ethernet communication using netifaces library
  #make sure to bash pip install netifaces
    interfaces = netifaces.interfaces()
    if 'eth0' in interfaces:
        addrs = netifaces.ifaddresses('eth0')
        if netifaces.AF_LINK in addrs:
            print("Ethernet cable is connected.")
            return True
        else:
            print("Ethernet cable is not connected.")
            return False
    else:
        print("Ethernet interface not found.")
        return False


def motor_status():
    motor_functions.motor_status()
    return True  # Placeholder, replace with actual logic


def sensor_status():
    return berry_Imu.DetectIMU()  # Placeholder, replace with actual logic


def calibration():
    return power_status() and comm_status() and motor_status() and sensor_status()


def ROV_mode():
    # Implement the functionality for ROV mode here
    print("System is in ROV mode")


def AOV_mode():
    # Implement the functionality for AOV mode here
    print("System is in AOV mode")


def joystick_input(signal):
    # Implement joystick input processing here
    pass


def check_mode():
    if calibration():
        if ROV_mode():
            joystick_input([0, 0, 0, 0])  # Sample 4DOF signal
        else:
            if is_gcode_present():
                AOV_mode()
            else:
                print("AOV mode is selected, but gcode.txt is not present.")


def is_gcode_present():
    try:
        with open('gcode.txt', 'r') as file:
            return True
    except FileNotFoundError:
        return False


if __name__ == '__main__':
    check_mode()
