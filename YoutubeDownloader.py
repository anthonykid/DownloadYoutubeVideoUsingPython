from pytube import YouTube

link = input("Enter Youtube Url : ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("Enter The Desired Format That You Want : ")
dn_option = int(input("Enter The Format : "))

dn_video = videos[dn_option]
dn_video.download()

print("You Have Downloaded It Successfully !")
