import time
import board
import adafruit_mpu6050
import busio
import usb_hid
from adafruit_hid.mouse import Mouse
from digitalio import DigitalInOut, Direction, Pull
import simpleio


m = Mouse(usb_hid.devices)
i2c = busio.I2C(board.GP1, board.GP0)  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

btn = DigitalInOut(board.GP2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

simpleio.tone(board.GP3, 1000, duration=2.0)
time.sleep(2)

m.move(x=-1920, y=1080)

while True:
    #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
    #print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
    #print("Temperature: %.2f C"%mpu.temperature)
    #print("")
    #print(btn.value)
    y = int((mpu.gyro[2])*45) + 0
    x = int((mpu.gyro[1])*45) + 1
    
    #print("Y: {}".format(y))
    #print("X: {}".format(x))
    if (x >=2 or x <= -2)  and (y >=2 or y <= -2):
        m.move(x=x, y=-y)
        
    if btn.value == False:
        m.click(Mouse.LEFT_BUTTON)
        simpleio.tone(board.GP3, 5000, duration=.25)

