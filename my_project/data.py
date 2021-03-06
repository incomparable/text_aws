class Palindrome:
    def is_palindrome(word):
        if (word == word[::-1]):
            if True:
                print('.................')
                return True
        else:
            return None

    @staticmethod
    def group_by_owners(files):
        val = (list(files.values()))        # get values from dict
        val = set(val)                      # make values a set to remove duplicates
        val = list(val)                     # make set a list so we can work with it
        keyst = (list(files.keys()))        # get keys from dict
        result = {}                         # creat empty dict for output
        for i in range(len(val)):           # loop over values(owners)
            for j in range(len(keyst)):     # loop over keys(files)
                if val[i] == list(files.values())[j]:       # boolean to pick out files for current owner loop
                    dummylist = [keyst[j]]                    # make string pulled from dict a list so we can add it to the output in the correct format
                    if val[i] in result:                       # if the owner is already in the output add the new file to the existing dictionary entry
                        result[val[i]].append(keyst[j])     # add the new file
                    else:                                   # if the owner is NOT already in the output make a new entry
                        result[val[i]] = dummylist          # make a new entry
        return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

Palindrome.group_by_owners(files)

# Palindrome.is_palindrome('deleveled')


