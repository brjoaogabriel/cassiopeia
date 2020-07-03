from source.funcoes.requisicoes import *

#   Criar um jeito do computador armazenar a ID da ultima jogada apontada para levar para todas as outras rotinas
#   A requisição de cadastro tem que retornar a ID da play cadastrada

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
                    1.  Cadastrar Jogada
                    
                    0.  Sair
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
                                
                                    0.  Sair
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

                    0.  Sair
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