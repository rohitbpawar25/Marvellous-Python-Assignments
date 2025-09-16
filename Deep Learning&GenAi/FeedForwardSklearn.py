# ----------------------------------------------------------
# Feedforward Neural Network Classification using scikit-learn
#
# - Generates synthetic 2D moon-shaped dataset
# - Splits data into training and testing sets
# - Trains MLPClassifier with two hidden layers (16 and 8 neurons)
# - Uses ReLU activation and Adam optimizer
# - Evaluates and prints test accuracy
# ----------------------------------------------------------

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Generate synthetic 2D classification data
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)

# Define and train the FNN model
clf = MLPClassifier(hidden_layer_sizes=(16, 8), activation='relu', solver='adam',
                    max_iter=500, random_state=42)
clf.fit(Xtr, ytr)

# Evaluate model performance
print("Test accuracy:", accuracy_score(yte, clf.predict(Xte)))
