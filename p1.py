import re


class Jsoncontainer(object):
    '''
    a dictionary object is used to generate the movie object.
    the key of the dictionary is the attribute of the movie
    object.
    Though this method is not safe, I can write less....

    Jsoncontainer(dict): initialize this class and return a
    Jsoncontainer object
    '''
    def __init__(self, d):
        pattern = re.compile(r'^[_A-Za-z][_\w]*$')
        for ind in d:
            # Use the regular expression to match the key.
            # Only keep the legal keys as attributes.
            if pattern.match(ind):
                self.__dict__[ind] = d[ind]
