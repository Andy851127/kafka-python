import json
import requests
import sseclient

# Wikimedia RecentChange stream URL
url = "https://stream.wikimedia.org/v2/stream/recentchange"

def get_wikimedia_stream(url):
    # Open the connection to the stream
    response = requests.get(url, stream=True)
    
    # Check if the response is successful and contains a valid URL
    if response.ok and response.url:
        client = sseclient.SSEClient(response.url)  # Use response.url instead of url

        for event in client:
            if event.event == 'message':
                try:
                    # Parse the event data as JSON
                    change = json.loads(event.data)
                    json_data = json.dumps(change, indent=2)
                    print(json_data)  # Pretty print the JSON data
                except json.JSONDecodeError as e:
                    print(f"JSON decode error: {e}")
    else:
        print("Failed to establish connection to the stream.")

if __name__ == "__main__":
    get_wikimedia_stream(url)
