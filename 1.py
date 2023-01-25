import re

original_list = ["name512", "same1example", "joy18full"]
modified_list = []

for string in original_list:
    modified_string = re.sub('\d', "", string)
    modified_list.append(modified_string)

print(modified_list)
