import sys

class Coin(object):
    @classmethod
    def static_header_offset(cls, height):
        raise Exception('Not implemented')


class Zcoin(Coin):
    PRE_MTP_BLOCKS = 117564
    PRE_MTP_HEADER_SIZE = 80
    MTP_HEADER_SIZE = 180

    @classmethod
    def static_header_offset(cls, height):
        if height >= cls.PRE_MTP_BLOCKS:
            return cls.PRE_MTP_HEADER_SIZE * cls.PRE_MTP_BLOCKS + cls.MTP_HEADER_SIZE * (height - cls.PRE_MTP_BLOCKS)
        return cls.PRE_MTP_HEADER_SIZE * height

    def get_header_size(self, header: bytes):
        hex_to_int = lambda s: int.from_bytes(s, byteorder='little')
        if hex_to_int(header[0:4]) & 0x1000:
            return self.MTP_HEADER_SIZE
        return self.PRE_MTP_HEADER_SIZE

    @classmethod
    def get_header_size_height(cls, height: int):
        return cls.MTP_HEADER_SIZE if height >= cls.PRE_MTP_BLOCKS else cls.PRE_MTP_HEADER_SIZE

    def check_header_size(self, header: bytes):
        size = self.get_header_size(header)
        if len(header) == self.PRE_MTP_HEADER_SIZE:
            return True
        if len(header) == size:
            return True
        return False


class ZcoinTestnet(Zcoin):
    PRE_MTP_BLOCKS = 1
