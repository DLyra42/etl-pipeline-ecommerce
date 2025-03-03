# ETL Pipeline for E-commerce Data Analysis (EN)

## Overview
This project implements an **ETL (Extract, Transform, Load)** pipeline to analyze e-commerce data. 
The pipeline extracts data from a Kaggle dataset, cleans and transforms it, and loads it into **Google BigQuery** for further analysis.

## Key Features
- **Extract**: Downloads the dataset from Kaggle.
   https://www.kaggle.com/datasets/carrie1/ecommerce-data/data
- **Transform**: Calculates total revenue, sales by country, and sales by category.
- **Load**: Uploads the transformed data to Google BigQuery.
- **Visualization**: Plots total revenue, sales by country, and sales by category in Looker Studio
   https://lookerstudio.google.com/reporting/c33ffe0a-e993-4acb-a1cf-b29d2cac0bdb
- **Automation**: Uses Google Cloud Storage, Run and Scheduler to update the pipeline weekly

## Prerequisites
1. **Python 3.8+**: Install Python from [python.org](https://www.python.org/).
2. **Google Cloud Platform (GCP) Account**: Set up a GCP account and create a project.
3. **Service Account Key**: Generate a service account key with BigQuery access and save it as `config/gcp_config.json`.
4. **Kaggle Account**: Create a Kaggle account and download your API token (`kaggle.json`).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/etl-ecommerce-pipeline.git

## Further Details
- **Doc**: https://docs.google.com/document/d/1qmzXRbRrlhXhmb1DvJBzfOqYBsk7Tf3EejJtL2orz1k/edit?usp=sharing

------------------------------------------------------------------------------------------------------------------

# Pipeline ETL para Análise de Dados de E-commerce (PT-BR)

## Visão Geral
Este projeto implementa um pipeline ETL (Extract, Transform, Load) para analisar dados de e-commerce.
O pipeline extrai dados de um conjunto de dados do Kaggle, limpa e transforma esses dados, e os carrega no Google BigQuery para análise posterior.

## Principais Funcionalidades
- **Extração((: Baixa o conjunto de dados do Kaggle.
https://www.kaggle.com/datasets/carrie1/ecommerce-data/data
- **Transformação**: Calcula a receita total, vendas por país e vendas por categoria.
- **Carregamento**: Envia os dados transformados para o Google BigQuery.
- **Visualização**: Plota a receita total, vendas por país e vendas por categoria no Looker Studio
https://lookerstudio.google.com/reporting/c33ffe0a-e993-4acb-a1cf-b29d2cac0bdb
- **Automação**: Utiliza o Google Cloud Storage, Run e Scheduler para atualizar o pipeline semanalmente.

## Pré-requisitos
1.**Python 3.8+**: Instale o Python a partir de python.org.
2.**Conta no Google Cloud Platform (GCP)**: Crie uma conta no GCP e um projeto.
3.**Chave de Conta de Serviço**: Gere uma chave de conta de serviço com acesso ao BigQuery e salve-a como 4.config/gcp_config.json.
**Conta no Kaggle**: Crie uma conta no Kaggle e baixe seu token de API (kaggle.json).

## Instalação
Clone o repositório:
```bash
git clone https://github.com/seu-usuario/etl-ecommerce-pipeline.git
```

## Detalhes Adicionais
- **Documentação**: https://docs.google.com/document/d/1qmzXRbRrlhXhmb1DvJBzfOqYBsk7Tf3EejJtL2orz1k/edit?usp=sharing
