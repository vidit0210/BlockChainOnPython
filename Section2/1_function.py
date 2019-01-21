blockChain = [[1]]


def get_last_blockChain_value():
    """Return Last Value from the BlockChain"""
    return blockChain[-1]


def add_value(value=0):
    """ Append a new Value as well as the lasty blockChain Value 
    Arguments:
        :value : Enter the value of the transaction Data
    """
    blockChain.append([get_last_blockChain_value(), value])
    print(blockChain)


def get_user_input():
    return float(input("Your Transaction Amount"))


tx_amount = get_user_input()

add_value(tx_amount)
tx_amount = get_user_input()

add_value(tx_amount)
