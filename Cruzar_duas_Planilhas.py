import pandas as pd
# Vamos carregar as duas planilhas em dois dataframes
# Os dois têm uma chave de string em comum - a coluna "nome"


df_1 = pd.read_excel("Planilha1.xlsx")
print(df_1)


df_2 = pd.read_excel("Planilha2.xlsx")
print(df_2)

# Agora eu uno os dois dataframes, apenas nos casos que possuem nomes iguais
# Os nomes da Planilha1 que não tiverem correspondente na Planilha2,
# ficarão com 'NaN' nos campos da Planilha2
# Será gravada uma planilha "Resultado.csv" com a união das duas planilhas
novo_df = pd.merge(df_1, df_2, left_on='NOME_1', right_on='NOME_2', how="left")
novo_df.info()
print(novo_df)

file_name = "Resultado.csv"

novo_df.to_csv(file_name)
#class 'pandas.core.frame.DataFrame'>
#Int64Index: 3 entries, 0 to 2
#Data columns (total 5 columns):
 #   Column   Non-Null Count  Dtype
#---  ------   --------------  -----
# 0   idade    3 non-null      int64
# 1   time     3 non-null      object
# 2   nome     3 non-null      object
 #3   sexo     3 non-null      object
# 4   veiculo  3 non-null      object
#dtypes: int64(1), object(4)
#memory usage: 96.0+ bytes
#Aqui mais sobre a documentação 1 do merge

