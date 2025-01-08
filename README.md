# Mulkip - IP Address Information Tool

## Description
Mulkip is a simple Python application that allows users to get detailed information about a specific IP address. It leverages the API of `ipinfo.io` to retrieve data such as hostname, location, city, region, country, and organization associated with the entered IP address.

## Features
- Validates the IP address format.
- Retrieves IP address related information from the API.
- Display IP information in an easy-to-read format.
- Save IP information into a text file for further reference.

## Prerequisites
Before running this application, make sure you have:
- Python 3.x installed on your system.
- A `.env` file that contains the libraries required to run the application. You can use `pip` to install the dependencies listed in the `.env` file.

## How to use
1. Clone this repository or download the `mulkip.py` file.
2. Make sure you have the `.env` file containing the required dependencies.
3. Open a terminal and navigate to the directory where the file is stored.
4. Run the application with the command:

```bash
python mulkip.py #For Windows
```

```bash
python3 mulkip.py #For Linux
```

5. Enter the IP address you want to search when prompted.
6. Information about the IP address will be displayed in the terminal and saved into the ip_info.txt file.

## Usage Example
```bash
Enter IP Address: 8.8.8.8

IP Address Information:
IP: 8.8.8.8
Hostname: dns.google
Location: 37.3860,-122.0838
City: Mountain View
Region: California
Country: US
Org: Google LLC
IP TRACK SUCCES!!

```

## Contributions
If you would like to contribute to this project, please fork this repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For questions or suggestions, please contact bangmulukkerenl@gmail.com.


### Changes Made
- Added information about using `.env` files to manage required libraries.

If there is anything else you would like to change or add, please let us know!
