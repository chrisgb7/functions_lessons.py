def tea_order(customer_name, tea_type,*args, **kwargs):
    print(customer_name, "ordered a", tea_type,"tea")
    for arg in args:
        print("   - add", arg)
    for key, value in kwargs.items():
        print("   - add", key, ":", value)
    # print("kwargs contains:", kwargs)
    # for arg in extras:
    #     print("   - Add:, arg")
# tea_order("Alice", "chamomile")
# tea_order("bob","black",milk="oat")
tea_order("tony", "black", "oat" , sweetner="honey")
# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
def sum_squares(*args):
    sum =0
    for num in args:
        sum += num ** 2
        #first tme through:sum =c0 + 1^2 = 1
        #second time: sum = 1 + 2^2
    return sum
print(sum_squares(1,2,3))    
# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0
    for num in args:
        total += abs(num)
    return total    
print(absolute_sum(-1,-2,3))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"