## YouTube-Sentiment-Analyzer

**This Python script retrieves comments from a YouTube video and analyzes the sentiment polarity of the comments. It uses the Google API Client library and TextBlob for sentiment analysis**. 



## Prerequisites

- Python 3.x
- Required libraries: TextBlob, google-api-python-client, matplotlib

## Setup

1. Obtain an API key from the Google Developers Console.
2. Install the required libraries 

## Usage

1. Replace the `api_key` variable in the code with your own YouTube Data API key.
2. Set the `video_id` variable to the ID of the YouTube video you want to analyze.
3. Set the `max_comments` variable to the maximum number of comments you want to retrieve.
4. Run the script.

## Output

The script retrieves comments and their replies from the specified YouTube video. It saves the comments and replies in a text file named "comments.txt". It then calculates the sentiment polarity of the text using TextBlob and generates a histogram of the sentiment polarity distribution using matplotlib.

The histogram shows the count of comments in different sentiment polarity ranges (-1 to 1). Vertical lines are added to indicate the neutral (0), positive (0.5), and negative (-0.5) polarity thresholds.

## Example
![Sentiment Polarity Histogram](/output/img.png)
## Notes

- The YouTube Data API has usage limits, so be mindful of the number of requests you make.
- The sentiment polarity score ranges from -1 to 1, where values closer to -1 indicate negative sentiment and values closer to 1 indicate positive sentiment.
- This code can be modified to suit different analysis requirements or integrate with other applications.