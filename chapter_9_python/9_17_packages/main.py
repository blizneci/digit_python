from somepackage import utils
#import sys


#utils.say_hello(sys.argv)
while True:
   name = input('Ведите имя, q для выхода\n')
   if name == 'q':
       break
   utils.say_hello(name)
