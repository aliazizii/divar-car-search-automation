# Divar Car Search Automation

This project automates the process of searching for cars on the Divar website. It uses Selenium to navigate through the site, apply filters, and select a random car from the search results based on specific criteria defined in a configuration file.

## Prerequisites

1. **Python 3.x**: Ensure Python 3.x is installed on your system.
2. **Google Chrome**: Install the latest version of Google Chrome.
3. **ChromeDriver**: Download the ChromeDriver that matches your Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your PATH.

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
