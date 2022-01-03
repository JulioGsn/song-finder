# Song-finder
Programa que rebebe um termo como entrada e busca por ele numa lista de músicas. As músicas recebem uma pontuação de acordo com algumas regras pré-estabelecidas
e no final é exibido um ranking com as 10 mais bem pontuadas.

### RUN
Primeiro, clone o repositório ou faça o download do código fonte.
Para executar o programa, é necessário ter Python instalado na sua máquina.
Esse projeto foi desenvolvido utilizando Python na versão 3.8.10. Deve funcionar em versões >= 3.0

No linux,
```
python3 search_song.py
```

## Como funciona?
Obs: No reposítório, o arquivo [songs.txt](https://github.com/JulioGsn/song-finder/edit/main/songs.txt) representa nosso banco de músicas, onde cada linha é uma canção. Assim é mais fácil adicionar ou retirar músicas desse arquivo. Uma possível melhora é utilizar o formato .json para conectar a alguma API.

Ao executar o programa, é pedido ao usuário que "# Digite sua busca: ". 
O programa então lê cada linha do arquivo "songs.txt" e cria um dicionário (uma estrutura de dados semelhante às hash tables, na linguagem Python) sendo a chave o nome da música,
e o valor sendo o score daquela música, que inicia zerado.
``` 
songs = {'musica 1': 0, 'musica 2': 0, ...} 
```
Para cada pontuação das músicas nesse dicionário, é invocada a função *score*, que recebe como parâmetro, respectivamente, as palavras pesquisadas (array searched_words)
e uma música da lista de músicas.
```
songs[song] = score(searched_words, song)
```
A função *score* é bem interessante. Para fazer a comparação entre as palavras pesquisadas e as palavras da música, foi utilizado arrays, uma estrutura de dados clássica
onde cada posição pode ser acessada por índices, iniciando com índice 0.
Como cada palavra é separada por um ou mais espaços, a função *split()* do python retorna essas palavras como valores de um array, podendo ser acessadas por índices.
Logo, a música "All Of Me" ficaria ``` ['All', 'Of', 'Me'] ```

Além disso, para poder comparar as músicas, foi preciso fazer uma "limpeza" tanto nas palavras pesquisadas, quanto nas músicas para que não houvesse dificuldade
ao calcular a pontuação. A palavra "Olá" deveria casar perfeitamente com a palavra "ola", sem acento e em caixa baixa (minúsculas). Para isso, a função **clear**
é chamada passando como parâmetro a palavra e tendo como retorno a mesma palavra normalizada, removendo caracteres especiais e deixando tudo em caixa baixa
para facilitar. A biblioteca *unicodedata* do python ajudou nessa tarefa.

### A busca

Para cada palavra pesquisada, é feita a comparação com cada palavra de cada música da lista de músicas. Por exemplo, se a palavra pesquisada for "Of",
será comparado da seguinte forma:
```
Of  Of Of
All Of Me
```
Para fazer a contagem de acordo com as regras, é chamada a função *countChars*, responsável por contar quando uma letra da palavra pesquisada for igual
a letra de um termo da música, na mesma posição. Essa função recebe, respectivamente, um termo pesquisado e um termo de uma música da lista.

Quando uma letra da palavra pesquisada for igual, na mesma posição, à uma letra da palavra da música, é somado mais 1 ao contador.
Caso as palavras sejam exatamente iguais, é somado mais 10. Se houver a presença da palavra 'feat' na música, é descontado -5 do contador, 
a menos que essa palavra também apareça entre os termos pesquisados. No final, é retornado um score total para a música, e assim em diante para cada música da lista.

Antes de exibir os resultados, foi preciso ordenar para que fosse possível mostrar um ranking com as 10 músicas em ordem decrescente de seus scores. 
Primeiro, foi utilizado a função *sorted*, passando como parâmetro a lista de músicas armazenadas no dicionário com suas pontuações já calculadas.
Músicas com a mesma pontuação, deveriam ser exibidas em
ordem alfabética, como foi orientado pelo problema. Logo, a função *sorted* foi chamada duas vezes, primeiro para ordenar alfabeticamente e depois de acordo com o score de cada música.

### Resultados
Por fim, o usuário se depara com a exibição dos resultados referentes à sua busca.

![alt text](https://github.com/JulioGsn/song-finder/blob/main/song-finder.png)
