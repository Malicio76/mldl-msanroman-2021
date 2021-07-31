import pandas as pd
import numpy as np
import csv

import utils.ajuste as ua

# import matplotlib.pyplot as plt
# import matplotlib.ticker as tck
# from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sns
# import seaborn as sb

def readCSV(filePath):
  """
  Esta función lee el archivo .csv con los datos, descartando los nombres de variables (header)
  asignando nombres y tipos estándar a las variables.
  Parámetros:
  filePath: Ruta y nombre del archivo .csv
  """
  nombres = ['index', 'camp', 'fundo', 'parcela', 'lote', 'patron', 'fecha', 'd1', 'd2', 'peso', 'dias', 'validacion']
  types = {'index': np.int32, 'camp': np.int32 }

  df = pd.read_csv( filePath,
                    decimal='.',
                    dtype = types,
                    names = nombres,
                    header = 0,
                    quoting = csv.QUOTE_NONNUMERIC )
  return df

HaasDataFrame = readCSV(r'pesos-hass.csv')

HaasDataFrame = ua.ajustar_data(HaasDataFrame)


