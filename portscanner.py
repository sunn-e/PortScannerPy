# -*- coding: utf-8 -*-
"""portscanner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CpnjNsDHFp8RosZazRrP5181rgG0auam
"""

#!/usr/bin/python3
import socket
import sys


def scanHost(ip, startPort, endPort):
    """ Starts a TCP scan on a given IP address """

    print('[*] Starting TCP port scan on host %s' % ip)

    # Begin TCP scan on host
    tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on host %s complete' % ip)


def scanRange(network, startPort, endPort):
    """ Starts a TCP scan on a given IP address range """

    print('[*] Starting TCP port scan on network %s.0' % network)

    # Iterate over a range of host IP addresses and scan each target
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on network %s.0 complete' % network)


def tcp_scan(ip, startPort, endPort):
    """ Creates a TCP socket and attempts to connect via supplied ports """

    for port in range(startPort, endPort + 1):
        try:
            # Create a new socket
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Print if the port is open
            if not tcp.connect_ex((ip, port)):
                print('[+] %s:%d/TCP Open' % (ip, port))
                tcp.close()
                
        except Exception:
            pass


if __name__ == '__main__':
    # Timeout in seconds
    socket.setdefaulttimeout(0.01)
    
    network   = str(input()) 
    startPort = 1
    endPort   = 65535

    scanHost(network, startPort, endPort)
    scanRange(network, startPort, endPort)