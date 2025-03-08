tables = [
    [0,        'T1(3)',  'T2(4)',  'T3(5)',  'T4(3)',  'T5(4)',  'T6(5)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'o',      'x',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'x',      'o',      'o',      'o',      'x',      'o']
]

def all_open_tables(tables):
#    gives user table IDs that are currently unoccupied
    open_tables = []
    for table in tables:
        if not table["occupied"]:  # occupied == False
            open_tables.append(table["table_id"])
    return open_tables

tables_data = [
        {"table_id": 1, "capacity": 3, "occupied": False, "adjacent2": [2]},
        {"table_id": 2, "capacity": 4, "occupied": False,  "adjacent2": [1, 3]},
        {"table_id": 3, "capacity": 5, "occupied": False, "adjacent2": [2, 4]},
        {"table_id": 4, "capacity": 3, "occupied": False, "adjacent2": [3, 5]},
        {"table_id": 5, "capacity": 4, "occupied": False, "adjacent2": [4, 6]},
        {"table_id": 6, "capacity": 5, "occupied": False, "adjacent2": [5]}
    ]

print("All the tables that are avalible at this time would be tables", all_open_tables(tables_data))