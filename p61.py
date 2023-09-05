import re
s = re.search("xsoft+", "I xx xsoftt1")
print(s)

p = re.compile(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])")
s = p.search("192.168.1.1")
print(s)