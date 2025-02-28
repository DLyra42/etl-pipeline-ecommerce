# ETL Pipeline for E-commerce Data Analysis

## Overview
This project implements an **ETL (Extract, Transform, Load)** pipeline to analyze e-commerce data. The pipeline extracts data from a Kaggle dataset, cleans and transforms it, and loads it into **Google BigQuery** for further analysis.

## Key Features
- **Extract**: Downloads the dataset from Kaggle.
- **Transform**: Calculates total revenue, sales by country, and sales by category.
- **Load**: Uploads the transformed data to Google BigQuery.

## Prerequisites
1. **Python 3.8+**: Install Python from [python.org](https://www.python.org/).
2. **Google Cloud Platform (GCP) Account**: Set up a GCP account and create a project.
3. **Service Account Key**: Generate a service account key with BigQuery access and save it as `config/gcp_config.json`.
4. **Kaggle Account**: Create a Kaggle account and download your API token (`kaggle.json`).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/etl-ecommerce-pipeline.git