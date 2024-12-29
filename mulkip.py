import re

import requests

from intro import intros


def hex_to_ansi(hex_color):
    """Convert hex color to ANSI escape code"""
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    ansi_code = 16 + (r // 51) * 36 + (g // 51) * 6 + (b // 51)
    return f"38;5;{ansi_code}"


def colored_text(text, hex_color):
    color_code = hex_to_ansi(hex_color)
    return f"\033[{color_code}m{text}\033[0m"


intros("Welcome to Mulkip", 94, 0.91, 0.57, border_char="=", smwt=True)


def is_valid_ip(ip_address):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip_address) is not None


def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def save_to_file(ip_address, info):
    with open("ip_info.txt", "a") as file:
        file.write("\nIP Address Information:\n")
        file.write(f"IP: {info.get('ip')}\n")
        file.write(f"Hostname: {info.get('hostname')}\n")
        file.write(f"Location: {info.get('loc')}\n")
        file.write(f"City: {info.get('city')}\n")
        file.write(f"Region: {info.get('region')}\n")
        file.write(f"Country: {info.get('country')}\n")
        file.write(f"Org: {info.get('org')}\n")
        file.write("\n---\n\n")


if __name__ == "__main__":
    ip_address = input(colored_text("\nEnter IP Address: ", "#00FFF3"))

    if is_valid_ip(ip_address):
        info = get_ip_info(ip_address)

        if info:
            print(colored_text("\nIP Address Information:", "#00FF00"))
            print(
                f"{colored_text('IP:', '#1B03A3.')} {colored_text(info.get('ip'), '#fbf8fd')}"
            )
            print(
                f"{colored_text('Hostname:', '#1B03A3.')} {colored_text(info.get('hostname'), '#fbf8fd')}"
            )
            print(
                f"{colored_text('Location:', '#1B03A3.')} {colored_text(info.get('loc'), '#fbf8fd')}"
            )
            print(
                f"{colored_text('City:', '#1B03A3.')} {colored_text(info.get('city'), '#fbf8fd')}"
            )
            print(
                f"{colored_text('Region:', '#1B03A3.')} {colored_text(info.get('region'), '#fbf8fd')}"
            )
            print(
                f"{colored_text('Country:', '#1B03A3.')} {colored_text(info.get('country'), '#fbf8fd')}"
            )
            print(
                f"{colored_text('Org:', '#1B03A3.')} {colored_text(info.get('org'), '#fbf8fd')}"
            )

            save_to_file(ip_address, info)
            print(colored_text("IP TRACK SUCCESS!!\n", "#00FF00"))
        else:
            print(colored_text("Can't find the IP address.", "#FF0000"))
    else:
        print(
            colored_text(
                "Invalid IP Address format. Please enter the correct IP Address.",
                "#FF0000",
            )
        )
