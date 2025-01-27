# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

import requests
import time

def get_load_time(url):
    start_time = time.time()  # Start time
    try:
        response = requests.get(url)  # Send request to the URL
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
    except requests.exceptions.RequestException as e:
        return str(e)  # Return the error as a string
    end_time = time.time()  # End time
    load_time = end_time - start_time  # Calculate the time it took to load
    return load_time

# Test with different websites
urls = [
    "https://www.google.com",
    "https://www.ynet.co.il",
    "https://www.imdb.com"
]

for url in urls:
    load_time = get_load_time(url)
    if isinstance(load_time, float):  # Check if load_time is a valid float
        print(f"Time to load {url}: {load_time:.4f} seconds")
    else:
        print(f"Error loading {url}: {load_time}")