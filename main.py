def check(s, strings, assigns):
    for string in strings:
        expanded = ""
        for char in string:
            if char in Gamma:
                expanded += assigns[char]
            else:
                expanded += char
        if expanded not in s:
            return False
    return assigns

def explore(s, strings, expansions, assigns, contained_letters):
    if len(expansions) == 0:
        return check(s, strings, assigns)
    letter = list(expansions.keys())[0]
    expansion_list = expansions[letter]

    for expansion in expansion_list:
        assigns[letter] = expansion
        expansions_copy = expansions.copy()
        expansions_copy.pop(letter)
        if res := explore(s, strings, expansions_copy, assigns, contained_letters):
            return res
        assigns.pop(letter)

    return False

# Removes expansions which contains letters not in s
def preprocess(s, letters, expansions):
    new_expansions = {}
    assigns = {}
    keys = list(expansions.keys())
    for key in keys:
        if key in letters:
            new_exp = []
            expansions_list = expansions[key]
            for e in expansions_list:
                if e in s:
                    new_exp.append(e)
            new_expansions[key] = new_exp
        else:
            assigns[key] = expansions[key][0]
    return new_expansions, assigns

def print_formatted(res):
    if not res:
        print("NO")
    else:
        assigns = list(res.keys())
        assigns.sort()
        for key in assigns:
            print(key + ":" + res[key])



Sigma = [chr(i) for i in range(ord('a'), ord('z') + 1)]
Gamma = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

def main():
    # Setup and input
    try:
        k = int(input())
    except ValueError:
        print("NO")
        return 
    if k < 0:
        print("NO")
        return
    s = input().strip()    

    strings = []
    contained_letters = []
    for _ in range(k):
        string = input()
        strings.append(string)
        for char in string:
            if char not in Gamma and char not in Sigma:
                print("NO")
                return
            if char not in contained_letters and char in Gamma:
                contained_letters.append(char)

    expansions = {}

    while True:
        try:
            line = input()
            try:
                letter, exp = line.split(":")
            except ValueError:
                print("NO")
                return
            if letter == "" or letter not in Gamma:
                print("NO")
                return
            expansions[letter] = exp.split(",")
        except EOFError: 
            break
    
    for letter in contained_letters:
        if letter not in expansions:
            print("NO")
            return

    assigns = {}
    expansions, assigns = preprocess(s, contained_letters, expansions)
    for key in expansions.keys():
        if expansions[key] == []:
            print("NO")
            return

    res = explore(s, strings, expansions, assigns, contained_letters)
    if res != 1:
        print_formatted(res)
    return

if __name__ == "__main__":
    main()
    