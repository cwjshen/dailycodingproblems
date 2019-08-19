# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

class OrderLog:
    def __init__(self, order_list=None):
        self.order_list = order_list if order_list != None else []

    def record(self, order_id):
        self.order_list.append(order_id)

    def get_last(self, i):
        return self.order_list[len(self.order_list) - i]

    def to_string(self):
        print(self.order_list)

my_log = OrderLog([1,2,3,4,5])
my_log.record(6)
my_log.record(7)
my_log.to_string()

# Should print 6
print(my_log.get_last(2))