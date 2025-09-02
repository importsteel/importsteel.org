```python
import steel

class PNG(steel.Structure):
    signature = steel.FixedString(b'\x89PNG\x0d\x0a\x1a\x0a')
    header_size = steel.Integer(size=4)
    header_id = steel.FixedString(b'IHDR')
    width = steel.Integer(size=4, endianness='<')
    height = steel.Integer(size=4, endianness='<')
```
