command=""

while command!="exit":
    command=input("perintah : ")

    if command=="exit":
        break
    if command!="+" and command!="-" and command!="*" and command!="/":
        print("perintah tidak dikenali")
        continue

    a=int(input("angka pertama : "))
    b=int(input("angka kedua : "))

    if command=="+":
        result=a+b
    if command=="-":
        result=a-b
    if command=="*":
        result=a*b
    if command=="/":
        result=a/b
    
    print(f"hasil : {result}")