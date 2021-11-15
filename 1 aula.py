#!/usr/bin/env python
# coding: utf-8

# In[1]:


#aqui é elevado ao quadrado
50**22


# In[2]:


1/(50**22)


# In[6]:


x=1
y=2
print (x+y)
x-y


# In[12]:


x=[11,15,26,28,31]
x[0]


# In[37]:


import numpy as np
import pandas as pd
np.average(x)


# In[44]:


x=[17,18,19,20,21,22,23,200]
f=[1,11,8,7,10,2,1,1]
np.average(x,weights=f)


# In[45]:


#Calculo de moda
L = [52,60,71,75,75,90]
lpd = pd.Series (L)
lpd.value_counts ()


# In[46]:


x=lpd.value_counts ()
x[x==max(x)]


# In[47]:


print ("Media = ", np.average(L))
print ("Moda = ",x[x==max(x)])
print ("Mediana = ",lpd.median())


# In[48]:


#L é a variavel, 50 é a porcentagem, para calculo de porcentagem
np.percentile(L,50)


# In[50]:


#L é a variavel, 25, 50 e 75 é a porcentagem, para calculo de porcentagem
np.percentile(L,(25,50,75))


# In[59]:


print(min (L))
print(max(L))


# In[72]:


altura = [1.72, 1.60,1.74,1.88,1.82,1.75,1.82, 1.75,1.75,1.73]


# In[90]:


media = np.average(altura)

variancia = np.std(altura)**2

desvio = np.sqrt(variancia)

coef = desvio / media

print(variacia)
print(coef)


# In[83]:


variancia = np.std(altura)**2

