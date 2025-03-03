from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import threading

# Instagram Credentials
USERNAME = "your username"
PASSWORD = "your pass"
TARGET_PROFILE = "thetarget profile"  # Change to the target account


# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

def save_to_excel(followers_list, batch_number):
    """Save a batch of followers to an Excel file."""
    df = pd.DataFrame(followers_list, columns=["Username"])
    filename = f"followers_batch_{batch_number}.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Saved {len(followers_list)} usernames to {filename}")

try:
    # Open Instagram & Login
    driver.get("https://www.instagram.com/accounts/login/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for login to complete
    time.sleep(8)

    # Navigate to target profile
    driver.get(f"https://www.instagram.com/{TARGET_PROFILE}/")
    time.sleep(5)

    # Click 'Followers' Button
    followers_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers/')]"))
    )
    followers_button.click()
    time.sleep(5)

    # Find scrollable div inside the followers popup
    scroll_div = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")

    last_height = driver.execute_script("return arguments[0].scrollHeight", scroll_div)
    followers_set = set()
    followers_batch = []
    batch_number = 1
    max_retries = 3  # To retry scrolling if usernames are missing
    retry_count = 0

    while True:
        # Extract followers
        followers = driver.find_elements(By.XPATH, "//div[@role='dialog']//a[contains(@href, '/')]")
        for user in followers:
            username = user.get_attribute("href").split("/")[-2]
            if username not in followers_set:
                followers_set.add(username)
                followers_batch.append(username)

            # Save every 200 followers
            if len(followers_batch) == 200:
                threading.Thread(target=save_to_excel, args=(followers_batch[:], batch_number)).start()
                batch_number += 1
                followers_batch.clear()

        # Scroll down with delay to allow Instagram to load new followers
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_div)
        time.sleep(5)  # Increased delay for better loading

        # Check if scrolling stopped (retries if needed)
        new_height = driver.execute_script("return arguments[0].scrollHeight", scroll_div)
        if new_height == last_height:
            retry_count += 1
            if retry_count >= max_retries:
                print("✅ No more followers to load.")
                break  # Stop scrolling if retries exceeded
            time.sleep(5)  # Additional delay before retrying
        else:
            retry_count = 0  # Reset retry count if scrolling continues
        last_height = new_height

    # Save any remaining usernames (if < 200)
    if followers_batch:
        threading.Thread(target=save_to_excel, args=(followers_batch, batch_number)).start()

    print(f"✅ Extraction complete! Total followers: {len(followers_set)}")

finally:
    driver.quit()
