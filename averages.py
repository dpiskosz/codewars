#Write a method, that gets an array of integer-numbers and return an array
# of the averages of each integer-number and his follower, if there is one.

num_list = [1, 3, 5, 1, -10]


def averages(input_list):
    aver_list = []
    try:
        if input_list == 1 or 0 or None:
            return []
        else:
            for x in range(0, len(input_list)-1):
                val = input_list[x] + input_list[x+1]
                aver = val / 2
                aver_list.append(aver)
            return aver_list
    except Exception as NoneType:
        return []


print(averages(num_list))
