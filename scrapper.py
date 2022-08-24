import praw
import csv
import re 
from collections import defaultdict

limit = 100
sort = 'hot'
subReddit = input('Which subreddit do you want to query? ') 

#praw identification codes 
def redditInfo(): 
    id = 'KyC8jQ01AU3dyM0EPra2Ow'
    secret = 'y6fzcvbxcJ-ZZ3ut9n2UDBTgMAsu-A'
    name = 'scrap'
    reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent = name)
    return reddit

def titleWriter(freq_title): 
    with open('title_frequency.csv', 'w', newline = '') as file: 
        writer = csv.writer(file) 
        writer.writerow(["Word", "Frequency"])
        for w in sorted(freq_title, key = freq_title.get, reverse=True):
            writer.writerow([w, freq_title[w]])

def generalInformationWritter(descriptions):
    with open('information.csv', 'w', newline = '') as file:
        writer = csv.writer(file) 
        writer.writerow(["Title", "Score", "ID", "Subreddit", "URL", "comments", "created"])
        for description in descriptions: 
            writer.writerow(description)

def main(): 
    try:
        reddit = redditInfo()
        posts = reddit.subreddit(subReddit).hot(limit = limit)
        freq_title = defaultdict(int)
        descriptions = []
        for post in posts: 
            descriptions.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.created])
            title = post.title
            title = re.sub(r'[^\w\s]', '', title).lower().split()
            for word in title: 
                freq_title[word] += 1
        titleWriter(freq_title) 
        generalInformationWritter(descriptions) 
    except:
        print('Not a subreddit :/') 

if __name__ == "__main__":
    main() 