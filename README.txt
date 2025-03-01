# ETL Pipeline for E-commerce Data Analysis

## Overview
This project implements an **ETL (Extract, Transform, Load)** pipeline to analyze e-commerce data. The pipeline extracts data from a Kaggle dataset, cleans and transforms it, and loads it into **Google BigQuery** for further analysis.

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
