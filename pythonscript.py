import serial
import vgamepad as vg


gamepad= vg.VX360Gamepad()
arduino = serial.Serial('COM4', 9600, timeout=.1)     #serial input from arduino. change COM port to wherever your arduino is connected

while True:
    rawdata = arduino.readline()            #read serial data from arduino one line at a time
    data = str(rawdata.decode('utf-8'))     #decode the raw byte data into UTF-8
    print(data)

    if data.startswith("A"):
        print(data+" : armed")
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.update()

    if data.startswith("B"):
        print(data+": dis-armed")
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()

    if data.startswith("N"):
        print(data)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        gamepad.update()

    if data.startswith("Z"):
        print(data)
        xAxisData=int(data[1:])
        print(xAxisData)
        gamepad.left_joystick(x_value=xAxisData, y_value=0)  # values between -32768 and 32767
        gamepad.update()

    if data.startswith("R"):
        print(data)
        gamepad.left_joystick(x_value=0, y_value=0)  # values between -32768 and 32767
        gamepad.update()


    # gamepad.right_joystick(x_value=-32768, y_value=15000)  # values between -32768 and 32767