_foundby_ = "zabilsabri"

n = [6, 6, 12, 18, 30]
x = n[0]
y = n[1]

p = len(n)

m = [x, y]
for i in range(1, p - 1):
    hasil = x + y
    x = y
    y = hasil
    m.append(hasil)

check = list(set(n) - set(m))
if len(check) == 0:
    print("IT CONTAINES ADDITIVE SEQUENCE!")
else:
    print("IT DID NOT CONTAINES ADDITIVE SEQUENCE!")