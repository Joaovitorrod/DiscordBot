import requests
import json
import random
import discord

from replit import db
from discord.ext import commands


bad_words = [
      "merda", "caralho", "porra", "filho da puta", "filha da puta", "cu",
      "desgraçado"
  ]

mensagemRepressora_starter = [
      "Olha a boca fiote", "Quem xingar muito vai tomar ban",
      "Sua mãe é tão gorda que quando ela deitou na praia, as pessoas correram pra volta dela gritando: FREEEE WILLYYYYYYYY",
      "A sua mãe é tão gorda que Deus não pôde colocar luz na Terra até ela se mexer!",
      "A sua mãe é tão gorda que ela fica em dois fusos horários!"
  ]

class messages(commands.Cog):
  def __init__(self, client):
    self.client = client

  def get_quote():
      response = requests.get("http://allugofrases.herokuapp.com/frases/random")
      json_data = json.loads(response.text)
      quote = json_data['frase'] + " - " + json_data['autor']
      return quote


  def update_mensagemRepressora(mensagem):
      if "mensagemRepressora" in db.keys():
          mensagemRepressora = db["mensagemRepressora"]
          mensagemRepressora.append(mensagem)
          db["mensagemRepressora"] = mensagemRepressora
      else:
          db["mensagemRepressora"] = [mensagem]


  def delete_mensagemRepressora(index):
      mensagemRepressora = db["mensagemRepressora"]
      if len(mensagemRepressora) > index:
          del mensagemRepressora[index]
          db["mensagemRepressora"] = mensagemRepressora

  def listar_mensagemRepressora():
    mensagemRepressora = db["mensagemRepressora"]
    return("As mensagens gravadas são:\n" + '\n'.join(mensagemRepressora))

  @commands.command(name="salve",help="Manda o salve pro pae",aliases=["oi", "olá", "ola", "hi"])
  async def salve(self, ctx: commands.Context):
    await ctx.reply('Salve carai')

  @commands.command(name="triste",help="Te ajudo com uma mensagem inspiradora",aliases=["bad", "depressivo", "depressiva", "chateado"])
  async def triste(self, ctx: commands.Context):
    quote = messages.get_quote()
    await ctx.reply(quote)

  @commands.command(name="gg",help="Avalio o game",aliases=["good game", "vitória", "vencemos", "win"])
  async def gg(self, ctx: commands.Context):
    await ctx.reply('Parabéns pelo game. Você parecia um Yasuo do meu time (ou não).')     

  @commands.command(name="goularte",help="Informações privilegiadas sobre o usuário Goularte",aliases=["gougou", "gou", "gui"])
  async def goularte(self, ctx: commands.Context):
    await ctx.reply('Até então essas são as informações sobre o usuário:')   
    embedvc = discord.Embed(
      colour= 1646116,#grey
      description = '17 Anos\nYasuo que não devia estar no prata\nTop #1 Jequiti Seller Awards 2020\nTem skin do Fortnite\nSente falta da morena (que é loira) diariamente\nVulgo: OCaraDoPao; GOLART AK TROVÃO'
    )
    await ctx.send(embed=embedvc)    

  @commands.command(name="guga",help="Informações privilegiadas sobre o usuário Guga ",aliases=["gustavo", "gustavol", "gugu"])
  async def guga(self, ctx: commands.Context):
    await ctx.reply('Até então essas são as informações sobre o usuário:')   
    embedvc = discord.Embed(
      colour= 1646116,#grey
      description = '24 years\nMorou na gringa\nTop #2 Avon Seller Awards 2016\nDentista de morena\nCerveja: Lokal\nResenhador\nVulgo: Guslac; Klebin da 300'
    )
    await ctx.send(embed=embedvc)  
     

def setup(client):
    client.add_cog(messages(client))