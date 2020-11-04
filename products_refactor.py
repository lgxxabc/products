# Refactor the func.py
# Check if the file exists, before reading it.
import os		# operating system

# 1. Read from a file
def read_file(filename):
	products = []
	if os.path.isfile(filename):
		print('File exists.')
		
		# Read from file 'products.csv'
		# Steps:
		# 1. .split('.')，用comma來做分割
		# 2. .strip()來除掉換行符號(\n)
		# 3. 加上encoding = 'utf-8'來去除UnicodeDecodeError
		with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				# get rid of the header when reading the file
				if 'product, price' in line:
					continue

				# s = line.strip().split(',')
				# name = s[0]
				# price = s[1]
				# this is equal to:
				name, price = line.strip().split(',')
				# 把讀到的内容裝進list
				products.append([name, price])
		print(products)
		# Outputs:
		# products: 讓user重複輸入他買過的products
		# while loop vs. for loop
		# when we are not sure how many loops are there, we choose while loop

	else:
		print('Could not find the file.')
	return products


# 2. 請使用者輸入
def user_input(products):
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
	return products


# 3. 印出所有商品
def user_input(products):
	for product in products:
		print(product[0])
	# a
	# b
	# c

	# # String calculation
	# 'abc' + '123' = 'abc123'
	# 'abc' * 3 = 'abcabcabc'


# 4. Write the outputs in a file（寫入檔案）
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
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


# Use the function 1~4
products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)
