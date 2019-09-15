# //Anagram
# //
# //abc
# //cab
# //bac
# //
# //aab
# //
# //AcB
# //cBa
# //
# //Input = "abc  BaC   Dfe EdF    xyz cAb   deF ....."
# //
# //Output = "abc BaC Dfe EdF cAb deF ....."


dictionaryOfIndices = dict();  # map to maintain the index to word mappings


##Step 1 : Create a duplicate list of word objects which maintains index flag.
##Step 2 : Sort each word in the duplicate array_problems wrt to its letters
##Step 3 : Sort the word list
##Step 4 : Now since the list is sorted, if a word does not have its next element equal to itself then it does not have an anagram
##Step 5 : If not anagram then set its index as -1 to indicate that its not an anagram
##Step 6 : Iterate through tthe input string again anad check in the dictionary if the index is -1 for that respective word.
##Step 7 : Add all strings whose index is not -1 to the output string


class word(object):
    def __init__(self, string, iindex):
        self.string = string
        self.index = index


def removeSingleOccurrencesOfWord(dupArray):
    currString = dupArray[0].string;
    currIndex = dupArray.[0].index;
    for i in xrange(1,
                    len(dupArray)):  # check for anagrams in the list by comparing with next elements since it is sorted
        if (dupArray[currIndex] != dupArray[i]):
            dupArray[currIndex].index = -1;
            dictionaryOfIndices[currIndex] = dupArray[currIndex]
        else:
            while (i < len(dupArray) and currString == dupArray[i]):  # select only
                i += 1
            currString = dupArray[i]
            i += 1


return dupArray


def getduplicate(input):
    duplicatearray = list()
    listOfWords = input.split(" ");
    # now listOfWords contains list of words, if multiple of
    for i in xrange(len(listOfWords)):
        if (listOfWords[i].isSpace()):
            continue
        else:
            newWord = word(listOfWords[i], i)
            duplicatearray.append(newWord)
            dictionaryOfIndices[i] = newWord
    return duplicatearray


def PrintAnagram(Input):
    listOfWordsFromInput = Input.split(" ")  # get list again to create the output
    dupArray = getduplicate(Input, len(Input));

    for i in xrange(len(dupArray)):
        dupArray[i] = sorted(dupArray[i].string)  # sort each word letters

    dupArray = sorted(dupArray, key=lamda
    k: k.string)

    dupArray = removeSingleOccurrencesOfWord(dupArray)

    outputString = ""

    index = 0
    for word in listOfWordsFromInput:
        if (word.isspace()):
            continue
        elif dictionaryOfIndices[index].index != -1:  # add to output only if the index of word is not set to -1
            outputString += word + " "

        index += 1
    return outputString


struct
node * inOrderSuccessor(struct
node * root, struct
node * n)
{
// step
1
of
the
above
algorithm
if (n->right != NULL )
return minValue(n->right);

struct
node * succ = NULL;

// Start
from root and search
for successor down the tree
while (root != NULL)
    {
    if (n->data < root->data)
{
    succ = root;
root = root->left;
}
else if (n->data > root->data)
root = root->right;
else
break;
}

return succ;
}
