# tabela FIPE dicionario, armazena o preço de cada modelo
tabelaFipe = {
    'Fiat Uno': 35000,
    'Fiat Toro': 80000,
    'Fiat Mobi': 40000,
    'Volkswagen Gol': 30000,
    'Volkswagen T-Cross': 85000,
    'Volkswagen Nivus': 75000,
    'Chevrolet Onix': 45000,
    'Chevrolet Cruze': 55000,
    'Chevrolet S10': 65000,
    'Honda Civic': 80000,
    'Honda Fit': 45000,
    'Honda City': 56000,
    'Ford Ka': 25000,
    'Ford Fiesta': 31000,
    'Ford Eco Sport': 41000,
}
#Lista de carros disponíveis para compra e aluguel

veiculosDispo = {
    "Fiat": ['Fiat Uno', 'Fiat Toro', 'Fiat Mobi'],
    "Volkswagen": ['Volkswagen Gol', 'Volkswagen T-Cross', 'Volkswagen Nivus'],
    "Chevrolet": ['Chevrolet Onix', 'Chevrolet Cruze', 'Chevrolet S10'],
    "Honda": ['Honda Civic', 'Honda Fit', 'Honda City'], 
    "Ford": ['Ford Ka', 'Ford Fiesta', 'Ford Eco Sport']
}

#lista de veiculos disponiveis apenas para venda (usuário vende para a concessionaria)
veiculosParaCompra = {
    "Fiat": ['Fiat Uno', 'Fiat Toro', 'Fiat Mobi'],
    "Volkswagen": ['Volkswagen Gol', 'Volkswagen T-Cross', 'Volkswagen Nivus'],
    "Chevrolet": ['Chevrolet Onix', 'Chevrolet Cruze', 'Chevrolet S10'],
    "Honda": ['Honda Civic', 'Honda Fit', 'Honda City'], 
    "Ford": ['Ford Ka', 'Ford Fiesta', 'Ford Eco Sport']
}

# Cadastro do cliente

nome = (input("Informe seu nome: "))
telefone = int (input("Informe seu telefone: "))
saldo = float (input("Informe seu saldo em R$: "))

print (nome)
print (telefone)
print (saldo)

# Aqui, o sistema solicita ao usuário que informe seu nome, telefone e saldo em reais. O saldo é utilizado para verificar se o usuário tem dinheiro suficiente para realizar a compra ou locação de veículos.

while True:
    menu = int (input("\n Menu de opções \n 1- Vender veiculo \n 2- Alugar veiculo \n 3- Comprar veiculo \n 4- Sair \n"))
# while True exibe um menu com as opções de ações que o usuário pode realizar. O menu é exibido indefinidamente até o usuário escolher a opção de sair (4).
    if menu == 1:
# Quando o usuário escolhe a opção de vender um veículo, o programa exibe as marcas de carros disponíveis. O usuário escolhe a marca e, em seguida, o modelo do veículo.
        print ("--Venda de veiculos:--")
        for exibir in veiculosDispo:
            print(exibir)

        exibir = input("Escolha a marca: ")
# O preço do modelo escolhido é exibido, junto com a proposta de venda, que é 88% do valor da tabela FIPE
        for modelo in veiculosDispo:
            print(veiculosDispo[exibir])
            modelo = input("Escolha o modelo: ")
            print (f"O valor  do modelo escolhido é: {tabelaFipe[modelo]}")
            print (f"A proposta de venda é de {tabelaFipe[modelo]*0.88}")
            confCompra = (input("Deseja concluir a venda? [s/n]"))
            if confCompra == 's': 
             saldo = (tabelaFipe[modelo]*0.88) + saldo
             print (f"Novo saldo é: {saldo}")
             break
            else:
               print ("Venda Cancelada! ")
               break
# Se o usuário confirmar a venda, o valor da venda é adicionado ao saldo e o programa termina a operação de venda. Caso contrário, a venda é cancelada. / tabelaFipe[modelo]*0.88 faz o calculo da proposta e também é utilizado para adicionar o valor da venda ao saldo

    if menu == 2:
        print ("--Aluguel de veiculos:--")
        for exibir in veiculosParaCompra:
            print(exibir)

        exibir = input("Escolha a marca: ")

# A opção de alugar um veículo exibe as marcas e os modelos de veículos disponíveis para locação. O usuário escolhe a marca e, em seguida, o modelo.

        for modelo in veiculosParaCompra:
            print(veiculosParaCompra[exibir])
            modelo = input("Escolha o modelo: ")
            break

        if modelo in veiculosParaCompra[exibir]:
            
            diaria = int (input("Quantos dias serão de aluguel?"))
            print (f"A proposta de aluguél é de {77*diaria}")
# O preço do aluguel é calculado multiplicando 77 reais (o valor da diária) pelo número de dias solicitados. / 77*diaria faz o calculo e também é utilizado para retirar o valor do saldo
            confLocacao = (input("Deseja concluir a locação? [s/n]"))
            if confLocacao == 's' and saldo >= (77*diaria): 
             saldo = saldo - (77*diaria) 
             print (f"Novo saldo é: {saldo}")
             print ("Locação concluida! ")
             veiculosParaCompra[exibir].remove(modelo)
             
            elif confLocacao == 's' and saldo - (77*diaria):
             print ("Saldo insuficiente! ")
             
            else:
               print ("Compra Cancelada! ")
        else:
             print("Veiculo indisponível! Escolha outro.")
             continue
# Se o usuário confirmar a locação e tiver saldo suficiente, o valor é descontado e o veículo é removido da lista de disponíveis para locação.

    if menu == 3:
        print ("--Compra de veiculos:--")
        for exibir in veiculosDispo:
# Aqui, o programa permite ao usuário comprar um veículo. O processo de escolha de marca e modelo é semelhante ao da venda, mas o valor da compra é 25% maior que o valor da tabela FIPE
            print(exibir)

        exibir = input("Escolha a marca: ")

        print(veiculosDispo[exibir])
        modelo = input("Escolha o modelo: ")

        if modelo in veiculosDispo[exibir]:
            
            print (f"O valor  do modelo escolhido é: {tabelaFipe[modelo]}")
            print (f"A proposta de compra é de {tabelaFipe[modelo]*1.25}")
#A proposta de compra é calculada com base no valor da tabela FIPE multiplicado por 1.25./ Fazendo a multiplicação por 1.25 retira a necessidade de fazer o valor do veiculo na fipe + a porcentagem do lucro, unificando o calculo.
            confCompra = (input("Deseja concluir a compra? [s/n]"))
            if confCompra == 's' and saldo >= (tabelaFipe[modelo]*1.25): 
# Utilizado para o calculo e para a remover o valor do saldo do usuário
             saldo = saldo - (tabelaFipe[modelo]*1.25) 
             print (f"Novo saldo é: {saldo}")
             print ("Compra concluida! ")
             veiculosDispo[exibir].remove(modelo)
             
            elif confCompra == 's' and saldo - (tabelaFipe[modelo]*1.25):
             print ("Saldo insuficiente! ")
             
            else:
               print ("Compra Cancelada! ")
            
        else:
             print("Veiculo indisponível! Escolha outro.")
             continue
# Se o usuário confirmar a compra e tiver saldo suficiente, o valor é descontado do saldo e o veículo é removido da lista de disponíveis para compra.
    if menu == 4: 
       print ("Programa encerrado! ")
       break
# Finaliza o código e encerra o Looping