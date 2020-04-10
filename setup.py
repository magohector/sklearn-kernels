from setuptools import setup
 
setup(
    name='sklearnkernels',
    packages=['sklearnkernels'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='GPL', # La licencia que tenga tu paqeute
    description='A random test lib',
    author='Mora Hector',
    author_email='hector.mora@gmail.com',
    url='https://github.com/magohector/sklearn-kernels/tree/master/sklearn-kernels', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/magohector/sklearn-kernels/archive/v0.1.tar.gz', # Te lo explico a continuación
    keywords='ANN, SVM, Kernels', # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paqeute
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
    
    install_requires=[
        'numpy>=1.9.3',
        'scipy>=0.16.0',        
        'scikit-learn>=0.18.0',
    ],
)