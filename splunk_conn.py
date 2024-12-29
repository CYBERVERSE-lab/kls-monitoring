import requests
import json

url = "https://localhost:8088/services/collector/event"

payload = json.dumps({
  "event": {
    "key": "Testing Splunk connection."
  }
})
headers = {
  'Authorization': 'Splunk 34b6647a-5fbe-4b1d-a443-ee7058ac9d13',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
