from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt 
import csv 
data_hoje = datetime.now().strftime('%Y-%m-%d')
class Aluno:
    def __init__(self, nome, cpf, celular, email, idade, peso, altura, historico_medico=None, metas=None, avaliacoes=None, dias_alerta=7):
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
        self.email = email
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.historico_medico = historico_medico if historico_medico else []
        self.metas = metas if metas else {
            'perda_peso': {'descricao': 'Perda de Peso', 'valor': 0, 'alcancada': False, 'data_limite': ''},
            'ganho_massa': {'descricao': 'Ganho de Massa Muscular', 'valor': 0, 'alcancada': False, 'data_limite': ''},
            'melhoria_resistencia_cardio': {'descricao': 'Melhoria na Resistência Cardiovascular', 'valor': 0, 'alcancada': False, 'data_limite': ''},
            'melhoria_resistencia_muscular': {'descricao': 'Melhoria na Resistência Muscular', 'valor': 0, 'alcancada': False, 'data_limite': ''},
            'aumento_flexibilidade': {'descricao': 'Aumento na Flexibilidade', 'valor': 0, 'alcancada': False, 'data_limite': ''},
            'reducao_estresse': {'descricao': 'Redução do Estresse', 'valor': 0, 'alcancada': False, 'data_limite': ''},
            'melhoria_postura': {'descricao': 'Melhoria na Postura', 'valor': 0, 'alcancada': False, 'data_limite': ''},
            'aumento_agilidade_velocidade': {'descricao': 'Aumento na Agilidade e Velocidade', 'valor': 0, 'alcancada': False, 'data_limite': ''}
        }
        self.avaliacoes = avaliacoes if avaliacoes else []
        self.dias_alerta = dias_alerta
    
    def sugerir_ajustes_plano_treino(self):
        ajustes = f"## Sugestões de Ajuste no Plano de Treino para {self.nome} ##\n"

        if self.metas['perda_peso']['alcancada']:
            ajustes += "- Como você alcançou sua meta de perda de peso, podemos focar agora em ganho de massa muscular.\n"

        if self.metas['ganho_massa']['alcancada']:
            ajustes += "- Como você alcançou sua meta de ganho de massa muscular, podemos focar agora em melhoria na resistência cardiovascular.\n"

        if self.metas['melhoria_resistencia_cardio']['alcancada']:
            ajustes += "- Como sua resistência cardiovascular melhorou, podemos intensificar os exercícios para ganho de força.\n"

        if self.metas['melhoria_resistencia_muscular']['alcancada']:
            ajustes += "- Como você melhorou sua resistência muscular, podemos adicionar exercícios para ganho de agilidade e velocidade.\n"

        if self.metas['aumento_flexibilidade']['alcancada']:
            ajustes += "- Como você alcançou sua meta de flexibilidade, podemos adicionar exercícios para melhoria na postura.\n"

        if self.metas['reducao_estresse']['alcancada']:
            ajustes += "- Como você reduziu seu nível de estresse, podemos incluir exercícios para melhorar a flexibilidade.\n"

        # Adicione outros ajustes conforme necessário

        if ajustes:
            return ajustes
        else:
            return f"Não há sugestões de ajuste para {self.nome} no momento.\n"

    def adicionar_historico_medico(self, informacao):
        self.historico_medico.append(informacao)

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

def adicionar_informacao_medica(aluno):
    informacao = input("Informe o histórico médico relevante: ")
    aluno.adicionar_historico_medico(informacao)

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

class Avaliacao:
    def __init__(self, tipo, data, testes_fisicos=None, medidas=None, desempenho_exercicios=None):
        self.tipo = tipo
        self.data = data
        self.testes_fisicos = testes_fisicos if testes_fisicos else {}
        self.medidas = medidas if medidas else {}
        self.desempenho_exercicios = desempenho_exercicios if desempenho_exercicios else {}
    
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
    
    with open('avaliacoes_alunos.csv', mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['Aluno', 'Tipo', 'Data', 'Flexibilidade', 'Resistencia', 'Forca',
                      'Peso', 'Altura', 'Circunferencia_Cintura', 'Desempenho_Agachamento',
                      'Desempenho_Corrida', 'Desempenho_Flexoes']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Se o arquivo ainda não existe ou está vazio, escreva o cabeçalho
        if file.tell() == 0:
            writer.writeheader()

        # Escreva os dados da avaliação para o aluno no arquivo CSV
        writer.writerow({
            'Aluno': aluno.nome,
            'Tipo': tipo,
            'Data': data,
            'Flexibilidade': testes_fisicos['flexibilidade'],
            'Resistencia': testes_fisicos['resistencia'],
            'Forca': testes_fisicos['forca'],
            'Peso': medidas['peso'],
            'Altura': medidas['altura'],
            'Circunferencia_Cintura': medidas['circunferencia_cintura'],
            'Desempenho_Agachamento': desempenho_exercicios['agachamento'],
            'Desempenho_Corrida': desempenho_exercicios['corrida'],
            'Desempenho_Flexoes': desempenho_exercicios['flexoes']
        })

def carregar_dados_avaliacoes():
    dados_avaliacoes = defaultdict(list)

    with open('avaliacoes_alunos.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            aluno = row['Aluno']
            # Processar as avaliações do aluno
            avaliacao = {
                'Flexibilidade': int(row['Flexibilidade']),
                'Resistencia': int(row['Resistencia']),
                'Forca': int(row['Forca']),
                'Peso': float(row['Peso']),
                'Altura': float(row['Altura']),
                'Circunferencia_Cintura': float(row['Circunferencia_Cintura']),
                'Desempenho_Agachamento': int(row['Desempenho_Agachamento']),
                'Desempenho_Corrida': float(row['Desempenho_Corrida']),
                'Desempenho_Flexoes': int(row['Desempenho_Flexoes'])
                # Adicione os demais campos conforme necessário
            }
            dados_avaliacoes[aluno].append(avaliacao)

    return dados_avaliacoes
def calcular_progresso_alunos(arquivo_csv):
    with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        avaliacoes_alunos = defaultdict(list)
        for row in reader:
            nome_aluno = row['Aluno']
            avaliacoes_alunos[nome_aluno].append(row)
        
        dados_avaliacoes = {}  # Dicionário para armazenar os dados das avaliações de cada aluno
        for aluno, avaliacoes in avaliacoes_alunos.items():
            # Aqui você pode fazer o cálculo do progresso com base nas avaliações do aluno
            # Vou criar um exemplo simples considerando a média da flexibilidade como progresso
            flexibilidades = [int(avaliacao['Flexibilidade']) for avaliacao in avaliacoes]
            progresso = sum(flexibilidades) / len(flexibilidades) if flexibilidades else 0
            dados_avaliacoes[aluno] = progresso
        
        return dados_avaliacoes

def gerar_relatorio_progresso(dados_avaliacoes):
    for aluno, progresso in dados_avaliacoes.items():
        print(f'Aluno: {aluno}')
        print(f'Progresso: {progresso:.2f}')  # Exibe o progresso médio com duas casas decimais
        print('--------------------------')

        # Gerar gráfico de pizza para o progresso do aluno
        labels = ['Progresso', 'Restante']  # Labels para progresso e restante
        sizes = [progresso, 100 - progresso]  # Progresso e restante (considerando 100 como total)
        
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(f'Progresso de {aluno}')

        plt.show()

arquivo_csv = 'avaliacoes_alunos.csv'
dados_progresso = calcular_progresso_alunos(arquivo_csv)
class MensagensInternas:
    def __init__(self):
        self.mensagens = []

    def enviar_mensagem(self, remetente, destinatario, conteudo):
        mensagem = f"De: {remetente}\nPara: {destinatario}\n{conteudo}\n"
        self.mensagens.append(mensagem)
        self.salvar_mensagens()

    def salvar_mensagens(self):
        with open('mensagens.txt', 'w') as file:
            for mensagem in self.mensagens:
                file.write(mensagem)
                file.write("-" * 30 + "\n")

    def carregar_mensagens(self):
        with open('mensagens.txt', 'r') as file:
            self.mensagens = file.readlines()

    def mostrar_mensagens(self):
        for mensagem in self.mensagens:
            print(mensagem)


mensagens = MensagensInternas()
#mensagens.carregar_mensagens()  # Carregar as mensagens salvas anteriormente

# Exemplo de uso:
mensagens.enviar_mensagem("Professor", "Aluno", "Olá! Aqui estão algumas sugestões para seu treino.")
mensagens.mostrar_mensagens()  # Mostrar todas as mensagens

class SistemaAlertas:
    def __init__(self, alunos):
        self.alunos = alunos

    def verificar_alertas(self, data_hoje):
        for aluno in self.alunos:
            self.verificar_presenca(aluno, data_hoje)
            self.verificar_avaliacoes_pendentes(aluno, data_hoje)
            self.verificar_metas_nao_alcancadas(aluno, data_hoje)

    def verificar_presenca(self, aluno, data_hoje):
        for avaliacao in aluno.avaliacoes:
            if avaliacao.tipo == "treino" and not avaliacao.presenca_confirmada:
                if avaliacao.data <= data_hoje:
                    print(f"ALERTA: Aluno {aluno.nome} não compareceu à sessão de treino programada em {avaliacao.data}.")

    def verificar_avaliacoes_pendentes(self, aluno, data_hoje):
        for avaliacao in aluno.avaliacoes:
            if avaliacao.tipo == "avaliacao" and not avaliacao.avaliacao_realizada:
                if avaliacao.data <= data_hoje:
                    print(f"ALERTA: Aluno {aluno.nome} possui avaliação pendente marcada para {avaliacao.data}.")

    def verificar_metas_nao_alcancadas(self, aluno, data_hoje):
        for chave_meta, meta in aluno.metas.items():
            if not meta['alcancada']:
                if meta['data_limite'] <= data_hoje:
                    print(f"ALERTA: Aluno {aluno.nome} não alcançou a meta '{meta['descricao']}' até a data limite {meta['data_limite']}.")
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

def salvar_csv(alunos):
    with open('alunos.csv', 'w', encoding='utf-8') as arquivo_csv:
        arquivo_csv.write("Nome,CPF,Celular,Email,Idade,Peso,Altura,Histórico Médico\n")
        for aluno in alunos:
            historico = ' | '.join(aluno.historico_medico).replace(',', ';')
            arquivo_csv.write(f"{aluno.nome},{aluno.cpf},{aluno.celular},{aluno.email},{aluno.idade},{aluno.peso},{aluno.altura},{historico}\n")


def mostrar_menu():
    print("### MENU ###")
    print("1. Cadastrar novo aluno")
    print("2. Adicionar histórico médico a um aluno")
    print("3. Realizar avaliação de um aluno")
    print("4. Verificar Alertas")
    print("5. mensagens entre(professor/aluno)")
    print("6. mostrar mensagens")
    print("7. mostrar dados da avaliação")
    print("8. gerar gráfico do relatório do progresso dos alunos")
    print("9. sugerir ajustes no treino")
    print("10. sair")

# Carregando os alunos do arquivo CSV
alunos = carregar_csv()
dados_avaliacoes = carregar_dados_avaliacoes()  # Carregar dados das avaliações

sistema_alertas = SistemaAlertas(alunos)

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_aluno = cadastrar_aluno()
        alunos.append(novo_aluno)
        salvar_csv(alunos)
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
                print("Avaliação realizada com sucesso!")

            else:
                print("Índice inválido.")

    elif opcao == "4":
        sistema_alertas.verificar_alertas(data_hoje)
    elif opcao == "5":
        remetente = input("Remetente: ")
        destinatario = input("Destinatário: ")
        conteudo = input("Conteúdo da mensagem: ")
        mensagens.enviar_mensagem(remetente, destinatario, conteudo)
        print("Mensagem enviada com sucesso!")
    elif opcao == "6":
        mensagens.mostrar_mensagens()
    elif opcao == "7":
        dados_avaliacoes = carregar_dados_avaliacoes()
    elif opcao == "8":
        gerar_relatorio_progresso(dados_progresso)
    elif opcao == "9":
        for aluno in alunos:
            ajustes = aluno.sugerir_ajustes_plano_treino()
            print(f"Sugestões de ajustes para {aluno.nome}:\n{ajustes}")        
    elif opcao == "10":
        print('saindo..')
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")



