from models import *
from conexaoBd import conectar_bd, desconectar_bd
from utils import inserir_bd
from extracaoDf import*

def main():
    try:
        motor, sessao = conectar_bd()
        Base.metadata.create_all(bind=motor)

        df_noc_regiao = extrair_noc()
        inserir_bd(df_noc_regiao, 'noc_regiao', motor)

        df_cidade = extrair_cidade()
        inserir_bd(df_cidade, 'cidade', motor)

        df_esporte = extrair_esporte()
        inserir_bd(df_esporte, 'esporte', motor)

        df_jogos = extrair_jogos()
        inserir_bd(df_jogos, 'jogos', motor)
            
        df_jogos_cidade = extrair_jogos_cidade(df_jogos, df_cidade)
        inserir_bd(df_jogos_cidade, 'jogos_cidade', motor)

        df_pessoa = extrair_pessoa()
        inserir_bd(df_pessoa, 'pessoa', motor)

        df_pessoa_regiao = extrair_pessoa_regiao(df_noc_regiao)
        inserir_bd(df_pessoa_regiao,'pessoa_regiao', motor)

        df_jogos_competidor = extrair_jogos_competidor(df_jogos)
        inserir_bd(df_jogos_competidor,'jogos_competidor', motor)

        df_evento = extrair_evento(df_esporte)
        inserir_bd(df_evento, 'evento', motor)

        df_medalha = extrair_medalha()
        inserir_bd(df_medalha, 'medalha', motor)

        df_competidor_evento = extrair_competidor_evento(df_evento, df_medalha)
        inserir_bd(df_competidor_evento, 'competidor_evento', motor)
    except Exception as ex:
        print(f'Error{ex}')
    finally:
        desconectar_bd(sessao)

if __name__ == "__main__":
    main()