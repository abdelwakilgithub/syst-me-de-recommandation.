import pandas as pd
import numpy as np

excel = pd.read_excel("Data/Reviews-Asmi.xlsx")
table_rating = excel.rename(
    columns={'reviewerName': 'Users', 'categories': 'Products'})
table_rating_new = table_rating.groupby(
    ['Users', 'Products']).agg({'rating': ['mean']})
matrice_rating = pd.pivot_table(table_rating_new, index=["Users"], columns=[
                                'Products'], values=['rating']).fillna(0)
# print(matrice_rating)
