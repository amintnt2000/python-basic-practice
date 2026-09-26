from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


data = load_breast_cancer(as_frame=True)
df = data.frame
X = df.drop(columns = ["target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(random_state=42))
])
pipeline.fit(X_train, y_train)

scores = cross_val_score(pipeline, X, y, cv=5)

joblib.dump(pipeline, "my_model.joblib")
loaded_pipeline = joblib.load("my_model.joblib")

y_pred = loaded_pipeline.predict(X_test)

print("Scores per fold:", scores)
print(f"Mean accuracy: {scores.mean():.4f}")
print(f"Std deviation: {scores.std():.4f}")
print(accuracy_score(y_test, y_pred))

