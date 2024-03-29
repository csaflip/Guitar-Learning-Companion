import re
import PySimpleGUI as sg
import random


#allmusic = {}
artistsongs = {} #list of all songs associated with each artist, is a map
#artists = [] #list of artists, no duplicates


def get_music():
    file = open('musiclist.txt', 'r')
    allmusic_str = file.read()
    file.close()
    allmusic = allmusic_str.split('\n')  # makes list of all songs with urls
    return allmusic


def get_sorted_artists(music_from_file):
    artists = []
    for music in music_from_file:
        a = re.search(r'\b(by )\b', music)
        artist = ''
        url = ''
        try:
            for x in range(a.end(), len(music)):
                if music[x] != '@':
                    artist = artist + music[x] #get name of artist
                else:
                    break
            artist = artist[:-1] #remove whitespace at the end of string.
            artistsongs[music] = artist
        except:
            artist = 'unassigned'
            artistsongs[music] = artist
        artists.append(artist)

    artists = sorted(artists)
    artists = list(set(artists)) #remove duplicates from list
    artists = sorted(artists) #resort after removing
    return artists



def get_artists_str(artists):
    artists_str = ''
    count = 0
    for artist in artists:
        if count == 6:
            artists_str = artists_str + ", " + artist + '\n'
            count = 0
        else:
            artists_str = artists_str + ", " + artist
            count = count+1
    return artists_str


def find_artist_songs(sg_user_input): #values[0] in pysimplegui
    user_input = sg_user_input
    if user_input == '': #if they dont enter anything, choose artist at random
        user_input = list_of_artists[random.randint(0, len(list_of_artists))]
    artists_songs_str = ''
    for name, artist in artistsongs.items(): #find songs from a certain artist
        if user_input == artist:
            artists_songs_str = artists_songs_str + name + '\n'
            #print(name) #print name
    return artists_songs_str


def find_alphabetical_artists(letter, artists):
    alphabetical_artists = ''
    for artist in artists:
        if artist[0] == letter:
            alphabetical_artists += artist + '\n'
    return alphabetical_artists


list_of_artists = get_artists_str(get_sorted_artists(get_music()))
array_of_artists = get_sorted_artists(get_music())


layout = [[sg.Text('Persistent window')],
          [sg.Button('A'), sg.Button('B'), sg.Button('C'),
           sg.Button('D'), sg.Button('E'),
           sg.Button('F'), sg.Button('G'),
           sg.Button('H'), sg.Button('I'),
           sg.Button('J'), sg.Button('K'),
           sg.Button('L'),
           sg.Button('M'), sg.Button('N'),
           sg.Button('O'), sg.Button('P'),
           sg.Button('Q'), sg.Button('R'),
           sg.Button('S'), sg.Button('T'),
           sg.Button('U'), sg.Button('V'),
           sg.Button('W'), sg.Button('X'),
           sg.Button('Y'), sg.Button('Z'),
           sg.Button('Next'), sg.Output(size=(30, 30), key='-OUTPUT-')]] #Scrollable output!
window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Next'):
        break
    if event:
        window['-OUTPUT-'].Update(find_alphabetical_artists(event[0], array_of_artists)) #list artists corresponding to button.
        #print(find_alphabetical_artists(event[0], array_of_artists))
    #sg.Popup(find_alphabetical_artists(event[0], array_of_artists)) #TODO consider this in revision.


window.Close()


layout = [[sg.Text('Enter in an artist from the list to search known songs.')],

          [sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.Read()
window.Close()

sg.Popup('Songs for: ' + values[0], find_artist_songs(values[0])) #put songs from artists to the screen

# layout = [
#           [sg.Text('This text is clickable', click_submits=True)],
#           [sg.Text('This text is clickable with a key', click_submits=True, key='Text Key')],
#           [sg.Text('This text is not clickable')],
#             [sg.Button('A')],
#           [sg.ReadButton('Button that does nothing')]
#          ]
#
# form = sg.FlexForm('Demo of clickable Text Elements').Layout(layout)
#
# while True:
#     button, values = form.Read()
#     if button is None: break
#     print(button, values)


