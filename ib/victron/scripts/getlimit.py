from serial import Serial
from ib.victron.mk2 import MK2
from ib.victron.scripts.options import options

def main():
    port = Serial(options.port, options.baudrate)
    mk2 = MK2(port)
    print mk2.master_multi_led_info()

    port.close()
