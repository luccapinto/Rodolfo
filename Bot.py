import discord
import time
import requests
import json
import random

client = discord.Client()
token = 'OTgyNjU0NjQzMTIzMzk2NjE5.GnbBXD.BXU68Xq93xgOxjpAZzTTXLhFsbdUUntK6TCn8o'
sabor = ['Calabresa','Mussarela','4 queijos','Figado','Vegetariana','Banana','Atum','Brigadeiro','Rucula','Peixe','Sem sabor','Abobrinha','Cimento']
preco = ['R$42','R$34','R$36','R$18','R$35','R$30','R$45','R$36','R$34','R$40','R$60','R$37','R$87']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$help'):
        await message.channel.send('>>> Bem vindo a Pizzaria Rodolfo!\n\
Voce pode interagir com nosso bot para fazer seu pedido.\n\
Digite:\n\
**$sabores:**\n\
		*opcoes de pizzas*\n\
**$entrega:** \n\
		*opcoes de entrega*\n\
**$pagamento:** \n\
		*opcoes de pagamento*\n\
**$tempo:**\n\
		*estima o tempo de entrega*\n\
**$observacao:**\n\
    *escreva preferencias ou pedidos adicionais. Ex: sem cebola*\n\
**$escolher: <sabor>** \n\
		*decidir qual pizza deseja*\n\
**$funcionamento:**\n\
    *mostra o horario de funcionamento do estabelecimento*')

    if message.content.startswith('$sabores'):
      for n in sabor:
        await message.channel.send(n)
        time.sleep(1)

    if message.content.startswith('$preco'):
      for n in preco:
        await message.channel.send(n)
        time.sleep(1)

    if message.content.startswith('$funcionamento'):
       await message.channel.send('Funcoes muito complexas ainda nao foram implementadas.')  
      
    if message.content.startswith('$escolher'):
      quote = message.content
      asabor = random.choice(sabor)
      apreco = random.choice(preco)
      await message.channel.send('Ah nao! Esse sabor e uma bosta. Deixa que eu escolho por voce')
      time.sleep(1)
      await message.channel.send(f'Sua pizza vai ser de {asabor} e vai custar {apreco}')
      time.sleep(10)
      await message.channel.send('TA ESPERANDO O QUE? ESCOLHA O METODO DE PAGAMENTO')

    if message.content.startswith('$pagamento'):
      await message.channel.send('1 - Dinheiro\n2 - Cartao de credito\n3 - Cartao de debito\n4 - Boleto\n5 - Cheque\n6 -  ( ͡° ͜ʖ ͡°)card')
      msg = await client.wait_for("message")
      await message.channel.send('Desculpe, essa opcao esta indisponivel. Voce vai pagar no cheque.')

    if message.content.startswith('$observacao'):
      await message.channel.send('Qual a sua observacao?')
      msg = await client.wait_for("message")
      await message.channel.send('Deixa de frescura! Come do jeito que ela e feita!')
      
    if message.content.startswith('$tempo'):
      contador = 10000
      while (contador > 9991):
        await message.channel.send(f'sua pizza chegara em {contador} segundos')
        time.sleep(1)
        contador -= 1
        if contador == 9997:
          await message.channel.send('**vish...**')
        if contador == 9993:
          await message.channel.send('**pessima noticia**')
        if contador == 9991:
          await message.channel.send('**o motoboy caiu, nao sei mais quanto tempo vai demorar**')
  
        
    if message.content.startswith('$entrega'):
      await message.channel.send('Opcoes de entrega:')
      await message.channel.send('1- Motoboy')
      msg = await client.wait_for("message")
      await message.channel.send('Sua pizza sera entregue pela opcao: "Motoboy"')      
      
client.run(token)
