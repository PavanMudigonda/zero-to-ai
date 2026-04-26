# Data Pipelines for ML Cheatsheet

> Building reliable data pipelines for training, feature engineering, and real-time inference.

---

## Table of Contents

- [Pipeline Orchestration Overview](#pipeline-orchestration-overview)
- [Apache Airflow](#apache-airflow)
- [Prefect](#prefect)
- [Data Validation (Great Expectations)](#data-validation-great-expectations)
- [Streaming for ML (Kafka)](#streaming-for-ml-kafka)
- [Data Lake Architecture](#data-lake-architecture)
- [Cloud Data Services for ML](#cloud-data-services-for-ml)
- [Interview Scenarios](#interview-scenarios)

---

## Pipeline Orchestration Overview

| Tool | Best For | Complexity | Cloud-Native |
|------|----------|------------|--------------|
| **Airflow** | Batch ETL, ML pipelines | High | MWAA (AWS), Cloud Composer (GCP) |
| **Prefect** | Modern ML pipelines | Medium | Prefect Cloud |
| **Dagster** | Data-aware orchestration | Medium | Dagster Cloud |
| **Luigi** | Simple batch pipelines | Low | No |
| **Kubeflow** | ML-specific K8s pipelines | High | GCP (native) |

---

## Apache Airflow

### Setup

```bash
# Install Airflow
pip install "apache-airflow[celery,postgres,redis]==2.8.1" \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt"

# Initialize database
airflow db init

# Create admin user
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin

# Start webserver and scheduler
airflow webserver --port 8080 &
airflow scheduler &
```

### ML Training DAG

```python
# dags/ml_training_pipeline.py
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.operators.s3 import S3CopyObjectOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "ml-team",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": True,
    "email": ["ml-team@example.com"],
}

with DAG(
    "ml_training_pipeline",
    default_args=default_args,
    description="End-to-end ML training pipeline",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["ml", "training"],
) as dag:

    def extract_data(**context):
        """Pull latest data from source."""
        import pandas as pd
        df = pd.read_sql("SELECT * FROM transactions WHERE date = %s",
                         con=get_db_conn(), params=[context["ds"]])
        output_path = f"/tmp/data_{context['ds']}.parquet"
        df.to_parquet(output_path)
        return output_path

    def validate_data(**context):
        """Run data quality checks."""
        import great_expectations as gx
        context_gx = gx.get_context()
        result = context_gx.run_checkpoint("data_quality_check")
        if not result.success:
            raise ValueError(f"Data validation failed: {result}")

    def feature_engineering(**context):
        """Create features for training."""
        import pandas as pd
        ti = context["ti"]
        data_path = ti.xcom_pull(task_ids="extract_data")
        df = pd.read_parquet(data_path)
        # Feature engineering logic
        df["amount_log"] = df["amount"].apply(lambda x: max(0, x)).apply(
            lambda x: __import__("math").log1p(x)
        )
        df["hour_of_day"] = pd.to_datetime(df["timestamp"]).dt.hour
        output_path = f"/tmp/features_{context['ds']}.parquet"
        df.to_parquet(output_path)
        return output_path

    def train_model(**context):
        """Train and log model."""
        import mlflow
        with mlflow.start_run():
            # Training logic
            mlflow.log_param("date", context["ds"])
            mlflow.log_metric("accuracy", 0.95)
            mlflow.sklearn.log_model(model, "model")

    def check_model_quality(**context):
        """Branch: deploy if quality is good enough."""
        accuracy = context["ti"].xcom_pull(task_ids="train_model", key="accuracy")
        if accuracy and accuracy > 0.90:
            return "deploy_model"
        return "notify_team"

    extract = PythonOperator(task_id="extract_data", python_callable=extract_data)
    validate = PythonOperator(task_id="validate_data", python_callable=validate_data)
    features = PythonOperator(task_id="feature_engineering", python_callable=feature_engineering)
    train = PythonOperator(task_id="train_model", python_callable=train_model)
    check = BranchPythonOperator(task_id="check_quality", python_callable=check_model_quality)

    deploy = BashOperator(
        task_id="deploy_model",
        bash_command="az ml online-deployment create --name blue --endpoint prod -f deploy.yml",
    )

    notify = BashOperator(
        task_id="notify_team",
        bash_command='echo "Model quality below threshold, skipping deployment"',
    )

    extract >> validate >> features >> train >> check >> [deploy, notify]
```

### Airflow CLI

```bash
# Test a specific task
airflow tasks test ml_training_pipeline extract_data 2024-01-15

# Trigger a DAG run
airflow dags trigger ml_training_pipeline

# List DAGs
airflow dags list

# Pause/unpause a DAG
airflow dags pause ml_training_pipeline
airflow dags unpause ml_training_pipeline

# Backfill
airflow dags backfill ml_training_pipeline \
  --start-date 2024-01-01 --end-date 2024-01-31
```

---

## Prefect

### Setup

```bash
pip install prefect
```

### ML Pipeline with Prefect

```python
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

@task(retries=2, cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=1))
def load_data(path: str):
    import pandas as pd
    return pd.read_parquet(path)

@task
def validate_data(df):
    assert len(df) > 0, "Empty dataset"
    assert df.isnull().sum().sum() == 0, "Null values found"
    return df

@task
def train_model(df):
    from sklearn.ensemble import RandomForestClassifier
    X, y = df.drop("target", axis=1), df["target"]
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

@task
def evaluate_model(model, test_df):
    X_test, y_test = test_df.drop("target", axis=1), test_df["target"]
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.4f}")
    return accuracy

@flow(name="ml-training-pipeline", log_prints=True)
def training_pipeline(train_path: str, test_path: str):
    # Load data
    train_df = load_data(train_path)
    test_df = load_data(test_path)

    # Validate
    train_df = validate_data(train_df)
    test_df = validate_data(test_df)

    # Train
    model = train_model(train_df)

    # Evaluate
    accuracy = evaluate_model(model, test_df)

    if accuracy > 0.90:
        print("Model passed quality gate!")
    else:
        raise ValueError(f"Model accuracy {accuracy} below threshold")

# Run locally
if __name__ == "__main__":
    training_pipeline(
        train_path="data/train.parquet",
        test_path="data/test.parquet",
    )
```

```bash
# Deploy as scheduled flow
prefect deployment build training_pipeline.py:training_pipeline \
  --name daily-training \
  --cron "0 6 * * *" \
  --pool default-agent-pool

prefect deployment apply training_pipeline-deployment.yaml
```

---

## Data Validation (Great Expectations)

### Setup

```bash
pip install great-expectations
great_expectations init
```

### Define Expectations

```python
import great_expectations as gx

context = gx.get_context()

# Create a data source
datasource = context.sources.add_pandas("my_datasource")
data_asset = datasource.add_dataframe_asset(name="training_data")

# Build expectation suite
suite = context.add_expectation_suite("training_data_quality")

# Add expectations
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(column="user_id")
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeInSet(
        column="transaction_type", value_set=["purchase", "refund", "transfer"]
    )
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="amount", min_value=0, max_value=1000000
    )
)
suite.add_expectation(
    gx.expectations.ExpectTableRowCountToBeBetween(min_value=1000, max_value=10000000)
)
suite.add_expectation(
    gx.expectations.ExpectColumnMeanToBeBetween(
        column="amount", min_value=10, max_value=5000
    )
)

context.save_expectation_suite(suite)
```

### Run Validation

```python
# Validate a DataFrame
import pandas as pd

df = pd.read_parquet("data/training_data.parquet")

batch_request = data_asset.build_batch_request(dataframe=df)

# Create checkpoint
checkpoint = context.add_or_update_checkpoint(
    name="training_data_checkpoint",
    validations=[{
        "batch_request": batch_request,
        "expectation_suite_name": "training_data_quality",
    }],
)

# Run validation
result = checkpoint.run()

if not result.success:
    print("Data validation FAILED!")
    for r in result.run_results.values():
        for er in r["validation_result"]["results"]:
            if not er["success"]:
                print(f"  FAILED: {er['expectation_config']['expectation_type']}")
else:
    print("Data validation PASSED!")
```

---

## Streaming for ML (Kafka)

### Real-Time Feature Pipeline

```python
# Kafka consumer for feature computation
from confluent_kafka import Consumer, Producer
import json

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "feature-pipeline",
    "auto.offset.reset": "latest",
})
consumer.subscribe(["raw-events"])

producer = Producer({"bootstrap.servers": "localhost:9092"})

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue

    event = json.loads(msg.value().decode("utf-8"))

    # Compute real-time features
    features = {
        "user_id": event["user_id"],
        "event_type": event["event_type"],
        "amount": event["amount"],
        "hour_of_day": event["timestamp"] % 86400 // 3600,
        "rolling_avg_amount": compute_rolling_avg(event["user_id"]),
    }

    # Publish features
    producer.produce(
        "computed-features",
        key=str(event["user_id"]),
        value=json.dumps(features),
    )
    producer.flush()
```

### Kafka CLI Quick Reference

```bash
# Create topic
kafka-topics --bootstrap-server localhost:9092 \
  --create --topic raw-events --partitions 6 --replication-factor 3

# List topics
kafka-topics --bootstrap-server localhost:9092 --list

# Consume messages (debug)
kafka-console-consumer --bootstrap-server localhost:9092 \
  --topic computed-features --from-beginning --max-messages 10

# Produce test message
echo '{"user_id": 1, "amount": 50.0}' | \
  kafka-console-producer --bootstrap-server localhost:9092 --topic raw-events

# Check consumer group lag
kafka-consumer-groups --bootstrap-server localhost:9092 \
  --group feature-pipeline --describe
```

---

## Data Lake Architecture

### Medallion Architecture (Bronze / Silver / Gold)

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│   BRONZE    │    │    SILVER    │    │    GOLD     │
│  Raw Data   │───▶│  Cleaned +   │───▶│  ML-Ready   │
│  (as-is)    │    │  Validated   │    │  Features   │
└─────────────┘    └──────────────┘    └─────────────┘
  S3/ADLS/GCS       Deduplicated         Feature tables
  JSON/CSV/Parquet   Schema enforced      Aggregated
  Append-only        Typed columns        Joined datasets
```

### Delta Lake (Lakehouse)

```python
# Write data with Delta Lake
from delta import DeltaTable
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .getOrCreate()

# Write Bronze (raw)
raw_df = spark.read.json("s3://data-lake/raw/events/")
raw_df.write.format("delta").mode("append").save("s3://data-lake/bronze/events/")

# Write Silver (cleaned)
bronze_df = spark.read.format("delta").load("s3://data-lake/bronze/events/")
silver_df = bronze_df.dropDuplicates(["event_id"]).filter("amount > 0")
silver_df.write.format("delta").mode("overwrite").save("s3://data-lake/silver/events/")

# Write Gold (ML features)
silver_df = spark.read.format("delta").load("s3://data-lake/silver/events/")
gold_df = silver_df.groupBy("user_id").agg(
    F.avg("amount").alias("avg_amount"),
    F.count("*").alias("total_events"),
)
gold_df.write.format("delta").mode("overwrite").save("s3://data-lake/gold/user_features/")

# Time travel (read historical version)
df_v1 = spark.read.format("delta").option("versionAsOf", 1).load("s3://data-lake/gold/")
```

---

## Cloud Data Services for ML

### AWS

```bash
# S3: Store training data
aws s3 cp data/ s3://ml-bucket/data/ --recursive

# Glue: Catalog data
aws glue create-crawler --name ml-data-crawler \
  --role GlueRole --database-name ml_data \
  --targets '{"S3Targets": [{"Path": "s3://ml-bucket/data/"}]}'

# Athena: Query data (SQL)
aws athena start-query-execution \
  --query-string "SELECT COUNT(*) FROM ml_data.events WHERE date='2024-01-15'" \
  --result-configuration '{"OutputLocation": "s3://ml-bucket/query-results/"}'

# EMR: Spark processing
aws emr create-cluster \
  --name "ML-Processing" \
  --release-label emr-7.0.0 \
  --applications Name=Spark \
  --instance-type m5.xlarge \
  --instance-count 3
```

### Azure

```bash
# Blob Storage: Store data
az storage blob upload-batch --destination ml-data --source data/

# Synapse: SQL analytics
az synapse sql-script create --workspace-name my-synapse \
  --name "feature-query" --file @query.sql

# Data Factory: ETL pipeline
az datafactory pipeline create \
  --factory-name my-factory \
  --resource-group my-rg \
  --name ml-etl-pipeline \
  --pipeline @pipeline.json
```

### GCP

```bash
# GCS: Store data
gsutil -m cp -r data/ gs://ml-bucket/data/

# BigQuery: SQL analytics
bq query --use_legacy_sql=false \
  "SELECT user_id, AVG(amount) as avg_amount
   FROM \`project.dataset.events\`
   GROUP BY user_id"

# Dataflow: Stream processing
gcloud dataflow jobs run ml-feature-pipeline \
  --gcs-location gs://dataflow-templates/latest/PubSub_to_BigQuery \
  --parameters inputTopic=projects/my-project/topics/events,outputTableSpec=project:dataset.features
```

---

## Interview Scenarios

**Q: How would you build a data pipeline for an ML system?**
> Design depends on latency requirements. For batch: use Airflow/Prefect to orchestrate ETL → data validation (Great Expectations) → feature engineering → write to feature store. For real-time: use Kafka for event streaming → Flink/Spark Streaming for feature computation → write to online feature store (Redis/DynamoDB). Always implement data validation gates before training to catch schema changes and data quality issues.

**Q: How do you handle data quality issues in ML pipelines?**
> Implement multi-layer validation: (1) Schema validation—check types, required fields, value ranges. (2) Statistical validation—check distributions haven't shifted (mean, variance, percentiles). (3) Business rules—domain-specific checks. Use Great Expectations or Pandera. Fail the pipeline early if validation fails. Log data quality metrics to dashboards. Set up alerts for gradual degradation.

**Q: What's the medallion architecture and why use it for ML?**
> Three layers: Bronze (raw, as-is data), Silver (cleaned, deduplicated, typed), Gold (aggregated, ML-ready features). Benefits for ML: clear data lineage, reproducible feature engineering, ability to time-travel to previous data versions (Delta Lake), separation of concerns between data engineering and ML teams, and easier debugging when model quality drops.
