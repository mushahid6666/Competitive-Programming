import datetime
class pallet(object):
    weight = float()

    def __init__(self, weight):
        self.weight = weight

class ListNode(object):
    def __init__(self, time, weight):
        self.time = time
        self.weight = weight
        self.next = None
        self.prev = None

class trailer(object):

    def __init__(self, capacity):
        self.total_capacity = capacity
        self.trailer_weight_list = None
        self.num_of_pallets = 0
        self.current_weight = 0

    def add_pallet(self, pallet):
        """
        :param pallet_weight:list[list]
        :return: bool
        """
        if self.current_weight + pallet.weight > self.total_capacity:
            return False

        self.num_of_pallets += 1
        self.current_weight = self.current_weight + pallet.weight
        new_node = ListNode(datetime.datetime.utcnow(), self.current_weight )
        if self.trailer_weight_list == None:
            self.trailer_weight_list = new_node
            return True

        j = self.trailer_weight_list
        while j.time < new_node.time and j.next != None:
            j = j.next

        if j.next == None:
            j.next = new_node
            new_node.prev = j
        else:
            j.prev.next = new_node
            new_node.prev = j.prev
            new_node.next = j
            j.prev = new_node

        return True

    def get_weight_at_time(self, given_time):
        """
        :param time:datetime
        :return:
        """
        j = self.trailer_weight_list
        while given_time > j.time and j.next != None:
            j = j.next

        k = self.trailer_weight_list
        # while k!=None:
        #     print k.time,k.weight, given_time
        #     k = k.next

        return j.weight


    def compare_time(self, time):
        node_time = (datetime.datetime.utcnow() + datetime.timedelta(days=2))
        node_time2 = (datetime.datetime.utcnow() - datetime.timedelta(days=3))
        weight = 100
        print node_time," : ", node_time2," : ", time
        if node_time > time and node_time2 < time:
            return weight
        return None



trailer_obj = trailer(3000)
success = trailer_obj.add_pallet(pallet(75))
print "pallet added 75: ", success
success = trailer_obj.add_pallet(pallet(100))
print "pallet added 100: ", success
success = trailer_obj.add_pallet(pallet(120))
print "pallet added 120: ", success
print trailer_obj.get_weight_at_time(datetime.datetime.utcnow())
