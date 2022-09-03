""" Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format."""
oct_num=0o25
dic_rep=bin(oct_num)
hex_num=0x39
dic_rep1=bin(hex_num)
bin_rep=oct_num+hex_num
print(bin(bin_rep))

#b1001110