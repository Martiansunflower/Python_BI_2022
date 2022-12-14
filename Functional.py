#!/usr/bin/env python
# coding: utf-8

# Task 1: write a function that takes as input several other functions and a list of values to which these functions will be applied

# In[27]:


def sequential_map(*args1):
    *functions, container = args1
    
    for fun in functions:
        result = map(fun, container)
        
    return list(result)


# Task 2: write a function that takes as input several other logical functions and a list of values to which these functions will be applied. The function returns values that have always been "True".

# In[203]:


def consensus_filter(*args2):
    *log_functions, container = args2
    
    for fun in log_functions:
        container = filter(fun, container)

    return list(container)


# Task 3: write a function that takes as input two other functions and a list of values. If the value passes the first function with 'True', it is fed to the second function. 

# In[123]:


def conditional_reduce(f1, f2, container):
    
    container = list(filter(f1, container))
    result = f2(container[0], container[1])

    return result  


# Task 4: write a function that takes as input several other functions. The function must return a function combining all passed functions with consecutive execution.

# In[166]:


def func_chain(*args4):
    
    def my_chain(x):
        for fun in args4:
            x = fun(x)
        return x
    
    return my_chain


# Task 5: write a function that takes as input several other functions and  and is analogue to the multiple_partial function.

# In[207]:


def multiple_partial(*args, **kwargs):
    for fun in args:
        result = lambda x: fun(*x, **kwargs)
    return result

