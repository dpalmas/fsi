class Estado:
  def __init__(self):
    self.tabuleiro = [
      ["-", "-", "-"],
      ["-", "-", "-"],
      ["-", "-", "-"]
    ]
    self.vez = "X"

  def mostra(self):
    for linha in self.tabuleiro:
      for posicao in linha:
        print(posicao, " ", sep="", end="")
      print()

class Acao:
  def __init__(self, linha, coluna, letra):
    self.linha = linha
    self.coluna = coluna
    self.letra = letra

  def mostra(self):
    print(f"estou jogando na linha {self.linha}, coluna {self.coluna} a letra {self.letra}")

def conjunto_acoes(estado):
  acoes = []
  for i in range(len(estado.tabuleiro)):
    for j in range(len(estado.tabuleiro[i])):
      if estado.tabuleiro[i][j] != "-":
        continue
      acao = Acao(i, j, estado.vez)
      acoes.append(acao)
  return acoes

def modelo_transicao(estado, acao):
  estado_novo = Estado()
  for i in range(len(estado.tabuleiro)):
    for j in range(len(estado.tabuleiro[0])):
      estado_novo.tabuleiro[i][j] = estado.tabuleiro[i][j]
  estado_novo.tabuleiro[acao.linha][acao.coluna] = acao.letra
  estado_novo.vez = "X" if acao.letra == "O" else "O"
  return estado_novo

def profundidade(estado):
  pilha = [estado]
  for i in range(100):
    topo = pilha.pop(0)
    print(f"nó {i}")
    topo.mostra()
    print()

    acoes = conjunto_acoes(topo)
    for acao in acoes:
      filho = modelo_transicao(topo, acao)
      pilha = [filho] + pilha
      pilha.append(filho)

estado_inicial = Estado()
profundidade(estado_inicial)