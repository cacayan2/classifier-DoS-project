from sklearn.metrics import classification_report, confusion_matrix
import pickle

def fit_model(model, X_train, y_train):
    """
    Fits any scikit-learn model using the training data.
    Returns the trained model.
    """
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluates a trained model on test data.
    Prints confusion matrix and classification report.
    Returns both objects.
    """
    y_pred = model.predict(X_test)

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n")
    print(cm)

    # Precision, Recall, F1-score
    report = classification_report(y_test, y_pred)
    print("\nClassification Report:\n")
    print(report)

    return cm, report


def save_model(model, path):
    """
    Saves a trained model to disk as a .pkl file using pickle.
    """
    with open(path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {path}")