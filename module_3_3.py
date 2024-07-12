def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
#print_params(23, 'error', False, 'уже нельзя') - TypeError: print_params() takes from 0 to 3 positional arguments but 4 were given
print_params(b=25)
print_params(c=[1,2,3])

value_list = [256.89, True, 'end']
print_params(*value_list)
value_dict = {'a': 25.45, 'b': 'словарь', 'c': True}
print_params(**value_dict)
values_list_2 = [False, 'слово']
print_params(*values_list_2, 42)