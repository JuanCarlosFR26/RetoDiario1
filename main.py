import pandas as pnd

file = 'dia1Mails.xlsx'

document = pnd.read_excel(file, usecols=['Email'])

print(document['Email'].unique)