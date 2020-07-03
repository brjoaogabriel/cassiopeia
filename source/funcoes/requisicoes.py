from source.funcoes.cadastros import *

#   Funcionando...
def RequisitaJogo():
    #   Responsável por requisitar dados do jogo
    #   id_jogo
    #   time_mandante
    #   time_visitante
    #   data
    #   horario

    print("\nDefinindo dados do jogo...")
    time_mandante   = str(input("Time mandante:             "))
    #time_mandante   = ValidaTime(time_mandante)

    time_visitante  = str(input("Time visitante:            "))
    #time_visitante  = ValidaTime(time_visitante)

    data            = str(input("Data do jogo:              "))
    #data            =   ValidaData(data)

    horario         = str(input("Horario do jogo:           "))
    #horario         = ValidaHorario(horario)
    print()

    CadastraJogo(time_mandante, time_visitante, data, horario)

#   Funcionando...
def RequisitaJogada(id_jogo):
    #   Responsável por requisitar dados da jogada
    #   id_jogo
    #   id_jogada
    #   tempo_inicio
    #   tempo_fim
    #   tipo_jogada
    print("\nDefinindo dados da jogada...")
    tempo_inicio    = str(input("Tempo de inicio:           "))
    #tempo_inicio    = ValidaHorario(tempo_inicio)

    tempo_fim       = str(input("Tempo de fim:              "))
    #tempo_fim       = ValidaHorario(tempo_fim)

    tipo_jogada     = str(input("Tipo da jogada:            "))
    #tipo_jogada     = ValidaJogada(tipo_jogada)
    print()
    
    CadastraJogada(id_jogo, tempo_inicio, tempo_fim, tipo_jogada)

#   Funcionando...
def RequisitaPBP(id_jogo, id_jogada):
    #   Responsável por requisitar dados play by play de cada jogador
    #   id_jogada
    #   tipo_time (time)
    #   posicao
    #   n_jogador
    #   tipo_estat
    #   resultado

    print("\nDefinindo dados PlayByPlay...")
    tipo_time       = str(input("Tipo do time:              "))
    #tipo_time       = ValidaTipoTime(tipo_time)

    __qt_jogadores  = int(input("Qt. jogadores envolvidos:  "))

    for i in range(__qt_jogadores):
        posicao         = str(input("Posicao do jogador:        "))
        n_jogador       = int(input("Identificação do jogador:  "))
        tipo_estat      = str(input("Tipo de estatística:       "))
        resultado     = float(input("Resultado da jogada:       "))
        CadastraPlayByPlay(id_jogo, id_jogada, tipo_time, posicao, n_jogador, tipo_estat, resultado)
        print()