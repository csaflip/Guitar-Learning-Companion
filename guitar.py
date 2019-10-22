import re

#
# file = open('Bookmarks', 'r')
# #print(shit)
# #print(file.read())
# names = []
# urls = []
# donothing = ''
# for x in range(0,187959):
#     shits = file.readline(x)
#     try:
#         a = re.search(r'\b(name)\b', shits)
#         string = ''
#         for x in range(a.end()+4, len(shits)):
#             if shits[x] == "\"":
#                 break
#             string = string + shits[x]
#
#         if string.find('music') == -1:
#             names.append(string)
#         else:
#             continue
#             #print(string)
#     except:
#         donothing = ''
#     try:
#         a = re.search(r'\b(url)\b', shits)
#         url = ''
#         for x in range(a.end() + 4, len(shits)):
#             if shits[x] == "\"":
#                 break
#             url = url + shits[x]
#         if url == "":
#             continue
#         else:
#             #print(url)
#             urls.append(url)
#     except:
#         continue
#
# file.close()
# file = open('names.txt', 'a')
# for name in names:
#     file.write(name + "\n")
# file.close()
# file = open('urls.txt', 'a')
# for url in urls:
#     file.write(url + "\n")
# file.close()

file = open('names.txt', 'r')
names = file.read()
names = names.split('\n')
file.close()
file = open('urls.txt', 'r')
urls = file.read()
urls = urls.split('\n')
file.close()
print(len(names))
print(len(urls))


for x in range(0, len(names)):
    names[x] = names[x] + ' '+ urls[x]

sorted_names = sorted(names)
# file = open('names_sorted.txt', 'w')
# for name in sorted_names:
#     file.write(name + '\n')
# file.close()
# print(sorted(names))
artistsongs = {}
artists = []
for name in names:
    a = re.search(r'\b(by )\b', name)
    artist = ''
    url = ''
    try:
        for x in range(a.end(), len(name)):
            if name[x] != '@':
                artist = artist + name[x]
                #mylist = list(artist)
                #artist = mylist[:-1]
            else:
                break
        artist = artist[:-1]
        artistsongs[name] = artist
    except:
        artist = 'unassigned'
        artistsongs[name] = artist
    artists.append(artist)

# file = open('artists', 'r')
#print(artistsongs)
artists = sorted(artists)
artists = list(set(artists)) #remove duplicates from list
artists = sorted(artists) #resort after removing

for name, artist in artistsongs.items(): #find songs from a certain artist
    if 'Johnny Cash' == artist:
        print('') #print name

for x in range(0, len(artists)):
    for name, artist in artistsongs.items():
        if artists[x] == artist:
            print('') #print name

file = open('musiclist.txt', 'r')
allmusic = file.read()
allmusic = allmusic.split('\n')
print(allmusic)
file.close()






# for name, artist in artistsongs.items():
#     for x in range(0, len(artists)):
#         if artists[x] == artist:
#             print(name)

# file = open('artists.txt', 'a')
# for artist in artists:
#     file.write(artist + '\n')
# file.close()
#print(artists)
#print(len(artists))
#print(sorted(artists))
# musicdict = {}
# for x in range(0, len(artists)):
#     musicdict[artists[x]] = (names[x], urls[x])

#file = open('musiclist.txt', 'a')

#for key in sorted(musicdict):
    #print ("%s: %s" % (key, musicdict[key]))
# for x in musicdict:
#     print(musicdict[x])
# for x in musicdict:
#     print(x)
