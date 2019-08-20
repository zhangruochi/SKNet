from sknet.sequential import Layer,Sequential,SKNeuron
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import LinearSVR
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer



data = load_breast_cancer()
features = data.data
target = data.target

print(target.shape,features.shape)
## (569,) (569, 30)

NFOLDS = 5 # set folds for out-of-fold prediction



layer1 = Layer([
    SKNeuron(RandomForestRegressor,params = {"random_state": 0}),
    SKNeuron(RandomForestRegressor,params = {"random_state": 1}),
    SKNeuron(AdaBoostRegressor,params = {"random_state": 0}),
    SKNeuron(AdaBoostRegressor,params = {"random_state": 1}),
    SKNeuron(LinearSVR,params = {"random_state": 0}),
    SKNeuron(LinearSVR,params = {"random_state": 1}),
])

layer2 = Layer([
    SKNeuron(Lasso,params = {"random_state": 0}),
    SKNeuron(Lasso,params = {"random_state": 1}),
])

layer3 = Layer([
    SKNeuron(LogisticRegression,params = {"random_state": 0}),
])

print(layer2[0])

# model = Sequential([layer1,layer2,layer3],kf = KFold(ntrain, n_folds= NFOLDS, random_state=0))
# model.fit(X_train,y_train)

# predicted = model.predict(X_test)