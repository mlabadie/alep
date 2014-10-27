"""

Run annual loop for the model of septoria in alep on the basis of 'annual_loop_decomposed' in echap

"""
import pandas
try:
    import cPickle as pickle
except:
    import pickle
import sys

# Imports for wheat and rain/light interception
from alinea.adel.newmtg import move_properties, adel_ids
from alinea.echap.architectural_reconstructions import EchapReconstructions
from alinea.alep.architecture import set_properties, update_healthy_area, get_leaves
from alinea.caribu.caribu_star import rain_and_light_star

# Imports for weather
from alinea.alep.alep_weather import wetness_rapilly, linear_degree_days
from alinea.alep.alep_time_control import *
from alinea.astk.TimeControl import *
from alinea.echap.weather_data import *
import alinea.septo3d
import alinea.alep
from openalea.deploy.shared_data import shared_data
from alinea.astk.Weather import Weather

# Imports for alep septoria
from alinea.alep.protocol import *
from alinea.alep.septoria import plugin_septoria
from alinea.septo3d.dispersion.alep_interfaces import SoilInoculum, Septo3DSoilContamination
from alinea.popdrops.alep_interface import PopDropsEmission, PopDropsTransport
from alinea.alep.growth_control import PriorityGrowthControl
from alinea.alep.infection_control import BiotrophDUPositionModel
from alinea.alep.disease_outputs import initiate_all_adel_septo_recorders, plot_severity_by_leaf, save_image

def get_weather(start_date="2010-10-15 12:00:00", end_date="2011-06-20 01:00:00"):
    """ Get weather data for simulation. """
    start = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    if start.year >= 2010:
        filename = 'Boigneville_0109'+str(start.year)+'_3108'+str(end.year)+'_h.csv'
        meteo_path = shared_data(alinea.echap, filename)
        weather = Weather(meteo_path, reader = arvalis_reader)
        weather.check(['temperature_air', 'PPFD', 'relative_humidity',
                       'wind_speed', 'rain', 'global_radiation', 'vapor_pressure'])
        notation_dates_file = shared_data(alinea.alep, 'notation_dates/notation_dates_'+str(end.year)+'.csv')
        weather.check(varnames=['notation_dates'], models={'notation_dates':add_notation_dates}, notation_dates_file = notation_dates_file)
    else:
        start_yr = str(start.year)[2:4]
        end_yr = str(end.year)[2:4]
        filename = 'meteo'+ start_yr + '-' + end_yr + '.txt'
        meteo_path = shared_data(alinea.septo3d, filename)
        weather = Weather(data_file=meteo_path)
    weather.check(varnames=['wetness'], models={'wetness':wetness_rapilly})
    weather.check(varnames=['degree_days'], models={'degree_days':linear_degree_days}, start_date=start_date, base_temp=0., max_temp=30.)
    weather.check(varnames=['septo_degree_days'], models={'septo_degree_days':linear_degree_days}, start_date=start_date, base_temp=0., max_temp=25.)
    return weather

def setup(start_date="2010-10-15 12:00:00", end_date="2011-06-20 01:00:00", variety='Mercia', nplants = 30, nsect = 7, disc_level = 5):
    """ Get plant model, weather data and set scheduler for simulation. """
    # Initialize wheat plant
    reconst = EchapReconstructions()
    adel = reconst.get_reconstruction(name=variety, nplants = nplants, nsect = nsect, disc_level = disc_level, aspect = 'line')

    # Manage weather
    weather = get_weather(start_date = start_date, end_date = end_date)
    
    # Define the schedule of calls for each model
    seq = pandas.date_range(start = start_date, end = end_date, freq='H')
    TTmodel = DegreeDayModel(Tbase = 0)
    every_dd = thermal_time_filter(seq, weather, TTmodel, delay = 10)
    every_rain = rain_filter(seq, weather)
    every_dd_or_rain = filter_or([every_dd, every_rain])
    canopy_timing = IterWithDelays(*time_control(seq, every_dd_or_rain, weather.data))
    septo_filter = septo_infection_filter(seq, weather, every_rain)
    rain_timing = IterWithDelays(*time_control(seq, every_rain, weather.data))
    septo_timing = CustomIterWithDelays(*time_control(seq, septo_filter, weather.data), eval_time='end')
    return adel, weather, seq, rain_timing, canopy_timing, septo_timing

def septo_disease(adel, sporulating_fraction, layer_thickness, **kwds):
    """ Choose models to assemble the disease model. """
    domain = adel.domain
    domain_area = adel.domain_area
    fungus = plugin_septoria()
    fungus.parameters(group_dus=True, nb_rings_by_state=1, **kwds)
    inoculum = SoilInoculum(fungus, sporulating_fraction=sporulating_fraction, domain_area=domain_area)
    contaminator = Septo3DSoilContamination(domain=domain, domain_area=domain_area)
    growth_controler = PriorityGrowthControl()
    infection_controler = BiotrophDUPositionModel()
    emitter = PopDropsEmission(domain=domain)
    transporter = PopDropsTransport(domain = domain, domain_area = domain_area, dh = layer_thickness)
    return inoculum, contaminator, infection_controler, growth_controler, emitter, transporter
   
def make_canopy(start_date = "2010-10-15 12:00:00", end_date = "2011-06-20 01:00:00", variety = 'Mercia',
                nplants = 30, nsect = 7, disc_level = 5, dir = './adel/mercia_2011_30pl_7sect'):
    """ Simulate and save canopy (prior to simulation). """
    adel, weather, seq, rain_timing, canopy_timing, septo_timing = setup(start_date = start_date,
        end_date = end_date, variety = variety, nplants = nplants, nsect = nsect, disc_level = disc_level)
    
    domain = adel.domain
    convUnit = adel.convUnit
    g = adel.setup_canopy(age=0.)
    rain_and_light_star(g, light_sectors = '1', domain=domain, convUnit=convUnit)
    it_wheat = 0
    adel.save(g, it_wheat, dir=dir)
    for i, controls in enumerate(zip(canopy_timing, septo_timing)):
        canopy_iter, septo_iter = controls
        if canopy_iter:
            it_wheat += 1
            g = adel.grow(g, canopy_iter.value)
            rain_and_light_star(g, light_sectors = '1', domain=domain, convUnit=convUnit)
            adel.save(g, it_wheat, dir=dir)

def run_disease(start_date = "2010-10-15 12:00:00", end_date = "2011-06-20 01:00:00", variety = 'Mercia', nplants = 30, nsect = 7,
                disc_level = 5, dir = './adel/mercia_2011_30pl_7sect', sporulating_fraction = 1e-3, layer_thickness = 0.1, 
                adel = None, weather = None, seq = None, rain_timing = None, canopy_timing = None, septo_timing = None, **kwds):
    """ Simulate epidemics. """
    if any(x==None for x in [adel, weather, seq, rain_timing, canopy_timing, septo_timing]):
        adel, weather, seq, rain_timing, canopy_timing, septo_timing = setup(start_date = start_date,
            end_date = end_date, variety = variety, nplants = nplants, nsect = nsect, disc_level = disc_level)
            
    if 'alinea.alep.septoria_age_physio' in sys.modules:
        del(sys.modules['alinea.alep.septoria_age_physio'])
    inoculum, contaminator, infection_controler, growth_controler, emitter, transporter = septo_disease(adel, sporulating_fraction, layer_thickness, **kwds)
    it_wheat = 0
    it_septo = 0
    g,TT = adel.load(it_wheat, dir=dir)
    
    # Prepare saving of outputs
    recorders = initiate_all_adel_septo_recorders(g, nsect)
    
    for i, controls in enumerate(zip(canopy_timing, rain_timing, septo_timing)):
        canopy_iter, rain_iter, septo_iter = controls
        
        # Grow wheat canopy
        if canopy_iter:
            it_wheat += 1
            newg,TT = adel.load(it_wheat, dir=dir)
            move_properties(g, newg)
            g = newg
            leaf_ids = adel_ids(g)
        
        # Get weather for date and add it as properties on leaves
        if septo_iter:
            set_properties(g,label = 'LeafElement',
                           temperature_sequence = septo_iter.value.temperature_air,
                           wetness = septo_iter.value.wetness.mean(),
                           relative_humidity = septo_iter.value.relative_humidity.mean())
        if rain_iter:
            set_properties(g,label = 'LeafElement',
                           rain_intensity = rain_iter.value.rain.mean(),
                           rain_duration = len(rain_iter.value.rain) if rain_iter.value.rain.sum() > 0 else 0.)

        # External contamination
        geom = g.property('geometry')
        if rain_iter and len(geom)>0:
            if rain_iter.value.rain.mean()>0.:
                g = external_contamination(g, inoculum, contaminator, rain_iter.value)

        # Develop disease (infect for dispersal units and update for lesions)
        if septo_iter:
            infect(g, septo_iter.dt, infection_controler, label='LeafElement')
            update(g, septo_iter.dt, growth_controler, senescence_model=None, label='LeafElement')
            
        # Disperse and wash
        if rain_iter and len(geom)>0:
            if rain_iter.value.rain.mean()>0.:
                g = disperse(g, emitter, transporter, "septoria", label='LeafElement', weather_data=rain_iter.value)
        
        # if canopy_iter:
            # scene = plot_severity_by_leaf(g)
            # if it_wheat < 10 :
                # image_name='./images_septo_mercia/image0000%d.png' % it_wheat
            # elif it_wheat < 100 :
                # image_name='./images_septo_mercia/image000%d.png' % it_wheat
            # elif it_wheat < 1000 :
                # image_name='./images_septo_mercia/image00%d.png' % it_wheat
            # elif it_wheat < 10000 :
                # image_name='./images_septo_mercia/image0%d.png' % it_wheat
            # else :
                # image_name='./images_septo_mercia/image%d.png' % it_wheat
            # save_image(scene, image_name=image_name)

        # Save outputs
        if septo_iter:
            date = septo_iter.value.index[-1]
            for plant in recorders:
                deads = []
                for lf, recorder in recorders[plant].iteritems():
                    recorder.update_vids_with_labels(adel_ids = leaf_ids)
                    recorder.record(g, date, degree_days = septo_iter.value.degree_days[-1])
                    if recorder.date_death != None and recorder.leaf_green_area[-1]!=0:
                        deads += [s for s in lf.split() if s.isdigit()]
                if len(deads) > 0:
                    map(lambda x: recorders[plant][x].inactivate(date), map(lambda x: 'F%d' % x, range(1, min(deads)+1)))
                    
    for plant in recorders:
        for recorder in recorders[plant].itervalues():
            recorder.get_complete_dataframe()
            recorder.get_normalized_audpc(variable='necrosis_percentage')
            recorder.get_audpc(variable='necrosis_percentage')
            
    return g, recorders

def stat_profiler(call='run_disease()'):
    import cProfile
    import pstats
    cProfile.run(call, 'restats')
    return pstats.Stats('restats')