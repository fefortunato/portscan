#!/usr/bin/env python

import socket
import sys

if len(sys.argv) <= 1:
    print('USE: {} 10.0.0.1'.format(sys.argv[0]))
else:
    ip = sys.argv[1]

    for port in range(1, 65536):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response = my_socket.connect_ex((ip, port))

        if response == 0:
            print('PORT [{}] [OPEN]'.format(port))
