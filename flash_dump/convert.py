import re

p = re.compile(r"(\S*): (\S*) (\S*) (\S*) (\S*)")


class rlist(list):
    def __init__(self, default):
        self._default = default

    def __setitem__(self, key, value):
        if key >= len(self):
            self += [self._default] * (key - len(self) + 1)
        super(rlist, self).__setitem__(key, value)


reconstructed_data = rlist(0xFF)

base_data_addr = 0x40000000


def set_word(address: int, data: int):
    reconstructed_data[address] = data & 0xFF
    reconstructed_data[address + 1] = (data >> 8) & 0xFF
    reconstructed_data[address + 2] = (data >> 16) & 0xFF
    reconstructed_data[address + 3] = (data >> 24) & 0xFF


with open("serial.log") as file:
    for line in file:
        res = p.match(line)
        if res != None:
            address = int(res.group(1), 16)
            address -= base_data_addr
            w1 = int(res.group(2), 16)
            w2 = int(res.group(3), 16)
            w3 = int(res.group(4), 16)
            w4 = int(res.group(5), 16)

            set_word(address, w1)
            set_word(address + 4, w2)
            set_word(address + 8, w3)
            set_word(address + 12, w4)

with open("output.bin", "wb") as file:
    file.write(bytearray(reconstructed_data))
