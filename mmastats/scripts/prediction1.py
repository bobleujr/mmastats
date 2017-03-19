import psycopg2
import pandas as pd
# import seaborn as sns
import random

# def case1(request):
#

conn = psycopg2.connect(dbname="mmastats", user="common", password="011092", port="5432", host="localhost")
cur = conn.cursor()

cur.execute("SELECT get_fighter_basics(%s, %s)",('Jimi Manuwa', 'mycursor'))

cur.fetchone()[0]


cur.execute('FETCH ALL IN "mycursor"')

colnames = [desc[0] for desc in cur.description]

result = cur.fetchall()

df = pd.DataFrame(result)

cur.close()

cur = conn.cursor()

cur.execute("SELECT get_fighter_basics(%s, %s)",('Corey Anderson', 'mycursor1'))

cur.fetchone()[0]

cur.execute('FETCH ALL IN "mycursor1"')

df.add(pd.DataFrame(cur.fetchall()))

cur.close()

print 'shape'
print df.shape

df.columns = colnames

# print df

X = df[colnames[2:22]]
y = df[colnames[22]]


cur = conn.cursor()

cur.execute("SELECT get_fighter_basics_tp(%s, %s, %s)",('Jimi Manuwa','Corey Anderson', 'mycursor2'))

cur.fetchone()[0]


cur.execute('FETCH ALL IN "mycursor2"')

colnames_pred = [desc[0] for desc in cur.description]

result_pred = cur.fetchall()

df_pred = pd.DataFrame(result_pred)
df_pred.columns = colnames_pred

X_pred = df_pred[colnames_pred[2:]]

from sklearn.neural_network import MLPClassifier


alpha = 1e-4
max_iter = 200
hidden_layer_sizes = (5,2)
# param_grid = dict(alpha=alpha, max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes)


mlp = MLPClassifier(solver='lbfgs', random_state=1, alpha=alpha, max_iter=max_iter, hidden_layer_sizes
                    =hidden_layer_sizes)

mlp.fit(X,y)
print list(mlp.predict(X_pred))



cur = conn.cursor()

cur.execute("SELECT get_fighter_basics_tp(%s, %s, %s)",('Corey Anderson','Jimi Manuwa', 'mycursor3'))

cur.fetchone()[0]


cur.execute('FETCH ALL IN "mycursor3"')

colnames_pred = [desc[0] for desc in cur.description]

result_pred = cur.fetchall()

df_pred = pd.DataFrame(result_pred)
df_pred.columns = colnames_pred

X_pred = df_pred[colnames_pred[2:]]

from sklearn.neural_network import MLPClassifier


# alpha = 1e-4
# max_iter = 200
# hidden_layer_sizes = (5,2)
# param_grid = dict(alpha=alpha, max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes)


# mlp = MLPClassifier(solver='lbfgs', random_state=1, alpha=alpha, max_iter=max_iter, hidden_layer_sizes
#                     =hidden_layer_sizes)

# mlp.fit(X,y)
print list(mlp.predict(X_pred))