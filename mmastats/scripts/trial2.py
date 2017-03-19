import psycopg2
import pandas as pd
import seaborn as sns
import random

# def case1(request):
#

conn = psycopg2.connect(dbname="mmastats", user="common", password="011092", port="5432", host="localhost")
cur = conn.cursor()

# cur.execute("SELECT get_fighter_basics(%s, %s)",('Edson Barboza', 'mycursor'))
cur.execute("SELECT get_fighter_basics(%s, %s)",('Anderson Silva', 'mycursor'))

print cur.fetchone()[0]


cur.execute('FETCH ALL IN "mycursor"')

colnames = [desc[0] for desc in cur.description]

result = cur.fetchall()

# labels = []

df = pd.DataFrame(result)
df.columns = colnames

print df

# sns.pairplot(df, x_vars=[colnames[21]],y_vars=colnames[2:5], size=7, aspect=0.7, kind='reg')


# import model
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
# import numpy as np
# from sklearn import metrics

X = df[colnames[2:21]]
y = df[colnames[22]]

# print X
# print y

# X = iris.data
# y = iris.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# print X_train
# print X_test



from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score


logreg = LogisticRegression()

if len(X) > 10:
    number_folds = 10
else:
    number_folds = len(X) - 2

print(cross_val_score(logreg, X, y, cv=number_folds, scoring='accuracy').mean())

from sklearn.neighbors import KNeighborsClassifier


k_range = list(range(1, len(X)-2))
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=number_folds, scoring='accuracy')
    k_scores.append(scores.mean())
print(k_scores)


from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=4)
print(cross_val_score(clf, X, y, cv=number_folds, scoring='accuracy').mean())