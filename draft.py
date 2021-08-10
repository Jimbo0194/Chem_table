##****************************************************************##
##            Universidad Internacional de las Americas           ##
##                                                                ##
##  Proyecto del curso Programacion II                            ##
##                                                                ##
##  Autores : Luis Montealegre                                    ##
##            Alvaro                                              ##
##            Adrian                                              ##
##  Fecha   : Jueves 12 de agosto, 2021                           ##
##                                                                ##
##  El programa consiste en una tabla periodica a base            ##
##  de consultas por elemento e incluye reacciones con            ##
##  elementos especificos o aleatorios                            ##
##                                                                ##
##****************************************************************##

# Importing required resources
from elementos import *

elementos = {'Hidrogeno': elemento('Hidrogeno', 'Alcalino', 'H', 1.0079, 'No metal', [-1, 1], '+1'),
             'Helio': elemento('Helio', 'Gas Noble'),
             'Litio': elemento('Litio', 'Alcalino', 'Li', 6.941, 'Metal', 1, '+1'),
             'Berilio': elemento('Berilio', 'Alcalinoterreo', 'Be', 9.0122, 'Metal', 2, '+2'),
             'Boro': elemento('Boro', 'Metaloide', 'B', 10.811, 'No Metal', 3, '+3'),
             'Carbono': elemento('Carbono', 'No Metal', 'C', 12.0107, 'No Metal', [2, +4, -4], '+4'),
             'Nitrogeno': elemento('Nitrogeno', 'No Metal', 'N', 14.0067, 'No Metal', [-3, 1, 2, 3, 4, 5], '+3'),
             'Oxigeno': elemento('Oxigeno', 'No Metal', 'O', 15.9994, 'No Metal', [-2, 2], '2-'),
             'Fluor': elemento('Fluor', 'Halógenos', 'F', 18.9984, 'No Metal', [-1, 1], '-1'),
             'Neón': elemento('Neón', 'Gas Noble', 'Ne', 20.1797, "No metal", 0, 'N/A'),
             'Sodio': elemento('Sodio', 'Alcalino', 'Na', 22.9897, 'Metal', 1, '+1'),
             'Magnesio': elemento('Magnesio', 'Alcalinoterreo', 'Mg', 24.305, 'Metal', 2, '+2'),
             'Aluminio': elemento('Aluminio', 'Metal', 'Al', 26.9815, 'Metal', 3, '+3'),
             'Silicio': elemento('Silicio', 'Metaloide', 'Si', 28.0855, 'No Metal', [-4, 4], '+4'),
             'Fósforo': elemento('Fósforo', 'No Metal', 'P', 30.9738, 'No Metal', [-3, 3, 4, 5], '+5'),
             'Azufre': elemento('Azufre', 'No Metal', 'S', 32.065, 'No Metal', [-2, 2, 4, 6], '+6'),
             'Cloro': elemento('Cloro', 'Halógeno', 'Cl', 35.453, 'No Metal', [-1, 1, 3, 5, 7], '-1'),
             'Potasio': elemento('Potasio', 'Alcalino', 'K', 39.0983, 'Metal', 1, '+1'),
             'Argón': elemento('Argon', 'Gas Noble', 'Ar', 39.948, 'No Metal', 0, 'N/A'),
             'Calcio': elemento('Calcio', 'Alcalinotérreo', 'Ca', 40.078, 'Metal', 2, '+2'),
             'Escandio': elemento('Escandio', 'De Transición', 'Sc', 44.9559, 'Metal', 3, '+3')}
