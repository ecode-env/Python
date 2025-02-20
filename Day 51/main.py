from InternetSpeedTwitterBot import InternetSpeedTwitterBot
PROMISED_DOWN = 10
PROMISED_UP = 5
CHROME_DRIVER_PATH = ''
TWITTER_EMAIL = 'codetestenv@gmail.com'
TWITTER_PASSWORD = ""
INTERNET_PROVIDER = '@ethiotelecom'

bot = InternetSpeedTwitterBot()
download, upload = bot.get_internet_speed()
print(download, upload)


bot.tweet_at_provider(email=TWITTER_EMAIL,
                      password=TWITTER_PASSWORD,
                      internet_provider=INTERNET_PROVIDER,
                      down=PROMISED_DOWN,
                      up=PROMISED_UP)



