# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://www.w3schools.com/python/python_ref_dictionary.asp

def make_dict():
    currency = {'Ten' : 10 ,'Twenty' : 20 ,'Thirty' : 30}

    return currency

def add_element():
    foods = {'fruit': 'apple', 'veggie': 'carrot', 'grain': 'barley'}
    foods['dairy'] = 'yogurt'

    return foods

def remove_element():
    foods = {'fruit': 'apple', 'veggie': 'carrot', 'grain': 'barley'}
    del foods['veggie']

    return foods

def merge_dict():
    # Merge these two dictionaries together so the contents are in numerical order:
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)

    return dict1  

def access_key():
    currency = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    val = currency.pop('Twenty')     

    return val

if __name__ == '__main__':
    # Test your code with this first
    # Change the function to test different sections
    print(merge_dict())
    

