# Flatten nested dictionaries 

def flatten(nested_dict, ancestors = None, final_dict={}):

    for key, val in nested_dict.items():

        if type(val) == int:
            if ancestors is None:
                final_dict[key] = val
            else:
                final_dict[ancestors + "." + key] = val
        else:
            if ancestors is not None:
                n_ancestors = ancestors + "." + key
            else:
                n_ancestors = key

            flatten(val, n_ancestors, final_dict)

    return final_dict

    

dict1 = {"a": 2,
        "b": {"c": 3,
            "d": 4,
            "e": {"f": 5,
                "g": 6}}}

print flatten(dict1)