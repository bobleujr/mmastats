import psycopg2
import pandas as pd
import seaborn as sns
import random

# def case1(request):
#

conn = psycopg2.connect(dbname="mmastats", user="common", password="011092", port="5432", host="localhost")
cur = conn.cursor()

# cur.execute("SELECT get_fighter_basics(%s, %s)",('Edson Barboza', 'mycursor'))
cur.execute("SELECT get_fighter_basics_regressor(%s, %s)",('Jimi Manuwa', 'mycursor'))

print cur.fetchone()[0]


cur.execute('FETCH ALL IN "mycursor"')

colnames = [desc[0] for desc in cur.description]

result = cur.fetchall()

# labels = []

df = pd.DataFrame(result)
df.columns = colnames

print type(df[colnames[22]][0])

X = df[colnames[2:21]]
y = df[colnames[22]].astype(float)

print y.head()

print len(X)
if len(X) > 15:
    number_folds = 8
else:
    number_folds = len(X) - 2


from sklearn.neural_network import MLPRegressor


alpha = [1e-3, 1e-4, 1e-5, 1e-6]
max_iter = [50,100,150,200,250,300]
hidden_layer_sizes = [(1,),(2,),(3,),(4,),(5,),(6,),(7,),(8,),
            (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2), (8,2),
            (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3), (8,3),
            (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4), (8,4)]
param_grid = dict(alpha=alpha, max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes)


clf = MLPRegressor(solver='lbfgs', random_state=1, alpha=1e-4, max_iter=200, hidden_layer_sizes=(5,2))
# grid = GridSearchCV(clf, param_grid, cv=number_folds, scoring='accuracy')
clf.fit(X, y)

clf.predict()
print 'chegou ao fim'
# print(grid.best_score_)
# print(grid.best_params_)