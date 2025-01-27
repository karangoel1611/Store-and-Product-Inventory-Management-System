import csv
import copy
from store import Store
import random
from stack import Stack

class StackStorage(object):

    def __init__(self, dataList):


    def get_store_obj_stack(self):


    def store_in_stack(self, str_id):


    def build_stack(self):


    def get_odd_even_store_stacks(self):


    def build_products_stack(self,slst):


def main():
    data = []
    with open('asn4Inventory.csv', encoding="utf-8-sig", newline='') as csv_file:
        reader = csv.reader(csv_file)
        flag = 0
        for row in reader:
            if flag == 0:
                flag = 1
                continue
            data.append(row)
    stackObj = StackStorage(data)
    print("******************************************************************************")
    print("Printing Stack of Store objects:")
    stk = stackObj.get_store_obj_stack()
    stk.print_stack(0)
    print("******************************************************************************")
    print("Building Stack of Store objects...")
    stackObj.build_stack()
    print("******************************************************************************")
    print("Printing Stack of Store objects:")
    stk = stackObj.get_store_obj_stack()
    stk.print_stack(0)
    print("******************************************************************************")
    oddStk, evenStk = stackObj.get_odd_even_store_stacks()
    print("Printing Stack of Store objects with odd store ids:")
    oddStk.print_stack(1)
    print("******************************************************************************")
    print("Printing Stack of Store objects with even store ids:")
    evenStk.print_stack(1)
    print("******************************************************************************")
    slst = ["S1001", "S1002", "S1003", "S1004", "S1005", "S1006", "S1007", "S1008", "S1009", "S10101", "S10111"]
    vlst = random.sample(slst, 5)
    vlst.sort(reverse=True)
    pstk = stackObj.build_products_stack(vlst)
    print(f"Printing stack of products for a given list of store ids:")
    print("Store ids:",vlst)
    pstk.print_stack(1)
    print("******************************************************************************")
    print("Printing to check if the Original Stack of Store objects is intact:")
    stk = stackObj.get_store_obj_stack()
    stk.print_stack(0)
    print("******************************************************************************")

if __name__ == "__main__":
    main()