# Reconocimiento de digitos escritos a mano con Keras Tensorflow

Demo para reconocimiento de digitos escritos a mano usando redes neuronales convolucionales para el curso de Inteligencia Artificial UPC / EPE.

Las herramientas que se utlizaron son: Python, Keras Tensorflow y Django.

Para el entrenamiento de la red neuronal se utilizó el conjunto de datos de Mnist de digitos escritos a mano.

## Para empezar:

### Prerequisitos

* Python 3.6

Poner la carpeta de instalación y la carpeta de Scripts en las variables de entorno del sistema
* Python36/
* Python36/Scripts

### Instalar los siguientes modulos con pip
* pip install django
* pip install numpy scipy matplotlib
* pip install tensorflow
* pip install keras
* pip install scikit-learn
* pip install h5py
* pip install pillow
* pip install opencv-python

### Correr la aplicación
python manage.py runserver

### Entrar a aplicación
http://localhost:8000/digits/

Ahi se presentan las opciones de Entrenar (20 min +), reconocer una imagen de un numero escrito en canvas y subir una imagen de un numero para probar reconocimiento.


### RED NEURONAL
El codigo donde se crea y gestiona la red neuronal esta en digits/services.py

### MISC.
* Al momento de realizar entrenamiento la información sobre este se muestra en la consola
