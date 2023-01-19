def encode(strs):
    encodedStr = ""
    for str in strs:
        encodedStr += str + ":;"
    return encodedStr

strs = ["lint","code","love","you"]
print("Encoded String: " + encode(strs))

def decode(str):
    return str.split(':;')

print("Decoded String: " + decode(encode(strs)))