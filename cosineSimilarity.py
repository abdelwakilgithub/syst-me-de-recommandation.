import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from readData import matrice_rating


matrice_similarite = cosine_similarity(matrice_rating, matrice_rating)
