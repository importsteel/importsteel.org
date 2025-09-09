import steel

class GIF(steel.Structure):
    tag = steel.FixedBytes(b'GIF')
    version = steel.Bytes(size=3)
    width = steel.Integer(size=2)
    height = steel.Integer(size=2)

class PNG(steel.Structure):
    signature = steel.FixedBytes(b'\x89PNG\x0d\x0a\x1a\x0a')
    header_size = steel.Integer(size=4)
    header_id = steel.FixedBytes(b'IHDR')
    width = steel.Integer(size=4)
    height = steel.Integer(size=4)

class BMP(steel.Structure, endianness='<'):
    signature = steel.FixedBytes(b'BM')
    filesize = steel.Integer(size=4)
    _reserved = steel.Bytes(size=4)
    data_offset = steel.Integer(size=4)
    header_size = steel.Integer(size=4)
    width = steel.Integer(size=4)
    height = steel.Integer(size=4)

class TGA(steel.Structure):
    id_size = steel.Integer(size=1)
    color_map_type = steel.Integer(size=1)
    image_type = steel.Integer(size=1)
    color_map_info = steel.Bytes(size=7)
    x_origin = steel.Integer(size=2)
    y_origin = steel.Integer(size=2)
    width = steel.Integer(size=2)
    height = steel.Integer(size=2)
