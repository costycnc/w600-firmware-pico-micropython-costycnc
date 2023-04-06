# setup the webserver
try:
    import usocket as socket
except:
    import socket
    
from machine import Pin
    
led = Pin(Pin.PA_00, Pin.OUT, Pin.PULL_FLOATING)    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket, address family type = AF_INET, socket type = SOCK_STREAM
s.bind(('', 80))
s.listen(5) # accept connections. backlog = 5 = max. number of unaccepted connections before refusing new connections


while True:
    conn, addr = s.accept() 
    request = conn.recv(200)
    print(request)
    if "/ledon" in request:
        led.value(0) 
    if "/ledoff" in request:
        led.value(1) 
    conn.send("HTTP/1.1 200 ok\n")
    conn.send("Content-type: text /html\n")		
    conn.send("Connection: close\n\n")		
    conn.sendall("Hello")	
    conn.close()
