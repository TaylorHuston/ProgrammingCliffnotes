#!/usr/bin/python3

"""
Demonstrates date and time handling in Python.
"""
import time
from datetime import datetime, timezone, timedelta
import calendar

# ==========================================
# SECTION 1: BASIC TIME FUNCTIONS
# ==========================================

print("=" * 50)
print("BASIC TIME FUNCTIONS")
print("=" * 50)

# Current timestamp (seconds since epoch - January 1, 1970, 00:00:00 UTC)
timestamp = time.time()
print(f"Current timestamp: {timestamp}")

# Convert timestamp to human-readable string
readable_time = time.ctime(timestamp)
print(f"Human readable time: {readable_time}")

# Get structured time (local time)
local_time = time.localtime()
print(f"Structured local time: {local_time}")
print(f"Year: {local_time.tm_year}")
print(f"Month: {local_time.tm_mon}")
print(f"Day: {local_time.tm_mday}")
print(f"Hour: {local_time.tm_hour}")
print(f"Minute: {local_time.tm_min}")
print(f"Second: {local_time.tm_sec}")

# Format time using strftime
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print(f"Formatted time: {formatted_time}")

# ==========================================
# SECTION 2: DATETIME MODULE
# ==========================================

print("\n" + "=" * 50)
print("DATETIME MODULE")
print("=" * 50)

# Current date and time (local timezone)
now = datetime.now()
print(f"Current datetime (local): {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")

# Create a specific datetime
specific_date = datetime(2025, 4, 21, 14, 30, 0)
print(f"Specific date: {specific_date}")

# Format datetime using strftime
print(f"Formatted date: {specific_date.strftime('%A, %B %d, %Y at %I:%M %p')}")

# ==========================================
# SECTION 3: TIMEZONES
# ==========================================

print("\n" + "=" * 50)
print("TIMEZONES")
print("=" * 50)

# Current date and time in UTC
now_utc = datetime.now(timezone.utc)
print(f"Current datetime (UTC): {now_utc}")
print(f"UTC Hour: {now_utc.hour}")

# Create a datetime with timezone
moon_landing = datetime(1969, 7, 20, 20, 17, 40, tzinfo=timezone.utc)
print(f"Moon landing: {moon_landing}")

# Calculate time difference
time_since_moon_landing = now_utc - moon_landing
print(f"Time since moon landing: {time_since_moon_landing}")
print(f"Days since moon landing: {time_since_moon_landing.days}")

# ==========================================
# SECTION 4: CALENDAR MODULE
# ==========================================

print("\n" + "=" * 50)
print("CALENDAR MODULE")
print("=" * 50)

# Get day of week (0 is Monday, 6 is Sunday)
weekday = moon_landing.weekday()
print(f"Moon landing weekday: {weekday}")

# Get list of day names
day_names = list(calendar.day_name)
print(f"Day names: {day_names}")
print(f"Moon landing day: {calendar.day_name[weekday]}")

# Current day of the week
current_day = calendar.day_name[datetime.now().weekday()]
print(f"Today is: {current_day}")

# Print a month's calendar
print("\nCalendar for April 2025:")
print(calendar.month(2025, 4))

# Check if a year is a leap year
leap_years = [2020, 2021, 2022, 2023, 2024, 2025]
for year in leap_years:
    print(f"{year} is leap year: {calendar.isleap(year)}")

# ==========================================
# SECTION 5: TIME OPERATIONS
# ==========================================

print("\n" + "=" * 50)
print("TIME OPERATIONS")
print("=" * 50)

# Add/subtract time
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Yesterday: {(now - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')}")

# Add hours, minutes, seconds
future_time = now + timedelta(hours=3, minutes=15, seconds=30)
print(
    f"3 hours, 15 minutes, 30 seconds from now: {future_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Sleep function demonstration (commented out to avoid waiting)
print("\nSleep function example:")
print("Starting...")
# time.sleep(1)  # Uncomment to wait for 1 second
print("...finished (normally would wait 1 second)")

# If you run this script directly
if __name__ == "__main__":
    print("\nThis script demonstrates time operations in Python.")
    print("It is part of the separation of the original math_and_time.py file.")
