from turtle import title
import tweepy
import keys
import flux as f

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print("Ok")

def concat():
    message = f"š­ {f.getfeed()[0]} \nš {f.getfeed()[1]}\nš³ {f.getfeed()[2]} \nš {f.getfeed()[3]}\nš° {f.getfeed()[4]}"
    return message

if __name__ == "__main__":
    api = api()
    tweet(api, concat())