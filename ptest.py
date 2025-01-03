from pymodbus.client.sync import ModbusTpClient

client10 = ModbusTpClient('192.168.95.10')
client11 = ModbusTpClient('192.168.95.11')
client12 = ModbusTpClient('192.168.95.12')
client13 = ModbusTpClient('192.168.95.13')

try:

    while True:
        res = client10.write_register(1, 65535)
        print("10:", res)
        res = client11.write_register(1, 65535)
        print("11:", res)
        res = client12.write_register(1, 65535)
        print("12:", res)
        res = client13.write_register(1, 65535)
        print("13:", res)

except KeyboardInterrupt:
    client10.close()
    client11.close()
    client12.close()
    client13.close()
