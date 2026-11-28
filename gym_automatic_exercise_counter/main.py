import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
)

# ==============================================================================
# STEP 1: Setup, Chrome Profile, and Basic Navigation
# ==============================================================================
# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
# Keep browser open after script completes so you can view results
chrome_options.add_experimental_option("detach", True)

# Set a local profile directory so login session and local state persist between runs
current_dir = os.path.dirname(os.path.abspath(__file__))
profile_path = os.path.join(current_dir, "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={profile_path}")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Explicit wait helper (up to 10 seconds for elements to load)
wait = WebDriverWait(driver, 10)

# Target URL for Snack & Lift Gym practice web app
GYM_URL = "https://appbrewery.github.io/gym/"
print(f"Step 1: Navigating to {GYM_URL}...")
driver.get(GYM_URL)


# ==============================================================================
# STEP 2: Automated Login
# ==============================================================================
# Credentials for logging in (you can register once or use test credentials)
USER_EMAIL = os.getenv("GYM_USER_EMAIL", "student@appbrewery.com")
USER_PASSWORD = os.getenv("GYM_USER_PASSWORD", "Password123!")

print("Step 2: Attempting automated login...")
try:
    # 1. Check if a navigation login button needs to be clicked
    nav_login_buttons = driver.find_elements(
        By.XPATH,
        "//button[contains(text(), 'Login')] | //a[contains(text(), 'Login')] | //*[@id='login-button']"
    )
    if nav_login_buttons and nav_login_buttons[0].is_displayed():
        nav_login_buttons[0].click()
        time.sleep(1)

    # 2. Locate email and password input fields using Step 9 resilient waits
    email_field = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type='email'], #login-email, input[name='email']")
        )
    )
    email_field.clear()
    email_field.send_keys(USER_EMAIL)

    password_field = driver.find_element(
        By.CSS_SELECTOR, "input[type='password'], #login-password, input[name='password']"
    )
    password_field.clear()
    password_field.send_keys(USER_PASSWORD)

    # 3. Submit the login form
    submit_btn = driver.find_element(
        By.XPATH,
        "//button[@type='submit'] | //button[contains(text(), 'Sign In')] | //button[contains(text(), 'Log In')] | //*[@id='login-submit']"
    )
    submit_btn.click()
    print("[SUCCESS] Login form submitted!")
    time.sleep(2)

except (TimeoutException, NoSuchElementException):
    # If the user profile already saved the session, login form may not appear
    print("[INFO] Already logged in or login form not displayed. Continuing to schedule...")


# ==============================================================================
# STEP 9: Add Resilience in case of Network Failures / Simulated Delays
# ==============================================================================
# Wait until the schedule container and class cards appear in the DOM
print("\nStep 9: Waiting for schedule to fully load with network resilience...")
try:
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[id^='class-card-'], .class-card, div[id^='day-group-'], #schedule-page")
        )
    )
except TimeoutException:
    print("[WARN] Network delay detected. Refreshing page...")
    driver.refresh()
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[id^='class-card-'], .class-card, div[id^='day-group-']")
        )
    )


# ==============================================================================
# STEP 5: Add Counters to Your Script to Provide a Neat Summary
# ==============================================================================
classes_booked_count = 0
already_booked_count = 0
skipped_classes_count = 0


# ==============================================================================
# STEP 3 & STEP 6: Class Booking (Book every Tuesday AND Thursday class)
# ==============================================================================
# Days to automatically reserve: Tuesday ("Tue") and Thursday ("Thu")
TARGET_DAYS = ["Tue", "Thu"]
print(f"Step 3 & 6: Looking for upcoming classes on: {', '.join(TARGET_DAYS)}...")

# Find all class cards available on the schedule
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-'], .class-card")
print(f"Found {len(class_cards)} total class cards on schedule.")

for card in class_cards:
    try:
        # Determine which day this class card belongs to
        day_name = ""
        try:
            # Check ancestor day group container (e.g. id='day-group-tuesday')
            day_group = card.find_element(By.XPATH, "ancestor::div[starts-with(@id, 'day-group-')]")
            heading = day_group.find_element(By.CSS_SELECTOR, "h2, h3, .day-heading")
            day_name = heading.text.strip()
        except NoSuchElementException:
            # Fallback: check text inside the card itself
            day_name = card.text

        # Filter only Tuesday and Thursday classes
        is_target_day = any(day in day_name for day in TARGET_DAYS)
        if not is_target_day:
            skipped_classes_count += 1
            continue

        # Extract class name for informative logs
        try:
            class_title = card.find_element(By.CSS_SELECTOR, "h3, h4, .class-title, strong").text
        except NoSuchElementException:
            class_title = "Workout Session"

        # ======================================================================
        # STEP 4: Check if a Class is Already Booked
        # ======================================================================
        # Locate the action button inside the class card
        action_button = card.find_element(By.CSS_SELECTOR, "button")
        btn_text = action_button.text.strip().lower()

        # Check booking status: button text 'booked' or data attribute indicates state
        is_already_booked = (
            "booked" in btn_text
            or card.get_attribute("data-booked") == "true"
            or not action_button.is_enabled()
        )

        if is_already_booked:
            print(f"  - [ALREADY BOOKED] '{class_title}' on {day_name[:12]}")
            already_booked_count += 1
        else:
            # Scroll element into view and click to book
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", action_button)
            time.sleep(0.3)
            try:
                action_button.click()
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click();", action_button)

            print(f"  + [BOOKED SUCCESS] Booked '{class_title}' on {day_name[:12]}!")
            classes_booked_count += 1
            time.sleep(0.5)

    except Exception as e:
        print(f"  ! [ERROR] Issue processing class card: {e}")

# Display Step 5 summary
print("\n" + "=" * 50)
print("             EXERCISE BOOKING SUMMARY")
print("=" * 50)
print(f"  Newly Booked Classes   : {classes_booked_count}")
print(f"  Already Booked Classes : {already_booked_count}")
print(f"  Skipped (Other Days)   : {skipped_classes_count}")
print("=" * 50 + "\n")


# ==============================================================================
# STEP 7: Verify Class Bookings on the 'My Bookings' Page
# ==============================================================================
print("Step 7: Verifying bookings on 'My Bookings' page...")
try:
    my_bookings_tab = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'My Bookings')] | //button[contains(text(), 'My Bookings')] | //*[@id='nav-my-bookings']")
        )
    )
    my_bookings_tab.click()

    # Wait for the My Bookings container to render
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[id^='booking-card-'], .booking-card, #my-bookings-page")
        )
    )

    confirmed_bookings = driver.find_elements(
        By.CSS_SELECTOR, "div[id^='booking-card-'], .booking-card, .booking-item"
    )
    print(f"[VERIFIED] Found {len(confirmed_bookings)} confirmed booking(s):")
    for idx, item in enumerate(confirmed_bookings, 1):
        clean_text = " | ".join(item.text.splitlines())
        print(f"   {idx}. {clean_text}")

except Exception as e:
    print(f"[NOTE] Could not open 'My Bookings' view: {e}")


# ==============================================================================
# STEP 8: Time Travel Quality Assurance (QA)
# ==============================================================================
# The Snack & Lift app has an admin tool to fast-forward time to test expiration
print("\nStep 8: Checking for Time Travel QA controls...")
try:
    time_travel_buttons = driver.find_elements(
        By.XPATH,
        "//button[contains(text(), 'Time Travel')] | //*[@id='time-travel-btn'] | //button[contains(text(), '+7 Days')] | //button[contains(text(), '+1 Week')]"
    )
    if time_travel_buttons:
        print("[QA] Time Travel button detected! Fast-forwarding time for QA check...")
        time_travel_buttons[0].click()
        time.sleep(1)
        print("[QA] Time advanced successfully. Schedule updated for the new week.")
    else:
        print("[QA] Time Travel button not visible on current screen.")
except Exception as e:
    print(f"[QA] Time Travel note: {e}")

print("\nAutomation routine completed! Browser remains open for inspection.")
