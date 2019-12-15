import socket
import serial
import time

ser = serial.Serial('/dev/cu.usbmodem141301', baudrate=9600, timeout=1)
# time.sleep(3)

# while True:
#     ser.write(b'0')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET represents IPV4, SOCK_STREAM represents TCP
# s.bind(("127.0.0.1", 1995))  # ip address, port
s.bind(("10.0.0.218", 1995))  # ip address, port

s.listen(5)

serverSocket, address = s.accept()
print(f"Connection from {address} has been established")

while True:
    commandCoded = serverSocket.recv(1024)
    command = commandCoded.decode("utf-8")
    print(command)
    ser.write(bytes(command, encoding='ascii'))


