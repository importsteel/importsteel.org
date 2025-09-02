```python
import steel

class BMP(steel.Structure, endianness=steel.ByteOrder.LITTLE_ENDIAN):
    signature = steel.FixedBytes(b'BM')
    filesize = steel.Integer(size=4, endianness='<')
    _ = steel.Bytes(size=4) # Reserved
    data_offset = steel.Integer(size=4, endianness='<')
    header_size = steel.Integer(size=4, endianness='<')
    width = steel.Integer(size=4, endianness='<')
    height = steel.Integer(size=4, endianness='<')
```
