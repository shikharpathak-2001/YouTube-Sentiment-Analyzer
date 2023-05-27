from textblob import TextBlob
from googleapiclient.discovery import build
import matplotlib.pyplot as plt
# enter your api key
api_key = 'AIzaSyCxF-ow9ZvVskknJLqdNnVmvPDKEUlRLhI'


def video_comments(video_id, max_comments):
    # empty list for storing reply
    replies = []
    count = 0  # counter for the number of comments extracted

    # creating YouTube resource object
    youtube = build('youtube', 'v3', developerKey=api_key)

    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
    ).execute()

    # iterate video response
    with open('comments.txt', 'w', encoding='utf-8') as f:  # open the file in 'w' mode to clear its contents
        while video_response and count < max_comments:
            # extracting required info
            # from each result object
            for item in video_response['items']:
                if count >= max_comments:
                    break

                # Extracting comments
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

                # counting number of reply of comment
                replycount = item['snippet']['totalReplyCount']

                # if reply is there
                if replycount > 0:
                    # iterate through all reply
                    for reply in item['replies']['comments']:
                        # Extract reply
                        reply = reply['snippet']['textDisplay']

                        # Store reply is list
                        replies.append(reply)

                # write comment with list of reply to file
                f.write(comment + '\n')
                for reply in replies:
                    f.write('\t' + reply + '\n')
                f.write('\n')

                # empty reply list
                replies = []

                # increment count
                count += 1

                if count >= max_comments:
                    break

            # Again repeat
            if count >= max_comments:
                break

            if 'nextPageToken' in video_response:
                video_response = youtube.commentThreads().list(
                    part='snippet,replies',
                    videoId=video_id,
                    pageToken=video_response['nextPageToken']
                ).execute()
            else:
                break

    with open('comments.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Calculate sentiment polarity
    blob = TextBlob(text)
    polarity_scores = blob.sentiment.polarity  # -1 to 1
    # polarity_scores = list(blob.sentiment.polarity for sentence in blob.sentences)

    # Create a histogram of sentiment polarity
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(polarity_scores, bins=50, range=(-1, 1), alpha=0.25)

    # Add labels and title
    ax.set_xlabel('Sentiment Polarity')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Sentiment Polarity')
    ax.set_title(polarity_scores)

    # Add vertical lines for neutral, positive, and negative polarity
    ax.axvline(0, color='black', linestyle='--', linewidth=1)
    ax.axvline(0.5, color='green', linestyle='--', linewidth=1)
    ax.axvline(-0.5, color='red', linestyle='--', linewidth=1)

    # Show the plot
    plt.show()
    print(polarity_scores)

# Enter video id
video_id = 'O0HCUfGsEK0'
# video_id = 'kBdlM6hNDAE'
max_comments = 100
video_comments(video_id, max_comments)
