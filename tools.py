#Victor Alejandro Salazar
# 12061468

numbers = [1, 2, 3, 4]
tokens = ['For', 'sail:', 'baby', 'schooner,', 'never', 'seen', 'before!']

# In here we define the functions and lists which will be used with  
# functions my_map(), my_filter(), my_reduce()
def square(x):
    return x * x

def repeat(x):
    return x + 10*x

def repeat(x):
    return x + 10*x
def replace(word):
    subs = {'sail:': 'sale:', 'schooner,': 'shoes,', 'seen': 'worn.'}
    new_word = subs.get(word, word)
    return new_word

numbers = [0, -10, 8, 0, 1, -4, -8]
tokens = ['For', 'sale:', 'baby', 'shoes,', 'never', 'worn.', 'before!']

def negative(x):
    return x < 0
def no_before(word):
    return word != 'before!'

negative_numbers = [-10, -4, -8]
tokens = ['For', 'sale:', 'baby', 'shoes,', 'never', 'worn.']

def negative_mul(a, b):
    return -(a * b)
def join(a, b):
    return a + ' ' + b

# Here the funcions  function my_map(), my_filter(), my_reduce() are done , so that 
# with on those functions we can call the operations or functions wanted 

def my_map(function_to_apply,  list_of_inputs):
    result = [function_to_apply(x) for x in list_of_inputs ]
    return result
def my_filter(function_to_apply, list_of_inputs):
    result = [x for x in list_of_inputs if function_to_apply(x)]
    return result
# For my reduce the list is divided , first we take the 1st element and then the rest
# thi is done so that we can be able to implement addition or multiplication, so diff functions
def my_reduce(function_to_apply, list_of_inputs):
    y = list_of_inputs[0]
    for x  in list_of_inputs[1:]:
       y = function_to_apply(y,x)
    return y    

squared_numbers = my_map(square, numbers)
repeated_numbers = my_map(repeat, numbers)
new_tokens = my_map(replace, tokens)
negative_numbers = my_filter(negative, numbers)
numbers = my_filter(lambda x:  x % 17 == 0, range(100))
new_tokens = my_filter(no_before, tokens)
number = my_reduce(negative_mul, negative_numbers)
text = my_reduce(join, tokens)

print(text)
print(number)




