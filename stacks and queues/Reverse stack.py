def reverseStack(inputStack, extraStack) :
  # If the length of input stack has reached to 1 that means there is no possibility to reverse the stack hence return.
	if len(inputStack) <= 1: 
		return
		
	while len(inputStack) != 1:
		ele = inputStack.pop()
		extraStack.append(ele)

  # This operation will keep a track of last element for every recursion call.
	lastElement = inputStack.pop()
	
	while len(extraStack) != 0:
		ele = extraStack.pop()
		inputStack.append(ele)
		
	# We have to reverse the input stack itself with the help of one extra stack.
  reverseStack(inputStack, extraStack)
	inputStack.append(lastElement)

#Example:
inputStack = [-90, 9, 20, 14, 6, 10]
extraStack = []
reverseStack(inputStack, extraStack)
print(inputStack) # Reversed Stack.
