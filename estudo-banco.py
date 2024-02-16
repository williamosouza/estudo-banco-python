menu = """
      SELECIONE A OPÇÃO

      1 - SAQUE
      2 - DEPÓSITO
      3 - EXTRATO
      0 - SAIR

"""

saldo = 1000
limite = 500
extrato = ""
saques_diarios = 1
LIMITE_SAQUE = 3


print(menu)

while True:
  option = input("\nDigite a opção: ")
  value = ""
  
  if option == "1":
    print("\nSAQUE")
    if saques_diarios > LIMITE_SAQUE:
      print("\nLIMITE DE SAQUES EXCEDIDO")
      print("\nGOSTARIA DE REALIZAR UMA NOVA OPERAÇÃO?")
      print(menu)
    else:
      saque = float(input("\nDigite o valor desejado: "))
      if saque > limite:
        print("\nVALOR EXCEDE O LIMITE")
        print("\nGOSTARIA DE REALIZAR UMA NOVA OPERAÇÃO?\n")
        print(menu)
      elif saque > saldo:
        print("\nSALDO INSUFICIENTE")
        print("\nGOSTARIA DE REALIZAR UMA NOVA OPERAÇÃO?\n")
        print(menu)
      elif saque < 0:
        print("\nVALOR INVÁLIDO")
        print("\nGOSTARIA DE REALIZAR UMA NOVA OPERAÇÃO?\n")
        print(menu)
      elif saque < saldo and saque <= limite and saque > 0:
        saldo -= saque
        extrato += f"D (R$ {saque:.2f})\n"
        saques_diarios += 1
        print("\nSAQUE REALIZADO COM SUCESSO")
        print("\nGOSTARIA DE REALIZAR UMA NOVA OPERAÇÃO?\n")
        print(menu)
      else:
        print("\nVALOR DIGITADO INVALIDO\n")
        print(menu)     
  elif option == "2":
    print("\nDEPÓSITO")
    deposito = float(input("\nDigite o valor depositado: "))
    saldo += deposito
    extrato += f"C R$ {deposito:.2f}\n"
    print("\nDEPÓSITO EFETUADO COM SUCESSO")
    print("\nGOSTARIA DE REALIZAR UMA NOVA OPERAÇÃO?\n")
  elif option == "3":
    print("\n=============== EXTRATO ===============")
    print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES." if not extrato else extrato)
    print(f"\nSALDO: R$ {saldo:.2f}")
    print("========================================")
    print("\nGOSTARIA DE REALIZAR UMA NOVA OPERAÇÃO?\n")
    print(menu)
  elif option == "0":
    print("\nOBRIGADO POR USAR NOSSO SERVIÇO")
    break
  else:
    print("\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE")