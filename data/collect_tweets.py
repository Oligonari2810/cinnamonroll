import tweepy
import pandas as pd

# Reemplaza con tus credenciales de Twitter
API_KEY = 'TU_API_KEY'
API_SECRET = 'TU_API_SECRET'
ACCESS_TOKEN = 'TU_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'TU_ACCESS_TOKEN_SECRET'

# Autenticación en Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define palabras clave para la búsqueda
keywords = ["cinnamon roll", "rollos de canela", "donuts", "dulces"]
tweets_data = []

# Recolecta tweets para cada palabra clave
for keyword in keywords:
    for tweet in tweepy.Cursor(api.search_tweets,
                               q=keyword,
                               lang="es",
                               tweet_mode="extended").items(100):
        tweets_data.append({
            "usuario": tweet.user.screen_name,
            "texto": tweet.full_text,
            "fecha": tweet.created_at
        })

# Convierte los datos a un DataFrame y guarda en CSV
df = pd.DataFrame(tweets_data)
df.to_csv("tweets_cinnamon.csv", index=False)
print("Datos guardados en tweets_cinnamon.csv")
