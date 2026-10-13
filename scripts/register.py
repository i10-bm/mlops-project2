import argparse, mlflow
from mlflow.tracking import MlflowClient

parser = argparse.ArgumentParser()
parser.add_argument("--alias", required=True)
args = parser.parse_args()

mlflow.set_tracking_uri("http://127.0.0.1:5000")
client = MlflowClient()
model_name = "Boston_Disease_Model"

latest_version = client.get_latest_versions(model_name)[0].version
client.set_registered_model_alias(model_name, args.alias, latest_version)
print(f"Assigned alias '{args.alias}' to version {latest_version}")
