
import requests
import json
import csv

# Public API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Send GET request
    response = requests.get(url, timeout=30)

    # Check whether the request succeeded
    response.raise_for_status()

    # Convert JSON response into Python data
    data = response.json()

    # Save the original response as JSON
    with open("api_response.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    # Convert JSON records into CSV
    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        columns = ["userId", "id", "title", "body"]
        writer = csv.DictWriter(file, fieldnames=columns)

        writer.writeheader()
        writer.writerows(data)

    print("API request successful!")
    print("Total records fetched:", len(data))
    print("JSON file saved: api_response.json")
    print("CSV file saved: posts.csv")

except requests.exceptions.RequestException as error:
    print("API request failed:", error)

except (ValueError, KeyError) as error:
    print("Data processing failed:", error)
