__author__ = 'mushahidalam'

#difficult , need to implement

class Solution:
    # @param A : tuple of gers
    # @param B : tuple of gers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        i = 0;  # Current index of i/p array ar1[] */
        j = 0; # Current index of i/p array ar2[] */
        m1 = -1, m2 = -1;

        # Since there are 2n elements, median will be average
        for count in range(0,n):
        {
            #Below is to handle case where all elements of ar1[] are
            if (i == n):
            {
                m1 = m2;
                m2 = ar2[0];
                break;
            }
            #Below is to handle case where all elements of ar2[] are
            elif (j == n):
            {
                m1 = m2;
                m2 = ar1[0];
                break;
            }

            if (ar1[i] < ar2[j]):
            {
                m1 = m2;  # Store the prev median */
                m2 = ar1[i];
                i++;
            }
            else:
            {
                m1 = m2;  # Store the prev median */
                m2 = ar2[j];
                j++;
            }
        }

        return (m1 + m2)/2;

