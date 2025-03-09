def input_int_list(prompt: str):
    input_string = input(prompt)

    # map(function, iterable)
    # apply a specified function to each item in an iterable
    return list(map(int, input_string.split()))


def find_sequence(l: list):
    output_list = list()
    for i in range(0, len(l) - 2):
        x = l[i: i + 3]
        if sum(x) == 0:
            output_list.append(x)

    return output_list


# -1 0 1 0 -1 -4
input_list = input_int_list("Input: ")
sequence_list = find_sequence(input_list)

print(f"There exists {len(sequence_list)} such sequence(s):")

# enumerate is used to iterate over output_list while keeping track of the index
for i, x in enumerate(sequence_list, start=1):
    output_string = " + ".join(str(n) for n in x)
    print(f"{i}) {output_string} = 0")

# [alternate method]
# for i, x in enumerate(output_list, start=1):
#     output_string = ""
#     for n in x:
#         output_string += str(n) + " + "
#     print(f"{i}) {output_string[:-2]}= 0")