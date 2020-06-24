import itertools as its
import json

class Letter_digitservice():
    #stre = "a2B"
    def change_string(self,value):
        lst = []
        for val in value:
            if(val.isupper() and not val.isdigit()):
                lst.append((val.lower(),val.upper()))
            elif not val.isdigit():
                lst.append((val.upper(),val.lower()))
            else:
                lst.append((val,))
        return  lst

    def show_string(self,value):
        lst = self.change_string(value)
        values_lst = []
        values_dict = {}
        for eachtuple in list(its.product(*lst)):
            values_lst.append("".join(eachtuple))
        values_dict["value"] = values_lst
        return values_dict

#l =Letter_digitservice()
#print(l.show_string('a2b'))