Required Packages


Open the terminal in PyCharm. You'll need these packages for this project:



- requests -- for making API calls

- requests_cache -- for caching API responses locally so you don't burn through your free tier during development

- python-dotenv -- for loading secrets from a .env file (optional but handy)

- twilio -- for sending SMS/WhatsApp notifications



You can install the packages now or in later steps when you actually need them.



APIs Required


- Google Sheet Data Management - https://sheety.co/

- SerpAPI Google Flights (Free Signup, 100 searches/month, no credit card required) - https://serpapi.com/google-flights-api

- Alternatively, you can use mock flight data if you want to give Serp a miss or you've hit a request limit: https://app.100daysofpython.dev/services/flights

- Twilio Messaging (SMS or WhatsApp) API - https://www.twilio.com/docs/messaging/quickstart/python





Program Requirements


1. Use the Sheety API to read the destination data from your Google Sheet. The sheet should already contain the airport IATA codes for each city (e.g. CDG for Paris, JFK for New York).

2. Use the SerpAPI Google Flights API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.


4. The SMS (or WhatsApp message) should include the departure airport IATA code, destination airport IATA code, flight price and flight dates.



In a nutshell, the program should work like this:




Notes and Gotchas


- Avoid hitting your rate limit on your trial accounts by not using too many destination airports in your Google Sheet (use 3 or at most 5).

- The free tier for SerpAPI gives you 100 searches/month. We will set up requests_cache early on to cache flight search responses locally -- this means re-running your code during development won't cost extra searches.

- The free tier for the Sheety API only allows 200 requests per month. Also avoid making too many unnecessary requests while testing your code.

- Twilio can be tricky with SMS messages in some countries, so you can use their WhatsApp service instead. Here's what it would look like:






Register with SerpAPI

SerpAPI provides a free API for searching Google Flights.



1. Go to https://serpapi.com/users/sign_up and create a free account (No credit card is required)

3. Once logged in, find your API key on the dashboard: https://serpapi.com/manage-api-key

4. Copy your API key and keep it safe -- you'll need it later








Resources for this lecture



297. Step 2 - Use Sheety to Read Airport and Price Data
2min
Not completed
Start
298. Step 3 - Get flights and prices for a single city
3min
Not completed
Start
299. Step 4 - Parse the flight data and show the cheapest flight
3min
Not completed
Start
300. Step 5 - Check all the flights in your sheet
1min
Not completed
Start
301. Step 6 - Send a notification with Twilio




used mail smtp in place of twilio



