import unicodedata

def remove_non_ascii_normalized(string):
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()


def clear(string):
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

def countChar(search_word, compared_word):
    count = 0
    #print(search_word + ' ' + compared_word)
    size = min(len(search_word), len(compared_word))
    for index in range(size):
        if search_word[index] == compared_word[index]:
            count += 1
    if search_word == compared_word:
        #match whole word
        count += 10
    return count

def score(sound, input_words):
    sound_words = sound.split()
    letter_counter = 0
    has_feat_in_word = False
    has_feat_in_song = False
    for word in input_words:
        for w_sound in sound_words:
            if clear(w_sound) == 'feat':
                has_feat_in_song = True
            letter_counter += countChar(clear(word), clear(w_sound))
        if clear(word) == 'feat':
            has_feat_in_word = True
            
    if has_feat_in_song and not has_feat_in_word:
        letter_counter -= 5

    return letter_counter
#############################################################
input_line = input("# Digite sua busca: ")
#input_line = "Havana"
input_words = input_line.split()

songs = {}
filename = 'songs.txt'
with open(filename) as song:
    for l in song.readlines():
        sound = l.replace('\n', '')
        songs[sound] = score(sound, input_words)
songs = sorted(songs.items(), key=lambda song: song[0])
songs = sorted(songs, key=lambda song: song[1], reverse= True)

######## Print method
print("#")
print("# Resultados:")
RANKING_NUMBER=10
for x in range(RANKING_NUMBER):
    print(f'# {songs[x][1]} pontos, {songs[x][0]}')
