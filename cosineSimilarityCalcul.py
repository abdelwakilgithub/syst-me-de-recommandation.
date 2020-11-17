import pandas as pd
import numpy as np
from readData import matrice_rating

multiplication_vector = matrice_rating.dot(matrice_rating.T)
norm_user = np.sqrt((matrice_rating**2).sum(axis=1))
matrice_norm = np.outer(norm_user, norm_user)
matrice_similarite_cacul = multiplication_vector/matrice_norm
