import requests
from bs4 import BeautifulSoup

# URL of FastDL page
fastdl_url = "https://fastdl.app/en"

# Headers to simulate a real browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Instagram video URL to download
instagram_video_url = input("Enter url: ")

# Send the POST request with the video URL
response = requests.post(fastdl_url, data={'url': instagram_video_url}, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the download link (update the selector as per the website's structure)
download_link = soup.find('a', class_='download-link')['href']

# Download the video
video_response = requests.get(download_link)
with open('video.mp4', 'wb') as file:
    file.write(video_response.content)

print("Video downloaded successfully!")
