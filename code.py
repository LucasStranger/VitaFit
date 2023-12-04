from datetime import datetime, timedelta

class SistemaAlertas:
    def __init__(self, alunos):
        self.alunos = alunos

    def verificar_alertas(self):
        hoje = datetime.now()

        for aluno in self.alunos:
            self.verificar_presenca(aluno, hoje)
            self.verificar_avaliacoes_pendentes(aluno, hoje)
            self.verificar_metas_nao_alcancadas(aluno, hoje)

    def verificar_presenca(self, aluno, hoje):
        for avaliacao in aluno.avaliacoes:
            if avaliacao.tipo == "treino" and not avaliacao.presenca_confirmada:
                data_avaliacao = datetime.strptime(avaliacao.data, "%Y-%m-%d")
                diferenca_dias = (hoje - data_avaliacao).days

                if diferenca_dias >= aluno.dias_alerta:
                    print(f"ALERTA: Aluno {aluno.nome} não compareceu à sessão de treino programada em {avaliacao.data}.")

    def verificar_avaliacoes_pendentes(self, aluno, hoje):
        for avaliacao in aluno.avaliacoes:
            if avaliacao.tipo == "avaliacao" and not avaliacao.avaliacao_realizada:
                data_avaliacao = datetime.strptime(avaliacao.data, "%Y-%m-%d")
                diferenca_dias = (hoje - data_avaliacao).days

                if diferenca_dias >= aluno.dias_alerta:
                    print(f"ALERTA: Aluno {aluno.nome} possui avaliação pendente marcada para {avaliacao.data}.")

    def verificar_metas_nao_alcancadas(self, aluno, hoje):
        for meta in aluno.metas:
            if not meta['alcancada']:
                data_meta = datetime.strptime(meta['data_limite'], "%Y-%m-%d")
                diferenca_dias = (hoje - data_meta).days

                if diferenca_dias >= aluno.dias_alerta:
                    print(f"ALERTA: Aluno {aluno.nome} não alcançou a meta '{meta['descricao']}' até a data limite {meta['data_limite']}.")


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
        self.metas = metas if metas else []
        self.avaliacoes = avaliacoes if avaliacoes else []
        self.dias_alerta = dias_alerta

    def adicionar_historico_medico(self, informacao):
        self.historico_medico.append(informacao)

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def adicionar_metas(self, metas):
        self.metas = metas

    def adicionar_meta(self, numero, descricao, data_limite):
        self.metas.append({'numero': numero, 'descricao': descricao, 'data_limite': data_limite, 'alcancada': False})

    def formatar_cpf(self):
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"

    def formatar_idade(self):
        return f"{self.idade[0]} - {self.idade[1]} - {self.idade[2]} - {self.idade[3]} - {self.idade[4]}"

    def formatar_pesos(self):
        return ' - '.join([f"{peso:.1f}" for peso in self.peso])

    def formatar_alturas(self):
        return ' - '.join([f"{altura:.1f}" for altura in self.altura])

    def mostrar_informacoes(self):
        print(f"{self.nome} (nota: {self.nome})")
        print(f"{self.formatar_cpf()} (nota: {self.cpf})")
        print(f"Celular: {self.celular} (nota: {self.celular})")
        print(f"Email: {self.email} (nota: {self.email})")
        print(f"Idades: {self.formatar_idade()} (nota: {' - '.join(map(str, self.idade))})")
        print(f"Pesos: {self.formatar_pesos()} (nota: {' - '.join(map(str, self.peso))})")
        print(f"Alturas: {self.formatar_alturas()} (nota: {' - '.join(map(str, self.altura))})")

        print("\nHistórico Médico:")
        for info in self.historico_medico:
            print(f"- {info}")

        print("\nMetas:")
        for meta in self.metas:
            print(f"{meta['numero']} - {meta['descricao']} (Data Limite: {meta['data_limite']}, Alcançada: {meta['alcancada']})")

        print("\nAvaliações:")
        for avaliacao in self.avaliacoes:
            print(avaliacao)


class Avaliacao:
    def __init__(self, tipo, data, descricao, presenca_confirmada=False, avaliacao_realizada=False):
        self.tipo = tipo
        self.data = data
        self.descricao = descricao
        self.presenca_confirmada = presenca_confirmada
        self.avaliacao_realizada = avaliacao_realizada

    def __str__(self):
        return f"{self.data}\n{self.descricao}\n"


# Código principal
def carregar_csv():
    alunos = []
    try:
        with open('alunos.csv', 'r', encoding='utf-8') as arquivo_csv:
            linhas = arquivo_csv.readlines()[1:]
            for linha in linhas:
                dados = linha.strip().split(',')
                nome, cpf, celular, email = dados[:4]
                idade, peso, altura = map(int, dados[4:7]), list(map(float, dados[7:9]))
                historico_medico = dados[9].split(' | ') if len(dados) > 9 else []
                metas = [{'numero': int(meta.split(' - ')[0]), 'descricao': meta.split(' - ')[1], 'data_limite': meta.split(' - ')[2], 'alcancada': meta.split(' - ')[3] == 'True'} for meta in dados[10].split(' | ')] if len(dados) > 10 else []
                avaliacoes = []
                aluno = Aluno(nome, cpf, celular, email, idade, peso, altura, historico_medico, metas, avaliacoes)
                alunos.append(aluno)
    except FileNotFoundError:
        pass
    return alunos


def salvar_csv(alunos):
    with open('alunos.csv', 'w', encoding='utf-8') as arquivo_csv:
        arquivo_csv.write("Nome,CPF,Celular,Email,Idade,Peso,Altura,Histórico Médico,Metas,Avaliações\n")
        for aluno in alunos:
            historico = ' | '.join(aluno.historico_medico).replace(',', ';')
            metas = ' | '.join([f"{meta['numero']} - {meta['descricao']} - {meta['data_limite']} - {meta['alcancada']}" for meta in aluno.metas]).replace(',', ';')
            avaliacoes = ' | '.join([f"{avaliacao.tipo} - {avaliacao.data} - {avaliacao.descricao} - {avaliacao.presenca_confirmada} - {avaliacao.avaliacao_realizada}" for avaliacao in aluno.avaliacoes]).replace(',', ';')
            arquivo_csv.write(f"{aluno.nome},{aluno.cpf},{aluno.celular},{aluno.email},{aluno.formatar_idade()},{aluno.formatar_pesos()},{aluno.formatar_alturas()},{historico},{metas},{avaliacoes}\n")


def mostrar_menu():
    print("### MENU ###")
    print("1. Cadastrar novo aluno")
    print("2. Adicionar histórico médico a um aluno")
    print("3. Realizar avaliação de um aluno")
    print("4. Visualizar informações de um aluno")
    print("5. Verificar Alertas")
    print("6. Atualizar Alarmes")
    print("7. Modificar Alarmes")
    print("8. Sair")


# Código principal
alunos = carregar_csv()
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
                adicionar_metas(alunos[indice_aluno])  # Adiciona metas ao histórico médico
                salvar_csv(alunos)
                print("Histórico médico e metas adicionados com sucesso!")

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
        if not alunos:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("Alunos disponíveis para visualizar informações:")
            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno.nome}")

            indice_aluno = int(input("Escolha o número do aluno para visualizar informações: ")) - 1
            if 0 <= indice_aluno < len(alunos):
                alunos[indice_aluno].mostrar_informacoes()
            else:
                print("Índice inválido.")

    elif opcao == "5":
        sistema_alertas.verificar_alertas()

    elif opcao == "6":
        if not
                print("Nenhum aluno cadastrado ainda.")
            else:
                print("Alunos disponíveis para visualizar informações:")
                for i, aluno in enumerate(alunos):
                    print(f"{i + 1}. {aluno.nome}")

                indice_aluno = int(input("Escolha o número do aluno para visualizar informações: ")) - 1
                if 0 <= indice_aluno < len(alunos):
                    alunos[indice_aluno].mostrar_informacoes()
                else:
                    print("Índice inválido.")

    elif opcao == "5":
        sistema_alertas.verificar_alertas()

    elif opcao == "6":
        if not alunos:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("Alunos disponíveis para atualizar presença:")
            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno.nome}")

            indice_aluno = int(input("Escolha o número do aluno para atualizar presença: ")) - 1
            if 0 <= indice_aluno < len(alunos):
                aluno = alunos[indice_aluno]
                print(f"Atualizando presença para o aluno {aluno.nome}")
                data_avaliacao = input("Informe a data da sessão de treino (AAAA-MM-DD): ")
                presente = input("O aluno esteve presente? (s/n): ").lower()

                for avaliacao in aluno.avaliacoes:
                    if avaliacao.tipo == "treino" and avaliacao.data == data_avaliacao:
                        avaliacao.presenca_confirmada = presente == 's'

                salvar_csv(alunos)
                salvar_txt(alunos)
                print("Presença atualizada com sucesso!")

    elif opcao == "7":
        if not alunos:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("Alunos disponíveis para modificar alarmes:")
            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno.nome}")

            indice_aluno = int(input("Escolha o número do aluno para modificar alarmes: ")) - 1
            if 0 <= indice_aluno < len(alunos):
                aluno = alunos[indice_aluno]
                print(f"Modificando alarmes para o aluno {aluno.nome}")
                aluno.dias_alerta = int(input("Informe o novo número de dias para alerta: "))
                salvar_csv(alunos)
                salvar_txt(alunos)
                print("Alarmes modificados com sucesso!")

    elif opcao == "8":
        if not alunos:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("Alunos disponíveis para configurar alarmes:")
            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno.nome}")

            indice_aluno = int(input("Escolha o número do aluno para configurar alarmes: ")) - 1
            if 0 <= indice_aluno < len(alunos):
                aluno = alunos[indice_aluno]
                print(f"Configurando alarmes para o aluno {aluno.nome}")
                aluno.dias_alerta = int(input("Informe o número de dias para alerta: "))
                salvar_csv(alunos)
                salvar_txt(alunos)
                print("Alarmes configurados com sucesso!")

    elif opcao == "9":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Escolha uma opção válida.")