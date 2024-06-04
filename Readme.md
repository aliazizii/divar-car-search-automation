# Divar Car Search Automation

This project automates the process of searching for cars on the Divar website. It uses Selenium to navigate through the site, apply filters, and select a random car from the search results based on specific criteria defined in a configuration file.


https://github.com/aliazizii/divar-car-search-automation/assets/77853490/ff64611a-b46c-44f8-8a00-ca05e28526b6


## Prerequisites

1. **Python 3.x**: Ensure Python 3.x is installed on your system.
2. **Google Chrome**: Install the latest version of Google Chrome.
3. **ChromeDriver**: Download the ChromeDriver that matches your Chrome version and ensure it's in your PATH.

## File Structure

- app.py: The main script containing the Selenium automation logic.
- config.ini: Configuration file containing user-defined settings for the car search.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/aliazizii/divar-car-search-automation.git
    cd divar-car-search-automation
    ```

2. Install the required Python packages:
    ```bash
    pip install selenium configparser
    ```

3. Create a `config.ini` file in the project directory with the following content:
    ```ini
    [settings]
    car_brand = <your_car_brand>
    desired_color_order = <color_order_number>
    maximum_price = <max_price>
    minimum_kilometrage = <min_kilometrage>
    ```

    Replace `<your_car_brand>`, `<color_order_number>`, `<max_price>`, and `<min_kilometrage>` with your desired values.

## Usage

To run the script, simply execute:
```bash
python app.py
```

## Notes

- The XPath values used in the script match the actual structure of the Divar website. If the website structure changes,  may need to update these values accordingly.
- The script is set up to simulate a Pixel 2 device. Adjust the device emulation as needed.
