import random
import numpy as np

NumeroDoBicho = np.random.randint(1, 51, (2))

print('As dezenas sorteadas são', NumeroDoBicho[0],'e', NumeroDoBicho[1])

#Primeira Dezena

if NumeroDoBicho[0] > 0 and NumeroDoBicho[0] < 6:
  print (NumeroDoBicho[0], "O bicho é o Major Porco")

elif NumeroDoBicho[0] > 5 and NumeroDoBicho[0] < 11: 
  print(NumeroDoBicho[0], "O bicho é o Porco Bola de Neve")

elif NumeroDoBicho[0] > 10 and NumeroDoBicho[0] < 16:
 print(NumeroDoBicho[0], "O bicho é o Porco Napoleão")

elif NumeroDoBicho[0] > 15 and NumeroDoBicho[0] < 21:
 print(NumeroDoBicho[0], "Os bichos são Ovelhas")

elif NumeroDoBicho[0] > 20 and NumeroDoBicho[0] < 26:
 print(NumeroDoBicho[0], "O bicho é Benjamin, o Burro")

elif NumeroDoBicho[0] > 24 and NumeroDoBicho[0] < 31:
 print(NumeroDoBicho[0], "O bicho é Sansão, o Cavalo")

elif NumeroDoBicho[0] > 30 and NumeroDoBicho[0] < 36:
 print(NumeroDoBicho[0], "O bicho é Maricota, a Cabra")

elif NumeroDoBicho[0] > 35 and NumeroDoBicho[0] < 41:
 print(NumeroDoBicho[0], "Os bichos são os Cachorros")

elif NumeroDoBicho[0] > 40 and NumeroDoBicho[0] < 46:
 print(NumeroDoBicho[0], "O bicho é Mimosa, a Égua")

elif NumeroDoBicho[0] > 45 and NumeroDoBicho[0] < 51:

print(NumeroDoBicho[0], "O bicho é Quitéria, a Égua")

  #Segunda Dezena
if NumeroDoBicho[1] > 0 and NumeroDoBicho[1] < 6:
  print (NumeroDoBicho[1], "O bicho é o Major Porco")
  
elif NumeroDoBicho[1] > 5 and NumeroDoBicho[1] < 11: 
  print(NumeroDoBicho[1], "O bicho é o Porco Bola de Neve")

elif NumeroDoBicho[1] > 10 and NumeroDoBicho[1] < 16:
 print(NumeroDoBicho[1], "O bicho é o Porco Napoleão")

elif NumeroDoBicho[1] > 15 and NumeroDoBicho[1] < 21:
 print(NumeroDoBicho[1], "Os bichos são Ovelhas")

elif NumeroDoBicho[1] > 20 and NumeroDoBicho[1] < 26:
 print(NumeroDoBicho[1], "O bicho é Benjamin, o Burro")

elif NumeroDoBicho[1] > 24 and NumeroDoBicho[1] < 31:
 print(NumeroDoBicho[1], "O bicho é Sansão, o Cavalo")

elif NumeroDoBicho[1] > 30 and NumeroDoBicho[1] < 36:
 print(NumeroDoBicho[1], "O bicho é Maricota, a Cabra")

elif NumeroDoBicho[1] > 35 and NumeroDoBicho[1] < 41:
 print(NumeroDoBicho[1], "Os bichos são os Cachorros")
  
elif NumeroDoBicho[1] > 40 and NumeroDoBicho[1] < 46:

 print(NumeroDoBicho[1], "O bicho é Mimosa, a Égua")

elif NumeroDoBicho[1] > 45 and NumeroDoBicho[1] < 51:

 print(NumeroDoBicho[1], "O bicho é Quitéria, a Égua")
