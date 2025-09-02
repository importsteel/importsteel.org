```python
import steel
from enum import StrEnum

class GifVersion(StrEnum):
    GIF_87a = '87a',
    GIF_89a = '89a',

class GifVersion(steel.StringEnum):
    inner_field = steel.FixedLengthString(size=3, encoding='ascii')
    enum_class = GifVersion

class GIF(steel.Structure):
    tag = steel.FixedBytes(b'GIF')
    version = GifVersion()
    width = steel.Integer(size=2, endianness='<')
    height = steel.Integer(size=2, endianness='<')
```
