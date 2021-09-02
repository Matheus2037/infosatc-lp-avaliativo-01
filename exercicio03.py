largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros:   "))

area = largura * altura

quantinta = area / 3

latastinta = quantinta / 3.6

valor = latastinta * 107

print("Para a parede ser pintada será necessário {:.2f} latas de tinta e custará R${:.2f} reais" .format(latastinta,valor))

