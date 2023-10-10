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
    print(assigns)
    return True


def explore(s, strings, expansions, assigns, contained_letters):
    if len(expansions) == 0:
        return check(s, strings, assigns)
    letter = list(expansions.keys())[0]
    expansion_list = expansions[letter]

    # Skip all expansions if letter not in any string
    if letter not in contained_letters:
        expansions_copy = expansions.copy()
        expansions_copy.pop(letter)
        if explore(s, strings, expansions_copy, assigns, contained_letters):
            return True
    else: 
        for expansion in expansion_list:
            # Skip expansion if not all letters in s
            skip_exp = False
            for char in expansion: 
                if char not in s:
                    skip_exp = True
                    break
            if skip_exp:
                continue


            assigns[letter] = expansion
            expansions_copy = expansions.copy()
            expansions_copy.pop(letter)
            if explore(s, strings, expansions_copy, assigns, contained_letters):
                return True
            assigns.pop(letter)

    return False



# Setup and input
Gamma = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
Sigma = [chr(i) for i in range(ord('a'), ord('z') + 1)]

n = int(input())
s = input()

strings = []
contained_letters = []
for i in range(n):
    string = input()
    strings.append(string)
    for char in string:
        if char not in contained_letters and char in Gamma:
            contained_letters.append(char)

expansions = {}
for _ in range(26):
    letter, exp = input().split(":")
    expansions[letter] = exp.split(",")

assigns = {}
print(explore(s, strings, expansions, assigns, contained_letters))
