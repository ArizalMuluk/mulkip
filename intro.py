import pyfiglet


def hsl_to_rgb(h, s, l):
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h < 360:
        r, g, b = c, 0, x

    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)

    return r, g, b


def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


def intros(text, h, s, l, border_char="-", smwt=False):
    """Prints ASCII art with a specified HSL color and border."""
    ascii_art = pyfiglet.figlet_format(text, font="small")
    r, g, b = hsl_to_rgb(h, s, l)
    colored_art = f"{rgb_to_ansi(r, g, b)}{ascii_art}\033[0m"

    # Menentukan warna border
    if smwt:
        border_color = rgb_to_ansi(r, g, b)  # Warna border sama dengan warna teks
    else:
        border_color = rgb_to_ansi(255, 255, 255)

    border = (
        border_color
        + (border_char * max(len(line) for line in ascii_art.splitlines()))
        + "\033[0m"
    )
    print(border)
    print(colored_art)
    print(border)  # Garis pembatas di bawah


if __name__ == "__main__":
    intros("Welcome to Mulkip", 94, 0.91, 0.57, border_char="*", smwt=True)
