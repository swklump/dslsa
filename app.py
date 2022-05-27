import os
import pandas as pd
import subprocess
from config import folder


df = pd.read_excel('Soils Report Record.xls')


x = True
while x is True:
    search1 = input('Enter Client: ')

    results = df[df['Client']==search1]['Report#'].values.tolist()
    print(f'There are {len(results)} results that were returned.')

    for r in results:
        report = '/' + r.lstrip('0') + '.pdf'
        try:
            os.startfile(folder + report)
        except FileNotFoundError:
            print(f'The {report[1:]} file does not exist.')

    shouldcontinue = input('Would you open another pdf? (yes/no): ')
    if shouldcontinue == 'no':
        print('See you later!')
        x = False