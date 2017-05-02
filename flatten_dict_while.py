def flatten(dic):

    result_d = {}
    ancestors = ""
    current_d = dic
    new_d = True
    while new_d:
        k_v = current_d
        new_d = False
        for key, value in k_v.items():
            if type(value) == int:
                if ancestors == '':
                    result_d[key] = value
                else:
                    result_d[ancestors + key] = value
            else:
                current_d = value
                new_d = True
                if ancestors == '':
                    new_anc = key + '.'
                else:
                    new_anc = ancestors + key + '.'
                current_anc = new_anc
        if current_anc:
            ancestors = current_anc
            current_anc = ''
    return result_d


dic = {'a': 2,
       'b': {'c': 3,
             'd': 4,
             'e': {
                 'f': 5
                       },
                       'g': 6}}

print flatten(dic)

# {a : 2, 
#  b.c : 3, 
#  b.d : 4
#  b.e.f : 5}