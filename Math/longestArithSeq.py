class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)==0:
            return 0
        if len(A)==1:
            return 1
        number_dict = dict()
        for i in range(len(A)):
            if A[i] in number_dict:
                number_dict[A[i]].append(i)
            else:
                number_dict[A[i]] = [i]
        max_seq_lenght = 1
        for i in range(len(A)):
            cur_numerb = A[i]
            cur_seq_lenght = 1
            for j in range(i+1, len(A)):
                cur_seq_lenght += 1

                diff =  A[j] - cur_numerb
                target_number = A[j] +  diff
                cur_index = j
                while target_number in number_dict:
                    index_list = number_dict[target_number]
                    found_index = -1
                    for index in index_list:
                        if index > cur_index:
                            cur_seq_lenght += 1
                            found_index = index
                            break
                    if found_index != -1:
                        target_number = A[index] + diff
                        cur_index = index
                    else:
                        break
                max_seq_lenght = max(max_seq_lenght,cur_seq_lenght )
                cur_seq_lenght = 1
        return max_seq_lenght

obj = Solution()
# sequence = [3,6,9,12]
sequence = [9,4,7,2,10]
# sequence = [20,1,15,3,10,5,8]
print obj.longestArithSeqLength(sequence)