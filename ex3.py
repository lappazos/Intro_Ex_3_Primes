def create_list():
    """This function gets from user_input a number of strings, and return
    them as combined list named list1. the func will end as soon as the
    user enters an empty string"""
    while True:
        # the loop will run until i break it, meaning, until the user enters an
        # empty string
        list1 = []
        string_from_user = str(input())
        if string_from_user == '':
            break
        else:
            list1.append(string_from_user)
            continue
    return list1


def concat_list(str_lst):
    """This function gets a list containing various strings, and concatenate
     them into one large string returned to us"""
    lst_len = len(str_lst)
    # check the list length in order to determine the loop length
    concat_str = ''
    for i in range(lst_len):
        concat_str += str_lst[i]
    return concat_str


def average(num_list):
    """This Function returns the average for a series of numbers"""
    lst_len = len(num_list)
    # check the list length in order to determine the loop length. in case
    # there are no numbers, we will be returned None
    if lst_len == 0:
        return None
    else:
        num_sum = 0
        for i in range(lst_len):
            num_sum += float(num_list[i])
        # Average definition
        num_average = num_sum/lst_len
        return num_average


def cyclic(lst1, lst2):
    """The function will check whether or not 2 seperate lists are cyclic
    permutation of one another"""
    val_cyclic = False
    # defines list 1 length as a variable
    lst_len = len(lst1)
    # id the 2 lengths are different - for sure this is not cyclic permutation
    if lst_len != len(lst2):
        return False
    # if the lists equals extacly one another - this is also a kind of
    # cyclic permutation
    elif lst1 == lst2:
        return True
    else:
        # we will check each letter in llist 2 in comprasion to list1[0]. as
        # soon as we will find a match, we will build a new check_list to
        # compare it with list1. if we get false, we'll continue to search
        # for other matches
        # comment - no need to check list2[0], because if the lists are
        # indeed cycles of one another, and the first letter will match,
        # we would find out earlier that the lists are actually equal.
        for i in range(lst_len - 1):
            if lst1[0] != lst2[i+1]:
                continue
            check_list = lst2[(i+1):] + lst2[0:(1+i)]
            if check_list == lst1:
                val_cyclic = True
                break
        return val_cyclic


def histogram(n, num_list):
    """the function creates new list with n items - every item is the number of
     times that item index appeared in the input list"""
    histogram_list = []
    for i in range (n):
        # the number of items in the list will be determined by n
        histogram_list.append(0)
        for j in range (len(num_list)):
            # the second loop is in charge of counting the amount of times
            # index i appear in  the input list
            if num_list[j] == i:
                histogram_list[i] += 1
    return histogram_list


def prime_factors(n):
    """by the theory of fundamental theorem of arithmetic, The function
    gives us the prime factors that create the input number"""
    ans = []
    # the following loop divide my number in all of the previous natural
    # numbers smaller than him, instead of 1 that will automatically give
    # us []. it will stop and enter the next loop only when  we will find
    # his first prime factor
    for i in range(2,n+1):
        # the next loop will continue devide the number in the specific
        # prime we found, until we could understand how many times it will
        # be used as one of the factors. only then, if needed, it will break
        #  and send us to the next i in our searching
        while n%i == 0:
            ans.append(i)
            n = n/i
            if n < i:
                return ans
    return ans


def cartesian(lst1, lst2):
    """The function gives us the cartesian product of 2 lists - the
    potential combinations of both lists items"""
    output = []
    # if one of the lists is empty the product list wil be empty
    if lst2 == []:
        return output
    if lst2 == []:
        return output
    # the first loop go over the items in lst1
    for i in range(len(lst1)):
        # # the second loop go over the items in lst2 for every item i
        for j in range(len(lst2)):
            # the output will be list, which every possible combination as a
            # tuple in it
            output.append((lst1[i], lst2[j]))
    return output


def pairs(n, num_list):
    """the function finds all of the item pairs in the list that their sum
    equal to n"""
    # we will begin with en empty list - default situation, ill only add
    # items if i find pairs who match the criteria
    ans = []
    # the next loop goes on  each end every item in the list
    for i in range(len(num_list)):
        #the next index grows every stage, while i is constant, which let us
        #  check i with each and every item. please pay attention index goes
        #  back to 1 every time we are moving to the next i in range
        index = i + 1
        while index < len(num_list) :
            if num_list[i] + num_list[index] == n:
                ans.append([num_list[i], num_list[index]])
            index += 1
    return ans