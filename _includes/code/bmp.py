import steel

class BMP(steel.Structure, endianness='<'):
    signature = steel.FixedBytes(b'BM')
    filesize = steel.Integer(size=4)
    _reserved = steel.Bytes(size=4)
    data_offset = steel.Integer(size=4)
    header_size = steel.Integer(size=4)
    width = steel.Integer(size=4)
    height = steel.Integer(size=4)
