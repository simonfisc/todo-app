file = open("../files/members.txt", 'r')
members = file.readlines()
file.close()

for member in members:
    new_member = input("Enter new member: ")
    members.append(f"{new_member}\n")
    file = open("../files/members.txt", 'w')
    file.writelines(members)
    file.close()
