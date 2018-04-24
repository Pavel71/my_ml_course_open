import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = (10, 8)

data = pd.read_csv(r'C:\projects\Python\mlcourse_open\Lesson1\adult.data.csv')


table_education_salary = pd.crosstab(data['education'], data['salary'] == '>50K')





# table_group_ed_sol = data.groupby(['education'])(['salary'] == '>50K')


table_ed_sol = data.pivot_table(index= ['education'], columns=['salary'])

Race_age_group = data.groupby(['race', 'sex'])['age'].describe()

# print(Race_age_group)

tb_cross = pd.crosstab(data['race'], data['sex'], margins=True)

# print(tb_cross)

tb_group_femail_merry_salary = data.groupby(['salary', 'sex'])['marital-status'].value_counts()

# print(tb_group_femail_merry_salary)

tb_group_solary_hoursweek = data.groupby(['hours-per-week'])['salary'].value_counts(normalize=True)

# print(tb_group_solary_hoursweek)

tb_group_salary_japan_mean = data.groupby(['native-country', 'salary'])['hours-per-week'].mean()


print(tb_group_salary_japan_mean['Japan'])

# print(tb_group_salary_japan_mean['hours-per-week'].value_counts())


