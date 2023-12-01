from tabulate import tabulate

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

def format_stack(input):
    # Since for our stack implementation is a list of numbers and strings, when we want to print 
    # it out we want to convert every element into a string and join it for readability
    result = [str(element) for element in input]
    return "".join(result)

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
    # initialize variables used for parsing
    step = 1
    stack = ["$", 0]
    input = format_input(input)
    # data is meant to store each step we do in the stack implementation to visualize later
    data = [
        ["0", format_stack(stack), "".join(input), ""]
    ]
    while(step != 20):
        # Grab the input variable we need
        next_value = input.pop(0)
        # Check if it exists in the parsing table and return its move
        table_result = check_parsing_table(stack[-1], next_value)

        # If the result is acc then we validated that the input works
        if(table_result == "acc"):
            data.append([step, format_stack(stack), "$", "ACCEPT"])
            return data
        # If the result is to shift then do this
        elif(table_result[0] == "S"):
            stack.append(next_value)
            stack.append(int(table_result[1:]))
        # If the result is to reduce then do this
        elif(table_result[0] == "R"):
            
            value_to_reduce = ""
            temp_stack = []

            # Keep looping, keep adding the grammar from the stack and checking if it exists in the parsing table
            # If we reach the end of the stack then we know for certain that reduction rule grammar is not valid
            # therefore we just reject and stop the parsing table.
            while True:
                temp_stack.insert(0, stack[-2])
                value_to_reduce = ''.join(temp_stack)

                stack.pop()
                stack.pop()
                if (value_to_reduce == "$"):
                    data.append([step, format_stack(stack), "".join(input), "REJECT"])
                    return data
                elif (value_to_reduce in reduction_rules[table_result]):
                    reduced_letter = reduction_rules[table_result][value_to_reduce]

                    goto_number = check_parsing_table(stack[-1], reduced_letter)
                    
                    stack.append(reduced_letter)
                    stack.append(goto_number)
                    # make sure we add back the old value to the input stack because we cant get rid of it yet
                    input.insert(0, next_value)
                    break
                
        # If it is neither accept, shift or reduce then just cry and Reject the input grammar
        else:
            data.append([step, format_stack(stack), "".join(input), "REJECT"])
            return data
        
        # After shifting or reducing add the entry to the data list so that we can tabulate the entry later
        data.append([step, format_stack(stack), "".join(input), table_result])
        step += 1

def main():

    input_values = ["(id+id)*id$", "id*id$", "(id*)$"]
    output_values = []
    headers = ["Step", "Stack", "Input", "Action"]

    for value in input_values:
        table_data = begin_parse(value)
        output_values.append(tabulate(table_data, headers, tablefmt='grid'))


    with open('output.txt', 'w') as file:
        file.write("CPSC 323 Project 2\n")

    with open('output.txt', 'a') as file:
        for i, value in enumerate(output_values):
            file.write(f"\n\nINPUT {i+1}: {input_values[i]}\n\n")
            file.write(value)

main()