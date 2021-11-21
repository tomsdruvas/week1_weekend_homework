# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(name):
    return name["name"]

def get_total_cash(name):
    return name["admin"]["total_cash"]

def add_or_remove_cash(name, amount):
    name["admin"]["total_cash"] += int(amount)


def get_pets_sold(name):
    return name["admin"]["pets_sold"]

def increase_pets_sold(name, amount):
    name["admin"]["pets_sold"] += amount


def get_stock_count(name):
    return len(name["pets"])


def get_pets_by_breed(name, breed):
    new_list = []
    for dog in name["pets"]:
        if dog["breed"] == breed:
            new_list.append(breed)
    return new_list

def find_pet_by_name(name, dog_name):
    for dog in name["pets"]:
        if dog["name"] == dog_name:
            return dog




def remove_pet_by_name(name, dog_name):
    for i in range(len(name["pets"])):
        if name["pets"][i]["name"] == dog_name:
            del name["pets"][i]
            break


def add_pet_to_stock(name, pet):
    name["pets"].append(pet)


def get_customer_cash(list):
    return list["cash"]

def remove_customer_cash(name, amount):
    name["cash"] -= amount

def get_customer_pet_count(name):
    return len(name["pets"])


def add_pet_to_customer(name, pet):
    name["pets"].append(pet)


def customer_can_afford_pet(name, new_pet):
    afford = False
    if name["cash"] >= new_pet["price"]:
        afford = True
    return afford

def can_afford(cost, price):
    affordable = price - cost
    return affordable


def sell_pet_to_customer(pet_shop, dog_name, name):
    
    if dog_name:
        if can_afford(dog_name["price"], name["cash"]) >= 0:
            add_pet_to_customer(name, dog_name)
            remove_customer_cash(name, dog_name["price"])
            increase_pets_sold(pet_shop, 1)
            add_or_remove_cash(pet_shop, dog_name["price"])



    
    