# with open('fixtures/binary', 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))
#     # for i in range(17):
#     #     bin_file.write(bytes([i]))
#
# with open('fixtures/binary', 'br') as binFile:
#     for b in binFile:
#         print(b)

a = 65534
b = 65535
c = 65636
d = 2998302

with open('fixtures/binary2', 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'little'))

with open('fixtures/binary2', 'br') as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    f = int.from_bytes(binFile.read(2), 'big')
    g = int.from_bytes(binFile.read(4), 'big')
    h = int.from_bytes(binFile.read(4), 'big')
    i = int.from_bytes(binFile.read(4), 'big')
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)