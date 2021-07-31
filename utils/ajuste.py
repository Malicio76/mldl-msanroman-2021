def ajustar_data(df):
  """
  Esta función factoriza las variables categóricas
  (usando pandas) e imputa la variable sumdiam.
  """
  import pandas as pd
  df['fundo'], fundo_uniq = pd.factorize( df['fundo'], sort=True )
  df['camp'], camp_uniq = pd.factorize( df['camp'], sort=True )
  df['parcela'], parcela_uniq = pd.factorize( df['parcela'], sort=True )
  df['lote'], lote_uniq = pd.factorize( df['lote'], sort=True )
  df['patron'], patron_uniq = pd.factorize( df['patron'], sort=True )

  df['sumdiam'] = df['d1'] * 2 + df['d2']
  return df