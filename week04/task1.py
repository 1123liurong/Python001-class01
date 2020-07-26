import pandas as pd
import numpy as np

#创建随机数据组
data=pd.DataFrame({
    "id":np.random.randint(200,210,20),
    "salary":np.random.randint(20,30,20),
    "age":np.random.randint(6000,8000,20)
    })
data2 =pd.DataFrame({
    "id":np.random.randint(205,210,5),
    "dep":np.random.randint(1,10,5)
    })

#1. SELECT * FROM data;
print(data)
print('-'*20)
#2. SELECT * FROM data LIMIT 10;
print(data[:10])
print('-'*20)
#3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data['id'])
print('-'*20)
#4. SELECT COUNT(id) FROM data;
print(data['id'].count())
print('-'*20)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data['id']<1000)&(data['age']>30)])
print('-'*20)
6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(data.groupby('id').aggregate({'id':'count',}))
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
result = pd.merge(data, data2, on='id', how='inner')
print(result)
print('-'*20)
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
result = pd.concat([data, data2])
print(result)
print('-'*20)
# 9. DELETE FROM table1 WHERE id=10;
df1=pd.DataFrame({
    "id":np.random.randint(200,210,20),
    "salary":np.random.randint(20,30,20),
    "age":np.random.randint(6000,8000,20)
    })


print (df1[df1['id']!=205])
print('-'*20)
# 10. ALTER TABLE table1 DR5OP COLUMN column_name;
df2=pd.DataFrame({
    "id":np.random.randint(200,210,20),
    "salary":np.random.randint(20,30,20),
    "age":np.random.randint(6000,8000,20)
    })
result = df2.drop(axis = 1, columns= 'salary')
print(result)
print('-'*20)