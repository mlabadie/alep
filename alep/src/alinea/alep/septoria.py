""" Classes of dispersal unit, lesion and ring specific of wheat septoria.

"""
# Imports #####################################################################
from alinea.alep.fungal_objects import *
# from alinea.alep import septoria_continuous, septoria_with_rings,
# septoria_exchanging_rings
# from alinea.alep.septoria_continuous import *
# from alinea.alep.septoria_with_rings import *
# from alinea.alep.septoria_exchanging_rings import *
try:
    from openalea.vpltk import plugin
except ImportError:
    from openalea.core import plugin

from random import random
import numpy as np
import pandas as pd

# Dispersal unit #############################################################
class SeptoriaDU(DispersalUnit):
    """ Define a dispersal unit specific of septoria.
    
    """
    #fungus = None
    def __init__(self, mutable=False):
        """ Initialize the dispersal unit of septoria.
        
        Parameters
        ----------
        mutable: bool
            True if each DU has its own parameters, False otherwise
        
        Returns
        -------
            None
        """
        super(SeptoriaDU, self).__init__(mutable=mutable)
        # self.cumul_wetness = 0.
        # self.cumul_loss_rate = 0.
        # Cumulation of temperature conditions
        self.temperature_sequence = []
        # Cumulation of wetness conditions
        self.wetness_sequence = []
        self.dry_dt = 0.       
        # Temp
        self.nb_spores = 10.      
                
    def infect(self, dt = 1, leaf = None, **kwds):
        """ Compute infection by the dispersal unit of Septoria.
        
        Parameters
        ----------
        dt: int
            Time step of the simulation (in hours)
        leaf: Leaf sector node of an MTG 
            A leaf sector with properties (e.g. area, green area, healthy area,
            senescence, rain intensity, wetness, temperature, lesions)

        Returns
        -------
            None
        """
        if self.is_active:
            f = self.fungus
            if leaf.green_area== 0. or self.nb_dispersal_units == 0. or self.nb_spores == 0.:
                self.disable()
                return
            else:
                props = leaf.properties()
                # Accumulate climatic data on the leaf sector during the time step
                self.temperature_sequence += props['temperature_sequence']
                self.wetness_sequence += props['wetness_sequence']
#                self.temperature_sequence += leaf.temperature_sequence.tolist()
#                self.wetness_sequence += leaf.wetness_sequence.tolist()
                
                # Infection success
                temps = self.temperature_sequence
                wets = self.wetness_sequence
                count_wet = 0
                count_dry = 0
                for i_wet, wet in enumerate(wets):
                    if wet==True:
                        count_wet += 1
                        temp = np.mean(temps[i_wet-count_wet:i_wet])
                        if (count_wet >=f.wd_min and
                            temp>f.temp_min and 
                            temp<f.temp_max):
                                new_temperature_sequence = temps[i_wet:]
                                # Intrinsec proba of infection
                                proba_infection = f.proba_inf * self.nb_spores / self.nb_spores
                                # Fongicide effect
#                                if 'global_efficacy' in leaf.properties():
#                                    proba_infection *= (1 - max(0, min(1, leaf.global_efficacy['protectant'])))                           
                                # Create lesion
                                if f.group_dus:
                                    nb_les = np.random.binomial(self.nb_dispersal_units, proba_infection)
                                    if nb_les > 0:
                                        self.create_lesion(nb_les, leaf, 
                                                       temperature_sequence=new_temperature_sequence)
                                    else:
                                        self.disable()
                                    return
                                else:
                                    if proba(proba_infection):
                                        self.create_lesion(1, leaf,
                                                            temperature_sequence=new_temperature_sequence)
                                    else:
                                        self.disable()
                                    return
                    else:
                        new_temperature_sequence = temps[i_wet:]
                        new_wetness_sequence = wets[i_wet:]
                        count_wet = 0
                        count_dry += 1
                        self.temperature_sequence = new_temperature_sequence
                        self.wetness_sequence = new_wetness_sequence
                self.dry_dt += count_dry
                
                if self.dry_dt>=f.loss_delay:
                    loss_rate = 1.
                else:
                    loss_rate = 1./(f.loss_delay - self.dry_dt)
                # Proba conditionnelle doit se cumuler.
                if f.group_dus:
                    nb_dead = np.random.binomial(self.nb_dispersal_units, loss_rate)
                    self.nb_dispersal_units -= nb_dead                
                    if self.nb_dispersal_units == 0.:
                        self.disable()
                        return
                else:
                    if proba(loss_rate):
                        self.disable()
                        return                

    def set_nb_spores(self, nb_spores=0.):
        """ Set the number of spores in the DU.
        
        Parameters
        ----------
        nb_spores: int
            Number of spores in the DU forming the lesion
        """
        self.nb_spores = nb_spores
        
    def set_position(self, position=None):
        """ Set the position of the DU to position given in argument
            (force iterable to manage cohorts)
        """
        if position is not None and len(position) > 0 and not is_iterable(position[0]):
            self.position = [position]
        else:
            self.position = position

    def create_lesion(self, nb_lesions = 1, leaf = None, **kwds):
        if leaf is None:
            les = self.fungus.lesion(mutable = self.mutable)
            les.__dict__.update(kwds)
            self.disable()
            return les
        elif leaf.green_length>0 and nb_lesions>0:        
            les = self.fungus.lesion(mutable = self.mutable)
            les.__dict__.update(kwds)

            les.age_leaf_infection = leaf.complex_at_scale(4).age
            les.set_position([[leaf.length - np.random.random()*leaf.green_length, 0] 
                                for i in range(nb_lesions)])
            self.nb_dispersal_units -= nb_lesions
            if 'temperature_sequence' in kwds:
                temps = kwds['temperature_sequence']
                leaf.temperature_sequence = temps
                les.update(dt=len(temps), leaf=leaf)
            try:
                leaf.lesions.append(les)
            except:
                leaf.lesions = [les]
            self.disable()
        else:
            self.disable()
    
    def set_status(self, status = 'deposited'):
        self.status = status
        
    def set_nb_dispersal_units(self, nb_dispersal_units = 1):
        self.nb_dispersal_units = nb_dispersal_units
        
# Fungus parameters (e.g. .ini): config of the fungus #############################
septoria_parameters = dict(name='septoria',
                         INCUBATING = 0,
                         CHLOROTIC = 1,
                         NECROTIC = 2,
                         SPORULATING = 3,
                         EMPTY = 4,
                         delta_age_ring = 20.,
                         basis_for_dday = 0.,
                         temp_min = 0.,
                         temp_max = 25.,
                         wd_min = 10.,
                         proba_inf = 1.,
                         loss_delay = 120.,
                         rh_max=35.,
                         rh_min=35.,
                         degree_days_to_chlorosis = 160.,
                         degree_days_to_necrosis = 160.,
                         degree_days_to_sporulation = 50.,
                         sporulating_capacity = 1.,
                         epsilon = 0.001,
                         Smin = 0.03,
                         Smax = 0.3,
                         growth_rate = 0.0006,
                         rain_events_to_empty = 10,
                         production_rate = 100000,
                         threshold_spores = 1000,
                         density_dus_emitted_ref = 1.79e3,
                         reduction_by_rain = 0.0,
                         threshold_spo = 1e-4,
                         nb_rings_by_state = 10,
                         age_physio_switch_senescence=0.,
                         group_dus = False,
                         rh_effect = True,
                         apply_rh = 'all')
                 
# class SeptoriaParameters(Parameters):
    # model = None
    # def __init__(self,
                 # model=None,
                 # INCUBATING = 0,
                 # CHLOROTIC = 1,
                 # NECROTIC = 2,
                 # SPORULATING = 3,
                 # EMPTY = 4,
                 # DEAD = 5,
                 # delta_age_ring = 20.,
                 # basis_for_dday = -2.,
                 # temp_min = 10.,
                 # temp_max = 30.,
                 # wd_min = 10.,
                 # loss_rate = 1./120,
                 # degree_days_to_chlorosis = 220.,
                 # degree_days_to_necrosis = 110.,
                 # degree_days_to_sporulation = 20.,
                 # epsilon = 0.001,
                 # Smin = 0.03,
                 # Smax = 0.3,
                 # growth_rate = 0.0006,
                 # rh_min = 85.,
                 # rain_events_to_empty = 3,
                 # production_rate = 100000,
                 # threshold_spores = 1000,
                 # density_dus_emitted_ref = 1.79e3,
                 # reduction_by_rain = 0.5,
                 # threshold_spo = 1e-4,
                 # nb_rings_by_state = 10,
                 # age_physio_switch_senescence=1,
                 # *args, **kwds):
        # """ Parameters for septoria.
        
        # Parameters
        # ----------
        # model: model of lesion
            # Model of lesion among : "ContinuousSeptoria", "SeptoriaExchangingRings", 
            # "SeptoriaWithRings"
        # delta_age_ring: int
            # Time step in degree days to create a new ring
        # basis_for_dday: float
            # Basis temperature for the accumulation of degree days (degrees celsius)
        # temp_min: float
            # Minimal temperature for infection
        # temp_max: float
            # Maximal temperature for infection
        # wd_min: float
            # Minimal wetness duration for infection
        # loss_rate: float
            # Loss rate of dispersal units in 1 hour
        # degree_days_to_chlorosis: float
            # Thermal time between emergence and chlorosis
            # (i.e. incubation for the first rings)
        # degree_days_to_necrosis: float
            # Thermal time between chlorosis and necrosis
            # (i.e. incubation for the first rings)
        # degree_days_to_sporulation: float
            # Thermal time between necrosis and sporulation
        # epsilon: float
            # Initial size of incubating lesion (cm2)
        # Smin: float
            # Initial size of chlorotic lesion (cm2)
        # Smax: float
            # Lesion maximum size (cm2)
        # growth_rate: float
            # Lesion growth rate (cm2.dday-1)
        # rh_min: float
            # Minimal relative humidity for sporulation
        # production_rate: float
            # Number of spores produced by cm2 of new sporulating surface
        # treshold_spores: int
            # Number of spores left in stock to consider the lesion empty
        # rain_events_to_empty: int
            # Number of dispersal events required to empty a surface in sporulation
        # density_dus_emitted_ref: float
            # Reference value for the number of dispersal units emitted at each event by a cm2 of surface in sporulation
            # Used to calculate 'density_dus_emitted_max': list([int, int, int])
                # Maximal number of dispersal units emitted at each event by a cm2 of surface in sporulation.
                # Indexes in list refer to the number of rain events undergone by the surface in sporulation.
                # len(density_dus_emitted_max) = nb_dispersal_events_to_emtpy
        # reduction_by_rain: float
            # Reduction factor of number of dus emitted by cm2 of surface in sporulation after each rain event.
        # """
        # self.name = "septoria"
        # self.__class__.model = model
        # self.INCUBATING = INCUBATING
        # self.CHLOROTIC = CHLOROTIC
        # self.NECROTIC = NECROTIC
        # self.SPORULATING = SPORULATING
        # self.EMPTY = EMPTY
        # self.DEAD = DEAD
        # self.delta_age_ring = delta_age_ring
        # self.basis_for_dday = basis_for_dday
        # self.temp_min = temp_min
        # self.temp_max = temp_max
        # self.wd_min = wd_min
        # self.loss_rate = loss_rate
        # self.degree_days_to_chlorosis = degree_days_to_chlorosis
        # self.degree_days_to_necrosis = degree_days_to_necrosis
        # # TODO : Find value for parameters !!
        # self.degree_days_to_sporulation = degree_days_to_sporulation
        # self.epsilon = epsilon
        # self.Smin = Smin
        # self.Smax = Smax
        # self.growth_rate = growth_rate
        # self.rh_min = rh_min
        # self.rain_events_to_empty = rain_events_to_empty
        # self.production_rate = production_rate
        # # TODO : Improve this parameter. Very Sensitive.
        # self.threshold_spores = threshold_spores
        # # TODO : link values in list of density_dus_emitted_max to rain_events_to_empty
        # self.density_dus_emitted_max = np.zeros(rain_events_to_empty)
        # for ind in range(rain_events_to_empty):
            # self.density_dus_emitted_max[ind] = density_dus_emitted_ref*(reduction_by_rain**ind)
        # self.threshold_spo = threshold_spo
        # # Parameters for new model of septoria with age physio
        # self.nb_rings_by_state = nb_rings_by_state
        # self.age_physio_switch_senescence = age_physio_switch_senescence
        
    # def __call__(self, nb_spores=None, position=None):
        # model = self.model
        # if model.fungus is None:
            # model.fungus = self
        # if SeptoriaDU.fungus is None:
            # SeptoriaDU.fungus = self
        # return model(nb_spores=nb_spores, position=position)

# def septoria(**kwds):
    # return SeptoriaParameters(**kwds)
        
# class Disease(object):
    # name = 'septoria'

    # @classmethod
    # def parameters(cls, **kwds):
        # return septoria(**kwds)
    
    # @classmethod
    # def dispersal_unit(cls, **kwds):
        # SeptoriaDU.fungus=cls.parameters(**kwds)
        # return SeptoriaDU
           
# Useful functions ################################################################
def proba(p):
    """ Compute the occurence of an event according to p.

    Parameters
    ----------
    p : float
        Probability of the event in [0,1]
    
    Returns
    -------
    True or False
    """
    return random() < p

import collections        
def is_iterable(obj):
    """ Test if object is iterable """
    return isinstance(obj, collections.Iterable)
    
# Plugin function #################################################################
# Disease == Fungus !!!!!!

# def plugin_septoria(model='septoria_age_physio'):
    # diseases=plugin.discover('alep.disease')
    # try:
        # septoria = diseases[model].load()
    # except KeyError:
        # if model=='septoria_exchanging_rings':
            # from alinea.alep.septoria_exchanging_rings import Disease
        # elif model=='septoria_continuous':
            # from alinea.alep.septoria_continuous import Disease
        # elif model=='septoria_with_rings':
            # from alinea.alep.septoria_with_rings import Disease
        # elif model=='septoria_age_physio':
            # from alinea.alep.septoria_age_physio import Disease
        # septoria=Disease()
    # return septoria      

def plugin_septoria(model='septoria_age_physio'):
    diseases=plugin.discover('alep.disease')
    try:
        septoria = diseases[model].load()
    except KeyError:
        if model=='septoria_exchanging_rings':
            from alinea.alep.septoria_exchanging_rings import SeptoriaFungus
        elif model=='septoria_continuous':
            from alinea.alep.septoria_continuous import SeptoriaFungus
        elif model=='septoria_with_rings':
            from alinea.alep.septoria_with_rings import SeptoriaFungus
        elif model=='septoria_age_physio':
            from alinea.alep.septoria_age_physio import SeptoriaFungus
        septoria=SeptoriaFungus()
    return septoria  
    