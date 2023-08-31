from classes import *
import os


def main():
    desctarefa1 = IrAoMercado('Para esta tarefa você vai precisar ir ao mercado fazer as compras.')
    desctarefa2 = PassearCmCachorro('Para esta tarefa você vai precisar ir passear com o seu cachorro.')
    desctarefa3 = EstudarPrProva('Para esta tarefa você vai precisar Estuda o conteudo para a sua prova de amanhã.')
    
sair = False
while sair == False:
    try:

        os.system('cls')
        print('Bem vindo ao ajudante pessoal de tarefas! \nSelecione a opção de Listar tarefas para iniciar \n1 - Listar Tarefas\n2 - Sair')
            
        menu = int(input('Selecione a opção >> '))
        os.system('pause')

        match menu:

            case 1:
                os.system('cls')
                print('Essas são suas tarefas >\n1° Ir ao mercado \n2° Passear com o cachorro \n3° Estudar para a prova')

                opcoes = int(input('Selecione qual tarefa realizar >> '))
                os.system('pause')

            case 0:
                print('saindo...')
                sair = True
                
            case _:
                print('Valor invalido!')

    except Exception as erro:
        print('Valor invalido!')
        print(erro.__class__.__name__)
        print('')
