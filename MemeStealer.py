try:
    import random
except:
    exit('install "random" library (pip install random)')
try:
    import urllib
except:
    exit('install "urllib" library (pip install urllib)')
try:
    import praw
except:
    exit('install "praw" library (pip install praw)')
try:
    from PIL import Image

except:
    exit('install "PIL" library (pip install PIL)')





reddit = praw.Reddit(client_id='Client ID',
                     client_secret="Client Secret",
                     password='Reddit Password',
                     user_agent='user agent',
                     username='Reddit Username')


def getimg(WatermarkName=None):
    MemNum=input("number of memes? ")
    Subreddit = "memes"
    X = reddit.subreddit(Subreddit).hot(limit=int(MemNum))
    for post in X:
        if str(post.url).endswith('.png') or str(post.url).endswith(".jpg") or str(post.url).endswith(".jpeg"):
            try:
                response = urllib.request.urlopen(post.url)
                PostName=str(random.randrange(0, 10000))
            except:
                print("breaking")
                break
            File = response.read()
            if str(post.url).endswith(".jpg"):
                with open(PostName+'.jpg', 'wb') as f:
                    f.write(File)
                    if WatermarkName!=None:
                        watermark(PostName+'.jpg',WatermarkName)
            elif str(post.url).endswith(".png"):
                with open(PostName+'.png', 'wb') as f:
                    f.write(File)
                    if WatermarkName!=None:
                        watermark(PostName+'.png',WatermarkName)
            else:
                with open(PostName+'.jpeg', 'wb') as f:
                    f.write(File)
                    if WatermarkName!=None:
                        watermark(PostName+'.jpeg',WatermarkName)

def watermark(FileName,WatermarkName):
    background = Image.open(FileName)
    img = Image.open(WatermarkName, 'r')

    img_w, img_h = img.size
    bg_w, bg_h = background.size
    
    new_height  = int(bg_h*15/100)
    new_width = int(new_height * img_w / img_h)

    img = img.resize((new_width, new_height), Image.ANTIALIAS)

    offset = (int(bg_w*77/100),int(bg_h*78/100))


    background.paste(img, offset)
    background.save(FileName)


if __name__ == '__main__':
    if input("want to add the watermark? (y/n): ")=="y":
        WatermarkName=input("watermark file's path: ")
        getimg(WatermarkName)
    else:
        getimg()