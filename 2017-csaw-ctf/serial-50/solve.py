import socket

HOST = 'misc.chal.csaw.io'
PORT = 4239
data = []


def count_ones(s):
    count = 0
    for letter in s:
        if letter == '1': count += 1

    return count


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    raw_data = s.recv(4096)
    if not raw_data:
        break

    x = raw_data.decode('ascii')\
        .split('\n')[-2]\
        .replace('\n', '')

    if int(x[-2]) == (count_ones(x[1:-2]) % 2):
        print(x, 'has valid parity')
        data.append(x)
        s.send(b'1')
    else:
        print(x, 'doesn\'t have valid parity')
        s.send(b'0')

s.close()
print(data)

res = ''

for e in data:
    e = e[1:-2]
    # print(e)
    print(chr(int(e, 2)), int(e, 2))
    # print(bytes(int(e, 2)).decode('ascii'))

    res += chr(int(e, 2))
print(res)

