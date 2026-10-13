import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("MLOps_Boston_Disease")

data = fetch_openml(name='breast_cancer', version=1, as_frame=True)
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run(run_name="RandomForest"):
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)
    acc = rf.score(X_test, y_test)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(rf, "model", registered_model_name="Boston_Disease_Model")
    print(f"Model Accuracy: {acc}")
