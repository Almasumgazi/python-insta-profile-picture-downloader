import instaloader

bot=instaloader.Instaloader()
username='it_s_ur_bunny'
print(bot.download_profile(username,profile_pic_only=True))