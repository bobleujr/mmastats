import psycopg2
import pandas as pd
import seaborn as sns
import random

# def case1(request):
#

conn = psycopg2.connect(dbname="mmastats", user="common", password="011092", port="5432", host="localhost")
cur = conn.cursor()

cur.execute("SELECT get_fighter_basics(%s, %s)",('Edson Barboza', 'mycursor'))

print cur.fetchone()[0]


cur.execute('FETCH ALL IN "mycursor"')

colnames = [desc[0] for desc in cur.description]

result = cur.fetchall()

# labels = []

df = pd.DataFrame(result)
df.columns = colnames

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


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# print X_train
# print X_test

# instantiate
linreg = LinearRegression()

# fit the model to the training data (learn the coefficients)
linreg.fit(X_train, y_train)

# print list(zip(colnames[2:20], linreg.coef_))

print X_test

print 'RESULT'
y_pred = linreg.predict(X_test)

print y_pred
# print(np.sqrt(metrics.mean_squared_error(true, pred)))