"""Saf Python ile logo.png dosyasından küçük sürümler üretir (PIL gerekmez).
Kullanım: python3 tools/resize_logo.py"""
import struct, zlib, sys, os

def read_png(path):
    d = open(path, "rb").read()
    pos, idat, w = 8, b"", 0
    while pos < len(d):
        n, t = struct.unpack(">I4s", d[pos:pos + 8])
        body = d[pos + 8:pos + 8 + n]
        if t == b"IHDR":
            w, h, bd, ct, _, _, il = struct.unpack(">IIBBBBB", body)
            assert bd == 8 and ct == 6 and il == 0, "RGBA 8-bit, interlace yok olmalı"
        elif t == b"IDAT":
            idat += body
        pos += 12 + n
    raw, bpp, stride = zlib.decompress(idat), 4, w * 4
    rows, prev = [], bytearray(stride)
    for y in range(h):
        f = raw[y * (stride + 1)]
        cur = bytearray(raw[y * (stride + 1) + 1:(y + 1) * (stride + 1)])
        for i in range(stride):
            a = cur[i - bpp] if i >= bpp else 0
            b = prev[i]
            c = prev[i - bpp] if i >= bpp else 0
            if f == 1: cur[i] = (cur[i] + a) & 255
            elif f == 2: cur[i] = (cur[i] + b) & 255
            elif f == 3: cur[i] = (cur[i] + ((a + b) >> 1)) & 255
            elif f == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
                cur[i] = (cur[i] + pr) & 255
        rows.append(cur); prev = cur
    return w, h, rows

def write_png(path, w, h, rows):
    def chunk(t, b):
        c = struct.pack(">I", len(b)) + t + b
        return c + struct.pack(">I", zlib.crc32(t + b) & 0xffffffff)
    raw = b"".join(b"\x00" + bytes(r) for r in rows)
    open(path, "wb").write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
                           + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))

def shrink(w, h, rows, size):
    k = w // size
    out = []
    for y in range(size):
        row = bytearray()
        for x in range(size):
            acc = [0, 0, 0, 0]; aw = 0
            for dy in range(k):
                r = rows[y * k + dy]
                for dx in range(k):
                    i = (x * k + dx) * 4
                    a = r[i + 3]
                    acc[0] += r[i] * a; acc[1] += r[i + 1] * a; acc[2] += r[i + 2] * a; acc[3] += a; aw += 1
            if acc[3]:
                row += bytes([acc[0] // acc[3], acc[1] // acc[3], acc[2] // acc[3], acc[3] // aw])
            else:
                row += b"\0\0\0\0"
        out.append(row)
    return size, size, out

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    w, h, rows = read_png(os.path.join(root, "logo.png"))
    for size in (64, 256):
        write_png(os.path.join(root, "assets", f"logo-{size}.png"), *shrink(w, h, rows, size))
    print("tamam")
