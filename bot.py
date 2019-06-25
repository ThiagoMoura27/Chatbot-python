# -*- coding: utf-8 -*-
#teste de chatbot  --Jarvis -- 
#teste 1 usando a biblioteca aiml.py - 25/06/2019

import telepot #classe para faser conexao com telegram 
import aiml  #classe que faz nosso bot conversar
import os
import sys

kernel = aiml.Kernel() #inicializa o bot
kernel.learn("simple.aiml") # Abre o arquivo principal da AIML (que faz referências aos outros).


#token do telegram fornecido pelo botfather
telegram = telepot.Bot('Token do Chatbot Telegram') 

#funcao utilizada para receber menssagens 
def recebendoMSg(msg):
	fala = (msg['text'])
	#imprime na tela o que o usuario digitou no bot telegram
	print(fala)
	resp = kernel.respond(fala)	
	tipoMsg, tipoChat, chatID = telepot.glance(msg)
	#enviar a resposta do bot para telegram
	mensagem = telegram.sendMessage(chatID, resp)	
	#imprime a resposta na tela 
	print(resp)
		
telegram.message_loop(recebendoMSg)

while True:
	pass
