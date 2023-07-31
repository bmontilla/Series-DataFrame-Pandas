import pandas as pd

Real_Madrid_players = pd.Series(['Thibaut Courtois', 'Andriy Lunin','Dani Carvajal','Eder Militao', 'David Alaba', 'Nacho Fernandez', 'Álvaro Odriozola', 'Francisco García', 'Antonio Rudiger', 'Ferland Mendu','Jude Bellingham', 'Toni Kross', 'Luka Modric', 'Eduardo Camavinga','Federico Valverde', 'Aurelién Tchouaméni','Dani Ceballos', 'Brahim Díaz', 'Arda Guler','Vinicius Jr.', 'Rodrygo', 'Joselu', 'Lucas Vázquez', 'Álvaro Rodríguez'])

dict = {'Jugador':['Thibaut Courtois', 'Andriy Lunin','Dani Carvajal','Eder Militao', 'David Alaba', 'Nacho Fernandez', 'Álvaro Odriozola', 'Francisco García', 'Antonio Rudiger', 'Ferland Mendu','Jude Bellingham', 'Toni Kross', 'Luka Modric', 'Eduardo Camavinga','Federico Valverde', 'Aurelién Tchouaméni','Dani Ceballos', 'Brahim Díaz', 'Arda Guler','Vinicius Jr.', 'Rodrygo', 'Joselu', 'Lucas Vázquez', 'Álvaro Rodríguez'],
 'Dorsal': [1, 13, 2, 3, 4, 6, 16, 20, 22, 23, 5, 8, 10, 12, 15, 18, 19, 21, 24, 7, 11, 14, 17, 39],
 'Posición': ['Arquero', 'Arquero', 'Defensor','Defensor','Defensor','Defensor','Defensor','Defensor','Defensor','Defensor', 'Mediocampista', 'Mediocampista', 'Mediocampista', 'Mediocampista', 'Mediocampista', 'Mediocampista', 'Mediocampista', 'Mediocampista', 'Mediocampista', 'Delantero','Delantero', 'Delantero', 'Delantero', 'Delantero']
 }
df_players = pd.DataFrame(dict)

print(df_players)

excel= 'Plantilla_Real_Madrid_2023.xlsx'
df_players.to_excel(excel, index=False)
