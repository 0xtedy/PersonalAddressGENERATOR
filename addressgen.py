from eth_account import Account
import secrets

def genAccount():
    prv = "0x" + secrets.token_hex(32)
    account = Account.from_key(prv)
    return account, prv

starting_char = input("Choose the prefix you want:")
print("Estimated try:",16**len(starting_char))
found = False
counter = 0

while found != True:
    counter += 1
    print("\r", end="")
    print("try: {:0} ".format(counter), end="")
    account, prv_address = genAccount()
    pbl_address = account.address
    if pbl_address[2:len(starting_char)+2] == starting_char:
        found = True
        print("\r Address found after",counter,"try !")
        print("Public address:",pbl_address)
        print("Private key:",prv_address)
