def findRedundantBrackets(s:str):
    stk = []

    for ch in s:
        if ch == ')':
            top = ch

            flag = True

            while (len(stk) != 0 and top != '('):
                if top == "+" or top == "-" or top == "*" or top == "/":
                    flag = False

                top = stk.pop()
            # If there is no operator present between the opening and closing brackets then the expression will be considered having redundant brackets.
            # Hence the output will be "Yes".
            if flag == True:
                return "Yes"

        else:
            stk.append(ch)
    # If no redundant brackets are found then function will return "No".
    return "No"
        
# Example:
s = "((b*c)*(a/b))"
ans = "No" # Since the expression does not contain any redundant brackets.
