# Instagram Followers Scraper

## Overview
This Python script uses Selenium to automate the extraction of followers from an Instagram profile. It logs in with your credentials, navigates to the target account, and scrapes follower usernames, saving them in batches to Excel files.

## Features
- Automated login to Instagram.
- Scrolls through the followers list to extract usernames.
- Saves usernames in batches of 200 to Excel files.
- Uses multi-threading for efficient file saving.
- Implements retry logic to handle Instagram's dynamic loading behavior.

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
Modify the script and replace the placeholders with your Instagram credentials:
```python
USERNAME = "your_username"
PASSWORD = "your_password"
TARGET_PROFILE = "target_account"  # Change this to the account whose followers you want to scrape
```

### 2. Run the Script
Execute the script:
```bash
python script.py
```

### 3. Output
- Extracted followers will be saved in Excel files named `followers_batch_<batch_number>.xlsx`.
- Each batch contains 200 followers.

## Notes
- Instagram may block or limit automation attempts, so use this script responsibly.
- If you receive a login challenge (e.g., "suspicious login attempt"), verify your account and try again.
- Ensure your IP is not blocked due to excessive requests.

## License
This project is licensed under the MIT License.

## Disclaimer
This script is intended for **educational purposes only**. Scraping data from Instagram violates its **Terms of Service**, and using automation may lead to your account being **restricted or banned**. Use at your own risk!

