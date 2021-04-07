'''This code is for the demo shown in 'Introduction to Git, GitHub and GitHub API' 
   hosted by Anubhav Madhav and Toshi Mudgal, 
   Microsoft Learn Student Ambassadors.'''

import requests             # run 'pip install requests' command to install 'requests' before running the code

username = 'AnubhavMadhav'      # You can enter any GitHub username

url = f'https://api.github.com/users/{username}'
url2 = url + '/orgs'

r = requests.get(url.format(username)).json()       # returns details of the user in json format
r2 = requests.get(url2.format(username)).json()     # returns details of the user's organisations in json format

print(r)

if r['name'] is not None:
    first_name = r['name'].strip().split(' ')[0]
    print("Hello", first_name)
else:
    print("Hello",r['login'])

print("Followers :", r['followers'])
print("Repositories (public) :", r['public_repos'])
print("No. of Organizations joined :", len(r2))
print("Profile Picture URL :", r['avatar_url'] + '.png')
print("full name :", r['name'])

if r['login'] == 'AnubhavMadhav':           # You can code any such thing further of your wish
    print("THOR")