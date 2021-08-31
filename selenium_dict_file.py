import pymysql

def data_store(data_dict):
	db=pymysql.connect(host="localhost",user="root",password="plungein12",database="LinkedIn_db")
	cur = db.cursor()
	ins = 'insert into LinkedIn_data values(%s,%s)'
	for key in data_dict.keys():
		li = [key,data_dict[key]]
		cur.execute(ins,li)
		db.commit()
	cur.close()
	db.close()
# class Data_store:
# 	def __init__(self,name,des):
# 		self.name = name
# 		self.des  = des

# 	def clean_data(self):
		 


# sotred_data = Data_store()
