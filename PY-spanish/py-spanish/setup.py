from setuptools import setup, find_packages

setup(
    name='PY-spanish',  # Nombre de la librería
    version='1.0.0',  # Marca como la primera versión estable
    packages=find_packages(),  # Detecta automáticamente los paquetes dentro de la librería
    description='Traduce y simplifica el uso de Python con comandos básicos en español.',
    # Contenido del README como descripción larga
    long_description=open('README.md', encoding='utf-8').read(),
    # Especifica que el README usa Markdown
    long_description_content_type='text/markdown',
    author='Legends_player',
    author_email='tucorreo@ejemplo.com',  # Actualiza con tu correo electrónico
    # Actualiza con tu URL de GitHub
    url='https://github.com/legendsplayer90/PY-spanish-',
    license='MIT',  # Usa la licencia MIT
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Indica que es estable
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    # Añade palabras clave útiles
    keywords='python español traducción programación educación',
    python_requires='>=3.6',  # Versión mínima requerida de Python
    install_requires=[],  # Dependencias (si las hay, agrégalas aquí)
)
