



import sqlite3 as sql

#   Funcionando...
def InsereBase(strSQL, parametros):
    try:
        with sql.connect('source\\database\\database.db') as con:
            cur = con.cursor()
            try:
                print("começando transação...")
                cur.execute("begin")
                print(f"realizando transação... {strSQL} - {parametros}")
                cur.execute(strSQL, parametros)
                print("comittando transação")
                cur.execute("commit")
            except:
                print("Erro - InsereBase (cursor)")
                return False
            else:
                return cur.lastrowid
    except:
        print("Erro - InsereBase (conexão)")
        return False

#CadastraJogo(time_mandante, time_visitante, data, horario)
def CadastraJogo(mandante, visitante, data, horario):
    try:
        __par = (mandante, visitante, data, horario)
        __consulta_sql = "INSERT INTO Jogos (time_mandante, time_visitante, data, horario) VALUES (?,?,?,?)"
        __her = InsereBase(__consulta_sql, __par)
        return __her
    except:
        print("Erro - CadastraJogo")
        return False

#CadastraJogada(id_jogo, tempo_inicio, tempo_fim, tipo_jogada)
def CadastraJogada(id_jogo, inicio, fim, tipo):
    try:
        __par = (id_jogo, inicio, fim, tipo)
        __consulta_sql = "INSERT INTO Jogada (id_jogo, tempo_inicio, tempo_fim, tipo_jogada) VALUES (?,?,?,?)"
        __her = InsereBase(__consulta_sql, __par)
        return __her
    except:
        print("Erro - CadastraJogo")
        return False

#CadastraPlayByPlay(tipo_time, posicao, n_jogador, tipo_estat, resultado)
def CadastraPlayByPlay(id_jogo, id_jogada, time, posicao, ident, tipo, resultado):
    try:
        __par = (id_jogo, id_jogada, time, posicao, ident, tipo, resultado)
        __consulta_sql = "INSERT INTO PlayByPlay (id_jogo, id_jogada, tipo_time, posicao, n_jogador, tipo_estat, resultado) VALUES (?,?,?,?,?,?,?)"
        __her = InsereBase(__consulta_sql, __par)
        return __her
    except:
        print("Erro - CadastraJogo")
        return False

print(CadastraJogo('time 1', 'time 2', '15/03/2020', '15:00'))