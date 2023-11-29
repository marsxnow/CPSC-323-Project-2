grammar = {
    "E": [["E", "+", "T"], ["T"]],
    "T": [["T", "*", "F"], ["F"]],
    "F": [["(", "E", ")"], ["id"]],
}

parsing_table = {
    ("E", "id"): ["T"],
    ("E", "("): ["T"],
    ("T", "id"): ["F"],
    ("T", "("): ["F"],
    ("F", "id"): ["id"],
    ("F", "("): ["(", "E", ")"],
    ("E", "+"): ["+", "T"],
    ("T", "*"): ["*", "F"],
}

def parse(input_string):
    stack = ["$", "E"]
    input_string = input_string + "$"
    cursor = 0

    while len(stack) > 0:
        print("Stack:", stack)
        top = stack[-1]
        current_input = input_string[cursor]

        if top in grammar:
            production = parsing_table.get((top, current_input), None)
            if production is None:
                return False
            else:
                stack.pop()
                if production != ["epsilon"]:
                    stack.extend(production[::-1])
        elif top == current_input:
            stack.pop()
            cursor += 1
        else:
            return False
    return True

print(parse("(id+id)*id"))
print(parse("id*id"))
print(parse("(id*)"))
