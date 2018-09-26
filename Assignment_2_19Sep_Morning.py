# 1. Create a new dictionary called prices using {}

prices = {'banana': '4', 'apple': '2','orange' : '1.5','pear' : '3'}
print(prices)

# 2. Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key' : 'hello'}
print(d['simple_key'])

d1 = {'k1' : {'k2' : 'hello'}}
print(d1['k1']['k2'])

d2 = {'k1' : [{'nest_key' : ['this is deep', ['hello']]}]}
print(d2['k1'][0]['nest_key'][1][0])

d3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])

# 3. What is the boolean output of the cell block below?
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1' : 4}]
print(l_one[2][0] >= l_two[2]['k1'])

# 4. Given the following dictionary:
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory.update({'pocket' : ['seashell', 'strange berry', 'lint']})

print(inventory)





