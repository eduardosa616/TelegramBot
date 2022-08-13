import telebot

CHAVE_API = "5354355578:AAHDOAM2aYXaNvoqvJYKUwRHTh1XZqGBYYo"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["animes"])
def op1(mensagem):
    bot.send_message(mensagem.chat.id, """Recomendações:
    Para assistir Naruto, clique no link: https://animesonline.cc/anime/naruto/
    Para assistir One Piece, clique no link: https://animesonline.cc/anime/one-piece/
    Para assistir Dragon Ball Z, clique no link: https://animesonline.cc/anime/dragon-ball/
Caso queira selecionar outra opção, clique aqui: /iniciar
    """)

@bot.message_handler(commands=["filmes"])
def op2(mensagem):
    bot.send_message(mensagem.chat.id, """Recomendações:
    Para assistir The Batman, clique no link: https://www4.playseries.club/batman/
    Para assistir Vingadores: Ultimato, clique no link: https://www4.playseries.club/vingadores-ultimato/ 
    Para assistir Homem-Aranha: Sem Volta Para Casa, clique no link: https://www4.playseries.club/homem-aranha-sem-volta-para-casa/
Caso queira selecionar outra opção, clique aqui: /iniciar
    """)

@bot.message_handler(commands=["series"])
def op3(mensagem):
    bot.send_message(mensagem.chat.id, """Recomendações:
    Para assistir Game of Thrones, clique no link: https://www4.playseries.club/game-of-thrones/
    Para assistir Lúcifer, clique no link: https://www4.playseries.club/lucifer/
    Para assistir Peaky Blinders, clique no link: https://www4.playseries.club/peaky-blinders-sangue-apostas-e-navalhas/
Caso queira selecionar outra opção, clique aqui: /iniciar
    """)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para conseguir links de recomendação de:
    Animes: Clique aqui /animes
    Filmes: Clique aqui /filmes
    Séries: Clique aqui /series
Outras opções não funcionarão, favor escolher entre as que estão listadas acima.
    """
    bot.reply_to(mensagem, texto)

bot.polling()