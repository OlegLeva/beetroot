""" using various string formatting methods to build the result string
                    % nafig)"""

name = 'Oleg'
day = 'Monday'

print('“Good day' ' ' + name +'!' + ' ' + day + ' ' 'is a perfect day to learn some python.”') #це шось страшне)))
print(f'“Good day {name}! {day} is a perfect day to learn some python.”')
print('“Good day {}! {} is a perfect day to learn some python.”'.format(name, day))
print('“Good day {1}! {0} is a perfect day to learn some python.”'.format(day, name))
print('“Good day {name}! {day} is a perfect day to learn some python.”'.format(name='Oleg', day='Monday'))
