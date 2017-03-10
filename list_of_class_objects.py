class FemtoDatas(object):
    def __init__(self, id=None, name =None, latitude=None, longitude=None, fddextlist=[]) :
         self.id = id
         self.name = name
         self.latitude = latitude
         self.longitude = longitude
         self.fddextlist = fddextlist

#create an empty list
femto_list = []

# append a class objects to list
femto_list.append(FemtoDatas(id="900",name="FemtoDummy",latitude="19993.343.53.34",
                             longitude="0.7.6.5",
                             fddextlist=["343.646.45.4","343.44.33.44"]))

# print the fddextlist
for items in femto_list:
    print items.fddextlist
