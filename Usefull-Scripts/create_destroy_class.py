""" Create  and delete class objects"""

class Vehicle:
    def __init__(self):
        print('Vehicle created.')
    def do(self,job):
        print('doing '+job)
    def __del__(self):
        print('Destructor called, vehicle deleted.')

car = Vehicle()
car.do('move')
del car

""" Using context manager"""

class Hello:
    def __init__(self):
        print('initialized')
    def __enter__(self):
        print('entered')
    def do(job):
        print('doing '+job)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('excited', exc_type, exc_val, exc_tb)
        

with Hello() as mc:
    print(Hello.do('greet'))

    
