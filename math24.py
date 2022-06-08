import itertools


def calculate(string, x, y):
    if string == 'multiplied by':
        return x*y
    if string == 'plus':
        return x+y
    if string == 'minus':
        return x-y
    if string == 'divided by':
        if y == 0:
            return 0
        return x/y
    
def func_1(combination, numbers, goal): #mult, mult, add 5,2,7,2
    w = numbers[0]
    x = calculate(combination[0], w, numbers[1])    
    y = calculate(combination[1], x, numbers[2])    
    z = calculate(combination[2], y, numbers[3])
    
    if z == goal:
        return '{} {} {} = {}. {} {} {} = {}. {} {} {} = {}'.format(w, combination[0], numbers[1], x,
                                                                    x, combination[1], numbers[2], y,
                                                                    y, combination[2], numbers[3], z)
    return ''

def func_2(combination, numbers, goal): #mult, mult, add 5,2,7,2
    w = numbers[0]
    x = calculate(combination[0], w, numbers[1])    
    y = calculate(combination[1], numbers[2], x)    
    z = calculate(combination[2], y, numbers[3])
    
    if z == goal:
        return '{} {} {} = {}. {} {} {} = {}. {} {} {} = {}'.format(w, combination[0], numbers[1], x,
                                                                    numbers[2], combination[1], x, y,
                                                                    y, combination[2], numbers[3], z)
    return ''

def func_3(combination, numbers, goal): #mult, mult, add 5,2,7,2
    w = numbers[0]
    x = calculate(combination[0], w, numbers[1])    
    y = calculate(combination[1], numbers[2], x)    
    z = calculate(combination[2], numbers[3], y)
    
    if z == goal:
        return '{} {} {} = {}. {} {} {} = {}. {} {} {} = {}'.format(w, combination[0], numbers[1], x,
                                                                    numbers[2], combination[1], x, y,
                                                                    numbers[3], combination[2], y, z)
    return ''



def func_4(combination, numbers, goal): #mult, mult, add 5,2,7,2
    w = numbers[0]
    x = calculate(combination[0], w, numbers[1])    
    y = calculate(combination[1], x, numbers[2])    
    z = calculate(combination[2], numbers[3], y)
    
    if z == goal:
        return '{} {} {} = {}. {} {} {} = {}. {} {} {} = {}'.format(w, combination[0], numbers[1], x,
                                                                    x, combination[1], numbers[2], y,
                                                                    numbers[3], combination[2], y, z)
    return ''

def func_double(combination, numbers, goal): #mult, mult, add 5,2,7,2
    v = numbers[0]
    w = calculate(combination[0], v, numbers[1])
    
    x = numbers[2]
    y = calculate(combination[1], x, numbers[3])
    
    z = calculate(combination[2], w, y)
    
    if z == goal:       
        return '{} {} {} = {}. {} {} {} = {}. {} {} {} = {}'.format(v, combination[0], numbers[1], w,
                                                                    x, combination[1], numbers[3], y,
                                                                    w, combination[2], y, z)
    return ''
    


combinations = ['plus','plus','plus',
         'minus','minus','minus',
         'divided by','divided by','divided by',
         'multiplied by','multiplied by','multiplied by',]

def math24(numbers, goal = 24, complete = False): #takes a list of 4 numbers and returns all solutions that equal the goal. Change complete to True to get all solutions
    
    solutions = []
    x = itertools.permutations(numbers, len(numbers))
    all_nums = list(set(x))
    all_comb = list(set(itertools.permutations(combinations, 3)))
    for val in all_nums:
        for comb in all_comb:
                                    
            answer = func_1(comb, val, goal)
            if answer != '':
                solutions.append(answer)

            answer = func_2(comb, val, goal)
            if answer != '':
                solutions.append(answer)                
 
            answer = func_3(comb, val, goal)
            if answer != '':
                solutions.append(answer)   
                
            answer = func_4(comb, val, goal)
            if answer != '':
                solutions.append(answer)                 
                
            answer = func_double(comb, val, goal)
            if answer != '':
                solutions.append(answer)                
                                
    if len(solutions) == 0:
        return('No soltuions')
       
    if complete == False:
        return solutions[:5]
    return solutions
            
            
            
            
            
            
            
            
            
            
            
            
            
