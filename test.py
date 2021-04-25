# from mutagen.easyid3 import EasyID3
# import eyed3 

# file=eyed3.load("Taylor Swift  I Knew You Were Trouble.mp3")  #image load
# file.initTag()  #  initialize tags
# file.tag.images.set(3,open("i knew trouble photo.jpg","rb").read(),"image/jpeg")  #changing image
# file.tag.save(version=eyed3.id3.ID3_V2_3) #encoding image

# audio=EasyID3("songs\\Come On Boy Move That Body_320(PaglaSongs).mp3")     #easyid3 used to change mp3 file details
# audio["title"]="Safari"
# audio["artist"]="Serena"
# audio.save()