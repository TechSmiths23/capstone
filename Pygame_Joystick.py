import pygame
from time import sleep

pygame.init()

def main():
    # This dict can be left as-is, since pygame will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}

    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # For each joystick:
        for joystick in joysticks.values():

            axis1 = joystick.get_axis(1)
            axis2 = joystick.get_axis(2)
            axis5 = joystick.get_axis(5)
            
            if axis1 <= -0.1:
                print("Forward")

                sleep(0.5)
            
            elif axis1 >= 0.1:
                print("Backward")
                sleep(0.5)
            
            elif axis2 <= -0.1:
                print("Turn Left")
                sleep(0.5)
            
            elif axis2 >= 0.1:
                print("Turn Right")
                sleep(0.5)
                
            elif axis5 >= -0.0:
                print("Downward")
                sleep(0.5)

if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()