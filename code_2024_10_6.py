# first_name="ada"
# last_name="lovelace"
# full_name=f"{first_name} {last_name}"
# print(f"Hello,{full_name.title()}")   #不赋给变量，直接打印
#
# message=f"Hello,{full_name.title()}"
# print(message)    #创建完消息后，把整条消息赋值给变量，再打印

# first_name="ada"
# last_name="lovelace"
# full_name="{} {}".format(first_name,last_name)
# print(full_name)

# print("Python")
# print("\tPython")

# print("Language:\nPython\nC\nJavaScript")

# print("Language:\n\tPython\n\tC\n\tJavaScript")

language=" Python "
x="a"
print(f"{x}{language}{x}")
print(f"{x}{language.rstrip()}{x}")
print(f"{x}{language.lstrip()}{x}")
print(f"{x}{language.strip()}{x}")