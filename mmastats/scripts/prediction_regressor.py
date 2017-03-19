import psycopg2
import pandas as pd
# import seaborn as sns
import random

def fighters_biased(fighter1, fighter2):

    conn = psycopg2.connect(dbname="mmastats", user="common", password="011092", port="5432", host="localhost")
    cur = conn.cursor()

    cur.execute("SELECT get_fighter_basics(%s, %s)",(fighter1, 'mycursor'))

    cur.fetchone()[0]


    cur.execute('FETCH ALL IN "mycursor"')

    colnames = [desc[0] for desc in cur.description]

    result = cur.fetchall()

    df = pd.DataFrame(result)

    cur.close()

    cur = conn.cursor()

    cur.execute("SELECT get_fighter_basics(%s, %s)",(fighter2, 'mycursor1'))

    cur.fetchone()[0]

    cur.execute('FETCH ALL IN "mycursor1"')

    df.add(pd.DataFrame(cur.fetchall()))

    cur.close()

    df.columns = colnames

    # print df

    X = df[colnames[2:22]]
    y = df[colnames[22]].astype(float)


    cur = conn.cursor()

    cur.execute("SELECT get_fighter_basics_tp(%s, %s, %s)",(fighter1,fighter2, 'mycursor2'))

    cur.fetchone()[0]


    cur.execute('FETCH ALL IN "mycursor2"')

    colnames_pred = [desc[0] for desc in cur.description]

    result_pred = cur.fetchall()

    df_pred = pd.DataFrame(result_pred)
    df_pred.columns = colnames_pred

    X_pred = df_pred[colnames_pred[2:]]

    from sklearn.neural_network import MLPRegressor


    alpha = 1e-4
    max_iter = 200
    hidden_layer_sizes = (5,2)
    # param_grid = dict(alpha=alpha, max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes)


    mlp = MLPRegressor(solver='lbfgs', random_state=1, alpha=alpha, max_iter=max_iter, hidden_layer_sizes
                        =hidden_layer_sizes)

    mlp.fit(X,y)
    res1 = list(mlp.predict(X_pred))



    cur = conn.cursor()

    cur.execute("SELECT get_fighter_basics_tp(%s, %s, %s)",(fighter2,fighter1, 'mycursor3'))

    cur.fetchone()[0]


    cur.execute('FETCH ALL IN "mycursor3"')

    colnames_pred = [desc[0] for desc in cur.description]

    result_pred = cur.fetchall()

    df_pred = pd.DataFrame(result_pred)
    df_pred.columns = colnames_pred

    X_pred = df_pred[colnames_pred[2:]]

    # from sklearn.neural_network import MLPRegressor


    # alpha = 1e-4
    # max_iter = 200
    # hidden_layer_sizes = (5,2)
    # # param_grid = dict(alpha=alpha, max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes)
    #
    #
    # mlp = MLPRegressor(solver='lbfgs', random_state=1, alpha=alpha, max_iter=max_iter, hidden_layer_sizes
    #                     =hidden_layer_sizes)

    mlp.fit(X,y)
    res2 =  list(mlp.predict(X_pred))

    return res1, res2


def category_biased(fighter1, fighter2, category):

    conn = psycopg2.connect(dbname="mmastats", user="common", password="011092", port="5432", host="localhost")
    cur = conn.cursor()

    cur.execute("SELECT get_category_fights(%s, %s)",(category, 'mycursor'))

    cur.fetchone()[0]


    cur.execute('FETCH ALL IN "mycursor"')

    colnames = [desc[0] for desc in cur.description]

    result = cur.fetchall()

    df = pd.DataFrame(result)


    cur.close()

    df.columns = colnames

    X = df[colnames[2:22]]
    y = df[colnames[22]].astype(float)


    cur = conn.cursor()

    cur.execute("SELECT get_fighter_basics_tp(%s, %s, %s)",(fighter1,fighter2, 'mycursor2'))

    cur.fetchone()[0]


    cur.execute('FETCH ALL IN "mycursor2"')

    colnames_pred = [desc[0] for desc in cur.description]

    result_pred = cur.fetchall()

    df_pred = pd.DataFrame(result_pred)
    df_pred.columns = colnames_pred

    X_pred = df_pred[colnames_pred[2:]]

    from sklearn.neural_network import MLPRegressor


    alpha = 1e-4
    max_iter = 200
    hidden_layer_sizes = (5,2)
    # param_grid = dict(alpha=alpha, max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes)


    mlp = MLPRegressor(solver='lbfgs', random_state=1, alpha=alpha, max_iter=max_iter, hidden_layer_sizes
                        =hidden_layer_sizes)

    mlp.fit(X,y)
    res3 = list(mlp.predict(X_pred))



    cur = conn.cursor()

    cur.execute("SELECT get_fighter_basics_tp(%s, %s, %s)",(fighter2,fighter1, 'mycursor3'))

    cur.fetchone()[0]


    cur.execute('FETCH ALL IN "mycursor3"')

    colnames_pred = [desc[0] for desc in cur.description]

    result_pred = cur.fetchall()

    df_pred = pd.DataFrame(result_pred)
    df_pred.columns = colnames_pred

    X_pred = df_pred[colnames_pred[2:]]

    # from sklearn.neural_network import MLPRegressor


    # alpha = 1e-4
    # max_iter = 200
    # hidden_layer_sizes = (5,2)
    # # param_grid = dict(alpha=alpha, max_iter=max_iter, hidden_layer_sizes=hidden_layer_sizes)
    #
    #
    # mlp = MLPRegressor(solver='lbfgs', random_state=1, alpha=alpha, max_iter=max_iter, hidden_layer_sizes
    #                     =hidden_layer_sizes)

    mlp.fit(X,y)
    res4 = list(mlp.predict(X_pred))

    return res3, res4


fighter1 = 'Jimi Manuwa'

fighter2 = 'Corey Anderson'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'LightHeavyweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')

fighter1 = 'Gunnar Nelson'

fighter2 = 'Alan Jouban'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Welterweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')



fighter1 = 'Brad Pickett'

fighter2 = 'Marlon Vera'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Bantamweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')



fighter1 = 'Arnold Allen'

fighter2 = 'Makwan Amirkhani'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Featherweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')



fighter1 = 'Joe Duffy'

fighter2 = 'Reza Madadi'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Lightweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')



fighter1 = 'Darren Stewart'

fighter2 = 'Francimar Barroso'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'LightHeavyweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')



fighter1 = 'Daniel Omielanczuk'

fighter2 = 'Tim Johnson'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Heavyweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')




fighter1 = 'Leon Edwards'

fighter2 = 'Vicente Luque'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Welterweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')






fighter1 = 'Marc Diakiese'

fighter2 = 'Teemu Packalen'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Lightweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')




fighter1 = 'Tom Breese'

fighter2 = 'Oluwale Bamgbose'


res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Middleweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')




fighter1 = 'Bradley Scott'

fighter2 = 'Scott Askham'

res1, res2 = fighters_biased(fighter1, fighter2)

res3, res4 = category_biased(fighter1, fighter2, 'Middleweight')

print (fighter1 +';'+ str(res1) +';'+ str(res3)).replace('[','').replace(']','')
print (fighter2 +';'+ str(res2) +';'+ str(res4)).replace('[','').replace(']','')


#
# fighter1 = 'Lina Lansberg'
# 
# fighter2 = 'Lucie Pudilova'
# 
# 
# res1, res2 = fighters_biased(fighter1, fighter2)
# 
# res3, res4 = category_biased(fighter1, fighter2, 'Women\'sBantamweight')
