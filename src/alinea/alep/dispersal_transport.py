""" Gather different strategies for modeling dispersal of fungus propagules.
from alinea.alep.fungus import Fungus
        if fungus is None:
            self.fungus = Fungus()
        else:
            self.fungus = fungus
                                deposits[leaf] = qc
            du = self.fungus.dispersal_unit()
            du.set_nb_dispersal_units(nb_dispersal_units=dep)
            deposits[vid] = [du]
        
        
        return d