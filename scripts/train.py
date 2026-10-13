import mlflow
import mlflow.sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset directly from sklearn (no network fetching issues)
data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("Boston_Disease_Model")

with mlflow.start_run():
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(clf, "model", registered_model_name="Boston_Disease_Model")
    print(f"Model trained with accuracy: {acc}")
