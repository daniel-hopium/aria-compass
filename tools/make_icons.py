"""Erzeugt favicon.svg, favicon.ico und apple-touch-icon.png aus EINER Geometrie.

Aufruf aus dem Repo: python tools/make_icons.py (braucht Pillow).

Farben und Linienstil wie bei der Schwester-App Daumenregel: dunkler Grund, blasses Blau,
ein goldener Akzent. Jede Form steht einmal in SHAPES und wird daraus für SVG (Pfad) wie
für PNG (Pillow kann kein SVG lesen) gezeichnet.
"""
from pathlib import Path

from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent.parent  # Repo-Wurzel
BG, LINE, GOLD = "#0F1418", "#C2D6EA", "#E0C48A"
W = 2.2
NAME = "Kompass"
# ("line", Punkte, Farbe, Deckkraft, geschlossen) · ("fill", Punkte, Farbe) · ("dot", cx, cy, r, Farbe)
SHAPES = [
    ('line', [(27.0, 16.0), (26.94, 17.15), (26.76, 18.29), (26.46, 19.4), (26.05, 20.47), (25.53, 21.5), (24.9, 22.47), (24.17, 23.36), (23.36, 24.17), (22.47, 24.9), (21.5, 25.53), (20.47, 26.05), (19.4, 26.46), (18.29, 26.76), (17.15, 26.94), (16.0, 27.0), (14.85, 26.94), (13.71, 26.76), (12.6, 26.46), (11.53, 26.05), (10.5, 25.53), (9.53, 24.9), (8.64, 24.17), (7.83, 23.36), (7.1, 22.47), (6.47, 21.5), (5.95, 20.47), (5.54, 19.4), (5.24, 18.29), (5.06, 17.15), (5.0, 16.0), (5.06, 14.85), (5.24, 13.71), (5.54, 12.6), (5.95, 11.53), (6.47, 10.5), (7.1, 9.53), (7.83, 8.64), (8.64, 7.83), (9.53, 7.1), (10.5, 6.47), (11.53, 5.95), (12.6, 5.54), (13.71, 5.24), (14.85, 5.06), (16.0, 5.0), (17.15, 5.06), (18.29, 5.24), (19.4, 5.54), (20.47, 5.95), (21.5, 6.47), (22.47, 7.1), (23.36, 7.83), (24.17, 8.64), (24.9, 9.53), (25.53, 10.5), (26.05, 11.53), (26.46, 12.6), (26.76, 13.71), (26.94, 14.85)], LINE, 0.45, True),
    ('fill', [(16, 6.5), (19.2, 16), (12.8, 16)], GOLD),
    ('fill', [(12.8, 16), (16, 25.5), (19.2, 16)], LINE),
]


def svg():
    out = []
    for s in SHAPES:
        if s[0] == "line":
            _, pts, col, op, closed = s
            d = "M" + " L".join(f"{x:g} {y:g}" for x, y in pts) + (" Z" if closed else "")
            out.append(f'  <path d="{d}" fill="none" stroke="{col}" stroke-width="{W}" '
                       f'stroke-linecap="round" stroke-linejoin="round"'
                       + (f' stroke-opacity="{op}"' if op < 1 else "") + "/>")
        elif s[0] == "fill":
            _, pts, col = s
            out.append(f'  <path d="M' + " L".join(f"{x:g} {y:g}" for x, y in pts) + f' Z" fill="{col}"/>')
        else:
            _, cx, cy, r, col = s
            out.append(f'  <circle cx="{cx:g}" cy="{cy:g}" r="{r:g}" fill="{col}"/>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">\n'
            f'  <!-- {NAME} im Linienstil der Daumenregel. Erzeugt von tools/make_icons.py. -->\n'
            f'  <rect width="32" height="32" rx="7" fill="{BG}"/>\n' + "\n".join(out) + "\n</svg>\n")


def rgba(hexcol, a=1.0):
    h = hexcol.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (round(255 * a),)


def png(size, rounded, ss=16):
    """In ss-facher Größe zeichnen und verkleinern – ergibt glatte Kanten."""
    k = size * ss / 32
    img = Image.new("RGBA", (size * ss, size * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, size * ss - 1, size * ss - 1], radius=7 * k, fill=rgba(BG))
    else:  # iOS rundet die Ecken selbst ab; transparente Ecken würden schwarz
        d.rectangle([0, 0, size * ss, size * ss], fill=rgba(BG))
    w = W * k
    for s in SHAPES:
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        op = 1.0
        if s[0] == "line":
            _, pts, col, op, closed = s
            pts = [(x * k, y * k) for x, y in pts]
            if closed:
                pts = pts + pts[:2]
            ld.line(pts, fill=rgba(col), width=round(w), joint="curve")
            for x, y in pts:  # runde Ecken und Linienenden
                ld.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=rgba(col))
        elif s[0] == "fill":
            _, pts, col = s
            ld.polygon([(x * k, y * k) for x, y in pts], fill=rgba(col))
        else:
            _, cx, cy, r, col = s
            ld.ellipse([(cx - r) * k, (cy - r) * k, (cx + r) * k, (cy + r) * k], fill=rgba(col))
        if op < 1:
            layer.putalpha(layer.getchannel("A").point(lambda v: round(v * op)))
        img = Image.alpha_composite(img, layer)
    return img.resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    (OUT / "favicon.svg").write_text(svg(), encoding="utf-8", newline="\n")
    icons = {s: png(s, True) for s in (16, 32, 48)}
    icons[48].save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)],
                   append_images=[icons[16], icons[32]])
    png(180, False).save(OUT / "apple-touch-icon.png")
    print("favicon.svg, favicon.ico, apple-touch-icon.png geschrieben")
