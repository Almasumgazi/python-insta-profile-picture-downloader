import instaloader

username=input("Enter the insta username :   ")

bot=instaloader.Instaloader()
print(bot.download_profile(username,profile_pic_only=True))