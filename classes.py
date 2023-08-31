class ToDoList:
    def __init__(self):
        self.listatrf = {}

    def adicionar_tarefa(self, desc, tarefas):
        self.desc = desc
        self.tarefas = tarefas

        match tarefas:

            case 1:
                x = 'Ir ao mercado'

            case 2:
                x = 'Passear com o cachorro'

            case 3:
                x = 'Estudar para a prova'

            case _:
                x = None

        self.tarefas[self.desc] = x


    def excluir_tarefa(self, tarefas):
        if tarefas in self.listatrf:
            del self.listatrf[self.desc]
        else: 
            print('Tarefa não incontrada')

    def listar_tarefa(self):
        for chave,valor in self.listatrf.items():
            print(f'Tarefa: {chave}, Descrição:{valor}')

class IrAoMercado:
    pass

class PassearCmCachorro:
    pass

class EstudarPrProva:
    pass