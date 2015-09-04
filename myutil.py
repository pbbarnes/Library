#!/usr/bin/env python3

# external modules

# my modules

def get_yn(question):
    ans = ''
    while (ans.upper() != 'Y') and (ans.upper() != 'N'):
        print(question,end="")
        ans = input()
    if ans.upper() == 'Y':
        return True
    return False

def remove_dict_from_list(thelist, key, value):
    # removes dictionaries containing the supplied key/value from a list of dictionaries
    thelist[:] = [d for d in thelist if d.get(key) != value]
    return(thelist)
    
def mod_dict_in_list(thelist, checkkey, checkvalue, changekey, changevalue):
    # modifies entries in a list of dictionaries based on check criteria
    outlist = []
    for d in thelist:
        if checkkey in d.keys():
            if d[checkkey] == checkvalue:
                d[changekey] = changevalue
        outlist.append(d)
    return(outlist)
    
    
def test_mod():
    mylist = [{'name':'scott'}, {'name':'roberts'}]
    outlist = mod_dict_in_list(mylist, 'name', 'scott', 'flag', False)
    print(outlist)
    
    
if __name__ == '__main__':
    print("Running module test code for",__file__)
    test_mod()
                