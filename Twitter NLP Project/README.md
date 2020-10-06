# Twitter NLP Demo
This demo performs sentiment analysis on a set of tweets specified by a hashtag based on user input. The sentiment analysis is done via Google Cloud natural language API.
The tweets are scraped via tweepy python package.
## Files:
**(1) twitter_api_demo2_without_keys.ipynb**\
Consists of a series of methods demonstrating the functionality of the twitter api. Also performs the tweet scraping method. The tweepy package is used to interface with the api.\
To use this file, install tweepy, pandas, and numpy.\
You will also need to create a developer account with twitter, and enter your secret keys and tokens in the first 4 lines of the demo file.\
You will also need to specify a directory on your local machine to write the results of the tweet API call.\
Specify your desired hashtag below the search function of the pull-methods.\
\
**(2) sentiment_analysis.py**\
Consists of a sentiment analysis method which applies the google cloud NLP api to a text file filled with tweets from a requested hashtag. Outputs a sentiment score from -1 to 1, 1 being the most positive sentiment and -1 being the most negative sentiment.\
You will need to go through the Google Cloud installation process to procure the proper keys, accounts, and packages: https://cloud.google.com/natural-language


## Workflow
Run twitter_api_demo2_without_keys.ipynb to scrape the desired tweets.\
Run the sentiment_analysis.py script:\
`python sentiment_analysis.py hashtag.txt`\
\
Results output to the shell are similar to the following (depending on your desired hashtag):\
\
`Sentence 0 has a sentiment score of 0.0`\
`Sentence 1 has a sentiment score of -0.20000000298023224`\
`Sentence 2 has a sentiment score of 0.20000000298023224`\
`Sentence 3 has a sentiment score of 0.20000000298023224`\
`Sentence 4 has a sentiment score of 0.30000001192092896`\
`Sentence 5 has a sentiment score of 0.20000000298023224`\
`Sentence 6 has a sentiment score of -0.699999988079071`\
`Sentence 7 has a sentiment score of 0.0`\
`Sentence 8 has a sentiment score of -0.30000001192092896`\
`Sentence 9 has a sentiment score of 0.20000000298023224`\
`Sentence 10 has a sentiment score of 0.5`\
`Sentence 11 has a sentiment score of 0.0`\
`Sentence 12 has a sentiment score of -0.30000001192092896`\
`Sentence 13 has a sentiment score of 0.0`\
`Sentence 14 has a sentiment score of -0.6000000238418579`\
`Sentence 15 has a sentiment score of 0.8999999761581421`\
`Sentence 16 has a sentiment score of 0.5`\
`Sentence 17 has a sentiment score of -0.10000000149011612`\
`Sentence 18 has a sentiment score of 0.4000000059604645`\
`Sentence 19 has a sentiment score of 0.20000000298023224`\
`Overall Sentiment: score of 0.0 with magnitude of 6.5`

In twitter_api_demo2_without_keys.ipynb, use the `trends_closest(lat,long)` method to determine locations with trending hashtags and their WOEID. Use `trends_place(woe_id)` method to determine the hashtags trending at a location specified by its WOEID. Use the hashtags obtained via this method to perform sentiment analysis as desired.
## MVP
A sentiment analysis tool for trending twitter hashtags. Scalable to the API limits for tweet scraping. Modular, can apply any of the twitter methods in the demo script.
## User Stories
* As a trader, I want to base my next trade on the sentiment (bearish/bullish) of a trending hashtag.
* As an influencer, I want to base my next tweet on the average sentiment of a certain hashtag.
* As a real estate developer, I want to make my next purchase based on the sentiment of trending tweets in a certain location.
* As a campaign manager, I want to determine if my candidate is performing well. I want to determine if they are performing well or poorly in certain locations.
