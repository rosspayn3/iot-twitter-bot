from twython import Twython
import config

APP_KEY = config.APP_KEY
APP_SECRET = config.APP_SECRET
OAUTH_TOKEN = config.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = config.OAUTH_TOKEN_SECRET

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#res = twitter.verify_credentials()
#print(json.dumps(res, indent=4, default=str))

twitter.update_status(status='Hello World!')

#photo = open('flurby-transparent.png', 'rb')
#response = twitter.upload_media(media=photo)
#twitter.update_status(status='Check out this cool image!', media_ids=[response['media_id']])

#video = open('video.mp4', 'rb')
#response = twitter.upload_video(media=video, media_type='video/mp4')
#print(response)
#twitter.update_status(status='Check out this cool video!', media_ids=[response['media_id']])
#print("done")
