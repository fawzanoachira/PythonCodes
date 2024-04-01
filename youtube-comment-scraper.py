import os
import csv
import re
from googleapiclient.discovery import build

def fetch_all_comments(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    comments = []
    nextPageToken = None

    while True:
        comments_request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            pageToken=nextPageToken
        )

        comments_response = comments_request.execute()

        new_comments = comments_response.get("items", [])
        comments.extend(new_comments)

        nextPageToken = comments_response.get("nextPageToken")

        if not nextPageToken:
            break

    return comments

def save_comments_to_csv(comments, csv_file_path):
    with open(csv_file_path, mode="w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        
        csv_writer.writerow(["Comment", "Author"])

        for comment in comments:
            text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            author = comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
            csv_writer.writerow([text, author])

def extract_video_id(youtube_url):
    """
    Extracts the video ID from a YouTube URL.

    Args:
    - youtube_url (str): The YouTube video URL.

    Returns:
    - str: The extracted video ID, or None if not found.
    """
    # Define a regular expression pattern to match the video ID
    pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
    
    # Search for the pattern in the URL
    match = pattern.search(youtube_url)

    # If a match is found, return the video ID, else return None
    return match.group(1) if match else None

if __name__ == "__main__":
    api_key = "YourAPIKey"
    video_id = extract_video_id("youtube-link")

    all_comments = fetch_all_comments(api_key, video_id)

    csv_file_path = "nameOfFile.csv"
    save_comments_to_csv(all_comments, csv_file_path)

    print(f"Comments have been saved to {os.path.abspath(csv_file_path)}")