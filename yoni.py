# def to_sum(n):
#     count =0
#     for i in range(n+1):
#         count += i
#     return count
# print(to_sum(5))

# def factorial(n):
#     count = 1
#     for i in range(1,n+1):
#         count *= i
#     return count
# print(factorial(5))

# def even_count(a,b):
#     count = 0
#     for i in range(a,b+1):
#         if i%2 == 0:
#             count += 1
#         else:
#             continue
#     return count
# print(even_count(3,10))

# def sum_digit(n):
#     count = 0
#     while n > 0:
#         d = n%10 
#         count += d
#         n = n //10
#     return count
# print(sum_digit(4343))

# def number_reverse(n):
#     num = []
#     while n > 0:
#         d = n%10
#         num.append(d)
#         n = n//10
#     return num
# print(number_reverse(1234))

# def prime_is(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#         return True
# print(prime_is(13))

# def fizzbuzz(n):
#     num = []
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             num.append("fizzbuzz")
#         elif i%5==0:
#             num.append("buzz")
#         elif i%3==0:
#             num.append("fizz")
#         else:
#             num.append(i)
#     return num
# print(fizzbuzz(30))

# def find_max(n):
#     num = 0
#     for i in n:
#         if n==[]:
#             return None
#         else:
#             if i > num:
#                 num = i
#     return num
# print(find_max([2,4,8,5,9]))

# def average(n):
#     num = 0 
#     for i in n:
#         num += i
#     return num/len(n)
# print(average([2,4,6]))

# def accurrences_count(n,x):
#     num = 0 
#     for i in x:
#         if i == n:
#             num += 1
#     return num
# print(accurrences_count(1,[1,4,2,1,6,1]))
ggkjhlghkj