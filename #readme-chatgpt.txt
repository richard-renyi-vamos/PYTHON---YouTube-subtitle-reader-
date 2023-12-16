
ChatGPT 3.5

User
Create a python script that reads the subtitle text from a YouTube video and copies it into a text file

ChatGPT
Certainly! To achieve this, you'll need to use the YouTube Data API to access the subtitles and the Python google-api-python-client library to interact with the API. Here's an outline of how you could approach this:

Set up Google API Credentials:

Go to the Google Developers Console.
Create a new project and enable the YouTube Data API.
Generate API credentials (an API key) for your project.
Install Required Python Libraries:

Use pip to install the necessary libraries:
bash
Copy code
pip install google-api-python-client google-auth-oauthlib
Python Script:

python
Copy code
from googleapiclient.discovery import build
import os

# YouTube Data API Key
api_key = 'YOUR_API_KEY'

# YouTube video ID
video_id = 'YOUR_VIDEO_ID'

# Build the YouTube API service
youtube = build('youtube', 'v3', developerKey=api_key)

# Request the captions (subtitles) for the video
captions = youtube.captions().list(
    part='snippet',
    videoId=video_id
).execute()

# Get the first available caption track (assuming it exists)
if captions['items']:
    caption_id = captions['items'][0]['id']

    # Download the caption track
    caption_info = youtube.captions().download(
        id=caption_id,
        tfmt='srt'  # SubRip (srt) format
    ).execute()

    # Save captions to a text file
    with open('captions.txt', 'w', encoding='utf-8') as file:
        file.write(caption_info.decode('utf-8'))

    print('Captions saved to captions.txt')
else:
    print('No captions found for this video.')
Replace 'YOUR_API_KEY' with your actual API key from the Google Developers Console, and 'YOUR_VIDEO_ID' with the ID of the YouTube video you want to retrieve subtitles from.

Run the Script:

Execute the script in your Python environment. It will create a captions.txt file containing the subtitles from the specified YouTube video.
Remember to handle exceptions and errors that might occur during the API request or file operations.






Message ChatGPT…

ChatGPT can make mistakes. Consider checking important information.
ChatGPT
