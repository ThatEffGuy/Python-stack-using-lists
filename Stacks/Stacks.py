# Py program to demonstrate stack using a list

stack = []

#append() func to push
#element in the stack
stack.append('Alex')
stack.append('Barry')
stack.append('Craig')

print('initial stack')
print(stack)

#pop() func to pop element from stack in LIFO (last in first out)
print('\n Elements popped from stack: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\n stack after elements are popped: ')
print(stack)
