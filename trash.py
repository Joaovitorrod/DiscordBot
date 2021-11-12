
          ################### Inicio Responder ###################

      if msg.startswith('$add'):
          mensagemRepressora = msg.split("$add ", 1)[1]
          update_mensagemRepressora(mensagemRepressora)
          await message.channel.send(
              "Mensagem adicionada. Você contribuiu para repreender alguém.")

      if msg.startswith('$del'):
          mensagemRepressora = []
          if "mensagemRepressora" in db.keys():
              index = int(msg.split("$del", 1)[1])
              delete_mensagemRepressora(index)
              mensagemRepressora = db["mensagemRepressora"]
              await message.channel.send(listar_mensagemRepressora())

              
      ## REFERENCIAS DE BAD WORDS //  XINGAMENTOS
      if msg.startswith('$mensagensmotivacionais'):
          mensagemRepressora = []
          if "mensagemRepressora" in db.keys():
              mensagemRepressora = db["mensagemRepressora"]
              await message.channel.send(listar_mensagemRepressora())


      options = mensagemRepressora_starter
      if "mensagemRepressora" in db.keys():
        options = options + db["mensagemRepressora"].value

      if db["respostas"]:
        if any(word in msg for word in bad_words):
            await message.channel.send(random.choice(options))

      if msg.startswith('$respostas'):
        try:
          value = msg.split("$respostas ",1)[1]
          if value.lower() == "true":
            db["respostas"] = True
            await message.channel.send("Respostas automáticas habilitadas")
          else:
            db["respostas"] = False
            await message.channel.send("Respostas automáticas desabilitadas")
        except:
          await message.channel.send("Você deve utilizar \"true\" ou \"false\" após o comando.")
          #################### Fim Responder ####################

      if msg.startswith('guapinho'):
          await message.channel.send(
              'Passei só pra dizer que um dia o Guapinho acaba a facul, fé.')

      if msg.startswith('goularte'):
          await message.channel.send(
              'Passei só pra dizer que um dia o Goularte acaba o ensino médio, fé.'
          )