import hashlib
import json
from time import time

class Blockchain (object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        #Creates a new block and adds it to the chain
        pass
    
    def new_transaction(self, sender, recipient, amount):
        #Adds a new transaction to the list of transactions
           """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,      
            })
        return self.last_block['index'] + 1
    
    @staticmethod 

    def hash(block):
        #hashes a block
        pass

    @property
    def last_block(self):
        #returns the last Block in the Chain
        pass

