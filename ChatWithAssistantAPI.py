import os
import json
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load environment variables
load_dotenv('../.env')

# Define constants
client_id = 'cc09b075-ca33-4b8f-952c-ca3c78dc2630'
client_secret = 'ccb917129b204285a55cf02e3214893b'

# Define URLs
url_token = 'https://id.trimble.com/oauth/token'
url_epic_to_userstories = "https://agw.construction-integration.trimble.cloud/trimbledeveloperprogram/assistants/v1/agents/epic-to-userstories/messages"

# Define headers
headers_token = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic IGNjMDliMDc1LWNhMzMtNGI4Zi05NTJjLWNhM2M3OGRjMjYzMDpjY2I5MTcxMjliMjA0Mjg1YTU1Y2YwMmUzMjE0ODkzYg=='
}
headers_epic_to_userstories = {
    'Content-Type': 'application/json'
}

# Define data
data_token = {
    'grant_type': 'client_credentials',
    'scope': 'trimble-assistant-hackathon'
}

# Define request body for epic to user stories
request_body_epic = {
    "message": "Mobile Application Development Epic Title: Mobile Application Development Epic Description: This epic involves developing a mobile application for the platform. It aims to provide a seamless user experience on mobile devices, including features like user login, profile management, notifications, and offline capabilities. The mobile app will increase user engagement and accessibility. Acceptance Criteria: Users can log in and manage their profiles on the mobile app. The app provides push notifications for important updates. Users can access key features offline. The app is available on both iOS and Android platforms. Project Components: Frontend: Mobile App UI Design User Authentication Screens Profile Management Screens Notifications Interface Offline Capability Features Backend: API Design for Mobile App Synchronization Logic for Offline Access Database: Mobile-specific Data Storage Testing: Unit Testing for Mobile App Features Integration Testing for Mobile API User Acceptance Testing for Mobile App Stakeholders: End Users Product Manager Mobile App Developers QA Testers Priority: High Priority",
    "stream": False,
    "model_id": "gpt-4"
}

# Function to send message
def send_message(url, headers, request_body):
    response = requests.post(url, headers=headers, data=json.dumps(request_body))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

# Main function
def main():
    # Get token
    response_token = requests.post(url_token, headers=headers_token, data=data_token)
    token = response_token.json()['access_token']

    # Update headers for assistant with the token
    headers_epic_to_userstories['Authorization'] = 'Bearer ' + token

    # Send message for epic to user stories
    response_data_epic = send_message(url_epic_to_userstories, headers_epic_to_userstories, request_body_epic)
    with open('response.json', 'w') as json_file:
        json.dump(response_data_epic, json_file, indent=4)
    print("The response has been saved to 'response.json'")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)