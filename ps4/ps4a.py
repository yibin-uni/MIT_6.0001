# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    import string
    permutations=[]
    perm=''
    if len(sequence)==1:
        permutations.append(sequence)
        return permutations
    else:                
        new_seq=list(sequence)
        del_letter=new_seq.pop(0)
        sub_perm=get_permutations(new_seq)
        for e in sub_perm:
            e=''.join(e)  
            new_space=str.replace(e,'','_')
            new_list=list(new_space)
            n=len(new_seq)
            for i in range(n+1):
                new_list[2*i]=del_letter
                for e in new_list:
                    if e in string.ascii_lowercase:
                        perm=perm+e
                        if len(perm)==n+1:
                            if not perm in permutations:
                                permutations.append(perm)
                            perm=''
                new_list=list(new_space)
    return permutations


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    example_input_1 ='ab'
    print('Input:', example_input_1)
    print('Expected Output:', ['ab','ba'])
    print('Actual Output:', get_permutations(example_input_1))
    example_input_2 = 'abc'
    print('Input:', example_input_2)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input_2))
    example_input_3 = 'aab'
    print('Input:', example_input_3)
    print('Expected Output:', ['aab', 'aba', 'baa'])
    print('Actual Output:', get_permutations(example_input_3))
     #delete this line and replace with your code here

