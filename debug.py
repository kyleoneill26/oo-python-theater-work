import ipdb
from lib import *

# Test your code below...
batman = Role("Batman")
spiderman = Role("SPiderman")

a1 = Audition("Michael", "LA", True, batman)
a2 = Audition("Alex", "Nashville", True, batman)
a2 = Audition("James", "NYC", False, spiderman)
a2 = Audition("Rhianna", "Miami", True, spiderman)




# the below line allows us to stop & try stuff!
ipdb.set_trace()