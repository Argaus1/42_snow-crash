def decode_ascii(ascii) :
    return ''.join(chr(code) for code in ascii if 32 <= code <= 126)


def reverse(list) : 
    newList = []
    for index, e in enumerate(list) :
        newList.append(e - index)
    return (newList)

def parse_meta_string(s):
    result = []
    i = 0
    while i < len(s):
        if s[i:i+3] == "M-^":  # Handle M-^X notation
            ctrl_char = s[i+3]
            ascii_val = ord(ctrl_char.upper()) - 64 + 128
            result.append(ascii_val)
            i += 4
        elif s[i:i+2] == "^?":  # ^? is DEL (127)
            result.append(127)
            i += 2
        elif s[i] == "^":  # Handle ^X notation
            ctrl_char = s[i+1]
            ascii_val = ord(ctrl_char.upper()) - 64
            result.append(ascii_val)
            i += 2
        elif s[i:i+2] == "M-":  # Handle M-x notation
            next_char = s[i+2]
            ascii_val = ord(next_char) + 128
            result.append(ascii_val)
            i += 3
        else:
            result.append(ord(s[i]))
            i += 1
    return result

if __name__ == '__main__' :
    token = open('token')
    s = token.read()
    ascii = parse_meta_string(s)
    decoded_ascii = reverse(ascii)
    flag = decode_ascii(decoded_ascii)
    print(flag)
