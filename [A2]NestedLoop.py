def input_int_list(prompt: str):
    input_string = input(prompt)

    # map(function, iterable)
    # apply a specified function to each item in an iterable
    return list(map(int, input_string.split()))


def digital_root(num: int):
    while True:
        res = 0
        while num > 0:
            res += num % 10
            num //= 10

        if res // 10 != 0:
            num = res
        else:
            break

    return res


# 125 23 156 89 22
input_list = input_int_list("Enter (int) elements: ")
output_list = list()

for n in input_list:
    output_list.append(digital_root(n))

print(f"list1 = {input_list}")
print(f"list2 = {output_list}")