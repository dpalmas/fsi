import random
def f(x):
  return (
      -x**8 + 77*x**7 - 2451*x**6 + 41817*x**5 - 414849*x**4 + 2429223*x**3 - 8130689*x**2 + 
      14117683*x - 9699690
  )

def busca_informada(x):
  while True:
    v1 = f(x)
    v2 = f(x+0.1)
    v3 = f(x-0.1)
    if v2 > v1:
      x = x + 0.1
    elif v3 > v1:
      x = x - 0.1
    else: 
      print(f"{x:.2f}, {v1:.2f}")
      break

for i in range(5):
  x = random.random()*20
  busca_informada(x)

18.28, 1320009.81
18.32, 1317786.03
6.00, 60044.67
2.36, 63278.58
6.06, 60086.78