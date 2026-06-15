#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


def f(x):
    return 3*x**2 - 4*x + 5


# In[6]:


f(3.0)


# In[7]:


xs = np.arange(-5, 5, 0.25)
ys = f(xs) 
plt.plot(xs, ys)


# In[8]:


h = 0.001
x = 3.0
f(x + h) 


# In[14]:


h = 0.0001
# inputs
a = 2.0
b = -3.0
c = 10.0



d1 = a*b + c
a += h
d2 = a*b + c

print('d1', d1)
print('d2', d2)
print('slope', (d2 - d1)/h)


# In[40]:


class Value:
    def __init__(self, data, _children=(), op=''):
        self.data = data
        self._prev = set(_children)
        
        self.grad = 0.0 # Standard for storing gradients
        self._op = op

    def __repr__(self):
        return f"value(data={self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out

a = Value(2.0)
b = Value(-3.0)
a * b
c = Value(10.0)
d = a*b + c
d


# In[37]:


d._prev


# In[38]:


d._op


# In[25]:


from graphviz import Digraph

dot = Digraph(comment = 'Learning Graphviz')
dot.node = ('A', 'Learn Python')
dot.node = ('B', 'Learn Neural Networks')
dot.node = ('C', 'Learning AI')

dot.edge = ('A', 'B')
dot.edge = ('B', 'C')
dot.edge = ('C', 'A')

dot.render('my_first_graph', format='png', view=True)


# In[26]:


pip install graphviz


# In[27]:


from graphviz import Digraph
from PIL import Image

dot = Digraph(comment = 'Learning Graphviz')
dot.node('A', 'Learn Python')
dot.node('B', 'Learn Neural Networks')
dot.node('C', 'Learning AI')

dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'A')

dot.render('my_first_graph', format='png', view=True)
dot


# In[41]:


from graphviz import Digraph

def trace(root):
      # builds a set of all nodes and edges in a graph
    nodes = set()  # Initialize nodes set
    edges = set()  # Initialize edges set
    
    def build(v):
        if v not in nodes: 
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

    
def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'}) # LR = left to right

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
    # for any value in the graph, create a rectangular ('record') node for it
        dot.node(name = uid, label = "{ %s data %.4f }" % (n.data, ), shape='record')
        if n._op:
            dot.node(name = uid + n._op, label = n._op)
            dot.edge(uid + n._op, uid)

    for n1,n2 in edges:
    # connect n1 to the op node of n2
    
        dot.edge(str(id(n1)), str(id(n1)) + n2._op)

    return dot


# In[42]:


draw_dot(d)


# In[ ]:




