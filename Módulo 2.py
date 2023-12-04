import csv

class Produto:
    def __init__(self, descricao, preco, tamanhos_disponiveis, imagem):
        self.descricao = descricao
        self.preco = preco
        self.tamanhos_disponiveis = tamanhos_disponiveis
        self.imagem = imagem

class SistemaLoja:
    def __init__(self):
        self.produtos = []
        self.estoque = {}

    def carregar_produtos_e_estoque(self):
        try:
            with open('produtos.csv', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader) 
                for row in reader:
                    descricao, preco, tamanhos, imagem = row
                    preco = float(preco)
                    tamanhos = tamanhos.split(',')
                    produto = Produto(descricao, preco, tamanhos, imagem)
                    self.produtos.append(produto)

            with open('estoque.csv', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    descricao, tamanho, quantidade = row
                    chave = (descricao, tamanho)
                    self.estoque[chave] = int(quantidade)

        except FileNotFoundError:
            pass 

    def salvar_produtos_e_estoque(self):
        with open('produtos.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Descrição', 'Preço', 'Tamanhos Disponíveis', 'Imagem'])
            for produto in self.produtos:
                writer.writerow([produto.descricao, produto.preco, ','.join(produto.tamanhos_disponiveis), produto.imagem])

        with open('estoque.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Descrição', 'Tamanho', 'Quantidade'])
            for (descricao, tamanho), quantidade in self.estoque.items():
                writer.writerow([descricao, tamanho, quantidade])

    def cadastrar_produto(self, produto, quantidades):
        if produto not in self.produtos:
            self.produtos.append(produto)
            self.atualizar_estoque(produto, quantidades)
            print("Produto cadastrado com sucesso!")
        else:
            print("Produto já cadastrado. Use a opção de adicionar quantidade.")

    def adicionar_quantidade(self, produto, quantidades):
        if produto in self.produtos:
            self.atualizar_estoque(produto, quantidades)
            print("Quantidade adicionada com sucesso!")
        else:
            print("Produto não cadastrado. Use a opção de cadastrar produto.")

    def retirar_quantidade(self, produto, quantidades):
        if produto in self.produtos:
            if all(quantidades[i] <= self.estoque.get((produto.descricao, produto.tamanhos_disponiveis[i]), 0) for i in range(len(quantidades))):
                self.atualizar_estoque(produto, [-q for q in quantidades])
                print("Quantidade retirada com sucesso!")
            else:
                print("Quantidade insuficiente no estoque.")
        else:
            print("Produto não cadastrado. Use a opção de cadastrar produto.")

    def atualizar_estoque(self, produto, quantidades):
        for i, tamanho in enumerate(produto.tamanhos_disponiveis):
            chave = (produto.descricao, tamanho)
            quantidade = quantidades[i]
            if chave in self.estoque:
                self.estoque[chave] += quantidade
            else:
                self.estoque[chave] = quantidade

    def exibir_estoque(self):
        print("Estoque:")
        for chave, quantidade in self.estoque.items():
            descricao, tamanho = chave
            print(f"{descricao} - Tamanho: {tamanho} - Quantidade: {quantidade}")

    def enviar_alerta(self, aluno, preferencias):
        pass

def menu():
    print("1. Cadastro de Produtos")
    print("2. Adicionar Quantidade ao Estoque")
    print("3. Retirar Quantidade do Estoque")
    print("4. Gestão de Estoque")
    print("5. Sair")

if __name__ == "__main__":
    sistema_loja = SistemaLoja()
    sistema_loja.carregar_produtos_e_estoque()

    while True:
        menu()
        opcao = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")

        if opcao == "1":
            descricao = input("Digite a descrição do produto: ")
            preco = float(input("Digite o preço do produto: "))
            tamanhos = input("Digite os tamanhos disponíveis (separados por espaço): ").split()
            imagem = input("Digite o nome da imagem representativa: ")

            quantidades = []
            for tamanho in tamanhos:
                quantidade = int(input(f"Digite a quantidade para o tamanho {tamanho}: "))
                quantidades.append(quantidade)

            produto = Produto(descricao, preco, tamanhos, imagem)
            sistema_loja.cadastrar_produto(produto, quantidades)

        elif opcao == "2":
            descricao = input("Digite a descrição do produto para adicionar quantidade: ")
            produto = next((p for p in sistema_loja.produtos if p.descricao == descricao), None)

            if produto:
                tamanhos = input("Digite os tamanhos disponíveis (separados por espaço): ").split()
                quantidades = []
                for tamanho in tamanhos:
                    quantidade = int(input(f"Digite a quantidade para o tamanho {tamanho}: "))
                    quantidades.append(quantidade)

                sistema_loja.adicionar_quantidade(produto, quantidades)
            else:
                print("Produto não encontrado. Cadastre o produto primeiro.")

        elif opcao == "3":
            descricao = input("Digite a descrição do produto para retirar quantidade: ")
            produto = next((p for p in sistema_loja.produtos if p.descricao == descricao), None)

            if produto:
                tamanhos = input("Digite os tamanhos disponíveis (separados por espaço): ").split()
                quantidades = []
                for tamanho in tamanhos:
                    quantidade = int(input(f"Digite a quantidade para o tamanho {tamanho}: "))
                    quantidades.append(quantidade)

                sistema_loja.retirar_quantidade(produto, quantidades)
            else:
                print("Produto não encontrado. Cadastre o produto primeiro.")

        elif opcao == "4":
            sistema_loja.exibir_estoque()

        elif opcao == "5":
            sistema_loja.salvar_produtos_e_estoque()
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
