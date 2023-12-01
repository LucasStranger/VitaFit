class Aluno:
    def __init__(self, nome, cpf, celular, email, idade, peso, altura, historico_medico=None, metas=None, avaliacoes=None):
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
        self.email = email
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.historico_medico = historico_medico if historico_medico else []
        self.metas = metas if metas else {}
        self.avaliacoes = avaliacoes if avaliacoes else []

    def adicionar_historico_medico(self, informacao):
        self.historico_medico.append(informacao)

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

class Avaliacao:
    def __init__(self, tipo, data, testes_fisicos=None, medidas=None, desempenho_exercicios=None):
        self.tipo = tipo
        self.data = data
        self.testes_fisicos = testes_fisicos if testes_fisicos else {}
        self.medidas = medidas if medidas else {}
        self.desempenho_exercicios = desempenho_exercicios if desempenho_exercicios else {}

def cadastrar_aluno():
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    celular = input("Número de celular: ")
    email = input("Email: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (metros): "))
    
    historico = []
    print("### Histórico Médico ###")
    while True:
        informacao = input("Adicione informações relevantes ao histórico médico (deixe em branco para sair): ")
        if informacao:
            historico.append(informacao)
        else:
            break

    metas = {}
    print("### Metas de Condicionamento Físico ###")
    metas['perda_peso'] = float(input("Informe a meta de perda de peso (em kg): "))
    metas['ganho_massa'] = float(input("Informe a meta de ganho de massa muscular (em kg): "))
    metas['melhoria_resistencia_cardio'] = int(input("Informe a meta de melhoria na resistência cardiovascular (em minutos): "))
    metas['melhoria_resistencia_muscular'] = int(input("Informe a meta de melhoria na resistência muscular (em minutos): "))
    metas['aumento_flexibilidade'] = int(input("Informe a meta de aumento na flexibilidade (em minutos): "))
    metas['reducao_estresse'] = int(input("Informe a meta de redução do estresse (em minutos): "))
    metas['melhoria_postura'] = int(input("Informe a meta de melhoria na postura (em minutos): "))
    metas['aumento_agilidade_velocidade'] = int(input("Informe a meta de aumento na agilidade e velocidade (em minutos): "))

    return Aluno(nome, cpf, celular, email, idade, peso, altura, historico, metas)

def adicionar_informacao_medica(aluno):
    informacao = input("Informe o histórico médico relevante: ")
    aluno.adicionar_historico_medico(informacao)

def realizar_avaliacao(aluno):
    tipo = input("Tipo de avaliação (semanal, quinzenal, mensal): ")
    data = input("Data da avaliação: ")

    testes_fisicos = {}
    print("### Testes Físicos ###")
    testes_fisicos['flexibilidade'] = int(input("Flexibilidade (em cm): "))
    testes_fisicos['resistencia'] = int(input("Resistência (em minutos): "))
    testes_fisicos['forca'] = int(input("Força (em kg): "))
    # Adicione outros testes físicos conforme necessário

    medidas = {}
    print("### Medidas ###")
    medidas['peso'] = float(input("Peso (em kg): "))
    medidas['altura'] = float(input("Altura (em cm): "))
    medidas['circunferencia_cintura'] = float(input("Circunferência da Cintura (em cm): "))
    # Adicione outras medidas conforme necessário

    desempenho_exercicios = {}
    print("### Desempenho em Exercícios ###")
    desempenho_exercicios['agachamento'] = int(input("Desempenho no Agachamento (em kg): "))
    desempenho_exercicios['corrida'] = float(input("Desempenho na Corrida (em minutos): "))
    desempenho_exercicios['flexoes'] = int(input("Desempenho em Flexões: "))
    # Adicione outros exercícios conforme necessário

    avaliacao = Avaliacao(tipo, data, testes_fisicos, medidas, desempenho_exercicios)
    aluno.adicionar_avaliacao(avaliacao)

def salvar_csv(alunos):
    with open('alunos.csv', 'w', encoding='utf-8') as arquivo_csv:
        arquivo_csv.write("Nome,CPF,Celular,Email,Idade,Peso,Altura,Histórico Médico\n")
        for aluno in alunos:
            historico = ' | '.join(aluno.historico_medico).replace(',', ';')
            arquivo_csv.write(f"{aluno.nome},{aluno.cpf},{aluno.celular},{aluno.email},{aluno.idade},{aluno.peso},{aluno.altura},{historico}\n")

def carregar_csv():
    alunos = []
    try:
        with open('alunos.csv', 'r', encoding='utf-8') as arquivo_csv:
            linhas = arquivo_csv.readlines()[1:]
            for linha in linhas:
                dados = linha.strip().split(',')
                nome, cpf, celular, email = dados[:4]
                idade, peso, altura = int(dados[4]), float(dados[5]), float(dados[6])
                historico_medico = dados[7].split(' | ') if len(dados) > 7 else []
                aluno = Aluno(nome, cpf, celular, email, idade, peso, altura, historico_medico)
                alunos.append(aluno)
    except FileNotFoundError:
        pass
    return alunos

def salvar_txt(alunos):
    with open('alunos.txt', 'w', encoding='utf-8') as arquivo_txt:
        for aluno in alunos:
            arquivo_txt.write(f"Nome: {aluno.nome}\n")
            arquivo_txt.write(f"CPF: {aluno.cpf}\n")
            arquivo_txt.write(f"Celular: {aluno.celular}\n")
            arquivo_txt.write(f"Email: {aluno.email}\n")
            arquivo_txt.write(f"Idade: {aluno.idade}\n")
            arquivo_txt.write(f"Peso: {aluno.peso}\n")
            arquivo_txt.write(f"Altura: {aluno.altura}\n")
            arquivo_txt.write("Histórico Médico:\n")
            for info in aluno.historico_medico:
                arquivo_txt.write(f"- {info}\n")
            arquivo_txt.write("\n")

def mostrar_menu():
    print("### MENU ###")
    print("1. Cadastrar novo aluno")
    print("2. Adicionar histórico médico a um aluno")
    print("3. Realizar avaliação de um aluno")
    print("4. Sair")

# Carregando os alunos do arquivo CSV
alunos = carregar_csv()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_aluno = cadastrar_aluno()
        alunos.append(novo_aluno)
        salvar_csv(alunos)
        salvar_txt(alunos)
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        if not alunos:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("Alunos disponíveis para adicionar histórico médico:")
            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno.nome}")

            indice_aluno = int(input("Escolha o número do aluno para adicionar histórico: ")) - 1
            if 0 <= indice_aluno < len(alunos):
                adicionar_informacao_medica(alunos[indice_aluno])
                salvar_csv(alunos)
                salvar_txt(alunos)
                print("Histórico médico adicionado com sucesso!")

            else:
                print("Índice inválido.")

    elif opcao == "3":
        if not alunos:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("Alunos disponíveis para realizar avaliação:")
            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno.nome}")

            indice_aluno = int(input("Escolha o número do aluno para realizar avaliação: ")) - 1
            if 0 <= indice_aluno < len(alunos):
                realizar_avaliacao(alunos[indice_aluno])
                salvar_csv(alunos)
                salvar_txt(alunos)
                print("Avaliação realizada com sucesso!")

            else:
                print("Índice inválido.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Escolha uma opção válida.")

