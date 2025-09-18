# Databricks notebook source
import pandas as pd

#csv no github: https://raw.githubusercontent.com/carvalh0-samuel/Faculdade/main/BigData/dados_veiculos_2025.csv

# Lendo arquivo csv com pandas e gravando em um dataframe pandas
url = "/Workspace/Users/202403616441@alunos.estacio.br/Aula_Teste/dados_veiculos_2025.csv"
pdf = pd.read_csv(url, sep=";", encoding="latin1")

# Convertendo Pandas em Spark
df = spark.createDataFrame(pdf)

display(df)
