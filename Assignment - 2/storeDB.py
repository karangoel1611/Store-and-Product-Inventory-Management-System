import csv
import copy

from store import Store

class storeDB(object):

    def __init__(self, filename):
        #TO DO


    def read_file(self):
        #TO DO

    def store_exists(self, str_obj):
        # TO DO

    def add_store_products(self):
        #TO DO

    def print_store_info(self, str_nm):
        #TO DO

    def print_product_info(self, str_id):
        #TO DO


    def remove_store_data(self, str_id):
        #TO DO

    def add_new_store(self, s_nm, s_city, s_area):
        #TO DO

    def add_new_product(self, s_id, p_nm, p_sold, p_avl, p_cost, p_price):
        #TO DO

def main():
    comp = storeDB("inventory.csv")
    print("******************************************************************************")
    comp.read_file()
    print("******************************************************************************")
    comp.add_store_products()
    print("******************************************************************************")
    #str_nm = input("Enter the store name that you want to search: ")
    comp.print_store_info("Walmart")
    print("******************************************************************************")
    #str_id = int(input("Enter the store ID for the product list: "))
    comp.print_product_info(29)
    print("******************************************************************************")
    #str_id = int(input("Enter the store ID of the store that you want to remove: "))
    comp.remove_store_data(996)
    print("******************************************************************************")
    comp.add_new_store('Walmart', 'Charlottetown', '1 abc st')
    print("******************************************************************************")
    comp.add_new_product(1001, 'Laptop', 300, 200, 2048.12, 2132.43)
    print("******************************************************************************")
    comp.print_store_info("Walmart")
    print("******************************************************************************")
    comp.print_product_info(1001)
    print("******************************************************************************")

if __name__ == "__main__":
    main()