'''plan
ask for sentence
split sentence by spaces
reverse listed order
spit out as string again in new order


'''

reverse_str = input('Give me a sentence to reverse:  ') #receive string
step1 = reverse_str.split() #seperate string
step2 = step1[::-1]
end_prod = " ".join(step2)
print(end_prod)