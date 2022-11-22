#!/usr/bin/env python3

import fcntl
import struct
import os
import time
from scapy.all import *

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000

# Create the tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'white%d', IFF_TUN | IFF_NO_PI)
ifname_bytes  = fcntl.ioctl(tun, TUNSETIFF, ifr)

# Get the interface name
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name: {}".format(ifname))

os.system("ip addr add 10.10.0.1/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))

os.system("ip route add 172.16.50.0/24 dev {}".format(ifname))

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# We assume that sock and tun file descriptors have already been created. 
while True:
  # this will block until at least one interface is ready
  ready, _, _ = select.select([sock, tun], [], [])

  for fd in ready:
    if fd is sock:
       # Read the data from the port and correctly set the 
       # ip and port variables based on the incoming values
       data, (ip, port) = sock.recvfrom(2048)
       pkt = IP(data)
       print("From socket <==: {} --> {}".format(pkt.src, pkt.dst))
       # Write the data to the tun device
       os.write(tun, data)

    if fd is tun:
       data = os.read(tun, 2048)
       pkt = IP(data)
       print("From tun    ==>: {} --> {}".format(pkt.src, pkt.dst))
       # Send the data to the server ip and port
       sock.sendto(data, ("192.168.40.20", 9090))


