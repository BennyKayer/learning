# OpenCV + SVM na wylosowanej próbce

from sklearn.datasets import make_classification as mc # Do generacji danych dla problemów klasyfikacyjnych lub regresyjnych
from sklearn.model_selection import train_test_split as tts # Do podziału danych
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Do inicjalizacji generatora liczb pseudolosowych
RANDOM_STATE = 5958

# Funkcja tworzy próbkę danych do klasyfikacji
X, y = mc(n_samples=100, n_features=2, n_redundant=0, n_classes=2, random_state=RANDOM_STATE)
									
# Rysujemy wykres rozkładu wylosowanych punktów
plt.style.use('ggplot')
plt.set_cmap('jet')
plt.scatter(X[:, 0], X[:, 1], c=y, s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Randomly generated points')
plt.show()

# Chcemy, aby predyktory były liczbami zmiennoprzecinkowymi
X = X.astype(np.float32)
# Chcemy, aby zmienna celu miała wartości -1 i +1
y = y * 2 - 1									

# Tworzymy zbiór treningowy (80%) i testowy (20%)
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=RANDOM_STATE)

# Tworzymy model svm korzystając z OpenCV i ML
svm = cv2.ml.SVM_create()
knn = cv2.ml.KNearest_create()

# Spróbujemy rozdzielić zbiór na dwie klasy za pomocą linii prostej - wybieramy kernel
svm.setKernel(cv2.ml.SVM_NU)


# Trenujemy model
svm.train(X_train, cv2.ml.ROW_SAMPLE, y_train)
knn.train(X_train, cv2.ml.ROW_SAMPLE, y_train)

# Dokonujemy predykcji wartości zmiennej celu na podstawie zbioru testowego
_, y_pred = svm.predict(X_test)
_, knn_y_pred = knn.predict(X_test)

# Sprawdzamy jakość modelu 
print("Accuracy = {}%".format(metrics.accuracy_score(y_test, y_pred)*100))
print(f"Accuracy {metrics.accuracy_score(y_test, knn_y_pred) * 100}%")

# Tworzymy funkcję rysującą półpłaszczyzny podziału
def plot_decision_boundary(svm, X_test, y_test):
    # Predykcja dla poszczególnych punktów siatki
    h = 0.02  # rozmiar kroku na siatce
    x_min, x_max = X_test[:, 0].min() - 1, X_test[:, 0].max() + 1
    y_min, y_max = X_test[:, 1].min() - 1, X_test[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))    
    X_hypo = np.c_[xx.ravel().astype(np.float32), yy.ravel().astype(np.float32)]
    _, zz = svm.predict(X_hypo)
    zz = zz.reshape(xx.shape)    
    plt.contourf(xx, yy, zz, cmap=plt.cm.coolwarm, alpha=0.8)
    # Dodanie do wykresu danych testowych
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, s=200)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('SVM results on a test data')
    plt.show()


# Rysujemy wykres wynikowy
plot_decision_boundary(svm, X_test, y_test)
plot_decision_boundary(knn, X_test, y_test)


