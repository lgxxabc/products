# Refactor(重構) the func.py
# 中心思想：每個function只做一件事情
# Check if the file exists, before reading it.
import os		# operating system

# 1. Read from a file
def read_file(filename):
	products = []
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
		price = int(price)
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
def print_products(products):
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


# Define the main function
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('File exists.')
		products = read_file(filename)
	else:
		print('Could not find the file.')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

# To operate the main function
main()
