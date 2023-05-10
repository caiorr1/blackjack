import requests
import json

response_baralho = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')

baralho = response_baralho.json()
deck_id = baralho['deck_id']

jogadores = []
quantidade_jogadores = int(input('Digite a quantidade de jogadores: '))
i = 1
while i <= quantidade_jogadores:
    nome_jogador = input('\nDigite o nome do jogador: ')
    deck_jogador = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1')
    jogadores.append({
        'nome' : nome_jogador,
        'deck' : deck_jogador,
        'validacao' : True
    })
    i += 1 
print(jogadores)



     