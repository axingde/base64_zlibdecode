# -*- coding: utf-8 -*-
import base64
import zlib

encoded = input("请输入要解码的字符串：")

decoded = base64.b64decode(encoded)
uncompressed = zlib.decompress(decoded,15+32)
result = uncompressed.decode('utf-8')
print(result)

