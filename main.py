import os
def clear():
  return os.system('cls' if os.name == 'nt' else 'clear')
usu = "s"
while(usu=="s"):
  fatorar = int(input("Fatorar: "))
  valores_a = 0
  valores_b = 0
  if((fatorar%2 != 0) and (fatorar%5 !=0) and (fatorar%3 != 0)):
    for x in range(1,fatorar):
      if (x%2==0) and (x !=2) or (x%5==0) and (x != 5) or (x%3==0) and (x !=3) or (x%7 ==0) and (x != 7):
        continue
      else:
        for y in range(1, fatorar): 
          if (y%2==0) and (y !=2) or (y%5==0) and (y != 5) or (y%3==0) and (y !=3) or (y%7 ==0) and (y != 7):
            continue
          else:
            resultado = x*y
            if(resultado == fatorar):
              valores_a = x
              valores_b = y
              break
      if(resultado == fatorar):
        break
    if((valores_a and valores_b) == 0):
      print(str(fatorar)+" é um número primo.")
    else:
      print("Valor1: "+str(valores_a)+"\nValor2: "+str(valores_b))
    usu = input("\nReiniciar?\n s = Sim, n = Não.\nR: ")
    clear()
  else:
    print("Tente outro valor, esse não resulta do produto de dois primos.")
  
