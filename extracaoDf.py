from utils import ler_csv

df = ler_csv('data/olimpiadas.csv')

def extrair_noc():
    try:
        if 'NOC' in df.columns and 'Team' in df.columns:
            df_noc_regiao = df[['NOC', 'Team']].drop_duplicates().rename(columns={'NOC': 'noc', 'Team': 'nome_regiao'})
            df_noc_regiao['id'] = df_noc_regiao.index + 1  
            return df_noc_regiao
    except Exception:
        print('Error')
    
def extrair_cidade():
    try:
        df_cidade = df[['City']].drop_duplicates().reset_index(drop=True)
        df_cidade = df_cidade.rename(columns={'City': 'nome_cidade'})
        df_cidade['id'] = df_cidade.index + 1 
        return df_cidade
    except Exception:
        print('Error')

def extrair_esporte():
    try:
        df_esporte = df[['Sport']].drop_duplicates().reset_index(drop=True)
        df_esporte = df_esporte.rename(columns={'Sport': 'nome_esporte'})
        df_esporte['id'] = df_esporte.index + 1  # Adiciona a coluna 'id'
        return df_esporte
    except Exception:
        print('Error')

def extrair_jogos():
    try:
        df_jogos = df[['Games', 'Year', 'Season']].drop_duplicates().reset_index(drop=True)
        df_jogos = df_jogos.rename(columns={'Games': 'nome_jogos', 'Year': 'ano_jogos', 'Season': 'estacao'})
        df_jogos['id'] = df_jogos.index + 1  
        return df_jogos
    except Exception:
        print('Error')

def extrair_jogos_cidade(df_jogos, df_cidade):
    try:
        df_jogos_cidade = df[['Games', 'City']].drop_duplicates().reset_index(drop=True)
        df_jogos_cidade = df_jogos_cidade.rename(columns={'Games': 'nome_jogos', 'City': 'nome_cidade'})
        df_jogos_cidade = df_jogos_cidade.merge(df_jogos[['id', 'nome_jogos']], left_on='nome_jogos', right_on='nome_jogos', how='left')
        df_jogos_cidade = df_jogos_cidade.merge(df_cidade[['id', 'nome_cidade']], left_on='nome_cidade', right_on='nome_cidade', how='left')
        df_jogos_cidade = df_jogos_cidade.rename(columns={'id_x': 'jogos_id', 'id_y': 'cidade_id'}).drop(columns=['nome_jogos', 'nome_cidade'])
        return df_jogos_cidade
    except Exception:
        print('Error')

def extrair_pessoa():
    try:
        df_pessoa = df[['ID', 'Name', 'Sex', 'Height', 'Weight']].drop_duplicates().reset_index(drop=True)
        df_pessoa = df_pessoa.rename(columns={'ID': 'id', 'Name': 'nome_completo', 'Sex': 'genero', 'Height': 'altura', 'Weight': 'peso'})
        return df_pessoa
    except Exception:
        print('Erro')

def extrair_pessoa_regiao(df_noc_regiao):
    try:
        df_pessoa_regiao = df[['ID', 'NOC']].drop_duplicates().reset_index(drop=True)
        df_pessoa_regiao = df_pessoa_regiao.rename(columns={'ID': 'pessoa_id', 'NOC': 'noc'})
        df_pessoa_regiao = df_pessoa_regiao.merge(df_noc_regiao[['id', 'noc']], left_on='noc', right_on='noc', how='left').drop(columns=['noc'])
        df_pessoa_regiao = df_pessoa_regiao.rename(columns={'id': 'regiao_id'})
        return df_pessoa_regiao
    except Exception:
        print('Error')

def extrair_jogos_competidor(df_jogos):
    try:
        df_jogos_competidor = df[['ID', 'Games', 'Age']].drop_duplicates().reset_index(drop=True)
        df_jogos_competidor = df_jogos_competidor.rename(columns={'ID': 'pessoa_id', 'Games': 'nome_jogos', 'Age': 'idade'})
        df_jogos_competidor = df_jogos_competidor.merge(df_jogos[['id', 'nome_jogos']], left_on='nome_jogos', right_on='nome_jogos', how='left').drop(columns=['nome_jogos'])
        df_jogos_competidor = df_jogos_competidor.rename(columns={'id': 'jogos_id'})
        return df_jogos_competidor
    except Exception:
        print('Error')

def extrair_evento(df_esporte):
    try:
        df_evento = df[['Event', 'Sport']].drop_duplicates().reset_index(drop=True)
        df_evento = df_evento.rename(columns={'Event': 'nome_evento', 'Sport': 'nome_esporte'})
        df_evento = df_evento.merge(df_esporte[['id', 'nome_esporte']], left_on='nome_esporte', right_on='nome_esporte', how='left').drop(columns=['nome_esporte'])
        df_evento = df_evento.rename(columns={'id': 'esporte_id'})
        return df_evento
    except Exception:
        print('Error')

def extrair_medalha():
    try:
        df_medalha = df[['Medal']].drop_duplicates().reset_index(drop=True)
        df_medalha = df_medalha.rename(columns={'Medal': 'nome_medalha'})
        df_medalha['id'] = df_medalha.index + 1  
        return df_medalha
    except Exception:
        print('Error')

def extrair_competidor_evento(df_evento, df_medalha):
    try:
        df_competidor_evento = df[['ID', 'Event', 'Medal']].drop_duplicates().reset_index(drop=True)
        df_competidor_evento = df_competidor_evento.rename(columns={'ID': 'competidor_id', 'Event': 'nome_evento', 'Medal': 'nome_medalha'})
        df_competidor_evento = df_competidor_evento.merge(df_evento[['esporte_id', 'nome_evento']], left_on='nome_evento', right_on='nome_evento', how='left').drop(columns=['nome_evento'])
        df_competidor_evento = df_competidor_evento.merge(df_medalha[['id', 'nome_medalha']], left_on='nome_medalha', right_on='nome_medalha', how='left').drop(columns=['nome_medalha'])
        df_competidor_evento = df_competidor_evento.rename(columns={'id_x': 'evento_id', 'id_y': 'medalha_id'})
        return df_competidor_evento
    except Exception:
        print('Error')
