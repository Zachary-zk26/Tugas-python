user={
    "name":"Zakaria",
    "age":20,
    "is_admin":True
}

temp=user.get("username")
print(temp)

temp=user.get("username","zakaria_26")
print(temp)

user["username"]="zakaria_26"
user["name"]="jek"

temp=user.get("name")
print(temp)