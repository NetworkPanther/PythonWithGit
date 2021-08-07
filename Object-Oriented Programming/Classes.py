class Router:
    '''Router model blueprint'''
    def __init__(self, model, softwareVersion, ipAddress):
        '''Initialize Router objects and associated values'''
        self.model = model
        self.softwareVersion = softwareVersion
        self.ipAddress = ipAddress

    def getDetails(self):
        '''Instantiate this method to get router's details'''
        details = f'Router Model                : {self.model}\n'\
                  f'Router Software Version     : {self.softwareVersion}\n'\
                  f'Router IP Address           : {self.ipAddress}'
        return details

class Switch(Router):
    #Inheritance
    '''Class Switch (child) to Class Router (parent)'''
    def getDetails(self):
        '''Instantiate this method to get router's details'''
        details = f'Switch Model                : {self.model}\n'\
                  f'Switch Software Version     : {self.softwareVersion}\n'\
                  f'Switch IP Address           : {self.ipAddress}'
        return details



rtr1 = Router('3400X', '15.1.6', '172.16.255.1')
rtr2 = Router('3650X', '15.2.4', '172.16.255.3')
sw1  = Switch('2960Z', '12.0.2', '192.168.1.2')

#Router1 attributes added description#
rtr1.desc = 'Virtual router 1'
#Router1 attributes added description#
rtr2.desc = 'Virtual router 2'


print("Model for Router1 is ", rtr1.model)
print("Description is ", rtr1.desc)
print("\n")
print("Model for Router1 is ", rtr2.model)
print("Description is ", rtr2.desc)


print('Router 1 ', '\n', rtr1.getDetails(), '\n', sep='')
print('Router 2 ', '\n', rtr2.getDetails(), '\n', sep='')
print('Switch 1', '\n', sw1.getDetails(), '\n', sep='')
