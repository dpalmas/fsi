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
    # criar em um estado novo 
    estado_novo = Estado()
    estado_novo.vez = "X" if estado.vez == "0" else "X"
    for i in range(3):
      for j in range(3):
        estado_novo.tabuleiro[i][j] = estado.tabuleiro[i][j]
        estado_novo.tabuleiro[acao.linha][acao.coluna] = estado_novo.vez 
    return estado_novo

estado_inicial = Estado()
acoes = conjunto_acoes(estado_inicial)
for acao in acoes:
  estado_atual = modelo_transicao(estado_inicial, acao)
  acao.mostra()
  estado_atual.mostra()
  print()