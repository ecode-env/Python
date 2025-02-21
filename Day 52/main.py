from InstaFollower import InstaFollower

PASSWORD = ''
EMAIL = 'eyobbmulugeta@gmail.com'

bot = InstaFollower()
bot.login(EMAIL, PASSWORD)
bot.find_followers()
bot.follow()



