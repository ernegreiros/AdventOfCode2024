# --- Parte Dois ---
# Sua análise apenas confirmou o que todos temiam: as duas listas de IDs de localização são de fato muito diferentes.

# Ou não?

# Os historiadores não conseguem concordar sobre qual grupo cometeu os erros ou como ler a maior parte da caligrafia do chefe, mas na comoção você percebe um detalhe interessante: muitas IDs de localização aparecem em ambas as listas! Talvez os outros números não sejam IDs de localização, mas sim caligrafia mal interpretada.

# Desta vez, você precisará descobrir exatamente com que frequência cada número da lista da esquerda aparece na lista da direita. Calcule uma pontuação de similaridade total somando cada número na lista da esquerda após multiplicá-lo pelo número de vezes que esse número aparece na lista da direita.

# Aqui estão as mesmas listas de exemplos novamente:

# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# Para essas listas de exemplo, aqui está o processo para encontrar a pontuação de similaridade:

# O primeiro número na lista da esquerda é 3. Ele aparece na lista da direita três vezes, então a pontuação de similaridade aumenta em .3 * 3 = 9
# O segundo número na lista da esquerda é 4. Ele aparece na lista da direita uma vez, então a pontuação de similaridade aumenta em .4 * 1 = 4
# O terceiro número na lista da esquerda é 2. Ele não aparece na lista da direita, então a pontuação de similaridade não aumenta ( 2 * 0 = 0).
# O quarto número, 1, também não aparece na lista da direita.
# O quinto número, 3, aparece na lista da direita três vezes; a pontuação de similaridade aumenta em 9.
# O último número, 3, aparece na lista da direita três vezes; a pontuação de similaridade aumenta novamente em 9.
# Portanto, para essas listas de exemplo, a pontuação de similaridade no final desse processo é 31( 9 + 4 + 0 + 0 + 9 + 9).

# Mais uma vez, considere suas listas esquerda e direita. Qual é a pontuação de similaridade delas?


with open('input.txt', 'r') as file:
    distance_split = [line.strip().split(" ") for line in file]
    
    left = [int(distance[0]) for distance in distance_split]
    left.sort()
    right = [int(distance[-1]) for distance in distance_split]
    right.sort()

    sum = 0
    memo = {}
    for i in range(0,len(left)):       
        number = left[i]

        if number not in memo:
            memo[number] = right.count(number)

        sum += number * memo[number]

    print(sum)
