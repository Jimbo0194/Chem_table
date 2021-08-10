from elementos import elemento
from tkinter import ttk
import tkinter as tk


class propiedad:

    def __init__(self):
        self.hidrogeno = elemento()
        self.hidrogeno.nombre = "Hidrogeno";
        self.hidrogeno.tipo = "Alcalino";
        self.hidrogeno.siglas = "H";
        self.hidrogeno.pesoAtomico = 1.0079;
        self.hidrogeno.clasificacion = "No metal";
        self.hidrogeno.valencia = [-1, 1]
        self.helio = elemento()
        self.helio.nombre = "Helio";
        self.helio.tipo = "Gas noble";
        self.helio.siglas = "He";
        self.helio.pesoAtomico = 4.0026;
        self.helio.clasificacion = "No metal";
        self.helio.valencia = [0]
        self.litio = elemento()
        self.litio.nombre = "Litio";
        self.litio.tipo = "Alcalino";
        self.litio.siglas = "Li";
        self.litio.pesoAtomico = 6.941;
        self.litio.clasificacion = "Metal";
        self.litio.valencia = [1]
        self.berilio = elemento()
        self.berilio.nombre = "	Berilio";
        self.berilio.tipo = "Alcalinoterreo";
        self.berilio.siglas = "Be";
        self.berilio.pesoAtomico = 9.0122;
        self.berilio.clasificacion = "Metal";
        self.berilio.valencia = [2]
        self.boro = elemento()
        self.boro.nombre = "Boro";
        self.boro.tipo = "Metaloide";
        self.boro.siglas = "B";
        self.boro.pesoAtomico = 10.811;
        self.boro.clasificacion = "No metal";
        self.boro.valencia = [+3]
        self.carbono = elemento()
        self.carbono.nombre = "Carbono";
        self.carbono.tipo = "No metal";
        self.carbono.siglas = "C";
        self.carbono.pesoAtomico = 12.0107;
        self.carbono.clasificacion = "No metal";
        self.carbono.valencia = [-4, 2, 4]
        self.nitrogeno = elemento()
        self.nitrogeno.nombre = "Nitrogeno";
        self.nitrogeno.tipo = "No metal";
        self.nitrogeno.siglas = "N";
        self.nitrogeno.pesoAtomico = 14.0067;
        self.nitrogeno.clasificacion = "No metal";
        self.nitrogeno.valencia = [-3, 1, 2, 3, 4, 5]
        self.oxigeno = elemento()
        self.oxigeno.nombre = "Oxigeno";
        self.oxigeno.tipo = "No metal";
        self.oxigeno.siglas = "O";
        self.oxigeno.pesoAtomico = 15.9994;
        self.oxigeno.clasificacion = "No metal";
        self.oxigeno.valencia = [-2, 2]
        self.fluor = elemento()
        self.fluor.nombre = "Fluor";
        self.fluor.tipo = "Halogeno";
        self.fluor.siglas = "F";
        self.fluor.pesoAtomico = 18.9984;
        self.fluor.clasificacion = "No metal";
        self.fluor.valencia = [-1, 1]
        self.neon = elemento()
        self.neon.nombre = "Neon";
        self.neon.tipo = "Gas noble";
        self.neon.siglas = "Ne";
        self.neon.pesoAtomico = 20.1797;
        self.neon.clasificacion = "No metal";
        self.neon.valencia = [0]
        self.sodio = elemento();
        self.sodio.nombre = "Sodio";
        self.sodio.tipo = "Alcalino";
        self.sodio.siglas = "Na";
        self.sodio.pesoAtomico = 22.9897;
        self.sodio.clasificacion = "Metal";
        self.sodio.valencia = [1]
        self.magnesio = elemento()
        self.magnesio.nombre = "Magnesio";
        self.magnesio.tipo = "Alcalinoterreo";
        self.magnesio.siglas = "Mg";
        self.magnesio.pesoAtomico = 24.305;
        self.magnesio.clasificacion = "Metal";
        self.magnesio.valencia = [2]
        self.aluminio = elemento()
        self.aluminio.nombre = "Aluminio";
        self.aluminio.tipo = "Metal";
        self.aluminio.siglas = "Al";
        self.aluminio.pesoAtomico = 26.9815;
        self.aluminio.clasificacion = "Metal";
        self.aluminio.valencia = [3]
        self.silicio = elemento()
        self.silicio.nombre = "Silicio";
        self.silicio.tipo = "Metaloide";
        self.silicio.siglas = "Si";
        self.silicio.pesoAtomico = 28.0855;
        self.silicio.clasificacion = "No metal";
        self.silicio.valencia = [-4, 4]
        self.fosforo = elemento()
        self.fosforo.nombre = "Fosforo";
        self.fosforo.tipo = "No metal";
        self.fosforo.siglas = "P";
        self.fosforo.pesoAtomico = 30.9738;
        self.fosforo.clasificacion = "No metal";
        self.fosforo.valencia = [-3, 3, 4, 5]
        self.azufre = elemento()
        self.azufre.nombre = "Azufre";
        self.azufre.tipo = "No metal";
        self.azufre.siglas = "S";
        self.azufre.pesoAtomico = 32.065;
        self.azufre.clasificacion = "No metal";
        self.azufre.valencia = [-2, 2, 4, 6]
        self.cloro = elemento()
        self.cloro.nombre = "Cloro";
        self.cloro.tipo = "Halogeno";
        self.cloro.siglas = "Cl";
        self.cloro.pesoAtomico = 35.453;
        self.cloro.clasificacion = "No metal";
        self.cloro.valencia = [-1, 1, 3, 5, 7]
        self.potasio = elemento()
        self.potasio.nombre = "Potasio";
        self.potasio.tipo = "Alcalino";
        self.potasio.siglas = "K";
        self.potasio.pesoAtomico = 39.0983;
        self.potasio.clasificacion = "Metal";
        self.potasio.valencia = [1]
        self.argon = elemento()
        self.argon.nombre = "Argon";
        self.argon.tipo = "Gas noble";
        self.argon.siglas = "Ar";
        self.argon.pesoAtomico = 39.948;
        self.argon.clasificacion = "No metal";
        self.argon.valencia = [0]
        self.calcio = elemento()
        self.calcio.nombre = "Calcio";
        self.calcio.tipo = "Alcalinoterreo";
        self.calcio.siglas = "Ca";
        self.calcio.pesoAtomico = 40.078;
        self.calcio.clasificacion = "Metal";
        self.calcio.valencia = [2]
        self.escandio = elemento()
        self.escandio.nombre = "Escandio";
        self.escandio.tipo = "De transicion";
        self.escandio.siglas = "Sc";
        self.escandio.pesoAtomico = 44.9559;
        self.escandio.clasificacion = "Metal";
        self.escandio.valencia = [3]
        self.titanio = elemento()
        self.titanio.nombre = "Titanio";
        self.titanio.tipo = "De transicion";
        self.titanio.siglas = "Ti";
        self.titanio.pesoAtomico = 47.867;
        self.titanio.clasificacion = "Metal";
        self.titanio.valencia = [-1, 1, 2, 3, 4]
        self.vanadio = elemento()
        self.vanadio.nombre = "Vanadio";
        self.vanadio.tipo = "De transicion";
        self.vanadio.siglas = "V";
        self.vanadio.pesoAtomico = 50.9415;
        self.vanadio.clasificacion = "Metal";
        self.vanadio.valencia = [2, 3, 4, 5]
        self.cromo = elemento()
        self.cromo.nombre = "Cromo";
        self.cromo.tipo = "De transicion";
        self.cromo.siglas = "Cr";
        self.cromo.pesoAtomico = 51.9961;
        self.cromo.clasificacion = "Metal";
        self.cromo.valencia = [2, 3, 4, 5, 6]
        self.manganeso = elemento()
        self.manganeso.nombre = "Manganeso";
        self.manganeso.tipo = "De transicion";
        self.manganeso.siglas = "Mn";
        self.manganeso.pesoAtomico = 54.938;
        self.manganeso.clasificacion = "Metal";
        self.manganeso.valencia = [2, 3, 4, 6, 7]
        self.hierro = elemento()
        self.hierro.nombre = "Hierro";
        self.hierro.tipo = "De transicion";
        self.hierro.siglas = "Fe";
        self.hierro.pesoAtomico = 55.845;
        self.hierro.clasificacion = "Metal";
        self.hierro.valencia = [2, 3]
        self.niquel = elemento()
        self.niquel.nombre = "Niquel";
        self.niquel.tipo = "De transicion";
        self.niquel.siglas = "Ni";
        self.niquel.pesoAtomico = 58.6934;
        self.niquel.clasificacion = "Metal";
        self.niquel.valencia = [2, 3]
        self.cobalto = elemento()
        self.cobalto.nombre = "Cobalto";
        self.cobalto.tipo = "De transicion";
        self.cobalto.siglas = "Co";
        self.cobalto.pesoAtomico = 58.9332;
        self.cobalto.clasificacion = "Metal";
        self.cobalto.valencia = [2, 3]
        self.cobre = elemento()
        self.cobre.nombre = "Cobre";
        self.cobre.tipo = "De transicion";
        self.cobre.siglas = "Cu";
        self.cobre.pesoAtomico = 63.546;
        self.cobre.clasificacion = "Metal";
        self.cobre.valencia = [1, 2]
        self.zinc = elemento()
        self.zinc.nombre = "Zinc";
        self.zinc.tipo = "De transicion";
        self.zinc.siglas = "Zn";
        self.zinc.pesoAtomico = 65.39;
        self.zinc.clasificacion = "Metal";
        self.zinc.valencia = [2]
        # adrian
        self.zirconio = elemento()
        self.zirconio.nombre = "Zirconio";
        self.zirconio.tipo = "De transicion";
        self.zirconio.siglas = "Zr";
        self.zirconio.pesoAtomico = 91.22;
        self.zirconio.clasificacion = "Metal";
        self.zirconio.valencia = [2, 3, 4];
        self.zirconio.oxidacion = [4]
        self.Niobio = elemento()
        self.Niobio.nombre = "Niobio";
        self.Niobio.tipo = "De transicion";
        self.Niobio.siglas = "Nb";
        self.Niobio.pesoAtomico = 92.906;
        self.Niobio.clasificacion = "Metal";
        self.Niobio.valencia = [2, 3, 4, 5];
        self.Niobio.oxidacion = [5]
        self.Molibdeno = elemento()
        self.Molibdeno.nombre = "Molibdeno";
        self.Molibdeno.tipo = "De transicion";
        self.Molibdeno.siglas = "Mo";
        self.Molibdeno.pesoAtomico = 92.906;
        self.Molibdeno.clasificacion = "Metal";
        self.Molibdeno.valencia = [2, 3, 4, 5, 6];
        self.Molibdeno.oxidacion = [6]
        self.Tecnecio = elemento()
        self.Tecnecio.nombre = "Tecnecio";
        self.Tecnecio.tipo = "De transicion";
        self.Tecnecio.siglas = "Tc";
        self.Tecnecio.pesoAtomico = 98;
        self.Tecnecio.clasificacion = "Metal";
        self.Tecnecio.valencia = [7];
        self.Tecnecio.oxidacion = []
        self.Rutenio = elemento()
        self.Rutenio.nombre = "Rutenio";
        self.Rutenio.tipo = "De transicion";
        self.Rutenio.siglas = "Ru";
        self.Rutenio.pesoAtomico = 101.07;
        self.Rutenio.clasificacion = "Metal";
        self.Rutenio.valencia = [2, 3, 4, 6, 8];
        self.Rutenio.oxidacion = [3]
        self.Rodio = elemento()
        self.Rodio.nombre = "Rodio";
        self.Rodio.tipo = "De transicion";
        self.Rodio.siglas = "Rh";
        self.Rodio.pesoAtomico = 102.905;
        self.Rodio.clasificacion = "Metal";
        self.Rodio.valencia = [2, 3, 4, 6];
        self.Rodio.oxidacion = [2]
        self.Paladio = elemento()
        self.Paladio.nombre = "Paladio";
        self.Paladio.tipo = "De transicion";
        self.Paladio.siglas = "Pd";
        self.Paladio.pesoAtomico = 106.42;
        self.Paladio.clasificacion = "Metal";
        self.Paladio.valencia = [1, 2, 4, 6];
        self.Paladio.oxidacion = [2]
        self.Plata = elemento()
        self.Plata.nombre = "Plata";
        self.Plata.tipo = "De transicion";
        self.Plata.siglas = "Ag";
        self.Plata.pesoAtomico = 107.868;
        self.Plata.clasificacion = "Metal";
        self.Plata.valencia = [1, 2, 3, 4];
        self.Plata.oxidacion = [1]
        self.Cadmio = elemento()
        self.Cadmio.nombre = "Cadmio";
        self.Cadmio.tipo = "De transicion";
        self.Cadmio.siglas = "Cd";
        self.Cadmio.pesoAtomico = 102.411;
        self.Cadmio.clasificacion = "Metal";
        self.Cadmio.valencia = [1, 2];
        self.Cadmio.oxidacion = [2]
        self.Indio = elemento()
        self.Indio.nombre = "Indio";
        self.Indio.tipo = "Metales del Bloque p";
        self.Indio.siglas = "In";
        self.Indio.pesoAtomico = 114.818;
        self.Indio.clasificacion = "Metal";
        self.Indio.valencia = [3];
        self.Indio.oxidacion = [3]
        self.Estaño = elemento()
        self.Estaño.nombre = "Estaño";
        self.Estaño.tipo = "Metales del Bloque p";
        self.Estaño.siglas = "Sn";
        self.Estaño.pesoAtomico = 118.71;
        self.Estaño.clasificacion = "Metal";
        self.Estaño.valencia = [2, 4];
        self.Estaño.oxidacion = [4]
        self.Antimonio = elemento()
        self.Antimonio.nombre = "Antimonio";
        self.Antimonio.tipo = "Metaloide";
        self.Antimonio.siglas = "Sb";
        self.Antimonio.pesoAtomico = 121.76;
        self.Antimonio.clasificacion = "No metal";
        self.Antimonio.valencia = [-3, 3, 5];
        self.Antimonio.oxidacion = [5]
        self.Iodo = elemento()
        self.Iodo.nombre = "Iodo";
        self.Iodo.tipo = "Halógeno";
        self.Iodo.siglas = "I";
        self.Iodo.pesoAtomico = 126.904;
        self.Iodo.clasificacion = "No metal";
        self.Iodo.valencia = [-1, 1, 3, 5, 7];
        self.Iodo.oxidacion = [-1]
        self.Teluro = elemento()
        self.Teluro.nombre = "Teluro";
        self.Teluro.tipo = "Metaloide";
        self.Teluro.siglas = "Te";
        self.Teluro.pesoAtomico = 127.6;
        self.Teluro.clasificacion = "No metal";
        self.Teluro.valencia = [-2, 2, 4, 6];
        self.Teluro.oxidacion = [-2]
        self.Xenón = elemento()
        self.Xenón.nombre = "Xenón";
        self.Teluro.tipo = "Gas noble";
        self.Xenón.siglas = "Xe";
        self.Xenón.pesoAtomico = 131.293;
        self.Xenón.clasificacion = "No metal";
        self.Xenón.valencia = [0];
        self.Xenón.oxidacion = []
        self.Cesio = elemento()
        self.Cesio.nombre = "Cesio";
        self.Teluro.tipo = "Alcalino";
        self.Cesio.siglas = "Cs";
        self.Cesio.pesoAtomico = 132.905;
        self.Cesio.clasificacion = "Metal";
        self.Cesio.valencia = [1];
        self.Cesio.oxidacion = [1]
        self.Bario = elemento()
        self.Bario.nombre = "Bario";
        self.Bario.tipo = "Alcalinotérreos";
        self.Bario.siglas = "Ba";
        self.Bario.pesoAtomico = 137.327;
        self.Bario.clasificacion = "Metal";
        self.Bario.valencia = [2];
        self.Bario.oxidacion = [2]
        self.Lantano = elemento()
        self.Lantano.nombre = "Lantano";
        self.Lantano.tipo = "Lantánidos";
        self.Lantano.siglas = "La";
        self.Lantano.pesoAtomico = 138.905;
        self.Lantano.clasificacion = "Metal";
        self.Lantano.valencia = [3];
        self.Lantano.oxidacion = [3]
        self.Cerio = elemento()
        self.Cerio.nombre = "Cerio";
        self.Cerio.tipo = "Lantánidos";
        self.Cerio.siglas = "Ce";
        self.Cerio.pesoAtomico = 140.116;
        self.Cerio.clasificacion = "Metal";
        self.Cerio.valencia = [3, 4];
        self.Cerio.oxidacion = [4]
        self.Praseodimio = elemento()
        self.Praseodimio.nombre = "Praseodimio";
        self.Praseodimio.tipo = "Lantánidos";
        self.Praseodimio.siglas = "Pr";
        self.Praseodimio.pesoAtomico = 140.907;
        self.Praseodimio.clasificacion = "Metal";
        self.Praseodimio.valencia = [3, 4];
        self.Praseodimio.oxidacion = [3]
        self.Neodimio = elemento()
        self.Neodimio.nombre = "Neodimio";
        self.Neodimio.tipo = "Lantánidos";
        self.Neodimio.siglas = "Nd";
        self.Neodimio.pesoAtomico = 144.24;
        self.Neodimio.clasificacion = "Metal";
        self.Neodimio.valencia = [3];
        self.Neodimio.oxidacion = [3]
        self.Promecio = elemento()
        self.Promecio.nombre = "Promecio";
        self.Promecio.tipo = "Lantánidos";
        self.Promecio.siglas = "Pm";
        self.Promecio.pesoAtomico = 145;
        self.Promecio.clasificacion = "Metal";
        self.Promecio.valencia = [3];
        self.Promecio.oxidacion = [3]
        self.Samario = elemento()
        self.Samario.nombre = "Samario";
        self.Samario.tipo = "Lantánidos";
        self.Samario.siglas = "Sm";
        self.Samario.pesoAtomico = 150.36;
        self.Samario.clasificacion = "Metal";
        self.Samario.valencia = [2.3];
        self.Samario.oxidacion = [3]
        self.Europio = elemento()
        self.Europio.nombre = "Europio";
        self.Europio.tipo = "Lantánidos";
        self.Europio.siglas = "Eu";
        self.Europio.pesoAtomico = 151.964;
        self.Europio.clasificacion = "Metal";
        self.Europio.valencia = [2.3];
        self.Europio.oxidacion = [2]
        self.Gadolinio = elemento()
        self.Gadolinio.nombre = "Gadolinio";
        self.Gadolinio.tipo = "Lantánidos";
        self.Gadolinio.siglas = "Gd";
        self.Gadolinio.pesoAtomico = 157.25;
        self.Gadolinio.clasificacion = "Metal";
        self.Gadolinio.valencia = [3];
        self.Gadolinio.oxidacion = [3]
        self.Terbio = elemento()
        self.Terbio.nombre = "Terbio";
        self.Terbio.tipo = "Lantánidos";
        self.Terbio.siglas = "Tb";
        self.Terbio.pesoAtomico = 158.925;
        self.Terbio.clasificacion = "Metal";
        self.Terbio.valencia = [3, 4];
        self.Terbio.oxidacion = [3]
        self.Disprosio = elemento()
        self.Disprosio.nombre = "Disprosio";
        self.Disprosio.tipo = "Lantánidos";
        self.Disprosio.siglas = "Dy";
        self.Disprosio.pesoAtomico = 162.5;
        self.Disprosio.clasificacion = "Metal";
        self.Disprosio.valencia = [3];
        self.Disprosio.oxidacion = [3]
        self.Holmio = elemento()
        self.Holmio.nombre = "Holmio";
        self.Holmio.tipo = "Lantánidos";
        self.Holmio.siglas = "Ho";
        self.Holmio.pesoAtomico = 164.930;
        self.Holmio.clasificacion = "Metal";
        self.Holmio.valencia = [3];
        self.Holmio.oxidacion = [3]
        self.Erbio = elemento()
        self.Erbio.nombre = "Erbio";
        self.Erbio.tipo = "Lantánidos";
        self.Erbio.siglas = "Er";
        self.Erbio.pesoAtomico = 167.259;
        self.Erbio.clasificacion = "Metal";
        self.Erbio.valencia = [3];
        self.Erbio.oxidacion = [3]
        self.Tulio = elemento()
        self.Tulio.nombre = "Tulio";
        self.Tulio.tipo = "Lantánidos";
        self.Tulio.siglas = "Tm";
        self.Tulio.pesoAtomico = 168.934;
        self.Tulio.clasificacion = "Metal";
        self.Tulio.valencia = [2, 3];
        self.Tulio.oxidacion = [3]
        self.Iterbio = elemento()
        self.Iterbio.nombre = "Iterbio";
        self.Iterbio.tipo = "Lantánidos";
        self.Iterbio.siglas = "Yb";
        self.Iterbio.pesoAtomico = 173.04;
        self.Iterbio.clasificacion = "Metal";
        self.Iterbio.valencia = [2, 3];
        self.Iterbio.oxidacion = [2]
        self.Lutecio = elemento()
        self.Lutecio.nombre = "Lutecio";
        self.Lutecio.tipo = "Lantánidos";
        self.Lutecio.siglas = "Lu";
        self.Lutecio.pesoAtomico = 174.967;
        self.Lutecio.clasificacion = "Metal";
        self.Lutecio.valencia = [3];
        self.Lutecio.oxidacion = [3]
        self.Hafnio = elemento()
        self.Hafnio.nombre = "Hafnio";
        self.Hafnio.tipo = "De transicion";
        self.Hafnio.siglas = "Hf";
        self.Hafnio.pesoAtomico = 178.49;
        self.Hafnio.clasificacion = "Metal";
        self.Hafnio.valencia = [2, 3, 4];
        self.Hafnio.oxidacion = [4]
        self.Tantalio = elemento()
        self.Tantalio.nombre = "Tantalio";
        self.Tantalio.tipo = "De transicion";
        self.Tantalio.siglas = "Ta";
        self.Tantalio.pesoAtomico = 180.947;
        self.Tantalio.clasificacion = "Metal";
        self.Tantalio.valencia = [2, 3, 4, 5];
        self.Tantalio.oxidacion = [5]
        self.Wolframio = elemento()
        self.Wolframio.nombre = "Wolframio";
        self.Wolframio.tipo = "De transicion";
        self.Wolframio.siglas = "W";
        self.Wolframio.pesoAtomico = 183.84;
        self.Wolframio.clasificacion = "Metal";
        self.Wolframio.valencia = [2, 3, 4, 5, 6];
        self.Wolframio.oxidacion = [4]
        self.Renio = elemento()
        self.Renio.nombre = "Renio";
        self.Renio.tipo = "De transicion";
        self.Renio.siglas = "Re";
        self.Renio.pesoAtomico = 186.207;
        self.Renio.clasificacion = "Metal";
        self.Renio.valencia = [2, 4, 6, 7];
        self.Renio.oxidacion = []
        self.Osmio = elemento()
        self.Osmio.nombre = "Osmio";
        self.Osmio.tipo = "De transicion";
        self.Osmio.siglas = "Os";
        self.Osmio.pesoAtomico = 190.23;
        self.Osmio.clasificacion = "Metal";
        self.Osmio.valencia = [2, 3, 4, 6, 8];
        self.Osmio.oxidacion = [4]
        self.Iridio = elemento()
        self.Iridio.nombre = "Iridio";
        self.Iridio.tipo = "De transicion";
        self.Iridio.siglas = "Ir";
        self.Iridio.pesoAtomico = 192.217;
        self.Iridio.clasificacion = "Metal";
        self.Iridio.valencia = [2, 3, 4, 6];
        self.Iridio.oxidacion = [4]
        self.Platino = elemento()
        self.Platino.nombre = "Platino";
        self.Platino.tipo = "De transicion";
        self.Platino.siglas = "Pt";
        self.Platino.pesoAtomico = 195.078;
        self.Platino.clasificacion = "Metal";
        self.Platino.valencia = [2, 4];
        self.Platino.oxidacion = [2]
        # Luis
        self.oro = elemento()
        self.oro.nombre = "Oro";
        self.oro.tipo = "Metales de transicion";
        self.oro.siglas = "Au";
        self.oro.pesoAtomico = 196.96;
        self.oro.clasificacion = "Metal";
        self.oro.valencia = [1, 3]
        self.mercurio = elemento()
        self.mercurio.nombre = "Mercurio";
        self.mercurio.tipo = "Metales de transicion";
        self.mercurio.siglas = "Hg";
        self.mercurio.pesoAtomico = 200.59;
        self.mercurio.clasificacion = "Metal";
        self.mercurio.valencia = [1, 2]
        self.talio = elemento()
        self.talio.nombre = "Talio";
        self.talio.tipo = "Metales del bloque p";
        self.talio.siglas = "Tl";
        self.talio.pesoAtomico = 204.38;
        self.talio.clasificacion = "Metal";
        self.talio.valencia = [1, 3]
        self.plomo = elemento()
        self.plomo.nombre = "Plomo";
        self.plomo.tipo = "Metales del bloque p";
        self.plomo.siglas = "Pb";
        self.plomo.pesoAtomico = 207.2;
        self.plomo.clasificacion = "Metal";
        self.plomo.valencia = [2, 4]
        self.bismuto = elemento()
        self.bismuto.nombre = "Bismuto";
        self.bismuto.tipo = "Metales del bloque p";
        self.bismuto.siglas = "Bi";
        self.talio.pesoAtomico = 208.98;
        self.bismuto.clasificacion = "Metal";
        self.bismuto.valencia = [1, 3, 5]
        self.polonio = elemento()
        self.polonio.nombre = "Polonio";
        self.polonio.tipo = "Metaloides";
        self.polonio.siglas = "Po";
        self.polonio.pesoAtomico = 209;
        self.polonio.clasificacion = "Metal";
        self.polonio.valencia = [4, 6]
        self.astato = elemento()
        self.astato.nombre = "Astato";
        self.astato.tipo = "Halogenos";
        self.astato.siglas = "At";
        self.astato.pesoAtomico = 210;
        self.astato.clasificacion = "Metal";
        self.bismuto.valencia = ["N/A"]
        self.radon = elemento()
        self.radon.nombre = "Radon";
        self.radon.tipo = "Gases nobles";
        self.radon.siglas = "Rn";
        self.radon.pesoAtomico = 222;
        self.radon.clasificacion = "Gas";
        self.radon.valencia = ["N/A"]
        self.francio = elemento()
        self.francio.nombre = "Francio";
        self.francio.tipo = "Metales alcalinos";
        self.francio.siglas = "Fr";
        self.francio.pesoAtomico = 223;
        self.francio.clasificacion = "Metal";
        self.francio.valencia = [1]
        self.radio = elemento()
        self.radio.nombre = "Radio";
        self.radio.tipo = "Alcalinoterreos";
        self.radio.siglas = "Ra";
        self.radio.pesoAtomico = 226;
        self.radio.clasificacion = "Metal";
        self.radio.valencia = [2]
        self.actinio = elemento()
        self.actinio.nombre = "Actinio";
        self.actinio.tipo = "Actinido";
        self.actinio.siglas = "Ac";
        self.actinio.pesoAtomico = 208.98;
        self.actinio.clasificacion = "Metal";
        self.actinio.valencia = [1, 3]
        self.protactinio = elemento()
        self.protactinio.nombre = "Protactinio";
        self.protactinio.tipo = "Actinidos";
        self.protactinio.siglas = "Pa";
        self.protactinio.pesoAtomico = 231.03;
        self.protactinio.clasificacion = "Metal";
        self.protactinio.valencia = [4, 5]
        self.torio = elemento()
        self.torio.nombre = "Torio";
        self.torio.tipo = "Actinidos";
        self.torio.siglas = "Th";
        self.torio.pesoAtomico = 232.03;
        self.torio.clasificacion = "Metal";
        self.torio.valencia = [3, 4]
        self.neptunio = elemento()
        self.neptunio.nombre = "Neptunio";
        self.neptunio.tipo = "Actinidos";
        self.neptunio.siglas = "Np";
        self.neptunio.pesoAtomico = 237;
        self.neptunio.clasificacion = "Metal";
        self.neptunio.valencia = [3, 4, 5, 6]
        self.uranio = elemento()
        self.uranio.nombre = "Uranio";
        self.uranio.tipo = "Actinidos";
        self.uranio.siglas = "U";
        self.uranio.pesoAtomico = 238.02;
        self.uranio.clasificacion = "Metal";
        self.uranio.valencia = [3, 4, 5, 6]
        self.americio = elemento()
        self.americio.nombre = "Americio";
        self.americio.tipo = "Actinidos";
        self.americio.siglas = "Am";
        self.americio.pesoAtomico = 243;
        self.americio.clasificacion = "Metal";
        self.americio.valencia = [3, 4, 5, 6]
        self.plutonio = elemento()
        self.plutonio.nombre = "Plutonio";
        self.plutonio.tipo = "Actinidos";
        self.plutonio.siglas = "Pu";
        self.plutonio.pesoAtomico = 244;
        self.plutonio.clasificacion = "Metal";
        self.plutonio.valencia = [3, 4, 5, 6]
        self.curio = elemento()
        self.curio.nombre = "Curio";
        self.curio.tipo = "Actinidos";
        self.curio.siglas = "Cm";
        self.curio.pesoAtomico = 247;
        self.curio.clasificacion = "Metal";
        self.curio.valencia = [3]
        self.berkelio = elemento()
        self.berkelio.nombre = "Berkelio";
        self.berkelio.tipo = "Actinidos";
        self.berkelio.siglas = "Bk";
        self.berkelio.pesoAtomico = 247;
        self.berkelio.clasificacion = "Metal";
        self.berkelio.valencia = [3, 4]
        self.californio = elemento()
        self.californio.nombre = "Californio";
        self.californio.tipo = "Actinidos";
        self.californio.siglas = "Cf";
        self.californio.pesoAtomico = 251;
        self.californio.clasificacion = "Metal";
        self.californio.valencia = [2, 3, 4]
        self.einstenio = elemento()
        self.einstenio.nombre = "Einstenio";
        self.einstenio.tipo = "Actinidos";
        self.einstenio.siglas = "Es";
        self.einstenio.pesoAtomico = 252;
        self.einstenio.clasificacion = "Metal";
        self.einstenio.valencia = ["N/A"]
        self.fermio = elemento()
        self.fermio.nombre = "Fermio";
        self.fermio.tipo = "Actinidos";
        self.fermio.siglas = "Fm";
        self.fermio.pesoAtomico = 257;
        self.fermio.clasificacion = "Metal";
        self.fermio.valencia = ["N/A"]
        self.mendelevio = elemento()
        self.mendelevio.nombre = "Mendelevio";
        self.mendelevio.tipo = "Actinidos";
        self.mendelevio.siglas = "Md";
        self.mendelevio.pesoAtomico = 258;
        self.mendelevio.clasificacion = "Metal";
        self.mendelevio.valencia = [3, 4]
        self.nobelio = elemento()
        self.nobelio.nombre = "Nobelio";
        self.nobelio.tipo = "Actinidos";
        self.nobelio.siglas = "No";
        self.nobelio.pesoAtomico = 244;
        self.nobelio.clasificacion = "Metal";
        self.nobelio.valencia = ["N/A"]
        self.rutherfordio = elemento()
        self.rutherfordio.nombre = "Rutherfordio";
        self.rutherfordio.tipo = "Metales de transicion";
        self.rutherfordio.siglas = "Rf";
        self.plutonio.pesoAtomico = 261;
        self.rutherfordio.clasificacion = "Metal";
        self.rutherfordio.valencia = ["N/A"]
        self.lawrencio = elemento()
        self.lawrencio.nombre = "Lawrencio";
        self.lawrencio.tipo = "Actinidos";
        self.lawrencio.siglas = "Lr";
        self.lawrencio.pesoAtomico = 262;
        self.lawrencio.clasificacion = "Metal";
        self.lawrencio.valencia = ["N/A"]
        self.dubnio = elemento()
        self.dubnio.nombre = "Dubnio";
        self.dubnio.tipo = "Metales de transicion";
        self.dubnio.siglas = "Db";
        self.dubnio.pesoAtomico = 262;
        self.dubnio.clasificacion = "Metal";
        self.dubnio.valencia = ["N/A"]
        self.bohrio = elemento()
        self.bohrio.nombre = "Bohrio";
        self.bohrio.tipo = "Metales de transicion";
        self.plutonio.siglas = "Bh";
        self.plutonio.pesoAtomico = 264;
        self.bohrio.clasificacion = "Metal";
        self.bohrio.valencia = ["N/A"]
        self.seaborgio = elemento()
        self.seaborgio.nombre = "Seaborgio";
        self.seaborgio.tipo = "Actinidos";
        self.seaborgio.siglas = "Sg";
        self.seaborgio.pesoAtomico = 266;
        self.seaborgio.clasificacion = "Metal";
        self.seaborgio.valencia = ["N/A"]
        self.meitnerio = elemento()
        self.meitnerio.nombre = "Meitnerio";
        self.meitnerio.tipo = "Actinidos";
        self.meitnerio.siglas = "Mt";
        self.meitnerio.pesoAtomico = 268;
        self.meitnerio.clasificacion = "Metal";
        self.meitnerio.valencia = [3, 4, 5, 6]
        self.hassio = elemento()
        self.hassio.nombre = "Hassio";
        self.hassio.tipo = "Metal del transcicion";
        self.hassio.siglas = "Hs";
        self.hassio.pesoAtomico = 277;
        self.hassio.clasificacion = "Metal";
        self.hassio.valencia = ["N/A"]
        self.darmstadio = elemento()
        self.darmstadio.nombre = "Darmstadio";
        self.darmstadio.tipo = "Metales de transicion";
        self.darmstadio.siglas = "Ds";
        self.darmstadio.pesoAtomico = 244;
        self.darmstadio.clasificacion = "Metal";
        self.darmstadio.valencia = ["N/A"]
        self.ununio = elemento()
        self.ununio.nombre = "Ununio";
        self.ununio.tipo = "Actinidos";
        self.ununio.siglas = "Uuu";
        self.ununio.pesoAtomico = 244;
        self.ununio.clasificacion = "Metal";
        self.ununio.valencia = [3, 4, 5, 6]
        self.ununbio = elemento()
        self.ununbio.nombre = "Ununbio";
        self.ununbio.tipo = "Actinidos";
        self.ununbio.siglas = "Uub";
        self.ununbio.pesoAtomico = 244;
        self.ununbio.clasificacion = "Metal";
        self.ununbio.valencia = [3, 4, 5, 6]
        self.ununtrio = elemento()
        self.ununtrio.nombre = "Ununtrio";
        self.ununtrio.tipo = "Actinidos";
        self.ununtrio.siglas = "Pu";
        self.ununtrio.pesoAtomico = 244;
        self.ununtrio.clasificacion = "Metal";
        self.ununtrio.valencia = [3, 4, 5, 6]
        self.ununquadio = elemento()
        self.ununquadio.nombre = "Ununquadio";
        self.ununquadio.tipo = "Actinidos";
        self.ununquadio.siglas = "Pu";
        self.ununquadio.pesoAtomico = 244;
        self.ununquadio.clasificacion = "Metal";
        self.ununquadio.valencia = [3, 4, 5, 6]
        self.ununpentio = elemento()
        self.ununpentio.nombre = "Ununpentio";
        self.ununpentio.tipo = "Actinidos";
        self.ununpentio.siglas = "Pu";
        self.ununpentio.pesoAtomico = 244;
        self.ununpentio.clasificacion = "Metal";
        self.ununpentio.valencia = [3, 4, 5, 6]
        self.ununhexio = elemento()
        self.ununhexio.nombre = "Ununhexio";
        self.ununhexio.tipo = "Actinidos";
        self.ununhexio.siglas = "Pu";
        self.plutonio.pesoAtomico = 244;
        self.ununhexio.clasificacion = "Metal";
        self.ununhexio.valencia = [3, 4, 5, 6]
        self.ununseptio = elemento()
        self.ununseptio.nombre = "Ununseptio";
        self.ununseptio.tipo = "Actinidos";
        self.ununseptio.siglas = "Pu";
        self.ununseptio.pesoAtomico = 244;
        self.ununseptio.clasificacion = "Metal";
        self.ununseptio.valencia = [3, 4, 5, 6]
        self.ununoctio = elemento()
        self.ununoctio.nombre = "Ununoctio";
        self.ununoctio.tipo = "Actinidos";
        self.ununoctio.siglas = "Pu";
        self.ununoctio.pesoAtomico = 244;
        self.ununoctio.clasificacion = "Metal";
        self.ununoctio.valencia = [3, 4, 5, 6]

    def hid(self):
        return self.hidrogeno

    def sod(self):
        return self.sodio

    def lit(self):
        return self.litio

    def bor(self):
        return self.boro

    def zir(self):
        return self.zirconio

    def nio(self):
        return self.Niobio

    def mol(self):
        return self.Molibdeno

    def tec(self):
        return self.Tecnecio

    def rut(self):
        return self.Rutenio

    def rod(self):
        return self.Rodio

    def pad(self):
        return self.Paladio

    def pla(self):
        return self.Plata

    def cad(self):
        return self.Cadmio

    def ind(self):
        return self.Indio

    def est(self):
        return self.Estaño

    def ant(self):
        return self.Antimonio

    def iod(self):
        return self.Iodo

    def tel(self):
        return self.Teluro

    def xen(self):
        return self.Xenón

    def ces(self):
        return self.Cesio

    def bar(self):
        return self.Bario

    def lan(self):
        return self.Lantano

    def cer(self):
        return self.Cerio

    def pra(self):
        return self.Praseodimio

    def neo(self):
        return self.Neodimio

    def pro(self):
        return self.Promecio

    def sam(self):
        return self.Samario

    def eup(self):
        return self.Europio

    def gad(self):
        return self.Gadolinio

    def teb(self):
        return self.Terbio

    def dis(self):
        return self.Disprosio

    def hol(self):
        return self.Holmio

    def erb(self):
        return self.Erbio

    def tul(self):
        return self.Tulio

    def ite(self):
        return self.Iterbio

    def lut(self):
        return self.Lutecio

    def haf(self):
        return self.Hafnio

    def tan(self):
        return self.Tantalio

    def wol(self):
        return self.Wolframio

    def osm(self):
        return self.Osmio

    def iri(self):
        return self.Iridio

    def pla(self):
        return self.Platino

    def oro(self):
        return self.oro

    def merc(self):
        return self.mercurio

    def tal(self):
        return self.talio

    def plo(self):
        return self.plomo

    def bis(self):
        return self.bismuto

    def pol(self):
        return self.polonio

    def ast(self):
        return self.astato

    def rad(self):
        return self.radon

    def fra(self):
        return self.francio

    def radio(self):
        return self.radio

    def act(self):
        return self.actinio

    def pro(self):
        return self.protactinio

    def tor(self):
        return self.torio

    def nep(self):
        return self.neptunio

    def ura(self):
        return self.uranio

    def ame(self):
        return self.americio

    def plu(self):
        return self.plutonio

    def cur(self):
        return self.curio

    def ber(self):
        return self.berkelio

    def cal(self):
        return self.californio

    def ein(self):
        return self.einstenio

    def fer(self):
        return self.fermio

    def men(self):
        return self.mendelevio

    def nob(self):
        return self.nobelio

    def rut(self):
        return self.rutherfordio

    def law(self):
        return self.lawrencio

    def dub(self):
        return self.dubnio

    def boh(self):
        return self.bohnio

    def sea(self):
        return self.seaborgio

    def mei(self):
        return self.meitnerio

    def has(self):
        return self.hassio

    def darm(self):
        return self.darmstadio

    def un(self):
        return self.ununio

    def unub(self):
        return self.ununbio

    def unut(self):
        return self.ununtrio

    def unuq(self):
        return self.ununquadio

    def unup(self):
        return self.ununpentio

    def unuh(self):
        return self.ununhexio

    def unus(self):
        return self.ununseptio

    def unuo(self):
        return self.ununoctio
