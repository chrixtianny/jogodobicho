import random
import numpy as np

NumeroDoBicho = np.random.randint(1, 56, (5))
x = 0
while x < 5:
  print('Dezena sorteada:', NumeroDoBicho[x])
  
  if NumeroDoBicho[x] > 0 and NumeroDoBicho[x] < 6:
    print (NumeroDoBicho[x], "O bicho é o Major Porco")
  
  elif NumeroDoBicho[x] > 5 and NumeroDoBicho[x] < 11: 
    print(NumeroDoBicho[x], "O bicho é o Porco Bola de Neve")
  
  elif NumeroDoBicho[x] > 10 and NumeroDoBicho[x] < 16:
   print(NumeroDoBicho[x], "O bicho é o Porco Napoleão")
  
  elif NumeroDoBicho[x] > 15 and NumeroDoBicho[x] < 21:
   print(NumeroDoBicho[x], "Os bichos são Ovelhas")
  
  elif NumeroDoBicho[x] > 20 and NumeroDoBicho[x] < 26:
   print(NumeroDoBicho[x], "O bicho é Benjamin, o Burro")
  
  elif NumeroDoBicho[x] > 24 and NumeroDoBicho[x] < 31:
   print(NumeroDoBicho[x], "O bicho é Sansão, o Cavalo")
  
  elif NumeroDoBicho[x] > 30 and NumeroDoBicho[x] < 36:
   print(NumeroDoBicho[x], "O bicho é Maricota, a Cabra")
  
  elif NumeroDoBicho[x] > 35 and NumeroDoBicho[x] < 41:
   print(NumeroDoBicho[x], "Os bichos são os Cachorros")
  
  elif NumeroDoBicho[x] > 40 and NumeroDoBicho[x] < 46:
   print(NumeroDoBicho[x], "O bicho é Mimosa, a Égua")
  
  elif NumeroDoBicho[x] > 45 and NumeroDoBicho[x] < 51:
  
   print(NumeroDoBicho[x], "O bicho é Quitéria, a Égua")
  
  elif NumeroDoBicho[x] > 50 and NumeroDoBicho[x] < 56:
  
    print(NumeroDoBicho[x], "O bicho é Moisés, o Corvo")

  
  x = x + 1
