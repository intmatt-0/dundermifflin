import struct, base64, time

# Crisp 5x7 pixel font (with descenders for g,j,p,q,y) - each row is 5 bits (MSB left)
# Row 0 is top (y=6), Row 6 is baseline (y=0), Row 7-8 are descenders (y=-1, -2)
GLYPHS = {
    ' ': [0,0,0,0,0,0,0],
    '!': [0b00100,0b00100,0b00100,0b00100,0b00100,0b00000,0b00100],
    '"': [0b01010,0b01010,0b00000,0b00000,0b00000,0b00000,0b00000],
    '#': [0b01010,0b11111,0b01010,0b01010,0b11111,0b01010,0b00000],
    '$': [0b00100,0b01111,0b10100,0b01110,0b00101,0b11110,0b00100],
    '%': [0b11001,0b11010,0b00100,0b01000,0b10110,0b00110,0b00000],
    '&': [0b01100,0b10010,0b10100,0b01000,0b10101,0b10010,0b01101],
    "'": [0b00100,0b00100,0b00000,0b00000,0b00000,0b00000,0b00000],
    '(': [0b00010,0b00100,0b01000,0b01000,0b01000,0b00100,0b00010],
    ')': [0b01000,0b00100,0b00010,0b00010,0b00010,0b00100,0b01000],
    '*': [0b00000,0b00100,0b10101,0b01110,0b10101,0b00100,0b00000],
    '+': [0b00000,0b00100,0b00100,0b11111,0b00100,0b00100,0b00000],
    ',': [0b00000,0b00000,0b00000,0b00000,0b00000,0b00100,0b00100,0b01000],
    '-': [0b00000,0b00000,0b00000,0b11111,0b00000,0b00000,0b00000],
    '.': [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00100],
    '/': [0b00001,0b00010,0b00100,0b00100,0b01000,0b10000,0b00000],
    '0': [0b01110,0b10001,0b10011,0b10101,0b11001,0b10001,0b01110],
    '1': [0b00100,0b01100,0b00100,0b00100,0b00100,0b00100,0b01110],
    '2': [0b01110,0b10001,0b00001,0b00110,0b01000,0b10000,0b11111],
    '3': [0b11110,0b00001,0b00001,0b01110,0b00001,0b00001,0b11110],
    '4': [0b00010,0b00110,0b01010,0b10010,0b11111,0b00010,0b00010],
    '5': [0b11111,0b10000,0b11110,0b00001,0b00001,0b10001,0b01110],
    '6': [0b00110,0b01000,0b10000,0b11110,0b10001,0b10001,0b01110],
    '7': [0b11111,0b00001,0b00010,0b00100,0b01000,0b01000,0b01000],
    '8': [0b01110,0b10001,0b10001,0b01110,0b10001,0b10001,0b01110],
    '9': [0b01110,0b10001,0b10001,0b01111,0b00001,0b00010,0b01100],
    ':': [0b00000,0b00000,0b00100,0b00000,0b00100,0b00000,0b00000],
    ';': [0b00000,0b00000,0b00100,0b00000,0b00100,0b00100,0b01000],
    '<': [0b00010,0b00100,0b01000,0b10000,0b01000,0b00100,0b00010],
    '=': [0b00000,0b00000,0b11111,0b00000,0b11111,0b00000,0b00000],
    '>': [0b01000,0b00100,0b00010,0b00001,0b00010,0b00100,0b01000],
    '?': [0b01110,0b10001,0b00001,0b00110,0b00100,0b00000,0b00100],
    '@': [0b01110,0b10001,0b10111,0b10101,0b10111,0b10000,0b01110],
    'A': [0b01110,0b10001,0b10001,0b11111,0b10001,0b10001,0b10001],
    'B': [0b11110,0b10001,0b10001,0b11110,0b10001,0b10001,0b11110],
    'C': [0b01110,0b10001,0b10000,0b10000,0b10000,0b10001,0b01110],
    'D': [0b11100,0b10010,0b10001,0b10001,0b10001,0b10010,0b11100],
    'E': [0b11111,0b10000,0b10000,0b11110,0b10000,0b10000,0b11111],
    'F': [0b11111,0b10000,0b10000,0b11110,0b10000,0b10000,0b10000],
    'G': [0b01110,0b10001,0b10000,0b10111,0b10001,0b10001,0b01110],
    'H': [0b10001,0b10001,0b10001,0b11111,0b10001,0b10001,0b10001],
    'I': [0b01110,0b00100,0b00100,0b00100,0b00100,0b00100,0b01110],
    'J': [0b00111,0b00010,0b00010,0b00010,0b00010,0b10010,0b01100],
    'K': [0b10001,0b10010,0b10100,0b11000,0b10100,0b10010,0b10001],
    'L': [0b10000,0b10000,0b10000,0b10000,0b10000,0b10000,0b11111],
    'M': [0b10001,0b11011,0b10101,0b10101,0b10001,0b10001,0b10001],
    'N': [0b10001,0b11001,0b10101,0b10011,0b10001,0b10001,0b10001],
    'O': [0b01110,0b10001,0b10001,0b10001,0b10001,0b10001,0b01110],
    'P': [0b11110,0b10001,0b10001,0b11110,0b10000,0b10000,0b10000],
    'Q': [0b01110,0b10001,0b10001,0b10001,0b10101,0b10010,0b01101],
    'R': [0b11110,0b10001,0b10001,0b11110,0b10100,0b10010,0b10001],
    'S': [0b01111,0b10000,0b10000,0b01110,0b00001,0b00001,0b11110],
    'T': [0b11111,0b00100,0b00100,0b00100,0b00100,0b00100,0b00100],
    'U': [0b10001,0b10001,0b10001,0b10001,0b10001,0b10001,0b01110],
    'V': [0b10001,0b10001,0b10001,0b10001,0b10001,0b01010,0b00100],
    'W': [0b10001,0b10001,0b10001,0b10101,0b10101,0b11011,0b10001],
    'X': [0b10001,0b10001,0b01010,0b00100,0b01010,0b10001,0b10001],
    'Y': [0b10001,0b10001,0b01010,0b00100,0b00100,0b00100,0b00100],
    'Z': [0b11111,0b00001,0b00010,0b00100,0b01000,0b10000,0b11111],
    '[': [0b01110,0b01000,0b01000,0b01000,0b01000,0b01000,0b01110],
    '\\': [0b10000,0b01000,0b00100,0b00100,0b00010,0b00001,0b00000],
    ']': [0b01110,0b00010,0b00010,0b00010,0b00010,0b00010,0b01110],
    '^': [0b00100,0b01010,0b10001,0b00000,0b00000,0b00000,0b00000],
    '_': [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b11111],
    '`': [0b01000,0b00100,0b00000,0b00000,0b00000,0b00000,0b00000],
    'a': [0b00000,0b00000,0b01110,0b00001,0b01111,0b10001,0b01111],
    'b': [0b10000,0b10000,0b11110,0b10001,0b10001,0b10001,0b11110],
    'c': [0b00000,0b00000,0b01110,0b10000,0b10000,0b10001,0b01110],
    'd': [0b00001,0b00001,0b01111,0b10001,0b10001,0b10001,0b01111],
    'e': [0b00000,0b00000,0b01110,0b10001,0b11111,0b10000,0b01110],
    'f': [0b00110,0b01001,0b01000,0b11100,0b01000,0b01000,0b01000],
    'g': [0b00000,0b00000,0b01111,0b10001,0b10001,0b01111,0b00001,0b01110],
    'h': [0b10000,0b10000,0b11110,0b10001,0b10001,0b10001,0b10001],
    'i': [0b00100,0b00000,0b01100,0b00100,0b00100,0b00100,0b01110],
    'j': [0b00010,0b00000,0b00110,0b00010,0b00010,0b00010,0b10010,0b01100],
    'k': [0b10000,0b10000,0b10010,0b10100,0b11000,0b10100,0b10010],
    'l': [0b01100,0b00100,0b00100,0b00100,0b00100,0b00100,0b01110],
    'm': [0b00000,0b00000,0b11010,0b10101,0b10101,0b10001,0b10001],
    'n': [0b00000,0b00000,0b11110,0b10001,0b10001,0b10001,0b10001],
    'o': [0b00000,0b00000,0b01110,0b10001,0b10001,0b10001,0b01110],
    'p': [0b00000,0b00000,0b11110,0b10001,0b10001,0b11110,0b10000,0b10000],
    'q': [0b00000,0b00000,0b01111,0b10001,0b10001,0b01111,0b00001,0b00001],
    'r': [0b00000,0b00000,0b10110,0b11001,0b10000,0b10000,0b10000],
    's': [0b00000,0b00000,0b01111,0b10000,0b01110,0b00001,0b11110],
    't': [0b01000,0b01000,0b11100,0b01000,0b01000,0b01001,0b00110],
    'u': [0b00000,0b00000,0b10001,0b10001,0b10001,0b10001,0b01111],
    'v': [0b00000,0b00000,0b10001,0b10001,0b10001,0b01010,0b00100],
    'w': [0b00000,0b00000,0b10001,0b10001,0b10101,0b10101,0b01010],
    'x': [0b00000,0b00000,0b10001,0b01010,0b00100,0b01010,0b10001],
    'y': [0b00000,0b00000,0b10001,0b10001,0b10001,0b01111,0b00001,0b01110],
    'z': [0b00000,0b00000,0b11111,0b00010,0b00100,0b01000,0b11111],
    '{': [0b00010,0b00100,0b00100,0b01000,0b00100,0b00100,0b00010],
    '|': [0b00100,0b00100,0b00100,0b00100,0b00100,0b00100,0b00100],
    '}': [0b01000,0b00100,0b00100,0b00010,0b00100,0b00100,0b01000],
    '~': [0b00000,0b00000,0b01000,0b10101,0b00010,0b00000,0b00000],
    '\u2014': [0b00000,0b00000,0b00000,0b11111,0b00000,0b00000,0b00000], # em-dash
    '\u2013': [0b00000,0b00000,0b00000,0b01110,0b00000,0b00000,0b00000], # en-dash
}

SCALE = 100 # 1 pixel = 100 font units; advance width = 600 units

def build_glyf_entry(rows):
    squares = []
    for r_idx, bits in enumerate(rows):
        y0 = (6 - r_idx) * SCALE + 2
        y1 = y0 + SCALE - 4
        c_idx = 0
        while c_idx < 5:
            if (bits >> (4 - c_idx)) & 1:
                start_c = c_idx
                while c_idx + 1 < 5 and ((bits >> (4 - (c_idx + 1))) & 1):
                    c_idx += 1
                x0 = start_c * SCALE + 2
                x1 = (c_idx + 1) * SCALE - 2
                squares.append((x0, y0, x1, y1))
            c_idx += 1
    if not squares:
        return b'', (0, 0, 0, 0), 0
    num_contours = len(squares)
    end_pts = [4 * i + 3 for i in range(num_contours)]
    xs, ys = [], []
    for (x0, y0, x1, y1) in squares:
        # Clockwise contour in TrueType: (x0,y0) -> (x0,y1) -> (x1,y1) -> (x1,y0)
        xs.extend([x0, x0, x1, x1])
        ys.extend([y0, y1, y1, y0])
    xmin, ymin, xmax, ymax = min(xs), min(ys), max(xs), max(ys)
    header = struct.pack('>hhhhh', num_contours, xmin, ymin, xmax, ymax)
    end_pts_bin = struct.pack('>' + 'H' * num_contours, *end_pts)
    instr_len = struct.pack('>H', 0)
    num_pts = len(xs)
    flags = bytes([0x01] * num_pts) # on-curve, 16-bit signed deltas
    dx = [xs[0]] + [xs[i] - xs[i-1] for i in range(1, num_pts)]
    dy = [ys[0]] + [ys[i] - ys[i-1] for i in range(1, num_pts)]
    x_bin = struct.pack('>' + 'h' * num_pts, *dx)
    y_bin = struct.pack('>' + 'h' * num_pts, *dy)
    raw = header + end_pts_bin + instr_len + flags + x_bin + y_bin
    if len(raw) % 4 != 0:
        raw += b'\x00' * (4 - (len(raw) % 4))
    return raw, (xmin, ymin, xmax, ymax), num_pts

# Order glyphs: .notdef first, then sorted by codepoint
char_list = sorted(GLYPHS.keys(), key=lambda c: ord(c))
all_rows = [[0b11111,0b10001,0b10001,0b10001,0b10001,0b10001,0b11111]] + [GLYPHS[c] for c in char_list]

glyf_chunks = []
loca_offsets = [0]
max_pts = 0
max_contours = 0
hmtx_entries = []

for rows in all_rows:
    chunk, bbox, npts = build_glyf_entry(rows)
    glyf_chunks.append(chunk)
    loca_offsets.append(loca_offsets[-1] + len(chunk))
    if npts > max_pts: max_pts = npts
    if npts // 4 > max_contours: max_contours = npts // 4
    hmtx_entries.append((600, bbox[0]))

glyf_table = b''.join(glyf_chunks)
loca_table = struct.pack('>' + 'I' * len(loca_offsets), *loca_offsets)
hmtx_table = b''.join(struct.pack('>Hh', adv, lsb) for adv, lsb in hmtx_entries)
num_glyphs = len(all_rows)

# cmap format 4
seg_chars = [ord(c) for c in char_list]
start_codes = seg_chars + [0xFFFF]
end_codes = seg_chars + [0xFFFF]
id_deltas = [(idx + 1 - code) & 0xFFFF for idx, code in enumerate(seg_chars)] + [1]
id_range_offsets = [0] * len(start_codes)
seg_count = len(start_codes)
search_range = 2 * (1 << (seg_count.bit_length() - 1))
entry_selector = seg_count.bit_length() - 1
range_shift = 2 * seg_count - search_range

subtable4 = struct.pack('>HHHHHHH', 4, 16 + 8 * seg_count, 0, seg_count * 2, search_range, entry_selector, range_shift)
subtable4 += struct.pack('>' + 'H' * seg_count, *end_codes)
subtable4 += struct.pack('>H', 0)
subtable4 += struct.pack('>' + 'H' * seg_count, *start_codes)
subtable4 += struct.pack('>' + 'H' * seg_count, *id_deltas)
subtable4 += struct.pack('>' + 'H' * seg_count, *id_range_offsets)
cmap_table = struct.pack('>HHHHI', 0, 1, 3, 1, 12) + subtable4

head_table = struct.pack('>IIIIHHqqhhhhHHhhh',
    0x00010000, 0x00010000, 0, 0x5F0F3CF5, 0x000B, 800,
    0, 0, 0, -200, 500, 700, 0, 8, 2, 1, 0)

hhea_table = struct.pack('>IhhhHhhhhhhHHHHH',
    0x00010000, 750, -250, 100, 600, 0, 0, 500, 1, 0, 0, 0, 0, 0, 0, num_glyphs)

maxp_table = struct.pack('>IH' + 'H'*13,
    0x00010000, num_glyphs, max_pts, max_contours, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0)

os2_table = struct.pack('>HhHHHhhhhhhhhhh10sIIII4sHHHhhhHHII',
    1, 600, 400, 5, 0, 400, 400, 0, -100, 400, 400, 0, 300, 50, 0,
    b'\x02\x00\x05\x09\x00\x00\x00\x00\x00\x00', 1, 0, 0, 0, b'DNDM',
    0x0040, 32, 0x2014, 750, -250, 100, 750, 250, 1, 0)

post_table = struct.pack('>IihhIIIII', 0x00030000, 0, -100, 50, 1, 0, 0, 0, 0)

# name table
family = "DunderPixel".encode('utf-16-be')
subfam = "Regular".encode('utf-16-be')
records = []
str_data = b''
for name_id, val in [(1, family), (2, subfam), (4, family), (6, family)]:
    records.append(struct.pack('>HHHHHH', 3, 1, 0x0409, name_id, len(val), len(str_data)))
    str_data += val
name_table = struct.pack('>HHH', 0, len(records), 6 + 12 * len(records)) + b''.join(records) + str_data

tables = {
    b'OS/2': os2_table,
    b'cmap': cmap_table,
    b'glyf': glyf_table,
    b'head': head_table,
    b'hhea': hhea_table,
    b'hmtx': hmtx_table,
    b'loca': loca_table,
    b'maxp': maxp_table,
    b'name': name_table,
    b'post': post_table,
}

def calc_checksum(data):
    padded = data + b'\x00' * ((4 - len(data) % 4) % 4)
    return sum(struct.unpack('>' + 'I' * (len(padded) // 4), padded)) & 0xFFFFFFFF

num_tables = len(tables)
sr = 16 * (1 << (num_tables.bit_length() - 1))
es = num_tables.bit_length() - 1
rs = num_tables * 16 - sr
sfnt = struct.pack('>IHHHH', 0x00010000, num_tables, sr, es, rs)

offset = 12 + 16 * num_tables
dir_entries = b''
body = b''
head_offset = 0
for tag in sorted(tables.keys()):
    raw = tables[tag]
    if tag == b'head':
        head_offset = offset
    csum = calc_checksum(raw)
    dir_entries += struct.pack('>4sIII', tag, csum, offset, len(raw))
    padded = raw + b'\x00' * ((4 - len(raw) % 4) % 4)
    body += padded
    offset += len(padded)

ttf = bytearray(sfnt + dir_entries + body)
adj = (0xB1B0AFBA - calc_checksum(bytes(ttf))) & 0xFFFFFFFF
struct.pack_into('>I', ttf, head_offset + 8, adj)
b64 = base64.b64encode(bytes(ttf)).decode('ascii')

style_block = f"""  <style>
    @font-face {{
      font-family: 'DunderPixel';
      src: url('data:font/ttf;base64,{b64}') format('truetype');
      font-weight: normal;
      font-style: normal;
    }}
    body, button, code, span, p, h2, li, div {{
      font-family: 'DunderPixel', 'Courier New', monospace !important;
      letter-spacing: 0.04em;
      -webkit-font-smoothing: none;
      font-smooth: never;
    }}
    .pixel-box {{
      border-radius: 0px !important;
      box-shadow: 3px 3px 0px 0px var(--border);
    }}
    .pixel-bar {{
      background-image: repeating-linear-gradient(
        90deg,
        transparent,
        transparent 6px,
        rgba(0, 0, 0, 0.28) 6px,
        rgba(0, 0, 0, 0.28) 8px
      );
    }}
  </style>
</head>"""

for path in [
    "C:/Users/Lenovo/.gemini/antigravity/brain/940969f1-7de6-4fc9-83cc-939d9202c499/dundermifflin-board.html"
]:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    if "@font-face" in html:
        import re
        html = re.sub(r"  <style>.*?</style>\s*</head>", style_block, html, flags=re.S)
    else:
        html = html.replace("</head>", style_block)
    html = html.replace("rounded-xl", "pixel-box").replace("rounded-lg", "rounded-none").replace("rounded-full", "rounded-none").replace("rounded-md", "rounded-none")
    html = html.replace("transition-all duration-300", "pixel-bar transition-all duration-300")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print(f"Injected DunderPixel font ({len(ttf)} bytes) into both board files!")
