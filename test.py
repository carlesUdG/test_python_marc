from openpyxl import load_workbook
import json
import re

class Departament():
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __init__(self, cost2, num_treb2, num_boss2):
        self.cost = cost2
        self.num_treb = num_treb2
        self.num_boss = num_boss2

    def mostra(self):
        print('COST: ' + str(self.cost))
        print('NUM. TREB: ' + str(self.num_treb))
        print('NUM. BOSSES: ' + str(self.num_boss))

        print(self.toJSON())

if __name__ == "__main__":
    nom_excel = input('Entra el teu nom del Exel\n')
    wb = load_workbook(filename=nom_excel, read_only=True, data_only=True)
    sheet1 = wb['Sheet1']
    cost_dep = sheet1['A1'].value
    num_treb = sheet1['A2'].value
    num_boss = sheet1['A3'].value
    dep = Departament(cost_dep, num_treb, num_boss)
    dep.mostra()
    # try:
    #     dep.mostra()
    # except Exception as ex:
    #     print('ha petat ')
    #     pass