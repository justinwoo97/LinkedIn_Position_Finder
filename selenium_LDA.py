import os
import gensim
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import pymysql
from sqlalchemy import create_engine

def data_extract():
    db=pymysql.connect(host="localhost",user="root",password="plungein12",database="LinkedIn_db")
    cur = db.cursor()
    cur.execute("select * from LinkedIn_data")
    output = [cur.fetchall()]
    frame = pd.read_sql("select * from test.uservitals", dbConnection);
    # print(output) 
    return output
    cur.close()
    db.close()
result = data_extract()
print(result)


from sqlalchemy import create_engine
import pandas as pd

hostname="localhost"
dbname="LinkedIn_db"
uname="root"
pwd="plungein12"
tablename="LinkedIn_data"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                           .format(host=hostname, db=dbname,
                                   user=uname,pw=pwd))
train = pd.read_sql(tablename, engine)
train.columns = ['name', 'total']

print(train.head())


from sqlalchemy import create_engine
import pandas as pd

hostname="localhost"
dbname="LinkedIn_db"
uname="root"
pwd="plungein12"
tablename="LinkedIn_data"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                           .format(host=hostname, db=dbname,
                                   user=uname,pw=pwd))
train = pd.read_sql(tablename, engine)
train.columns = ['name', 'total']

print(train.head())


import pyLDAvis
import pyLDAvis.gensim_models
import pickle 
import pyLDAvis
import os 

# Visualize the topics
pyLDAvis.enable_notebook()

LDAvis_data_filepath = os.path.join('/Users/justinding/Desktop/winlab/sample-dis/img-pyLDAvis/ldavis_prepared_M_'+str(num_topics))

# # this is a bit time consuming - make the if statement True
# # if you want to execute visualization prep yourself
if 1 == 1:
    LDAvis_prepared = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
    with open(LDAvis_data_filepath, 'wb') as f:
        pickle.dump(LDAvis_prepared, f)

# load the pre-prepared pyLDAvis data from disk
with open(LDAvis_data_filepath, 'rb') as f:
    LDAvis_prepared = pickle.load(f)

pyLDAvis.save_html(LDAvis_prepared, '/Users/justinding/Desktop/winlab/sample-dis/img-pyLDAvis/ldavis_prepared_M_'+ str(num_topics) +'.html')

LDAvis_prepared

