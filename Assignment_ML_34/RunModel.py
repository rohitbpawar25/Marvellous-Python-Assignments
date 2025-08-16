########################################################
# Required Python Packages
########################################################
import joblib
from Assignment34 import Predict_With_User_Input
from sklearn.datasets import load_breast_cancer

########################################################
# Main Execution 
# Loads saved model and predicts cancer diagnosis 
# Using user-provided input features.
########################################################
def main():
    # Load saved model
    model = joblib.load("Assignment_34_Model.pkl")

    # Load feature names
    data = load_breast_cancer()
    feature_names = data.feature_names

    # Call the imported function
    Predict_With_User_Input(model, feature_names)


########################################################
# Run Main
########################################################
if __name__ == "__main__":
    main()

