import re

import requests

from intro import intros


# Fungsi untuk menambahkan warna pada teks
def colored_text(text, color_code):
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
    ip_address = input(colored_text("\nEnter IP Address: ", "36"))  # Cyan

    if is_valid_ip(ip_address):
        info = get_ip_info(ip_address)

        if info:
            print(colored_text("\nIP Address Information:", "32"))  # Green
            print(f"IP: {colored_text(info.get('ip'), '34')}")  # Blue
            print(f"Hostname: {colored_text(info.get('hostname'), '34')}")
            print(f"Location: {colored_text(info.get('loc'), '34')}")
            print(f"City: {colored_text(info.get('city'), '34')}")
            print(f"Region: {colored_text(info.get('region'), '34')}")
            print(f"Country: {colored_text(info.get('country'), '34')}")
            print(f"Org: {colored_text(info.get('org'), '34')}")

            # Simpan informasi ke dalam file
            save_to_file(ip_address, info)
            print(colored_text("IP TRACK SUCCES!!\n", "32"))  # Green
        else:
            print(colored_text("Can't find the IP address.", "31"))  # Red
    else:
        print(
            colored_text(
                "Invalid IP Address format. Please enter the correct IP Address.",
                "31",
            )
        )  # Red
