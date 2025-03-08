tables = [
    [0,        'T1(3)',  'T2(4)',  'T3()',  'T4(3)',  'T5(4)',  'T6(5)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'x',      'o',      'x',      'x',      'o'],
    [3,        'x',      'o',      'x',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'x',      'o',      'o',      'o',      'x',      'o']
]

max_capacity = 5

party_size = input("How many people are with you today? ")

def convertStr(party_size):
    party = int(party_size)
    return party

def tables_for_size(tables, party_size):

#    gives user all table IDs that can seat the party size and that are unoccupied

    suitable_tables = []
    for table in tables:
        if not table["occupied"] and table["capacity"] >= party_size:
            suitable_tables.append(table["table_id"])
    return suitable_tables

if convertStr(party_size) > max_capacity :
    # this if statement is used to weed out whether there is enough room or not for the party
    print("There are no avalible tables of that size at this time. Please wait, go some where else, sit separately, or you may try to combine 2 tables.")
else:
    tables_data = [
            {"table_id": 1, "capacity": 3, "occupied": False, "adjacent2": [2]},
            {"table_id": 2, "capacity": 4, "occupied": False,  "adjacent2": [1, 3]},
            {"table_id": 3, "capacity": 5, "occupied": False, "adjacent2": [2, 4]},
            {"table_id": 4, "capacity": 3, "occupied": False, "adjacent2": [3, 5]},
            {"table_id": 5, "capacity": 4, "occupied": False, "adjacent2": [4, 6]},
            {"table_id": 6, "capacity": 5, "occupied": False, "adjacent2": [5]}
        ] 
    print("All of the avalible tables for a party size of " + party_size + " would be tables", tables_for_size(tables_data, convertStr(party_size)))