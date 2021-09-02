premio = float(input("Digite o valor do premio: "))

premiodes = premio * 0.93

valordesconto = premio - premiodes

g1 = premiodes * 0.46
g2 = premiodes * 0.32
g3 = (premiodes - g1) - g1

print("O total do prêmio é de R$ {}, com o desconto do imposto será de  R$ {:.2f}," .format(premio,premiodes)+
"\no valor do imposto é de  R$ {:.2f}, o primeiro ganhador ganhou  R$ {:.2f}, e o segundo ganhou  R$ {:.2f}, e o terceiro ganhou  R$ {:.2f}" .format(valordesconto,g1,g2,g3))