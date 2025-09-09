import steel

class PNG(steel.Structure):
    signature = steel.FixedBytes(b'\x89PNG\x0d\x0a\x1a\x0a')
    header_size = steel.Integer(size=4)
    header_id = steel.FixedBytes(b'IHDR')
    width = steel.Integer(size=4)
    height = steel.Integer(size=4)
