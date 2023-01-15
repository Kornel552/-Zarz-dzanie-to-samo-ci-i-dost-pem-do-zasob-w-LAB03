import base64

# wpisujemy dowolne słowo
slowo = "ekran"
base = slowo.encode('ascii')

binary = base64.b64encode(base)
decode = binary.decode('ascii')

print("Encoded Data: ", decode)