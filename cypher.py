ROWS = [
    ";+ěščřžýáíé=",
    "qwertzuiopú)",
    "asdfghjklů§",
    "yxcvbnm,.-",
    "°1234567890%",
    "QWERTZUIOP/(",
    "ASDFGHJKL\"!'",
    "YXCVBNM?:_"
]

def shift_qwertz(text, shift=1):
    result = []
    for char in text:
        found = False
        for row in ROWS:
            if char in row:
                idx = row.index(char)
                new_idx = (idx + shift) % len(row)
                result.append(row[new_idx])
                found = True
                break
        if not found:
            result.append(char)
    return "".join(result)

plaintext = "Hi, the flag is: haxagon{dmlraW5nYmVycnlqZWxvd2tleW5lamxlcHNpCg==}"
ciphertext = shift_qwertz(plaintext, shift=1)
deciphertext = shift_qwertz(ciphertext, shift=-1)

print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
print("Decipheredtext:", deciphertext)

if plaintext == deciphertext:
    print("success")
else:
    print("failure")
