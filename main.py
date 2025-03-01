# Initialize GCS client
def initialize_gcs_client():
    """
    Initializes the Google Cloud Storage client.

    Returns:
        storage.Client: The GCS client object.
    """
    return storage.Client()

# Upload a file to GCS
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a file to Google Cloud Storage.

    Args:
        bucket_name (str): Name of the GCS bucket.
        source_file_name (str): Path to the local file to upload.
        destination_blob_name (str): Name of the file in GCS.
    """
    client = initialize_gcs_client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Download a file from GCS
def download_from_gcs(bucket_name, source_blob_name, destination_file_name):
    """
    Downloads a file from Google Cloud Storage.

    Args:
        bucket_name (str): Name of the GCS bucket.
        source_blob_name (str): Name of the file in GCS.
        destination_file_name (str): Path to save the downloaded file.
    """
    client = initialize_gcs_client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"File {source_blob_name} downloaded to {destination_file_name}.")

# Save cleaned data to GCS
def save_cleaned_data_to_gcs(data, bucket_name, file_name):
    """
    Saves cleaned data to Google Cloud Storage.

    Args:
        data (pd.DataFrame): The cleaned dataset.
        bucket_name (str): Name of the GCS bucket.
        file_name (str): Name of the file in GCS.
    """
    local_file = "/tmp/cleaned_data.csv"  # Temporary local file
    data.to_csv(local_file, index=False)
    upload_to_gcs(bucket_name, local_file, file_name)

# Load raw data from GCS
def load_raw_data_from_gcs(bucket_name, file_name):
    """
    Loads raw data from Google Cloud Storage.

    Args:
        bucket_name (str): Name of the GCS bucket.
        file_name (str): Name of the file in GCS.

    Returns:
        pd.DataFrame: The raw dataset.
    """
    local_file = "/tmp/raw_data.csv"  # Temporary local file
    download_from_gcs(bucket_name, file_name, local_file)
    return pd.read_csv(local_file)

# Extract data
def extract_data():
    """
    Downloads the dataset from Kaggle and loads it into a pandas DataFrame.

    Returns:
        pd.DataFrame: The extracted dataset.
    """
    od.download("https://www.kaggle.com/datasets/carrie1/ecommerce-data/data")
    try:
        data = pd.read_csv("/content/ecommerce-data/data.csv", encoding='latin-1')
    except UnicodeDecodeError:
        data = pd.read_csv("/content/ecommerce-data/data.csv", encoding='ISO-8859-1')
    return data

# Inspect data
def inspect_data(data):
    """
    Inspects the dataset for basic information and missing values.

    Args:
        data (pd.DataFrame): The dataset to inspect.
    """
    print("Dataset Head:")
    print(data.head())
    print("\nDataset Info:")
    print(data.info())
    print("\nMissing Values:")
    print(data.isnull().sum())

# Clean data
def clean_data(data):
    """
    Cleans the dataset by handling missing values, removing invalid rows, and dropping duplicates.

    Args:
        data (pd.DataFrame): The dataset to clean.

    Returns:
        pd.DataFrame: The cleaned dataset.
    """
    data.dropna(subset=['CustomerID', 'Description'], inplace=True)
    data['Description'].fillna('Unknown', inplace=True)
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data = data[data['Quantity'] > 0]
    data = data[data['UnitPrice'] > 0]
    data.drop_duplicates(inplace=True)
    return data

# Transform data
def transform_data(data):
    """
    Transforms the dataset by calculating total revenue, sales by country, and sales by category.

    Args:
        data (pd.DataFrame): The dataset to transform.

    Returns:
        pd.DataFrame: The transformed dataset.
    """
    data['TotalRevenue'] = data['Quantity'] * data['UnitPrice']
    total_revenue = data['TotalRevenue'].sum()
    print(f"Total Revenue: ${total_revenue: .2f}")

    sales_per_country = data.groupby('Country')['InvoiceNo'].nunique().reset_index(name='NumberOfSales')
    print("\nSales by Country:")
    print(sales_per_country)

    sales_by_category = data.groupby('Description')['TotalRevenue'].sum().reset_index(name='TotalRevenue')
    print("\nSales by Category:")
    print(sales_by_category.sort_values(by='TotalRevenue', ascending=False))

    return data

# Load data into BigQuery
def load_data(data, project_id, dataset_id, table_id, credentials_path):
    """
    Loads the transformed data into Google BigQuery.

    Args:
        data (pd.DataFrame): The dataset to load.
        project_id (str): The GCP project ID.
        dataset_id (str): The BigQuery dataset ID.
        table_id (str): The BigQuery table ID.
        credentials_path (str): Path to the GCP service account key.
    """
    try:
        pandas_gbq.to_gbq(
            data,
            destination_table=f"{dataset_id}.{table_id}",
            project_id=project_id,
            if_exists="replace",
            credentials_path=credentials_path
        )
        print(f"Data uploaded to BigQuery: {dataset_id}.{table_id}")
    except Exception as e:
        print(f"Error loading data into BigQuery: {e}")

# Main function
def main():
    # Set up
    project_id = os.getenv("composed-hold-452215-v4")
    dataset_id = os.getenv("composed-hold-452215-v4.ecommerce_data")
    table_id = os.getenv("composed-hold-452215-v4.ecommerce_data.sales_report")
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    bucket_name = "amentoria" 

    # Step 1: Extract Data
    print("Extracting data...")
    data = extract_data()

    # Step 2: Inspect Data
    print("\nInspecting data...")
    inspect_data(data)

    # Step 3: Clean Data
    print("\nCleaning data...")
    data = clean_data(data)

    # Step 4: Save Cleaned Data to GCS
    cleaned_data_file = "cleaned_data.csv"
    save_cleaned_data_to_gcs(data, bucket_name, cleaned_data_file)

    # Step 5: Transform Data
    print("\nTransforming data...")
    data = transform_data(data)

    # Step 6: Load Data into BigQuery
    print("\nLoading data into BigQuery...")
    load_data(data, project_id, dataset_id, table_id, credentials_path)

    print("\nETL pipeline completed successfully!")

if __name__ == "__main__":
    main()
     
