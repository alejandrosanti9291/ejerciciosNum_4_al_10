#!/usr/bin/env python
# coding: utf-8

# # Implementacion de los ejercicios 4,5,6,7,8,9,10 en python usando las librerias matplotlib y numpy

# ## Gráfica del ejercicio 4, literal a.  donde las entradas negras eran: (0,2), (-2,2), (-2,0), (-2,-2). Y las entradas blancas eran: (2,2), (2,0), (2,-2) (0-2)

# In[11]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# In[4]:


#x_n y y_n para las entradas (x,y) de color negro
#x_b y y_b para las entradas (x,y) de color blanco
x_n = [0, -2, -2, -2]
y_n = [2, 2, 0, -2]
x_b = [0, 2, 2, 2]
y_b = [-2, 2, 0, -2]


# In[5]:


#se grafican las entradas 
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Negras")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Blancas")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ### Se decide trazar la frontera de decision pasando por los puntos (x1,y1) = (-1, -2); y (x2,y2)=(1,2).

# In[6]:


#x_fd y y_fd son dos puntos por donde se va a trazar la frontera de decisión
x_fd = [-1, 1]
y_fd = [-2, 2]


# In[7]:


#se calcula la pendiente (m) de la recta dibujada
m = (y_fd[1]-y_fd[0]) / (x_fd[1] - x_fd[0])
m


# In[8]:


#se calcula el baias utilizando uno de los puntos de la frontera de decisión y la pendiente de la recta
b = y_fd[1] - m * x_fd[1]
b


# In[9]:


#se calcula la función de la recta
def funcion_y (x):
    return m * x + b


# In[10]:


#se deducen los pesos (w) de la funcion de la recta de la frontera de decision
w = [m,-1]


# In[11]:


#se cargan las listas que nos indicaran los puntos por donde pasan la frontera de decisión
for i in range(-2,3):
    x_fd.append(i)
    y_fd.append(funcion_y(i))


# In[13]:


#graficamos la funcion de la recta de la frontera de decision
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Negras")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Blancas")
plt.plot(x_fd,y_fd, linestyle="-", color="black", label="Frontera decision")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ## Gráfica del ejercicio 4, literal b. donde las entradas negras eran: (-2,-2), (0,-2), (2,-2). Y las entradas blancas eran: (-2,0), (-2,2), (0,2), (2,2), (2,0) 

# In[19]:


#x_n y y_n para las entradas (x,y) de color negro
#x_b y y_b para las entradas (x,y) de color blanco
x_n = [-2, 0, 2]
y_n = [-2, -2, -2]
x_b = [-2, -2, 0, 2, 2]
y_b = [0, 2, 2, 2, 0]


# In[20]:


#se grafican las entradas 
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Negras")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Blancas")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ### Se decide trazar la frontera de decision pasando por los puntos (x1,y1) = (-2, -1); y (x2,y2)=(2,-1).

# In[110]:


#x_fd y y_fd son dos puntos por donde se va a trazar la frontera de decisión
x_fd = [-2, 2]
y_fd = [-1, -1]

#se calcula la pendiente (m) de la recta dibujada
m = (y_fd[1]-y_fd[0]) / (x_fd[1] - x_fd[0])
print("pendiente = %s" % str(m))

#se calcula el baias utilizando uno de los puntos de la frontera de decisión y la pendiente de la recta
b = y_fd[1] - m * x_fd[1]
print("bias b = %s" % str(b))

#se deducen los pesos (w) de la funcion de la recta de la frontera de decision
w = [m,-1]
print("pesos W = %s" % str(w))

#se cargan las listas que nos indicaran los puntos por donde pasan la frontera de decisión
for i in range(-2,3):
    x_fd.append(i)
    y_fd.append(funcion_y(i))


# In[23]:


#graficamos la funcion de la recta de la frontera de decision
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Negras")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Blancas")
plt.plot(x_fd,y_fd, linestyle="-", color="black", label="Frontera decision")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ## Gráfica del ejercicio 4, literal c. donde las entradas negras eran: (-2,0), (-2,-2), (0,-2), (2,-2) (2,0), (2,2), (0,2). Y las entradas blancas eran: (-2,2)

# In[25]:


#x_n y y_n para las entradas (x,y) de color negro
#x_b y y_b para las entradas (x,y) de color blanco
x_n = [-2, -2, 0, 2, 2, 2, 0]
y_n = [0, -2, -2, -2, 0, 2, 2]
x_b = [-2]
y_b = [2]


# In[26]:


#se grafican las entradas 
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Negras")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Blancas")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ### Se decide trazar la frontera de decision pasando por los puntos (x1,y1) = (-2, 1); y (x2,y2)=(-1,2).

# In[29]:


#x_fd y y_fd son dos puntos por donde se va a trazar la frontera de decisión
x_fd = [-2, -1]
y_fd = [1, 2]

#se calcula la pendiente (m) de la recta dibujada
m = (y_fd[1]-y_fd[0]) / (x_fd[1] - x_fd[0])
print("pendiente = %s" % str(m))

#se calcula el baias utilizando uno de los puntos de la frontera de decisión y la pendiente de la recta
b = y_fd[1] - m * x_fd[1]
print("bias b = %s" % str(b))

#se deducen los pesos (w) de la funcion de la recta de la frontera de decision
w = [m,-1]
print("pesos w = %s" % str(w))

#se cargan las listas que nos indicaran los puntos por donde pasan la frontera de decisión
for i in range(-1,2):
    x_fd.append(i)
    y_fd.append(funcion_y(i))


# In[30]:


#graficamos la funcion de la recta de la frontera de decision
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Negras")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Blancas")
plt.plot(x_fd,y_fd, linestyle="-", color="black", label="Frontera decision")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ## Gráfica del ejercicio 5. donde las entradas negras eran: (1,-1), (1,-2), (2,-1). Y las entradas blancas eran: (0,0), (0,1), (-1,1)

# In[31]:


#x_n y y_n para las entradas (x,y) de color negro
#x_b y y_b para las entradas (x,y) de color blanco
x_n = [1, 1, 2]
y_n = [-1, -2, -1]
x_b = [0,0,-1]
y_b = [0,1,1]


# In[32]:


#se grafican las entradas 
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Negras")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Blancas")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ### Se decide trazar la frontera de decision pasando por los puntos (x1,y1) = (0, -1); y (x2,y2)=(1,0).

# In[109]:


#x_fd y y_fd son dos puntos por donde se va a trazar la frontera de decisión
x_fd = [0,1]
y_fd = [-1,0]

#se calcula la pendiente (m) de la recta dibujada
m = (y_fd[1]-y_fd[0]) / (x_fd[1] - x_fd[0])
print("pendiente = %s" % str(m))

#se calcula el baias utilizando uno de los puntos de la frontera de decisión y la pendiente de la recta
b = y_fd[1] - m * x_fd[1]
print("bias = %s" % str(b))

#se deducen los pesos (w) de la funcion de la recta de la frontera de decision
w = [m,-1]
print("pesos w = %s" % str(w))

#se cargan las listas que nos indicaran los puntos por donde pasan la frontera de decisión
for i in range(-2,3):
    x_fd.append(i)
    y_fd.append(funcion_y(i))


# In[35]:


#graficamos la funcion de la recta de la frontera de decision
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Negras")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Blancas")
plt.plot(x_fd,y_fd, linestyle="-", color="black", label="Frontera decision")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ## Gráfica del ejercicio 6. donde las entradas con salida 1 eran: (-1,1), (0,0), (1,-1). Y las entradas con salida 0 eran: (1,0), (0,1)

# In[36]:


#x_n y y_n para las entradas (x,y) de salida 1
#x_b y y_b para las entradas (x,y) de salida 0
x_n = [-1,0,1]
y_n = [1,0,-1]
x_b = [1,0]
y_b = [0,1]


# In[38]:


#se grafican las entradas 
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Unos")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Ceros")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ### Se decide trazar la frontera de decision pasando por los puntos (x1,y1) = (-0.5, 1); y (x2,y2)=(1, -0.5).

# In[108]:


#x_fd y y_fd son dos puntos por donde se va a trazar la frontera de decisión
x_fd = [-0.5,1]
y_fd = [1,-0.5]

#se calcula la pendiente (m) de la recta dibujada
m = (y_fd[1]-y_fd[0]) / (x_fd[1] - x_fd[0])
print("pendiente = %s" % str(m))

#se calcula el baias utilizando uno de los puntos de la frontera de decisión y la pendiente de la recta
b = y_fd[1] - m * x_fd[1]
print("bias b = %s" % str(b))

#se deducen los pesos (w) de la funcion de la recta de la frontera de decision
w = [m,-1]
print("pesos = %s" % str(w))

#se cargan las listas que nos indicaran los puntos por donde pasan la frontera de decisión
for i in range(-2,3):
    x_fd.append(i)
    y_fd.append(funcion_y(i))


# In[69]:


#graficamos la funcion de la recta de la frontera de decision
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="Unos")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="Ceros")
plt.plot(x_fd,y_fd, linestyle="-", color="black", label="Frontera decision")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ## Gráfica del ejercicio 7. Donde las entradas con salida 1 eran: (1,1), (1,2). Las entradas con salida 2 eran: (2,-1), (2,0). Las entradas con salida 3 eran: (-1,2), (-2,1). Las entradas con salida 4 eran: (-1,-1), (-2,-2)

# In[43]:


#x_uno y y_uno para las entradas (x,y) de salida 1
#x_dos y y_dos para las entradas (x,y) de salida 2
#x_tres y y_tres para las entradas (x,y) de salida 3
#x_cuat y y_cuat para las entradas (x,y) de salida 4
x_uno = [1,1]
y_uno = [1,2]
x_dos = [2,2]
y_dos = [-1,0]
x_tres = [-1,-2]
y_tres = [2,1]
x_cuat = [-1,-2]
y_cuat = [-1,-2]


# In[45]:


#se grafican las entradas 
plt.plot(x_uno,y_uno, linestyle="none", marker="o", color="black", label="Clase 1")
plt.plot(x_dos,y_dos, linestyle="none", marker="o", color="yellow", label="Clase 2")
plt.plot(x_tres,y_tres, linestyle="none", marker="o", color="red", label="Clase 3")
plt.plot(x_cuat,y_cuat, linestyle="none", marker="o", color="green", label="Clase 4")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ### Se decide trazar la frontera de decision 1 pasando por los puntos (x1,y1) = (-0.5, 2); y (x2,y2)=(0.5,-2).
# 
# ### También se decide trazar la frontera de decision 2 pasando por los puntos (x1,y1) = (-2,-0.5); y (x2,y2)=(2,0.5).

# In[111]:


#x_fd_uno y y_fd_uno son dos puntos por donde se va a trazar la frontera de decisión 1
x_fd_uno = [-0.5,0.5]
y_fd_uno = [2,-2]

#x_fd_dos y y_fd_dos son dos puntos por donde se va a trazar la frontera de decisión 2
x_fd_dos = [-2,2]
y_fd_dos = [-0.5, 0.5]

#se calcula la pendiente (m_uno) de la frontera de decisión 1
m_uno = (y_fd_uno[1]-y_fd_uno[0]) / (x_fd_uno[1] - x_fd_uno[0])
print("pendiente fd 1 = %s" % str(m_uno))

#se calcula la pendiente (m_dos) de la frontera de decisión 2
m_dos = (y_fd_dos[1]-y_fd_dos[0]) / (x_fd_dos[1] - x_fd_dos[0])
print("pendiente fd 2 = %s" % str(m_dos))


#se calcula el baias (b_uno) utilizando uno de los puntos de la frontera de decisión 1 y la pendiente de la recta 1
b_uno = y_fd_uno[1] - m_uno * x_fd_uno[1]
print("bias fd 1 = %s" % str(b_uno))


#se calcula el baias (b_dos) utilizando uno de los puntos de la frontera de decisión 2 y la pendiente de la recta 2
b_dos = y_fd_dos[1] - m_dos * x_fd_dos[1]
print("bias fd 2 = %s" % str(b_dos))


#se deducen los pesos (w) de las funcion de la recta de la frontera de decision 1 y 2
w_uno = [m_uno,-1]
w_dos = [m_dos, -1]
print("pesos w fd 1 = %s" % str(w_uno))
print("pesos w fd 2 = %s" % str(w_dos))


#se calcula la función de la recta 1
def funcion_y_uno (x):
    return m_uno * x + b_uno

#se calcula la función de la recta 2
def funcion_y_dos (x):
    return m_dos * x + b_dos

#se cargan las listas que nos indicaran los puntos por donde pasan las frontera de decisión 1 y 2
for i in range(-2,2):
    x_fd_uno.append(i)
    x_fd_dos.append(i)
    y_fd_uno.append(funcion_y_uno(i))
    y_fd_dos.append(funcion_y_dos(i))    

w_uno
w_dos


# In[61]:


#se grafican las entradas 
plt.plot(x_uno,y_uno, linestyle="none", marker="o", color="black", label="Clase 1")
plt.plot(x_dos,y_dos, linestyle="none", marker="o", color="yellow", label="Clase 2")
plt.plot(x_tres,y_tres, linestyle="none", marker="o", color="red", label="Clase 3")
plt.plot(x_cuat,y_cuat, linestyle="none", marker="o", color="green", label="Clase 4")
plt.plot(x_fd_uno,y_fd_uno, linestyle="-", color="black", label="Frontera decision 1")
plt.plot(x_fd_dos,y_fd_dos, linestyle="-", color="blue", label="Frontera decision 2")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ## Gráfica del ejercicio 8. donde las entradas con salida t=1 eran: (0,2), (-2,2), (-2,2), (-2,-2), (2,2). Y las entradas con salida t=0 eran: (0,-2), (2,-2), (2,0)

# In[63]:


#x_n y y_n para las entradas (x,y) de salida 1
#x_b y y_b para las entradas (x,y) de salida 0
x_n = [0,-2,-2,-2,2]
y_n = [2,2,2,-2,2]
x_b = [0,2,2]
y_b = [-2,-2,0]


# In[64]:


#se grafican las entradas 
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="t=1")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="t=0")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ### Se decide trazar la frontera de decision pasando por los puntos (x1,y1) = (0,-1); y (x2,y2)=(1,0).

# In[107]:


#x_fd y y_fd son dos puntos por donde se va a trazar la frontera de decisión
x_fd = [0,1]
y_fd = [-1,0]

#se calcula la pendiente (m) de la recta dibujada
m = (y_fd[1]-y_fd[0]) / (x_fd[1] - x_fd[0])
print("pendiente = %s" % str(m))

#se calcula el baias utilizando uno de los puntos de la frontera de decisión y la pendiente de la recta
b = y_fd[1] - m * x_fd[1]
print("bias b = %s" % str(b))

#se deducen los pesos (w) de la funcion de la recta de la frontera de decision
w = [m,-1]
print("pesos w = %s" % str(w))

#se cargan las listas que nos indicaran los puntos por donde pasan la frontera de decisión
for i in range(-2,3):
    x_fd.append(i)
    y_fd.append(funcion_y(i))


# In[70]:


#graficamos la funcion de la recta de la frontera de decision
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="t=1")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="t=0")
plt.plot(x_fd,y_fd, linestyle="-", color="black", label="Frontera decision")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# In[96]:


#se crea la funcion Hardlim() o funcion escalonada de 0 a 1 
def hardlim(neto):
    if neto > 0:
        resultado = 1
    else:
        resultado = 0
    return resultado

#se crea la función error
def error(activation, salida_esperada):
    e = int(activation) - salida_esperada
    return e

#se crea la funcion de activación con la cual validaremos el funcionamiento de clasificación de la neurona
def funcion_validacion(entrada, w, b, t):
    activacion = hardlim((w[0]*entrada[0])+(w[1]*entrada[1])+b)
    
    if activacion == t:
        print("La neurona trabaja correctamente y hace la clasificación deseada")
    else:
        print("Hay que utilizar un algoritmo de entrenamiento para ajustar los parametros de la frontera de decisión")
        print("El error de la neurona para esta entrada es de %s \n" % str(error(int(activacion), t)))


# In[97]:


#se valida el comportamiento del perceptron con las entradas p1 = [0,2] t=1. y p5 = [0,-2] t=0

#para p1
funcion_validacion([0,2],w,b,1)
#para p5
funcion_validacion([0,-2],w,b,0)


# ### conclusión: se debe entrenar el perceptrón, ya que la neurona no esta clasificando correctamente las entradas con relación a la salida esperada

# ## Gráfica del ejercicio 9. donde las entradas con salida t=1 son: (1,2). Y las entradas con salida t=0 son:(-1,2), (0,-1)

# In[99]:


#x_n y y_n para las entradas (x,y) de salida 1
#x_b y y_b para las entradas (x,y) de salida 0
x_n = [1]
y_n = [2]
x_b = [-1,0]
y_b = [2,-1]


# In[100]:


#se grafican las entradas 
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="t=1")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="t=0")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# ### Se decide trazar la frontera de decision pasando por los puntos (x1,y1) = (0,1); y (x2,y2)=(1,-1).

# In[103]:


#x_fd y y_fd son dos puntos por donde se va a trazar la frontera de decisión
x_fd = [0,1]
y_fd = [1,-1]

#se calcula la pendiente (m) de la recta dibujada
m = (y_fd[1]-y_fd[0]) / (x_fd[1] - x_fd[0])
print("pendiente = %s" % str(m))

#se calcula el baias utilizando uno de los puntos de la frontera de decisión y la pendiente de la recta
b = y_fd[1] - m * x_fd[1]
print("bias b = %s" %str(b))

#se deducen los pesos (w) de la funcion de la recta de la frontera de decision
w = [m,-1]
print("pesos w = %s" %str(w))

#se cargan las listas que nos indicaran los puntos por donde pasan la frontera de decisión
for i in range(-2,3):
    x_fd.append(i)
    y_fd.append(funcion_y(i))


# In[104]:


#graficamos la funcion de la recta de la frontera de decision
plt.plot(x_n,y_n, linestyle="none", marker="o", color="black", label="t=1")
plt.plot(x_b,y_b, linestyle="none", marker="o", color="yellow", label="t=0")
plt.plot(x_fd,y_fd, linestyle="-", color="black", label="Frontera decision")
plt.legend(bbox_to_anchor=(1.05, 1.05))
plt.grid()
plt.show()


# In[106]:


#se valida el comportamiento del perceptron con las entradas p1 = [1,2] t=1. y p2 = [-1,2] t=0

#para p1
funcion_validacion([1,2],w,b,1)
#para p5
funcion_validacion([-1,2],w,b,0)


# ### conclusión: se debe entrenar el perceptrón, ya que la neurona no esta clasificando correctamente las entradas con relación a la salida esperada

# ## Gráfica del ejercicio 10. donde las naranjas con salida t=0 son: [1,-1,-1]. Y las manzanas con salida t=1 son: [1,1,-1]. La matriz de peso inicial es [0.5, -1, -0.5] y b = 0.5

# In[4]:


#x_forma_nar para las entradas forma de de las naranjas 
#y_textura_nar para las entradas textura de de las naranjas 
#z_peso_nar para las entradas peso de de las naranjas
x_forma_nar = [1]
y_textura_nar = [-1]
z_peso_nar = [-1]
#t_naranja para la salida esperada de las naranjas
t_naranja = 0

#x_forma_man para las entradas forma de de las manzanas
#y_textura_man para las entradas textura de de las manzanas 
#z_peso_man para las entradas peso de de las manzanas
x_forma_man = [1]
y_textura_man = [1]
z_peso_man = [-1]
#t_manzana para la salida esperada de las manzanas
t_manzana = 1


# In[54]:


#Axes3D son los ejes en 3D para los gráficos

#se crea una figura, donde vamos a cargar nuestro grafico 3D
fig = plt.figure()
ax = fig.gca(projection='3d')


ax.plot(xs=x_forma_nar,ys=y_textura_nar,zs=z_peso_nar, zdir='z', label="naranja", color='orange', marker='o')
ax.plot(xs=x_forma_man,ys=y_textura_man,zs=z_peso_man, zdir='z', label="manzana", color='red', marker='o')
ticks = np.arange(-1, 2, 1)
labels = range(-1, 2, 1)
plt.xticks(ticks, labels)
plt.yticks(ticks, labels)
ax.set_xlabel('Forma')
ax.set_ylabel('Textura')
ax.set_zlabel('Peso')
ax.legend()
plt.show()


# In[ ]:




