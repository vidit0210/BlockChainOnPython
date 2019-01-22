blockChain = []
# is checks with memory Location
# in chcek whether the item is the stuff or not
# Check where 2 in Data


def get_last_blockChain_value():
    """Return Last Value from the BlockChain"""
    if len(blockChain) < 1:
        return "Genesis Block"
    return blockChain[-1]


def add_value(value=0):
    """ Append a new Value as well as the lasty blockChain Value 
    Arguments:
        :value : Enter the value of the transaction Data
    """
    blockChain.append([get_last_blockChain_value(), value])
    print(blockChain)


def get_transaction_input():
    return float(input("Your Transaction Amount"))


def get_user_choice():
    """ Gets user choice """
    user_input = int(input("Get User Choice "))
    return user_input


def print_bockChain_value():
    """Prints all the Blocks in the BlockChain"""
    for block in blockChain:
        print('Outputing Block')
        print(block)

# tx_amount = get_transaction_input()
# add_value(tx_amount)


def verify_chain():
    blockIndex = 0
    is_valid = True

    for block in blockChain:
        if blockIndex == 0:
            blockIndex += 1
            continue
        elif block[0] == blockChain[blockIndex - 1]:
            is_valid = True
        else:
            is_valid = False
        blockIndex += 1
    return is_valid


while True:
    print("1:add New transaction value \n 2: Output the Blocks \n  3 exit  \n 4 Manipulate Chain \n 5 Verify Chain")
    choice = get_user_choice()
    if choice == 1:
        tx_amount = get_transaction_input()
        add_value(tx_amount)
        print('Value Added Succesfully')

    elif choice == 2:
        print_bockChain_value()
    elif choice == 3:
        break
    elif choice == 4:
        if len(blockChain) > 1:
            blockChain[0] = 2
    else:
        print("Enter correct Value")
    if not verify_chain():
        print("Invalid Chain")
        break


print("Outside The Loop")
