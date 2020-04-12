"""
Miscellaneous functions
"""


# Ever so gracefully Ctrl+C, Ctrl+V ed from Stack Overflow
# https://stackoverflow.com/questions/12898023/replacing-a-sublist-with-another-sublist-in-python
def find_first_sublist(seq, sublist, start=0):
    length = len(sublist)
    for index in range(start, len(seq)):
        if seq[index:index+length] == sublist:
            return index, index+length


def replace_sublist(seq, sublist, replacement):
    length = len(replacement)
    index = 0
    for start, end in iter(lambda: find_first_sublist(seq, sublist, index), None):
        seq[start:end] = replacement
        index = start + length
