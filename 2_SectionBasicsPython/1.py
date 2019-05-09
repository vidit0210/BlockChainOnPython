blockchain = [['Genesis Block']]


def get_last_blockchain_value():
    """ Returns the Last value of the Blockchain """
    return blockchain[-1]


def add_value(value):
    """ Apppends Value into the BlockChain. 

    Arguments:
         : value : The Amount to be Added
    """
    return blockchain.append([get_last_blockchain_value(),
                              value])


def get_user_input():
    return float(input("Enter Transaction Amount"))


Tx = get_user_input()
add_value(Tx)
print(blockchain)
