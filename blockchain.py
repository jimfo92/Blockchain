import hashlib
import datetime

class Block():
      def __init__(self, timestamp, data, previous_hash):
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.calc_hash(timestamp+data+str(previous_hash))
            self.next = None

      def calc_hash(self, data):
            sha = hashlib.sha256(data.encode())
            return sha.hexdigest()

      def get_hash(self):
            return self.hash


class Blockchain():
      def __init__(self):
          self.frist_block = None
          self.head_block = None 

      def insert_block(self, data):
            data = str(data) #if data is other type than data

            if data=="" or data==None:
                  raise ValueError("Value can not be empty or None")

            #day and time that block was created
            date_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")

            if self.head_block == None:
                  self.head_block = Block(date_time, data, 0)
                  self.frist_block = self.head_block

                  return self.head_block
            
            #get the previous hash
            previous_hash = self.head_block.get_hash()
            new_block = Block(date_time, data, previous_hash)
            self.head_block.next = new_block
            self.head_block = new_block

            return self.head_block


#-----------TEST BLOCKCHAIN------------

b_chain = Blockchain()

def test_case1():
      try:
            b_chain.insert_block("trasaction 1")
            b_chain.insert_block("transaction 2")
      except:
            print("Value can not be empty or None")
test_case1()

def test_case2():
      try:
            b_chain.insert_block("")
      except:
            print("Value can not be empty or None")
test_case2()

def test_case3():
      try:
            b_chain.insert_block(None)
      except:
            print("Value can not be empty or None")
test_case3()

def test_case4():
      try:
            b_chain.insert_block("trasaction 3")
            print(b_chain.head_block.timestamp)
            b_chain.insert_block("trasaction 4")
            print(b_chain.head_block.timestamp)
            b_chain.insert_block("trasaction 5")
            print(b_chain.head_block.timestamp)
      except:
            print("Value can not be empty or None")
test_case4()

def test_case5():
      try:
            b_chain.insert_block(584309859038509)
            print(b_chain.head_block.data)
      except:
            print("Value error")
test_case5()