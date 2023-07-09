'''
Insta data using python

#lets use insta loader to connect to insta
'''
import instaloader
a = instaloader.Instaloader()
print(a)
#a.download_profile('sridphotography')
a.download_profile('manjarithiru',profile_pic_only = True)
