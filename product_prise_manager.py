products = []
count = int(input('How many product do you have:'))

for i in range(count):
    name = input(f'Enter the name of product {i+1}:')
    price = int(input(f'Enter the price of {name}:'))
    products.append({'name': name, 'price': price})

avg = sum(p['price'] for p in products) / len(products)
maximum = max(products, key = lambda p: p['price'])
minimum = min(products,key = lambda p: p['price'])
sorted_product = sorted(products, key = lambda p: p['price'])

print('Average price:', avg)
print('Most expensive:', maximum['name'] , maximum['price'])
print('Cheapest:' ,minimum['name'], minimum['price'])
print('\nSorted products:')
for p in sorted_product:
    print(p['name'], '-' , p['price'])
