reduction_rules = {
    "R1": { "E+T": "E" },
    "R2": { "T": "E" },
    "R3": { "T*F": "T" },
    "R4": { "F": "T" },
    "R5": { "(E)": "F" },
    "R6": { "id": "F" },
}

parsing_table = [
    [{"id": "S5"}, {"(": "S4"}, {"E": 1}, {"T": 2}, {"F": 3}],
    [{"+": "S6"}, {"$": "acc"}],
    [{"+": "R2"}, {"*": "S7"},{")": "R2"}, {"$": "R2"}],
    [{"+": "R4"}, {"*": "R4"},{")": "R4"}, {"$": "R4"}],
    [{"id": "S5"}, {"(": "S4"}, {"E": 8}, {"T": 2}, {"F": 3}],
    [{"+": "R6"}, {"*": "R6"},{")": "R6"}, {"$": "R6"}],
    [{"id": "S5"}, {"(": "S4"}, {"T": 9}, {"F": 3}],
    [{"id": "S5"}, {"(": "S4"}, {"F": 10}],
    [{"+": "S6"}, {")": "S11"}],
    [{"+": "R1"}, {"*": "S7"},{")": "R1"},{"$": "R1"}],
    [{"+": "R3"}, {"*": "R3"},{")": "R3"},{"$": "R3"}],
    [{"+": "R5"}, {"*": "R5"},{")": "R5"},{"$": "R5"}],
]


def format_input(input):
    # initialize empty list
    formatted_input = []
    # for every character in input push into list
    for nonterminal in input:
        # if there ever is an i then we know to push "id" into it and ignore the following 'd' character
        if (nonterminal == "i"):
            formatted_input.append("id")
        elif (nonterminal == "d"):
            continue
        else:
            formatted_input.append(nonterminal)
    return formatted_input


def check_parsing_table(go_to_number, next_value):
    # Accessing the first "row"
    first_row = parsing_table[go_to_number]

    # Checking if the key "id" exists in the first dictionary
    for entry in first_row:
        if next_value in entry:
            value_of_id = entry[next_value]
            return value_of_id

    # If the value is not found in the row in the parsing table then cry
    else:
        return "NOT FOUND"
    

def begin_parse(input):
    print("Step | Stack | Input | Action ")
    step = 0
    stack = ["$", 0]
    input = format_input(input)
    
    print(f'{step} | {stack} | {"".join(input)} | ')
    step += 1

    while(step != 4):
        # next_number = stack[-1];
        next_value = input.pop(0)

        table_result = check_parsing_table(stack[-1], next_value)

        # If the result is acc then we validated that the input works
        if(table_result == "acc"):
            return True
        # If the result is to shift then do this
        elif(table_result[0] == "S"):
            print("shift")
            stack.append(next_value)
            stack.append(int(table_result[1]))
        # If the result is to reduce then do this
        elif(table_result[0] == "R"):
            print("reduce")
        # If neither then just cry honestly
        else:
            return False

        
        print(f'{step} | {stack} | {"".join(input)} | {table_result}')
        step += 1


begin_parse("(id+id)*id$")
