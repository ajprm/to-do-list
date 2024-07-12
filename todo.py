from termcolor import colored
import colorama
lista = []
sair= False 
def apagarlista():
    deleta = input("Você tem certeza que quer deletar a lista?\n Digite sim ou não:  ")
    if deleta.lower() == "sim":
        del lista[:]

def strikethrough(text):
    return f"\033[9m{text}\033[0m"
def checar():
    entrada = input("\nDigite o número do item a ser checado: ")
    indice = int(entrada)
    if 0 <= indice < len(lista):
        lista[indice] = strikethrough(lista[indice])
    else:
        print("Índice inválido.")
def remover():
    entrada  = input("\n Digite o número do item a ser removido: ")
    menositem = int(entrada)
    del lista[menositem]
def adicionar():
    plusitem = input("\nDigite: ")
    if plusitem:
        a = input("\n[0] Confirma \n [1] Não confirma ")
        if a == "0":
            lista.append(plusitem)
        else: 
            main()

def envio_lista():
    if not lista:
        print("Oops, você ainda não adicionou nada na sua lista :( ")
    else:
        print("Itens: ")
        for item in lista:
            print(item)
def main():
   print(" **Sua Lista TO-DO**  \n") 
   envio_lista()

   print("\n [ 1 ] Adicionar item")
   print("\n [ 2 ] Remover item ")
   print("\n [ 3 ] Check Item")
   print("\n [ 4 ] Apagar Lista")
   print("\n [ 5 ] Sair")
while not sair:
    print("\n")
    main()
    escolha = input("\nDIGITE O NÚMERO DA SUA OPÇÃO: ")
    if escolha =="1":
        print("\n Add")
        adicionar()
    elif escolha == "2":
        print("\nRemove")
        remover()
    elif escolha == "3":
        print("\n Checar")
        checar()
    elif escolha == "4":
        apagarlista()
    elif escolha == "5":
        sair = True     
    else: 
        print("Opção Invalida. Tente again")

