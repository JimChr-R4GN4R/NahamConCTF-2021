from Crypto.Util.number import bytes_to_long, long_to_bytes


def extended_string (word, length) :

    extra_long_word = word * (length//len(word) + 1)
    required_string = extra_long_word[:length]
    return required_string


file = open('eaxy','rb').read()

for i in range(256):
	key = bytes([i])
	key = extended_string(key, len(file))


	xored_file = long_to_bytes( bytes_to_long(key) ^ bytes_to_long(file) )

	if b'XOR' in xored_file:
		print(b'key:', bytes([i]))
		print(xored_file)
