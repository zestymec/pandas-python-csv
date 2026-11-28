The Day 49: Automating your Exercise Routine at the Gym project has been implemented in 
main.py
 inside your gym_automatic_exercise_counter folder.

All 9 steps shown in your checklist are implemented with clear, detailed comments explaining how each part works.

Step-by-Step Overview of the Implementation
Step 1: Setup, Chrome Profile, and Basic Navigation
python


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Persistent user profile directory so login state and cookies persist
profile_path = os.path.join(current_dir, "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={profile_path}")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")
Why Chrome Profile? --user-data-dir tells Chrome to save your session data locally. If you run the script again, you remain logged in and your booked classes stay saved in local storage.
detach: True: Keeps the browser window open after the script ends so you can visually verify the bookings.
Step 2: Automated Login
python


email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], #login-email")))
email_field.send_keys(USER_EMAIL)
password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password'], #login-password")
password_field.send_keys(USER_PASSWORD)
submit_btn.click()
Automatically identifies the login inputs and fills in your gym credentials, submitting the form to access the schedule page.
Step 3 & Step 6: Class Booking (Every Tuesday AND Thursday Class)
python


TARGET_DAYS = ["Tue", "Thu"]
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-'], .class-card")
for card in class_cards:
    day_group = card.find_element(By.XPATH, "ancestor::div[starts-with(@id, 'day-group-')]")
    heading = day_group.find_element(By.CSS_SELECTOR, "h2, h3, .day-heading")
    day_name = heading.text.strip()
    
    if not any(day in day_name for day in TARGET_DAYS):
        skipped_classes_count += 1
        continue
Uses XPath ancestor::div[starts-with(@id, 'day-group-')] to look up the parent day container and check whether the heading contains "Tue" or "Thu". Classes on Monday, Wednesday, Friday, etc., are skipped.
Step 4: Check If a Class Is Already Booked
python


action_button = card.find_element(By.CSS_SELECTOR, "button")
btn_text = action_button.text.strip().lower()
is_already_booked = (
    "booked" in btn_text
    or card.get_attribute("data-booked") == "true"
    or not action_button.is_enabled()
)
Inspects the button state before clicking. If the button already reads "Booked" or is disabled, the script avoids clicking it again and increments the already-booked counter.
Step 5: Add Counters to Provide a Neat Summary
python


classes_booked_count = 0
already_booked_count = 0
skipped_classes_count = 0
Tracks each action during the loop and outputs a clean console summary at the end:
text


==================================================
             EXERCISE BOOKING SUMMARY
==================================================
  Newly Booked Classes   : 2
  Already Booked Classes : 1
  Skipped (Other Days)   : 5
==================================================
Step 7: Verify Class Bookings on the "My Bookings" Page
python


my_bookings_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'My Bookings')]")))
my_bookings_tab.click()
confirmed_bookings = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-'], .booking-card")
Navigates to the My Bookings view and prints out the confirmed list of booked classes.
Step 8: Time Travel Quality Assurance (QA)
python


time_travel_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Time Travel')] | //*[@id='time-travel-btn']")
if time_travel_buttons:
    time_travel_buttons[0].click()
Triggers the built-in time-shift feature on the practice site to advance time by a week, verifying that past classes expire and the next week's schedule loads properly.
Step 9: Add Resilience for Network Failures & Delays
python


try:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='class-card-']")))
except TimeoutException:
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='class-card-']")))
Protects the bot from slow network loading or simulated latency using WebDriverWait and automatic retry/page refresh handling.
How to Run
From your project root:

bash


/Users/apple/umeraziz/pandas-python-csv/.venv/bin/python gym_automatic_exercise_counter/main.py

