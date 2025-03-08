tables = [
    [0,        'T1(3)',  'T2(4)',  'T3(5)',  'T4(3)',  'T5(4)',  'T6(5)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'o',      'x',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'o'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'x',      'o',      'o',      'o',      'x',      'o']
]

max_capacity = 9

party_size = input("How many people are with you today? ")

def convertStr(party_size):
    party = int(party_size)
    return party
 

def table_combos(tables, party_size):

#    gives user tables or table combinations that can seat the party size
#    combos are determined by the table's adjacent2 list 
#    which help if there is not enough room at one table for the entire party

    results = []

    for table in tables:
        # checks for single tables
        if (not table["occupied"]) and (table["capacity"] >= party_size):
            results.append((table["table_id"],))
        
        # checks adjacent2 combos if a single table can't seat them
        if table["adjacent2"] and not table["occupied"]:
            for neighbor_id in table["adjacent2"]:
                neighbor_table = next((t for t in tables if t["table_id"] == neighbor_id), None)
                
                # If adjacent2 also exists, is unoccupied, and combined capacity is equal to or less then the party size
                if neighbor_table and (not neighbor_table["occupied"]):
                    total_capacity = table["capacity"] + neighbor_table["capacity"]
                    if total_capacity >= party_size:
                        # to avoid duplicates like (3,4) and (4,3) and other such unnessacary things
                        combo = tuple(sorted([table["table_id"], neighbor_table["table_id"]]))
                        if combo not in results:
                            results.append(combo)
    
    return results

if convertStr(party_size) > max_capacity :
    # this if statement is used to weed out whether there is enough room or not for the party
    print("There are no avalible tables of that size at this time. Please wait, go some where else, sit separately, or you may try to combine 3 tables.")
else:
    tables_data = [
            {"table_id": 1, "capacity": 3, "occupied": False, "adjacent2": [2]},
            {"table_id": 2, "capacity": 4, "occupied": False,  "adjacent2": [1, 3]},
            {"table_id": 3, "capacity": 5, "occupied": False, "adjacent2": [2, 4]},
            {"table_id": 4, "capacity": 3, "occupied": False, "adjacent2": [3, 5]},
            {"table_id": 5, "capacity": 4, "occupied": False, "adjacent2": [4, 6]},
            {"table_id": 6, "capacity": 5, "occupied": False, "adjacent2": [5]}
        ]
    combos = table_combos(tables_data, convertStr(party_size))
    print("Single or combined tables for a party size " + party_size + " would be tables", combos)
