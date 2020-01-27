rom sklearn.linear_model import LinearRegression

reg = Ridge()
reg = LinearRegression() # making an object

reg.fit(nd1,nd2)
reg.predict(nd1)

#utils
shuffle

#preprocessing
LabelEncoder, OrdinalEncoder , label_binarize
PolynomialFeatures
MinMaxScaler, StandardScaler, RobustScaler # scale

#model_selection
train_test_split ,  cross_val_score , cross_validate, learning_curve## only one split, cv split only scores, cv split scores and more info, cross_validate on different train_sizes 
GridSearchCV , RandomizedSearchCV , validation_curve # on params


#metrics
from sklearn.metrics import make_scorer
from sklearn.metrics import mean_squared_error, f1_score, accuracy_score, precision_score, recall_score
from sklearn.metrics import confusion_matrix,  classification_report #cnfmatrix = confusion_matrix(Y,predicted_Y)
from sklearn.metrics import precision_recall_curve , roc_curve , roc_auc_score



############################################################

#####
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import RidgeClassifier, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import BaggingClassifier, ExtraTreesClassifier, RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
#####
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Ridge, Lasso, LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
#####
