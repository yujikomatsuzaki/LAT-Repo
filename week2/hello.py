# RUN : shift + enter

import pandas as pd

df = pd.read_csv('foreign_students_by_department.csv')

# print(df.to_string())

df.head()
df.info()

df['學校名稱'].value_counts()

temp = df[['學年度','學校名稱','外國學生小計']]
temp

Type = temp.groupby(['學校名稱'])['外國學生小計'].sum().reset_index()
Type

Type['Year'] = 2015
Type