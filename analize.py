import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# excel_file = 'Test_case/train.xlsx'
# csv_file = 'train.csv'

# df = pd.read_excel(excel_file)

# df.to_csv(csv_file, encoding='utf-8')



# ЗАДАНИЕ 1

# # a
# df = pd.read_csv('Test_case/train.csv')
# print(df)
# gr = df.groupby('Sub-Category')['Sales'].sum()

# top_gr = gr.nlargest(4)
# print("Наиболее частопокупаемые", top_gr)


# # б
# df['Order Date'] = pd.to_datetime(df['Order Date'])
# two_years = df[(df['Order Date'] >= '2016-01-01') & (df['Order Date'] <= '2018-12-31')]

# res = two_years.groupby('Sub-Category')['Sales'].sum()
# top_res = res.nlargest(4)
# print('За последние два года', top_res)


# # в
# df['Order Date'] = pd.to_datetime(df['Order Date'])
# last_year = df[(df['Order Date'] >= '2018-01-01') & (df['Order Date'] <= '2018-12-31')]
# last_res = last_year.groupby('Sub-Category')['Sales'].sum()
# top_last_res = last_res.nlargest(4)
# print('За последний год', top_last_res)


# ЗАДАНИЕ 2

# df = pd.read_csv('Test_case/train.csv')
# print(df)

# sales = df['Sales']

# plt.figure(figsize=(10, 6))
# sns.boxplot(x=sales)
# plt.title('Неотфильтрованные данные о продажах')
# plt.xlabel('Sales')
# plt.show()


# mean = sales.mean()
# std = sales.std()

# lower_gran = mean - 3 * std
# upper_gran = mean + 3 * std

# filter = sales[(sales >= lower_gran) & (sales <= upper_gran)]

# plt.figure(figsize=(10, 6))
# sns.boxplot(x=filter)
# plt.title('Отфильтрованные данные о продажах')
# plt.xlabel('Sales')
# plt.show()

# print(f'''Среднее значение продаж {mean}
# Стандартное отклонение: {std}
# Нижняя граница: {lower_gran}
# Верхняя граница: {upper_gran}
# Отфильтрованные данные без аномалий: {filter}''')

# ЗАДАНИЕ 3

df = pd.read_csv('Test_case/train.csv')
print(df)

reg_all = df['Region'].unique()
print(reg_all)

sub_all = df['Sub-Category'].unique()
print(len(sub_all)) #17 категорий

min_s = df['Sales'].min()
print(min_s)
sr_s = df['Sales'].mean()
print(sr_s)
max_s = df['Sales'].max()
print(max_s)

def categorize(sales):
    if sales >= min_s and sales < sr_s:
        return 'Низкие продажи'
    if sales >= sr_s and sales < max_s:
        return 'Средние продажи'
    if sales >= max_s:
        return 'Большие продажи'
    
df['Sales_group'] = df['Sales'].apply(categorize)

gr = df.groupby(['Region','Sales_group'])['Sales'].sum().reset_index()
print(gr)


# excel_file = 'Test_case/test1.xlsx'
# csv_file = 'test1.csv'

# df = pd.read_excel(excel_file)
# df.to_csv(csv_file, encoding='UTF-8')
# print(df)

# trouble = df['Проблема'].unique()
# print(trouble)

# filter = trouble[(trouble == 'Нет СМС') | (trouble == 'проблема с ПСБ банком')]
# print(filter)







