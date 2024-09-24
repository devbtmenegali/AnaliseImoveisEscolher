import pandas as pd
import matplotlib.pyplot as plt

def importar_dados():

    url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"

    df = pd.read_csv(url, sep = ";")

    return df

def escolher_tipo_imoveis(df):

    #Retorna um array NumPy com os valores únicos encontrados na coluna 'Tipo'.
    tipo_de_imoveis = df['Tipo'].unique()
    print("Lista de imóveis disponíveis: ")

    #A função enumerate() cria um iterador que gera pares (índice, valor) para cada item na sequência tipo_de_imoveis.
    for i, tipo in enumerate(tipo_de_imoveis):
        print(f"{i + 1}. {tipo}")
    

    digitar_escolha = int(input("Digite o tipo de imóvel desejado: "))
    #Acessando o elemento da lista tipo_de_imoveis 
    imovel_escolhido = tipo_de_imoveis[digitar_escolha]

    return imovel_escolhido

def main():

     # Importar os dados
    df = importar_dados()
    
    # Chamar a função para escolher o tipo de imóveis
    escolher_tipo_imoveis(df)

if __name__ =="__main__":
    
    main()