import sqlite3 as sql

#0.
def InstalaBase():
    try:
        with sql.connect('source\\database\\database.db') as con:
            cur = con.cursor()
            cur.execute('begin')
            try:
                for strSQL in (CriaDatabase, CriaTabelaJogada, CriaTabelaPBP):
                    try:
                        cur.execute(strSQL)
                    except:
                        print(f"Erro na consulta sql: {strSQL}")
                        cur.execute('rollback')
            except:
                print("Erro ao startar instalação de database")
                cur.execute('rollback')
            else:
                cur.execute('commit')

            cur.close()
            return True
    except:
        print("Erro ao criar o database")
        return False

#1.
#   DEU CERTO
CriaDatabase = """
CREATE TABLE Jogos (
    id_jogo             integer primary key autoincrement,
    time_mandante       text,
    time_visitante      text,
    data                text,
    horario             text
)
"""

#2.
#   DEU CERTO
CriaTabelaJogada = """
CREATE TABLE Jogada (
    id_jogo             integer not null,
    id_jogada           integer primary key autoincrement,
    tempo_inicio        text,
    tempo_fim           text,
    tipo_jogada         text,

    foreign key (id_jogo) references Jogos(id_jogo)
)
"""

#3.
#   DEU CERTO
CriaTabelaPBP = """
CREATE TABLE PlayByPlay (
    id_jogo             integer not null,
    id_jogada           integer not null,
    id_pbp              integer primary key autoincrement,
    tipo_time           text,
    posicao             text,
    n_jogador           text,
    tipo_estat          text,
    resultado           integer not null,

    foreign key (id_jogo) references Jogos(id_jogo),
    foreign key (id_jogada) references Jogada(id_jogada)
)
"""