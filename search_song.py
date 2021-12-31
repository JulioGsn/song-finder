import unicodedata

def remove_non_ascii_normalized(string):
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()


def clear(string):
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

def countChar(search_word, compared_word):
    count = 0
    if compared_word == 'feat':
        count -= 5
    if search_word == 'feat':
        count += 5
    #print(search_word + ' ' + compared_word)
    size = min(len(search_word), len(compared_word))
    for index in range(size):
        if search_word[index] == compared_word[index]:
            count += 1
    if count == size:
        #match whole word
        count += 10
    return count

def score(sound, input_words):
    sound_words = sound.split()
    letter_counter = 0
    for word in input_words:
        for w_sound in sound_words:
            letter_counter += countChar(clear(word), clear(w_sound))
    return letter_counter
#############################################################
input_line = "Havana"
input_words = input_line.split()

songs = {}
with open('songs.txt') as song:
    for l in song.readlines():
        sound = l.replace('\n', '')
        songs[sound] = score(sound, input_words)
print(songs)
