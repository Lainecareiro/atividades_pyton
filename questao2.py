def min():
  senha_correta = "123456"
  tentativas_restantes = 3

while tentativas_restantes > 0:
  senha_informada = input("Digite sua enha:")
  if senha_informada == senha_correta:
    print(f" olá , <SEUNOME>. SEJA BEM VINDO(A) AO NOSSO SISTEMA!")
    return 
  else: tentativas_restantes -=1
    if tentativas_restante > 0:
       print(f"senha incoratas ! voê ainda tem {tentativas_retantes} tentativas(s). ")
else: print(" sua senha ESTÁ INCORRETA! por favor , TENTE NOVAMENTE OU FAÇA UMA NOVA SENHA!,")
      return 
if __nome__ == "__main__":
  main()
