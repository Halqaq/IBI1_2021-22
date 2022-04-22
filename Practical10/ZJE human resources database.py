# Use 'class' to contain information like name, role, and location of the staff working at ZJE.
class Staff(object):
    def __init__(self, n, r, l):  # Initialization.
        self.name = n
        self.role = r
        self.location = l

    def hdr(self):
        print('%s, as a %s, is in %s.' % (self.name, self.role, self.location))
        return '%s, as a %s, is in %s.' % (self.name, self.role, self.location)


# For example, Pr. Guo Wei is in International Campus. He is staff1.
staff1 = Staff('Guo Wei', 'Professor', 'International Campus')  # The order is name, role, location.
staff1.hdr()
