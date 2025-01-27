import csv
import copy
from store import Store
from random import randint

class MyStore(Store):

    store_obj_list = {}
    product_id_mapping = {}

    def __init__(self, dataList):


    def print_stores(self):


    def print_prod_id_mapping(self):


    def print_product_in(self, pid):


    def add_new_store(self, sID, sName, sCity, sAddress):


    def add_new_product(self, sID, pID, pName, pSold, pAvl, pCost, pPrice):


    def delete_store(self, sID):



def main():
    data = []
    with open('storeInventory.csv', encoding="utf-8-sig", newline='') as csv_file:
        reader = csv.reader(csv_file)
        flag = 0
        for row in reader:
            if flag == 0:
                flag = 1
                continue
            data.append(row)
    storeObj = MyStore(data)
    print("******************************************************************************")
    print("Printing Store objects:")
    storeObj.print_stores()
    print("******************************************************************************")
    print("Printing ProductID mapping:")
    storeObj.print_prod_id_mapping()
    print("******************************************************************************")
    plst = ["P2001", "P2002", "P2003", "P2004", "P2005", "P2006", "P2007", "P2008", "P2009", "P2010"]
    val = randint(0, 9)
    print(f"Printing all-stores inventory of Product ID {plst[val]}:")
    storeObj.print_product_in(plst[val])
    print("******************************************************************************")
    storeObj.add_new_store("S1011", "MnMPlaza", "Stratford", "123 ABC Parkway")
    storeObj.add_new_store("S1003", "CityPlaza", "Jiukeng", "634 Jackson Parkway")
    print("******************************************************************************")
    storeObj.add_new_product("S1020", "P2015", "Chair", 1234, 324, 523.45, 432.12)
    storeObj.add_new_product("S1001", "P2015", "Chair", 1234, 324, 523.45, 432.12)
    print("Updated ProductID mapping:")
    storeObj.print_prod_id_mapping()
    print("******************************************************************************")
    storeObj.delete_store("S1080")
    storeObj.delete_store("S1009")
    print("Updated Store objects dictionary:")
    storeObj.print_stores()
    print("******************************************************************************")

if __name__ == "__main__":
    main()