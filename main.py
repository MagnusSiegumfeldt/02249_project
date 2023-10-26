# Verifies a specific assignment
def check(s, strings, assigns):
    for string in strings:
        expanded = ""
        for char in string:
            expanded += assigns[char] if char in Gamma else char
        if expanded not in s:
            return False
    return assigns

# Recursively search combinations of the preprocessed input. Returns if a satisfying assignment is found.
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

# Removes expansions which contains letters not in s and assigns letters in Gamma not in any t_i to first possibilty.
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
    expansions = {}
    assigns = {}

    # Read and handle strings t_i¨
    
    for _ in range(k):
        string = input()
        for char in string:
            if char not in Gamma and char not in Sigma:
                print("NO")
                return
            if char not in contained_letters and char in Gamma:
                contained_letters.append(char)
        strings.append(string)
    
    # Read expansion sets R_i
    while True:
        try:
            line = input()
        except EOFError: 
            break

        if line.count(":") != 1:
            print("NO")
            return
        letter, exp = line.split(":")
        
        if letter == "" or letter not in Gamma or letter in expansions:
            print("NO")
            return
        expansion_list = exp.split(",")
        if (len(expansion_list) != len(set(expansion_list))):
            print("NO")
            return
        for expans in expansion_list:
            for char in expans: 
                if char not in Sigma:
                    print("NO")
                    return
        expansions[letter] = expansion_list
    
    # Ensure no contained letter is missing expansion definition
    for letter in contained_letters:
        if letter not in expansions:
            print("NO")
            return
       
        
    # Preproces
    expansions, assigns = preprocess(s, contained_letters, expansions)
    
    # Explore and print result
    if res := explore(s, strings, expansions, assigns, contained_letters):
        print_formatted(res)
    else: 
        print("NO")
    
if __name__ == "__main__":
    main()
    
    