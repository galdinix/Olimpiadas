import pandas as pd

def ler_csv(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo CSV não encontrado em {caminho_arquivo}")
    except pd.errors.EmptyDataError:
        print(f"Erro: Arquivo CSV vazio em {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV em {caminho_arquivo}: {e}")
        return None
    
def inserir_bd(df, tabela, motor):
    try:
        df.to_sql(tabela, motor, if_exists='replace', index=False)
    except Exception:
        print('Error')