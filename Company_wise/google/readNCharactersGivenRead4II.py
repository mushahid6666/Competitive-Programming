"""
Given a file and assume that you can only read the file using a given method read4,
implement a method read to read n characters. Your method read may be called multiple times.


Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf
    Returns:    int

Note: buf[] is destination not source, the results from read4 will be copied to buf[]
Below is a high level example of how read4 works:

File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of file


Method read:

By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]


Example 1:

File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Example 2:

File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.


Note:

Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.
"""
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
file = "abcdefghijk"
def read4(buf):
    for i in range(4):
        buf[i] = file[i]
    return 4

class Solution(object):
    def __init__(self):
        self.overReadList = list()
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type requested_charecters: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        requested_charecters = n
        buffer_index = 0
        char_read_from_file = 0

        while buffer_index < requested_charecters:
            #If previous call had over read charecters from file
            if len(self.overReadList) != 0:
                while buffer_index < requested_charecters and len(self.overReadList) !=0 :
                    buf[buffer_index] = self.overReadList.pop(0)
                    buffer_index+=1
                    char_read_from_file += 1
            if buffer_index==requested_charecters:
                return char_read_from_file

            #Call Read4 Api to read from file

            #1.create buffer for read4
            read4_buf = [None] * 4
            r4_count = read4(read4_buf)

            #If EOF return
            if r4_count == 0:
                break
            #Requested charecter might be less than charecters read from file or we might have reached EOF
            k = min(requested_charecters - buffer_index, 4, r4_count)
            read4_buf_index = 0
            while buffer_index < k:
                buf[buffer_index] = read4_buf[read4_buf_index]
                read4_buf_index+=1
                buffer_index+=1
            char_read_from_file += read4_buf_index

            # if read4buf has left over charecters store it in overread list
            if r4_count > read4_buf_index:
                self.overReadList = []
                while read4_buf_index < r4_count:
                    self.overReadList.append(read4_buf[read4_buf_index])
                    read4_buf_index += 1
        return char_read_from_file

obj  = Solution()
buf = [' ']* 4
print obj.read(buf, 4)
print buf