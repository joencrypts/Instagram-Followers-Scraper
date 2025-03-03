# Instagram Followers Scraper

## Overview
This project consists of two Python scripts, **IGS.py** and **IGST.py**, that automate the process of extracting and filtering Instagram followers.

- **IGS.py**: Logs into Instagram, scrapes followers from a target profile, and saves them in batches to Excel files.
- **IGST.py**: Reads the saved Excel sheets, scrapes profile details for each username, and modifies the sheets accordingly.

## Features
- **IGS.py**
  - Automated login to Instagram.
  - Scrolls through the followers list to extract usernames.
  - Saves usernames in batches of 200 to Excel files.
  - Uses multi-threading for efficient file saving.
  - Implements retry logic to handle Instagram's dynamic loading behavior.

- **IGST.py**
  - Reads the previously saved follower batches.
  - Scrapes additional profile details for each follower.
  - Updates the corresponding Excel sheets with new data.

## Requirements
### Dependencies
Ensure you have the following Python libraries installed:

```bash
pip install selenium pandas openpyxl
```

### WebDriver
Download and install the latest **Chrome WebDriver** compatible with your Chrome version from [here](https://chromedriver.chromium.org/downloads). Place it in your system PATH or specify its location when initializing Selenium.

## Usage
### 1. Set Up Instagram Credentials
Modify **IGS.py** and replace the placeholders with your Instagram credentials:
```python
USERNAME = "your_username"
PASSWORD = "your_password"
TARGET_PROFILE = "target_account"  # Change this to the account whose followers you want to scrape
```

### 2. Run the Scripts
#### Step 1: Extract Followers
Run **IGS.py** to scrape followers and save them into Excel batches:
```bash
python IGS.py
```

#### Step 2: Filter and Update Follower Data
Run **IGST.py** to read and update the follower batches with profile details:
```bash
python IGST.py
```

### 3. Output
- **IGS.py** saves extracted followers into `followers_batch_<batch_number>.xlsx` files (each containing 200 usernames).
- **IGST.py** updates these Excel sheets by adding profile details scraped from Instagram.

## Notes
- Instagram may block or limit automation attempts, so use this script responsibly.
- If you receive a login challenge (e.g., "suspicious login attempt"), verify your account and try again.
- Ensure your IP is not blocked due to excessive requests.

## License
This project is licensed under the MIT License.

## Disclaimer
This script is intended for **educational purposes only**. Scraping data from Instagram violates its **Terms of Service**, and using automation may lead to your account being **restricted or banned**. Use at your own risk!

