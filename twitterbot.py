import sys
from twython import Twython
import json

# Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
APP_KEY = 'KSLEypBfhqfLMdNkfKb3moxus'
APP_SECRET = '04ptUYdtLFWqBGvi1efVsnaBA0g3SMItHVwOJX7XfdgKSNAX10'
OAUTH_TOKEN = '1456353831978102791-isd43oqV6N0mklJVFIFFd9T8VbA7ug'
OAUTH_TOKEN_SECRET = 'KmfKPXl12nR0kdPjpwbU3vgdmRydRJZ4wJbePczTAlYGR'


# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
#api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# Using our newly created object, utilize the update_status to send in the text passed in through CMD
#api.update_status(status='Hello World!')


#########################################


# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#res = twitter.verify_credentials()
#print(json.dumps(res, indent=4, default=str))

twitter.update_status(status='Hello World!')

photo = open('flurby-transparent.png', 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status='Check out this cool image!', media_ids=[response['media_id']])

#video = open('video.mp4', 'rb')
#response = twitter.upload_video(media=video, media_type='video/mp4')
#print(response)
#twitter.update_status(status='Check out this cool video!', media_ids=[response['media_id']])
#print("done")
