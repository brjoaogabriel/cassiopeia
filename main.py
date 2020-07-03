#   Biliotecas importadas
from source.funcoes.requisicoes  import *       # Responsável por solicitar as entradas do usuário
from source.database.sql         import *       # Responsável por fazer instalação de banco de dados, se necessário

SolicitaInstalacao()

print("Inciaindo o sistema...")

#....................................................................................................................
#
#                       Descrição do sistema
#   Banco de dados: Local
#   Tecnologias:    Python, SQLite
#   Criador por:    brjoaogabriel (https://github.com/brjoaogabriel?tab=repositories)
#   Criado em:      3/7/2020
#   Versão:         1.0.0
#   O que é:        Aplicação utilizada para realizar apontamentos estatísticos de partidas de futebol americano
#   Para quem é:    Treinadores com noção avançada em informática
#   Quanto custou:  A ideia levou 3 horas para ser consolidada e 3 para ser concretizada, um custo total de R$282,50
#   Como funciona:  O usuário deve seguir somente as opções informadas pelos menus, sendo o responsável pela integri_
#                       dade do banco de dados e do código.
#   Como usar:      O usuário deve conseguir trabalhar com vetores e consultas sql para poder extrair os dados e modelar
#
#   Não tenho noções avançadas e gostaria de utilizar
#       Entre em contato comigo através de:
#       -   Github:     https://github.com/brjoaogabriel?tab=repositories
#       -   Linkedin:   https://www.linkedin.com/in/jo%C3%A3o-gabriel-maciel-288637163/
#       -   WhatsApp:   +55 15 99109645
#
#   Caso tenha gostado da ideia e queira contribuir financeiramente ou com mão de obra, entre em contato para que possamos
#       democratizar o acesso a informação para os times de futebol americano do Brasil!
#
#....................................................................................................................


application: bool
application = True
while application == True:
    __opcoes = range(4)
    print("""\n
    1.  Cadastrar Jogo
    2.  Cadastrar Jogada
    3.  Cadastrar PlayByPlay

    0.  Sair
    \n""")
    __user = int(input("Insira a opção desejada: "))
    if __user not in __opcoes:
        print("Por favor, insira uma opção válida!")
    else:
        if __user == 1:
            id_herd = RequisitaJogo()
            application = True
            application2: bool
            application2 = True
            while application2 == True:
                __opcoes2 = range(2)
                print("""\n
                1.  Cadastrar
                    
                0.  Voltar
                \n""")
                __user2 = int(input("Insira a opção desejada: "))
                if __user2 not in __opcoes2:
                    print("Por favor, insira uma opção válida!")
                else:
                    if __user2 == 1:
                        id_herd2 = RequisitaJogada(id_herd)
                        application3: bool
                        application3 = True
                        while application3 == True:
                            __opcoes3 = range(2)
                            print("""\n
                            1.  Cadastrar PlayByPlay
                                
                            0.  Voltar
                            \n""")
                            __user3 = int(input("Insira a opção desejada: "))

                            if __user3 not in __opcoes3:
                                print("Por favor, insira uma opção válida!")
                            else:
                                if __user3 == 1:
                                    for i in range(2):
                                        id_herd3 = RequisitaPBP(id_herd, id_herd2)
                                        application3 = False

                                elif __user3 == 0:
                                    print("\nOK\n")
                                    application3 = False
                                else:
                                    print("\nNenhuma opção escolhida\n")
                                    application3 = True

                    elif __user2 == 0:
                        print("\nOK\n")
                        application2 = False

                    else:
                        print("\nNenhuma opção escolhida\n")
                        application2 = True

        elif __user == 2:
            id_req = int(input("Qual é a id do jogo:       "))
            id_herd = RequisitaJogada(id_req)
            application2: bool
            application2 = True
            while application2 == True:
                __opcoes2 = range(2)
                print("""\n
                1.  Cadastrar PlayByPlay

                0.  Voltar
                \n""")
                __user2 = int(input("Insira a opção desejada: "))
                if __user2 not in __opcoes2:
                    print("Por favor, insira uma opção válida!")
                else:
                    if __user2 == 1:
                        for i in range(2):
                            RequisitaPBP(id_req, id_herd)
                            application3 = False
                    elif __user2 == 0:
                        print("\nOK\n")
                        application2 = False
                    else:
                        print("\nNenhuma opção escolhida\n")
                        application3 = True
                
            application = True
        
        elif __user == 3:
            id_req = int(input("Qual é a id do jogo:       "))
            id_req2= int(input("Qual é a id da jogada:       "))
            id_herd = RequisitaPBP(id_req, id_req2)

            application = True
        
        elif __user == 0:
            print("\nFinalizando a execução\n")
            application = False
        
        else:
            print("\nNenhuma opção foi escolhida\n")

            application = True