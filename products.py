# products: 讓user重複輸入他買過的products
# while loop vs. for loop
# when we are not sure how many loops are there, we choose while loop
products = []
while True:
	name = input('Please enter products you purchased: ')
	if name == 'q':
		break
	price = input('Please enter the prices: ')
	# p = []
	# p.append(name)
	# p.append(price)
	p = [name, price]
	products.append(p)
	# Or: products.append([name, price])
print(products)
# structure: products = [ [n|p] | [n|p] | [n|p] ]
# e.g. [['a', '1'], ['b', '2'], ['c', '3']]

# for product in products:
# 	print(product)
# # ['a', '1']
# # ['b', '2']
# # ['c', '3']

# for product in products:
# 	print(product[0])
# # a
# # b
# # c

# # String calculation
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# Write the outputs in a file 
with open('products.csv', 'w') as f:
# with open('products.csv', 'w', encoding = 'utf-8') as f:
# if we want to print Chinese characters, then need to add encoding
	f.write('Product, Price\n')		# add headers
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
# If the messy codes are still there in the excel sheet, that's because
# excel does not using ctf-8 to read the data
# Solution:
# In excel: data > get data > From text/csv
# encoding: utf-8
# delimiter: comma

