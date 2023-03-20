trying=0
secret_number=2
limit=3

while trying<limit:
    guess_number=input("masukkan angka (1-9): ")
    guess_number=int(guess_number)

    if guess_number==secret_number:
        print("selamat, kamu menang")
        break
trying+=1