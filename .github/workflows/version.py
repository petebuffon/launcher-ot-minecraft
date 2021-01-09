from sys import argv, exit
import yaml

with open(argv[1], "rb") as f:
    byte_string = f.read()
text = ""
for byte in byte_string:
    text += chr(byte)
key_string = "https://api-staging.mojang.com\x00\x00"
version_position = text.find(key_string) + len(key_string)
if not version_position:
    exit("Version number not found.")
version = ""
for char in text[version_position:]:
    if char == "\x00":
        break
    version += char
    
with open("snapcraft.yaml") as f:
    snapcraft = yaml.safe_load(f.read())

if snapcraft["version"] == version:
    print("no commit needed")
else:
    snapcraft["version"] = version
    with open("snapcraft.yaml", "w") as f:
        f.write(yaml.dump(snapcraft))
    print(version)
