import unicodedata

# CONSTANTS
RANKING_NUMBER=10

# Remover caracteres não ASCII
# ... e deixar em caixa baixa
# ... para que LanTerná seja igual a lanterna
def clear(string):
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

# Calcular quantidade de caracteres iguais entre as palavras
def countChars(searched_word, song_word):
    count = 0
    size = min(len(searched_word), len(song_word))
    for index in range(size):
        if searched_word[index] == song_word[index]:
            count += 1
    if searched_word == song_word:
        count += 10
    return count

# Calcular score para cada música no banco de músicas
def score(searched_words, song):
    song_words = song.split() # Transformar a música em array de palavras/termos
    letter_counter = 0
    has_feat_in_word = False
    has_feat_in_song = False

    for searched_word in searched_words:
        for song_word in song_words:
            # Se tem a palavra "feat" na música
            if clear(song_word) == 'feat':
                has_feat_in_song = True

            letter_counter += countChars(clear(searched_word), clear(song_word))

        # Se tem a palavra "feat" palavra buscada
        if clear(song_word) == 'feat':
            has_feat_in_word = True
            
    if has_feat_in_song and not has_feat_in_word:
        letter_counter -= 5

    return letter_counter
#############################################################

input_line = input("# Digite sua busca: ")
searched_words = input_line.split()

# Banco de músicas transferido para um arquivo de texto
# Cada música é uma linha nesse arquivo
songs = {}
filename = 'songs.txt'

# Calcular o score para cada linha/música no arquivo 'songs.txt'
with open(filename) as songs_file:
    for line in songs_file.readlines():
        song = line.replace('\n', '') # Retira \n (quebra de linha)
        songs[song] = score(searched_words, song)

# Ordenar os resultados por ordem alfabética
songs = sorted(songs.items(), key=lambda song: song[0])
# Ordernar os resultados por score
songs = sorted(songs, key=lambda song: song[1], reverse= True)

######## EXIBIR RESULTADOS
print("#")
print("# Resultados:")
for x in range(RANKING_NUMBER):
    print(f'# {songs[x][1]} pontos, {songs[x][0]}')
print("#")
print("--------------------------------------")
