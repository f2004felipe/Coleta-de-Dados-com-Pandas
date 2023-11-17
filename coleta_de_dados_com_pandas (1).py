#https://docs.google.com/spreadsheets/d/1O3W46SZpmI77fyufgWKDN-9N8mCTCIhNstaH2uDPiNc/edit?usp=sharing
import pandas as pd
import matplotlib.pyplot as plt

sheet_id = '1O3W46SZpmI77fyufgWKDN-9N8mCTCIhNstaH2uDPiNc'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
df

# Enviar os dados de cada coluna para suas repequitivas variaveis
respostaSalario = df.iloc[:,1]
respostaOpcao = df.iloc[:,2]
respostaInvestir = df.iloc[:,3]
respostaQual = df.iloc[:,4]
respostaInvestimento = df.iloc[:,5]

# Contar a quantidade de elementos em cada variavel
contagemSalario = respostaSalario.value_counts()
contagemOpçao = respostaOpcao.value_counts()
contagemInvestir = respostaInvestir.value_counts()
contagemQual = respostaQual.value_counts()
contagemInvestimento = respostaInvestimento.value_counts()

# Grafico de Quantidade Salarial
categoriaSalario = contagemSalario.index
valorSalario = contagemSalario.values

plt.pie(valorSalario, labels=categoriaSalario, autopct='%1.1f%%', startangle=140)
plt.title('Qual a sua faixa salarial?')

plt.show()

# Grafico de Investimento
categoriaOpcao = contagemOpçao.index
valorOpcao = contagemOpçao.values

plt.pie(valorOpcao, labels=categoriaOpcao, autopct='%1.1f%%', startangle=140)
plt.title('Você tem alguma opção de investimento?')

plt.show()

# Grafico de Opcões de Investimento
categoriaInvestir = contagemInvestir.index
valorInvestir = contagemInvestir.values

plt.pie(valorInvestir, labels=categoriaInvestir, autopct='%1.1f%%', startangle=140)
plt.title('Você investe seu dinheiro?')

plt.show()

#Grafico das opções de investimento
categoriaQual = contagemQual.index
valorQual = contagemQual.values

plt.pie(valorQual, labels=categoriaQual, autopct='%1.1f%%', startangle=140)
plt.title('Se a resposta for sim, qual seu investimento?')

plt.show()

# Grafico de querer Investir
categoriaInvestimento = contagemInvestimento.index
valorInvestimento = contagemInvestimento.values

plt.pie(valorInvestimento, labels=categoriaInvestimento, autopct='%1.1f%%', startangle=140)
plt.title('Quantos porcento você guarda do seu salário por mês para investir?')

plt.show()
