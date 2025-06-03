# ''' 
# Para ler e escrever dados em Python, utilizamos as seguintes funções: 
# - input: lê UMA linha com dado(s) de Entrada do usuário;
# - print: imprime um texto de Saída (Output), pulando linha.  
# '''

# def filtrar_transacoes(transacoes, limite):
#     transacoes_filtradas = [valor for valor in transacoes if valor > limite ]
#     return transacoes_filtradas


# entrada = input()

# entrada_transacoes, limite = entrada.split("],")
# entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
# limite = float(limite.strip())  # Converte o limite para float


# transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# resultado = filtrar_transacoes(transacoes, limite)


# print(f"Transações: {resultado}")


class pessoas: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"{self.nome} tem {self.idade}"
    
    def exibir(self):
        print(f"{self.nome} tem {self.idade}")
    
    def config(self):
        print(f"classe: {self.__class__.__name__}")
    

p1 = pessoas("kalebe", 19)

print(p1)
p1.exibir()
p1.config()