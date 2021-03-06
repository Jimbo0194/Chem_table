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

elementos = {'Hidrógeno': elemento('Hidrógeno', 'No Metal', 'H', 1.0079, 'No Metal', [-1, 1], '+1', (2, 0)),
             'Helio': elemento('Helio', 'Gas Noble', 'He', 4.0026, 'No Metal', [0], 'N/A', (2, 17)),
             'Litio': elemento('Litio', 'Alcalino', 'Li', 6.941, 'Metal', [1], '+1', (3, 0)),
             'Berilio': elemento('Berilio', 'Alcalinotérreo', 'Be', 9.0122, 'Metal', [2], '+2', (3, 1)),
             'Boro': elemento('Boro', 'Metaloide', 'B', 10.811, 'No Metal', [3], '+3', (3, 12)),
             'Carbono': elemento('Carbono', 'No Metal', 'C', 12.0107, 'No Metal', [2, +4, -4], '+4', (3, 13)),
             'Nitrogeno': elemento('Nitrógeno', 'No Metal', 'N', 14.0067, 'No Metal', [-3, 1, 2, 3, 4, 5], '+3',(3, 14)),
             'Oxígeno': elemento('Oxígeno', 'No Metal', 'O', 15.9994, 'No Metal', [-2, 2], '2-', (3, 15)),
             'Fluor': elemento('Flúor', 'Halógenos', 'F', 18.9984, 'No Metal', [-1, 1], '-1', (3, 16)),
             'Neón': elemento('Neón', 'Gas Noble', 'Ne', 20.1797, "No metal", [0], 'N/A', (3, 17)),
             'Nitrogeno': elemento('Nitrogeno', 'No Metal', 'N', 14.0067, 'No Metal', [-3, 1, 2, 3, 4, 5], '+3',(3, 14)),
             'Oxigeno': elemento('Oxigeno', 'No Metal', 'O', 15.9994, 'No Metal', [-2, 2], '2-', (3, 15)),
             'Fluor': elemento('Fluor', 'Halógeno', 'F', 18.9984, 'No Metal', [-1, 1], '-1', (3, 16)),
             'Neón': elemento('Neón', 'Gas Noble', 'Ne', 20.1797, "No Metal", [0], 'N/A', (3, 17)),
             'Sodio': elemento('Sodio', 'Alcalino', 'Na', 22.9897, 'Metal', [1], '+1', (4, 0)),
             'Magnesio': elemento('Magnesio', 'Alcalinotérreo', 'Mg', 24.305, 'Metal', [2], '+2', (4, 1)),
             'Aluminio': elemento('Aluminio', 'Metal', 'Al', 26.9815, 'Metal', [3], '+3', (4, 12)),
             'Silicio': elemento('Silicio', 'Metaloide', 'Si', 28.0855, 'No Metal', [-4, 4], '+4', (4, 13)),
             'Fósforo': elemento('Fósforo', 'No Metal', 'P', 30.9738, 'No Metal', [-3, 3, 4, 5], '+5', (4, 14)),
             'Azufre': elemento('Azufre', 'No Metal', 'S', 32.065, 'No Metal', [-2, 2, 4, 6], '+6', (4, 15)),
             'Cloro': elemento('Cloro', 'Halógeno', 'Cl', 35.453, 'No Metal', [-1, 1, 3, 5, 7], '-1', (4, 16)),
             'Argón': elemento('Argón', 'Gas Noble', 'Ar', 39.948, 'No Metal', [0], 'N/A', (4, 17)),
             'Potasio': elemento('Potasio', 'Alcalino', 'K', 39.0983, 'Metal', [1], '+1', (5, 0)),
             'Calcio': elemento('Calcio', 'Alcalinotérreo', 'Ca', 40.078, 'Metal', [2], '+2', (5, 1)),
             'Escandio': elemento('Escandio', 'De Transición', 'Sc', 44.9559, 'Metal', 3, '+3', (5, 2)),
             'Titanio': elemento('Titanio', 'De transición', 'Ti', 47.867, 'Metal', [2, 3, 4], '+4', (5, 4)),
             'Vanadio': elemento('Vanadio', 'De transición', 'V', 50.9415, 'Metal', [2, 3, 4, 5], '+3', (5, 5)),
             'Cromo': elemento('Cromo', 'Cr', 'De transición', 51.9961, 'Metal', [6, 3, 2], '+4 y +5', (5, 6)),
             'Manganeso': elemento('Manganeso', 'Mn', 'De transición', 54.938049, 'Metal', [7, 6, 4, 2, 3], '+2',(5, 7)),
             'Hierro': elemento('Hierro', 'Fe', 'De transición', 55.847, 'Metal', [2], '+2 y +3', (5, 8)),
             'Cobalto': elemento('Cobalto', 'Co', 'De transición', 58.933200, 'Metal', [2, 3], '+3', (5, 8)),
             'Níquel': elemento('Níquel', 'Ni', 'De transición', 58.6934, 'Metal', [2, 3], '+2', (5, 10)),
             'Cobre': elemento('Cobre', 'De transición', 'Ce', 63.546, 'Metal', [1, 2], '+2', (5, 11)),
             'Zinc': elemento('Zinc', 'De Transición', 'Zn', 65.38, 'Metal', [2], '+2', (5, 12)),
             'Galio': elemento('Galio', 'Metales del bloque p', 'Ga', 69.723, 'Metal', [3], '+3', (5, 13)),
             'Germanio': elemento('Germanio', 'Metaloide', 'Ge', 72.64, 'Metal', [4], '+4', (5, 14)),
             'Arsénico': elemento('Arsénico', 'Metaloide', 'As', 74.92160, 'Metal', [3, -3, 5], '+5', (5, 15)),
             'Selenio': elemento('Selenio', 'No metal', 'Se', 78.96, 'No metal', [2, -2, 4, 6], '-2', (5, 16)),
             'Bromo': elemento('Bromo', 'Hálogeno', 'Br', 79.904, 'No metal', [1, -1, 3, 5, 7], '-1', (5, 17)),
             'Kriptón': elemento('Kriptón', 'Gas Noble', 'Kr', 83.80, 'No metal', [0], 'N/A', (5, 18)),
             'Escandio': elemento('Escandio', 'De Transición', 'Sc', 44.9559, 'Metal', 3, '+3', (5, 2)),
             'Titanio': elemento('Titanio', 'De Transición', 'Ti', 47.867, 'Metal', [2, 3, 4], '+4', (5, 3)),
             'Vanadio': elemento('Vanadio', 'De Transición', 'V', 50.9415, 'Metal', [2, 3, 4, 5], '+3', (5, 4)),
             'Cromo': elemento('Cromo', 'De Transición', 'Cr', 51.9961, 'Metal', [6, 3, 2], '+4 y +5', (5, 5)),
             'Manganeso': elemento('Manganeso', 'De Transición', 'Mn', 54.938049, 'Metal', [7, 6, 4, 2, 3], '+2',(5, 6)),
             'Hierro': elemento('Hierro', 'De Transición', 'Fe', 55.847, 'Metal', [2], '+2 y +3', (5, 7)),
             'Cobalto': elemento('Cobalto', 'De Transición', 'Co', 58.933200, 'Metal', [2, 3], '+3', (5, 8)),
             'Níquel': elemento('Níquel', 'De Transición', 'Ni', 58.6934, 'Metal', [2, 3], '+2', (5, 9)),
             'Cobre': elemento('Cobre', 'De Transición', 'Ce', 63.546, 'Metal', [1, 2], '+2', (5, 10)),
             'Zinc': elemento('Zinc', 'De Transición', 'Zn', 65.38, 'Metal', [2], '+2', (5, 11)),
             'Galio': elemento('Galio', 'Metales del bloque p', 'Ga', 69.723, 'Metal', [3], '+3', (5, 12)),
             'Germanio': elemento('Germanio', 'Metaloide', 'Ge', 72.64, 'Metal', [4], '+4', (5, 13)),
             'Arsénico': elemento('Arsénico', 'Metaloide', 'As', 74.92160, 'Metal', [3, -3, 5], '+5', (5, 14)),
             'Selenio': elemento('Selenio', 'No Metal', 'Se', 78.96, 'No Metal', [2, -2, 4, 6], '-2', (5, 15)),
             'Bromo': elemento('Bromo', 'Halógeno', 'Br', 79.904, 'No Metal', [1, -1, 3, 5, 7], '-1', (5, 16)),
             'Kriptón': elemento('Kriptón', 'Gas Noble', 'Kr', 83.80, 'No Metal', [0], 'N/A', (5, 17)),
             'Rubidio': elemento('Rubidio', 'Alcalino', 'Rb', 83.80, 'Metal', [1], '+1', (6, 0)),
             'Estroncio': elemento('Estroncio', 'Alcalinotérreo', 'Sr', 87.62, 'Metal', [2], '+2', (6, 1)),
             'Itrio': elemento('Itrio', 'De Transición', 'Y', 88.90585, 'Metal', [3], '+3', (6, 2)),
             'Zirconio': elemento('Zirconio', 'De Transición', 'Zr', 91.224, 'Metal', [2, 3, 4], '+4', (6, 3)),
             'Niobio': elemento('Niobio', 'De Transición', 'Nb', 92.90638, 'Metal', [2, 3, 4, 5], '+5', (6, 4)),
             'Molibdeno': elemento('Molibdeno', 'De Transición', 'Mo', 95.94, 'Metal', [2, 3, 4, 5, 6], '+6', (6, 5)),
             'Tecnecio': elemento('Tecnecio', 'De Transición', 'Tc', 98.90631, 'Metal', [7], 'N/A', (6, 6)),
             'Rutenio': elemento('Rutenio', 'De Transición', 'Ru', 101.07, 'Metal', [2, 3, 4, 6, 8], '+3', (6, 7)),
             'Rodio': elemento('Rodio', 'De Transición', 'Rh', 102.90550, 'Metal', [2, 3, 4, 6], '+2', (6, 8)),
             'Paladio': elemento('Paladio', 'De Transición', 'Pd', 106.42, 'Metal', [2, 4], '+2', (6, 9)),
             'Plata': elemento('Plata', 'De Transición', 'Ag', 107.8683, 'Metal', [1], '+1', (6, 10)),
             'Cadmio': elemento('Cadmio', 'De Transición', 'Cd', 112.411, 'Metal', [2], '+2', (6, 11)),
             'Indio': elemento('Indio', 'Metales del bloque p', 'In', 114.818, 'Metal', [3], '+3', (6, 12)),
             'Estaño': elemento('Estaño', 'Metales del bloque p', 'Sn', 118.710, 'Metal', [2, 4], '+4', (6, 13)),
             'Antimonio': elemento('Antimonio', 'Metaloide', 'Sb', 121.760, 'Metaloide', [3, -3, 5], '+5', (6, 14)),
             'Telurio': elemento('Telurio', 'Metaloide', 'Te', 127.6, 'Metaloide', [2, -2, 4, 6], '-2', (6, 15)),
             'Yodo': elemento('Yodo', 'Halógeno', 'I', 126.90447, 'No Metal', [1, -1, 3, 5, 7], '-1', (6, 16)),
             'Xenón': elemento('Xenón', 'Gas Noble', 'Xe', 131.293, 'No Metal', [0], 'N/A', (6, 17)),
             'Cesio': elemento('Cesio', 'Alcalino', 'Cs', 132.90545, 'Metal', [1], '+1', (7, 0)),
             'Bario': elemento('Bario', 'Alcalinotérreo', 'Ba', 137.327, 'Metal', [2], '+2', (7, 1)),
             'Lantano': elemento('Lantano', 'Lántanido', 'La', 138.9055, 'Metal', [2], '+3', (12, 3)),
             'Cerio': elemento('Cerio', 'Látanido', 'Ce', 140.116, 'Metal', [3, 4], '+4', (12, 4)),
             'Praseodimio': elemento('Praseodimio', 'Lántanido', 'Pr', 140.90765, 'Metal', [3, 4], '+3', (12, 5)),
             'Neodimio': elemento('Neodimio', 'Lántanido', 'Nd', 144.24, 'Metal', [3], '+3', (12, 6)),
             'Prometio': elemento('Prometio', 'Lántanidos', 'Pm', 145, 'Metal', [3], '+3', (12, 7)),
             'Samario': elemento('Samario', 'Lántanido', 'Sm', 150.35, 'Metal', [2, 3], '+3', (12, 8)),
             'Europio': elemento('Europio', 'Lántanido', 'Eu', 151.964, 'Metal', [2, 3], '+2', (12, 9)),
             'Gadolinio': elemento('Gadolinio', 'Lántanido', 'Gd', 157.25, 'Metal', [3], '+3', (12, 10)),
             'Terbio': elemento('Terbio', 'Lántanido', 'Tb', 158.92534, 'Metal', [3, 4], '+3', (12, 11)),
             'Disprosio': elemento('Disprosio', 'Lántanido', 'Dy', 158.924, 'Metal', [3], '+3', (12, 12)),
             'Holmio': elemento('Holmio', 'Lántanido', 'Ho', 164.9304, 'Metal', [3], '+3', (12, 13)),
             'Erbio': elemento('Erbio', 'Lántanido', 'Er', 167.259, 'Metal', [3], '+3', (12, 14)),
             'Tulio': elemento('Tulio', 'Lántanido', 'Tm', 168.934, 'Metal', [2, 3], '+3', (12, 15)),
             'Iterbio': elemento('Iterbio', 'Lántanido', 'Yb', 173.04, 'Metal', [2, 3], '+2', (12, 16)),
             'Lutecio': elemento('Lutecio', 'Lántanido', 'Lu', 174.967, 'Metal', [3], '+3', (12, 17)),
             'Hafnio': elemento('Hafnio', 'De transición', 'Hf', 178.49, 'Metal', [2, 3, 4], '+4', (7, 2)),
             'Tantalio': elemento('Tantalio', 'De transición', 'Ta', 180.9479, 'Metal', [2, 3, 4, 5], '+5', (7, 3)),
             'Wolframio': elemento('Wolframio', 'De transición', 'W', 183.84, 'Metal', [2, 3, 4, 5, 6], '+4', (7, 4)),
             'Renio': elemento('Renio', 'De transición', 'Re', 186.207, 'Metal', [2, 4, 6, 7], 'N/A', (7, 5)),
             'Osmio': elemento('Osmio', 'De transición', 'Os', 190.23, 'Metal', [2, 3, 4, 6, 8], '+4', (7, 6)),
             'Iridio': elemento('Iridio', 'De transición', 'Ir', 192.217, 'Metal', [2, 3, 4, 5], '+4', (7, 7)),
             'Platino': elemento('Platino', 'De transición', 'Pt', 195.084, 'Metal', [2, 4], '+2', (7, 8)),
             'Oro': elemento('Oro', 'De transición', 'Au', 196.966569, 'Metal', [1, 3], '+1', (7, 9)),
             'Mercurio': elemento('Mercurio', 'De transición', 'Hg', 200.59, 'Metal', [1, 2], '+2', (7, 10)),
             'Talio': elemento('Talio', 'Del bloque p', 'Tl', 204.3833, 'Metal', [1, 3], '+3', (7, 11)),
             'Plomo': elemento('Plomo', 'Del bloque p', 'Pb', 207.2, 'Metal', [2, 4], '+2', (7, 12)),
             'Bismuto': elemento('Bismuto', 'Del bloque p', 'Bi', 208.980386, 'Metal', [3, 5], '+3', (7, 13)),
             'Polonio': elemento('Polonio', 'Metaloides', 'Po', 209.9824, 'Metaloide', [4, 8], 'N/A', (7, 14)),
             'Ástato': elemento('Ástato', 'Hálogenos', 'At', 210, 'Metal', [0], 'N/A', (7, 15)),
             'Radón': elemento('Radón', 'Gas Noble', 'Rn', 222, 'No metal', [0], 'N/A', (7, 16)),
             'Lantano': elemento('Lantano', 'Lantánido', 'La', 138.9055, 'Metal', [2], '+3', (12, 3)),
             'Cerio': elemento('Cerio', 'Lantánido', 'Ce', 140.116, 'Metal', [3, 4], '+4', (12, 4)),
             'Praseodimio': elemento('Praseodimio', 'Lantánido', 'Pr', 140.90765, 'Metal', [3, 4], '+3', (12, 5)),
             'Neodimio': elemento('Neodimio', 'Lantánido', 'Nd', 144.24, 'Metal', [3], '+3', (12, 6)),
             'Prometio': elemento('Prometio', 'Lantánido', 'Pm', 145, 'Metal', [3], '+3', (12, 7)),
             'Samario': elemento('Samario', 'Lantánido', 'Sm', 150.35, 'Metal', [2, 3], '+3', (12, 8)),
             'Europio': elemento('Europio', 'Lantánido', 'Eu', 151.964, 'Metal', [2, 3], '+2', (12, 9)),
             'Gadolinio': elemento('Gadolinio', 'Lantánido', 'Gd', 157.25, 'Metal', [3], '+3', (12, 10)),
             'Terbio': elemento('Terbio', 'Lantánido', 'Tb', 158.92534, 'Metal', [3, 4], '+3', (12, 11)),
             'Disprosio': elemento('Disprosio', 'Lantánido', 'Dy', 158.924, 'Metal', [3], '+3', (12, 12)),
             'Holmio': elemento('Holmio', 'Lantánido', 'Ho', 164.9304, 'Metal', [3], '+3', (12, 13)),
             'Erbio': elemento('Erbio', 'Lantánido', 'Er', 167.259, 'Metal', [3], '+3', (12, 14)),
             'Tulio': elemento('Tulio', 'Lantánido', 'Tm', 168.934, 'Metal', [2, 3], '+3', (12, 15)),
             'Iterbio': elemento('Iterbio', 'Lantánido', 'Yb', 173.04, 'Metal', [2, 3], '+2', (12, 16)),
             'Lutecio': elemento('Lutecio', 'Lantánido', 'Lu', 174.967, 'Metal', [3], '+3', (12, 17)),
             'Hafnio': elemento('Hafnio', 'De Transición', 'Hf', 178.49, 'Metal', [2, 3, 4], '+4', (7, 3)),
             'Tantalio': elemento('Tantalio', 'De Transición', 'Ta', 180.9479, 'Metal', [2, 3, 4, 5], '+5', (7, 4)),
             'Wolframio': elemento('Wolframio', 'De Transición', 'W', 183.84, 'Metal', [2, 3, 4, 5, 6], '+4', (7, 5)),
             'Renio': elemento('Renio', 'De Transición', 'Re', 186.207, 'Metal', [2, 4, 6, 7], 'N/A', (7, 6)),
             'Osmio': elemento('Osmio', 'De Transición', 'Os', 190.23, 'Metal', [2, 3, 4, 6, 8], '+4', (7, 7)),
             'Iridio': elemento('Iridio', 'De Transición', 'Ir', 192.217, 'Metal', [2, 3, 4, 5], '+4', (7, 8)),
             'Platino': elemento('Platino', 'De Transición', 'Pt', 195.084, 'Metal', [2, 4], '+2', (7, 9)),
             'Oro': elemento('Oro', 'De Transición', 'Au', 196.966569, 'Metal', [1, 3], '+1', (7, 10)),
             'Mercurio': elemento('Mercurio', 'De Transición', 'Hg', 200.59, 'Metal', [1, 2], '+2', (7, 11)),
             'Talio': elemento('Talio', 'Metales del bloque p', 'Tl', 204.3833, 'Metal', [1, 3], '+3', (7, 12)),
             'Plomo': elemento('Plomo', 'Metales del bloque p', 'Pb', 207.2, 'Metal', [2, 4], '+2', (7, 13)),
             'Bismuto': elemento('Bismuto', 'Metales del bloque p', 'Bi', 208.980386, 'Metal', [3, 5], '+3', (7, 14)),
             'Polonio': elemento('Polonio', 'Metaloide', 'Po', 209.9824, 'Metaloide', [4, 8], 'N/A', (7, 15)),
             'Ástato': elemento('Ástato', 'Halógeno', 'At', 210, 'Metal', [0], 'N/A', (7, 16)),
             'Radón': elemento('Radón', 'Gas Noble', 'Rn', 222, 'No Metal', [0], 'N/A', (7, 17)),
             'Francio': elemento('Francios', 'Alcalino', 'Fr', 223, 'Metal', [1], '+1', (8, 0)),
             'Radio': elemento('Radio', 'Alcalinotérreo', 'Ra', 226.0254, 'Metal', [2], '+2', (8, 1)),
             'Actinio': elemento('Actinio', 'Actínido', 'Ac', 227, 'Metal', [3], '+3', (13, 3)),
             'Torio': elemento('Torio', 'Actínido', 'Th', 232.0381, 'Metal', [3], '+4', (13, 4)),
             'Protactinio': elemento('Protactinio', 'Actínido', 'Pa', 231.03588, 'Metal', [4, 5], '+4', (13, 5)),
             'Uranio': elemento('Uranio', 'Actínido', 'U', 238.02891, 'Metal', [3, 4, 5, 6], '+3', (13, 6)),
             'Neptunio': elemento('Neptunio', 'Actínido', 'Np', 237, 'Metal', [3, 4, 5, 6], '+3', (13, 7)),
             'Plutonio': elemento('Plutonio', 'Actínido', 'Pu', 244, 'Metal', [3, 4, 5, 6], '+3', (13, 8)),
             'Americio': elemento('Americio', 'Actínido', 'Am', 243, 'Metal', [3, 4, 5, 6], '+3', (13, 9)),
             'Curio': elemento('Curio', 'Actínido', 'Cm', 247, 'Metal', [3], '+3', (13, 10)),
             'Berkelio': elemento('Berkelio', 'Actínido', 'Bk', 247, 'Metal', [3, 4], '+3', (13, 11)),
             'Californio': elemento('Californio', 'Actínido', 'Cf', 251, 'Metal', [3], '+3', (13, 12)),
             'Einstenio': elemento('Einstenio', 'Actínido', 'Es', 252, 'Metal', [3], '+3', (13, 13)),
             'Fermio': elemento('Fermio', 'Actínido', 'Fm', 257, 'Metal', [0], 'N/A', (13, 14)),
             'Mendelevio': elemento('Mendelevio', 'Actínido', 'Md', 258, 'Metal', [0], 'N/A', (13, 15)),
             'Nobelio': elemento('Nobelio', 'Actínido', 'No', 259, 'Metal', [0], 'N/A', (13, 16)),
             'Lawrencio': elemento('Lawrencio', 'Actínido', 'Lr', 262, 'Metal', [0], 'N/A', (13, 17)),
             'Rutherfordio': elemento('Rutherfordio', 'De Transición', 'Rf', 261, 'Metal', [0], 'N/A', (8, 3)),
             'Dubnio': elemento('Dubnio', 'De Transición', 'Db', 262, 'Metal', [0], 'N/A', (8, 4)),
             'Seaborgio': elemento('Seaborgio', 'De Transición', 'Sg', 269, 'Metal', [0], 'N/A', (8, 5)),
             'Bohrio': elemento('Bohrio', 'De Transición', 'Bh', 264, 'Metal', [0], 'N/A', (8, 6)),
             'Hasio': elemento('Hasio', 'De Transición', 'Hs', 269, 'Metal', [0], 'N/A', (8, 7)),
             'Meitnerio': elemento('Meitnerio', 'De Transición', 'Mt', 268, 'Metal', [0], 'N/A', (8, 8)),
             'Darmstadio': elemento('Darmstadio', 'De Transición', 'Ds', 281, 'Metal', [0], 'N/A', (8, 9)),
             'Roetgenio': elemento('Roetgenio', 'De Transición', 'Rg', 282, 'Metal', [0], 'N/A', (8, 10)),
             'Copernicio': elemento('Copernicio', 'De Transición', 'Cn', 285, 'Metal', [0], 'N / A', (8, 11)),
             'Nihonio': elemento('Nihonio', 'Metales del bloque p', 'Nh', 286, 'Metal', [0], 'N/A', (8, 12)),
             'Flerovio': elemento('Flerovio', 'Metales del bloque p', 'F', 287, 'Metal', [0], 'N/A', (8, 13)),
             'Moscovio': elemento('Moscovio', 'Metales del bloque p', 'Nh', 286, 'Metal', [0], 'N/A', (8, 14)),
             'Livermorio': elemento('Livermorio', 'Metales del bloque p', 'Lv', 291, 'Metal', [0], 'N/A', (8, 15)),
             'Teneso': elemento('Teneso', 'Halógeno', 'Ts', 294, 'No Metal', [0], 'N/A', (8, 16)),
             'Oganesón': elemento('Oganesón', 'Gas Noble', 'Og', 294, 'No Metal', [0], 'N/A', (8, 17)),
             'Ununennio': elemento('Ununennio', 'Alcalino', 'Uue', 294, 'Metal', [0], 'N/A', (9, 0))}
