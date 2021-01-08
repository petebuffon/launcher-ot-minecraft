from sys import argv

with open(argv[1], "rb") as f:
    byte_string = f.read()
text = ""
for byte in byte_string:
    text += chr(byte)
key_string = "https://api-staging.mojang.com\x00\x00"
version_position = text.find(key_string) + len(key_string)
version = ""
for char in text[version_position:]:
    if char == "\x00":
        break
    version += char
print(version)
