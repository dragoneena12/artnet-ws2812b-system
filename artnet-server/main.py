from SAS import StupidArtnetServer
from PyDMX import PyDMX

dmx = PyDMX()


def dmx_callback(data):
    for i in range(512):
        dmx.set_data(i + 1, data[i])
    dmx.send()


universe = 0
a = StupidArtnetServer()
u1_listener = a.register_listener(
    universe, callback_function=dmx_callback)

print(a)

while True:
    pass
