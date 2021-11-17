from Sync import receiver
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

r = receiver.Receiver()
r.start(local_ip)


