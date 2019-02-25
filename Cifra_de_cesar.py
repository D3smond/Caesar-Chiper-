#-*- coding: utf-8 -*-
import os

alfabeto = "abcdefghijklmnopqrstuvwxyz"
ROT_lista = list(range(-1, 27))


def banner():
	print("""


 $$$$$$\                                                           $$$$$$\  $$\           $$\                                 
$$  __$$\                                                         $$  __$$\ \__|          $$ |                                
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\        $$ /  \__|$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        
$$ |       \____$$\ $$  __$$\ $$  _____| \____$$\ $$  __$$\       $$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       
$$ |       $$$$$$$ |$$$$$$$$ |\$$$$$$\   $$$$$$$ |$$ |  \__|      $$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      
$$ |  $$\ $$  __$$ |$$   ____| \____$$\ $$  __$$ |$$ |            $$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |            
\$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |            \$$$$$$  |$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |            
 \______/  \_______| \_______|\_______/  \_______|\__|             \______/ \__|$$  ____/ \__|  \__| \_______|\__|            
                                                                                $$ |                                          
                                                                                $$ |                                          
                                                                                \__|                                          
    [+] Script em python para decifrar e fazer cifra de césar.
    [+] Data: 24/02/2019
    [+] Telegram: @desmondelite                                                                           	

		""")

def cifrar(texto, rot):
	#print(texto)
	t = ""
	for let in texto:
		if let in alfabeto:
			let_index = alfabeto.index(let)
		
			t += alfabeto[(let_index + ROT_lista[rot]) % len(alfabeto)]
		else:
			t += let	
	print(t)

def decifrar(texto, rot):
	#print(texto)
	t = ""
	for let in texto:
		if let in alfabeto:
			let_index = alfabeto.index(let)
		
			t += alfabeto[(let_index - ROT_lista[rot]) % len(alfabeto)]
		else:
			t += let	
	print(t)

def main():
	banner()
	escolha = input(str("---> [1] Cifrar [2] Decifrar: "))
	mensagem = input(str("[+] Coloque aqui o texto: "))

	if escolha == "1":
		mensagem = mensagem.lower()
		rot_i = input("[+] Em qual escala deseja cifrar: ")
		cifrar(mensagem, ROT_lista[int(rot_i)])

	elif escolha == "2":
		mensagem = mensagem.lower()
		for num in ROT_lista:
			decifrar(mensagem, ROT_lista[num])

	else:
		print("[-] O comando não foi reconhecido: ")		

if __name__ == "__main__":
	try:
		os.system("cls")
		main()
	except:
		print("\n[-] Ocorreu um erro ou você saiu do script! ")	