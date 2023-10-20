import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pins for the H-bridges (current GPIO pins are from LED test)
down_pins = [23,24]  # Example GPIO pins for the down H-bridges
forward_pins = [27,25]  # Example GPIO pins for the forward H-bridges
backward_pins = [17,22]  # Example GPIO pins for the backward H-bridges
turn_left_pins = [27,22]  # Example GPIO pins for the turn left H-bridges
turn_right_pins = [17,25]  # Example GPIO pins for the turn right H-bridges

# Initialize all the H-bridge pins
all_pins = down_pins + forward_pins + backward_pins + turn_left_pins + turn_right_pins
for pin in all_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to send short PWM signal to H-bridge pins
def send_short_pwm(pins):
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(0.5)  # Adjust the sleep time according to your requirement
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)

def motor_status():
    print("Testing down H-bridges...")
    send_short_pwm(down_pins)
    print("Testing forward H-bridges...")
    send_short_pwm(forward_pins)
    print("Testing backward H-bridges...")
    send_short_pwm(backward_pins)
    print("Testing turn left H-bridges...")
    send_short_pwm(turn_left_pins)
    print("Testing turn right H-bridges...")
    send_short_pwm(turn_right_pins)

    # Clean up the GPIO
    GPIO.cleanup()

