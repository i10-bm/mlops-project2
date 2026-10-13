import argparse, mlflow
from mlflow.tracking import MlflowClient

parser = argparse.ArgumentParser()
parser.add_argument("--from", dest="old_alias", required=True)
parser.add_argument("--to", dest="new_alias", required=True)
args = parser.parse_args()

mlflow.set_tracking_uri("http://127.0.0.1:5000")
client = MlflowClient()
model_name = "Boston_Disease_Model"

model_version = client.get_model_version_by_alias(model_name, args.old_alias)
client.delete_registered_model_alias(model_name, args.old_alias)
client.set_registered_model_alias(model_name, args.new_alias, model_version.version)
print(f"Updated alias from '{args.old_alias}' to '{args.new_alias}'")
