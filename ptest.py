from pymodbus.client import ModbusTcpClient
import sys

args = sys.argv
valve1 = ModbusTcpClient('192.168.95.10')
valve2 = ModbusTcpClient('192.168.95.12')

try:
    match args[1]:
        case fullopen:
            while True:
                valve1.write_register(1, 65535)
        case shutoff:
            while True:
                valve2.write_register(1, 0)
except KeyboardInterrupt:
    valve1.close()
    valve2.close()
