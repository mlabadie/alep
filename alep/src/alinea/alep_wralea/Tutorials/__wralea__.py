
# This file has been generated at Thu May 23 14:27:34 2013

from openalea.core import *


__name__ = 'Alep.Tutorials'

__editable__ = True
__description__ = ''
__license__ = 'CeCILL-C'
__url__ = 'http://openalea.gforge.inria.fr'
__alias__ = []
__version__ = '0.8.0'
__authors__ = ''
__institutes__ = None
__icon__ = ''


__all__ = ['_365462160', '_353571664']



_365462160 = CompositeNodeFactory(name='theoric_tutorial_septoria',
                             description='This is what a dataflow of septoria should look like (except miss washing)',
                             category='Unclassified',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('Alep.Test_nodes', 'wheat'),
   3: ('openalea.data structure', 'int'),
   4: ('Alep.Test_nodes', 'distribute_dispersal_units'),
   5: ('openalea.data structure', 'int'),
   6: ('Alep.Models', 'NoPriorityGrowthControl'),
   7: ('Alep.Protocol', 'infect'),
   8: ('Alep.Protocol', 'update'),
   9: ('Alep.Protocol', 'disperse'),
   10: ('openalea.data structure', 'int'),
   11: ('Alep.Models', 'RandomDispersal'),
   12: ('openalea.data structure.string', 'string'),
   13: ('Alep.Test_nodes', 'scene_from_g'),
   14: ('openalea.flow control', 'pool setdefault'),
   15: ('Alep.Test_nodes', 'weather_reader'),
   16: ('openalea.data structure.string', 'string'),
   17: ('Alep.Test_nodes', 'microclimate'),
   18: ('Alep.Test_nodes', 'scene_from_g'),
   19: ('openalea.data structure', 'int'),
   20: ('Alinea.Echap.Tests_nodes', 'update_meteo_date'),
   21: ('openalea.flow control', 'annotation')},
                             elt_connections={  19061656: (20, 0, 17, 4),
   19061668: (17, 0, 7, 0),
   19061680: (19, 0, 17, 6),
   19061692: (14, 0, 18, 0),
   19061704: (18, 0, 17, 1),
   19061716: (16, 0, 15, 0),
   19061728: (15, 0, 17, 2),
   19061740: (2, 0, 4, 0),
   19061752: (6, 0, 8, 2),
   19061764: (14, 0, 17, 0),
   19061776: (8, 0, 13, 0),
   19061788: (7, 0, 8, 0),
   19061800: (5, 0, 4, 1),
   19061812: (13, 0, 9, 1),
   19061824: (12, 0, 9, 3),
   19061836: (3, 0, 8, 1),
   19061848: (4, 0, 14, 1),
   19061860: (11, 0, 9, 2),
   19061872: (8, 0, 9, 0),
   19061884: (10, 0, 7, 1)},
                             elt_data={  2: {  'block': False,
         'caption': 'wheat',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x14C6C3B0> : "wheat"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -169.91452131554934,
         'posy': -37.10000337541274,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': '1',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x14F77970> : "int"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 107.0141914386444,
         'posy': 243.19997846131056,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'distribute_dispersal_units',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x14C6C490> : "distribute_dispersal_units"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -128.11673935246137,
         'posy': 20.291590020079475,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': '10',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x14F77970> : "int"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -86.80525339980198,
         'posy': -38.003486191985274,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'NoPriorityGrowthControl',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x14FE9110> : "NoPriorityGrowthControl"',
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 130.11620716303764,
         'posy': 243.19997846131045,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'infect',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x150B85D0> : "infect"',
         'hide': True,
         'id': 7,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 50.02323884418219,
         'posy': 214.44112229694463,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   8: {  'block': False,
         'caption': 'update',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x150B85F0> : "update"',
         'hide': True,
         'id': 8,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 73.506968193459,
         'posy': 311.07199692139966,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'disperse',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x150B8610> : "disperse"',
         'hide': True,
         'id': 9,
         'lazy': False,
         'port_hide_changed': set(),
         'posx': 106.10008665633065,
         'posy': 423.1946821961434,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': '1',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14F77970> : "int"',
          'hide': True,
          'id': 10,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 111.13670269753959,
          'posy': 156.67452196878233,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   11: {  'block': False,
          'caption': 'RandomDispersal',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14FE92D0> : "RandomDispersal"',
          'hide': True,
          'id': 11,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 231.7184738650594,
          'posy': 350.9975022228184,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   12: {  'block': False,
          'caption': '\'"septoria"\'',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14F86E90> : "string"',
          'hide': True,
          'id': 12,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 329.3710927859301,
          'posy': 351.009385175146,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   13: {  'block': False,
          'caption': 'scene_from_g',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14C6C3F0> : "scene_from_g"',
          'hide': True,
          'id': 13,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': 148.27723043416086,
          'posy': 350.976063616483,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   14: {  'block': False,
          'caption': 'g',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x13110470> : "pool setdefault"',
          'hide': True,
          'id': 14,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -92.01882467078107,
          'posy': 58.57159409380556,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   15: {  'block': False,
          'caption': 'weather_reader',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14C6C430> : "weather_reader"',
          'hide': True,
          'id': 15,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 114.99101469039701,
          'posy': 79.88838185418388,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   16: {  'block': False,
          'caption': '\'"weather_file"\'',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14F86E90> : "string"',
          'hide': True,
          'id': 16,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 117.00713632610868,
          'posy': 48.46867828452781,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   17: {  'block': False,
          'caption': 'microclimate',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14C6C450> : "microclimate"',
          'hide': True,
          'id': 17,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': 13.283884653755273,
          'posy': 156.11970547432756,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   18: {  'block': False,
          'caption': 'scene_from_g',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14C6C3F0> : "scene_from_g"',
          'hide': True,
          'id': 18,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': 32.81513954963852,
          'posy': 80.58263703155824,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   19: {  'block': False,
          'caption': '1',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14F77970> : "int"',
          'hide': True,
          'id': 19,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 324.50288428562413,
          'posy': 79.76800923300915,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   20: {  'block': False,
          'caption': 'update_meteo_date',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x14C8C0F0> : "update_meteo_date"',
          'hide': True,
          'id': 20,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 208.59556159669532,
          'posy': 80.58633219497332,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   21: {  'factory': '<openalea.core.node.NodeFactory object at 0x13110290> : "annotation"',
          'id': 21,
          'posx': 8.148264124870963,
          'posy': 21.185486724664376,
          'txt': u'Simulation loop'},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [(0, "'adel_mtg2'")],
   3: [(0, '1')],
   4: [  (2, "'powdery_mildew'"),
         (  3,
            '<alinea.alep.inoculation.RandomInoculation instance at 0x15856E40>')],
   5: [(0, '10')],
   6: [],
   7: [(2, 'None'), (3, "'LeafElement'"), (4, 'True')],
   8: [(0, 'None'), (3, 'None'), (4, "'LeafElement'"), (5, 'True')],
   9: [(4, "'LeafElement'"), (5, 'True')],
   10: [(0, '1')],
   11: [],
   12: [(0, '\'"septoria"\'')],
   13: [],
   14: [(0, "'g'")],
   15: [],
   16: [(0, '\'"weather_file"\'')],
   17: [  (  3,
             '<alinea.echap.microclimate_leaf.MicroclimateLeaf instance at 0x158E3288>'),
          (5, "'LeafElement'")],
   18: [],
   19: [(0, '1')],
   20: [(0, '1'), (1, "'2000-10-01 01:00:00'")],
   21: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {'position': [-169.91452131554934, -37.10000337541274], 'userColor': None, 'useUserColor': False},
   3: {'position': [107.0141914386444, 243.19997846131056], 'userColor': None, 'useUserColor': False},
   4: {'position': [-128.11673935246137, 20.291590020079475], 'userColor': None, 'useUserColor': False},
   5: {'position': [-86.80525339980198, -38.003486191985274], 'userColor': None, 'useUserColor': False},
   6: {'position': [130.11620716303764, 243.19997846131045], 'userColor': None, 'useUserColor': False},
   7: {'position': [50.02323884418219, 214.44112229694463], 'userColor': None, 'useUserColor': False},
   8: {'position': [73.506968193459, 311.07199692139966], 'userColor': None, 'useUserColor': False},
   9: {'position': [106.10008665633065, 423.1946821961434], 'userColor': None, 'useUserColor': False},
   10: {'position': [111.13670269753959, 156.67452196878233], 'userColor': None, 'useUserColor': False},
   11: {'position': [231.7184738650594, 350.9975022228184], 'userColor': None, 'useUserColor': False},
   12: {'position': [329.3710927859301, 351.009385175146], 'userColor': None, 'useUserColor': False},
   13: {'position': [148.27723043416086, 350.976063616483], 'userColor': None, 'useUserColor': False},
   14: {'position': [-92.01882467078107, 58.57159409380556], 'userColor': None, 'useUserColor': False},
   15: {'useUserColor': False, 'position': [114.99101469039701, 79.88838185418388], 'userColor': None},
   16: {'useUserColor': False, 'position': [117.00713632610868, 48.46867828452781], 'userColor': None},
   17: {'useUserColor': False, 'position': [13.283884653755273, 156.11970547432756], 'userColor': None},
   18: {'useUserColor': False, 'position': [32.81513954963852, 80.58263703155824], 'userColor': None},
   19: {'useUserColor': False, 'position': [324.50288428562413, 79.76800923300915], 'userColor': None},
   20: {'position': [208.59556159669532, 80.58633219497332], 'userColor': None, 'useUserColor': False},
   21: {'visualStyle': 1, 'position': [8.148264124870963, 21.185486724664376], 'color': None, 'text': u'Simulation loop', 'textColor': None, 'rectP2': (391.004697057272, 439.9873383059811)},
   '__in__': {'position': [0, 0], 'userColor': None, 'useUserColor': True},
   '__out__': {'position': [0, 0], 'userColor': None, 'useUserColor': True}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_353571664 = CompositeNodeFactory(name='tutorial_powdery_mildew_draft',
                             description='First draft to simulate powdery mildew on wheat',
                             category='category test',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('Alep.Test_nodes', 'wheat'),
   3: ('Alep.Test_nodes', 'set_properties_node'),
   4: ('openalea.data structure.dict', 'dict'),
   5: ('Alep.Test_nodes', 'distribute_dispersal_units'),
   6: ('openalea.data structure', 'int'),
   7: ('Alep.Models', 'NoPriorityGrowthControl'),
   8: ('Alep.Test_nodes', 'set_properties_node'),
   9: ('openalea.data structure.dict', 'dict'),
   10: ('Alep.Protocol', 'infect'),
   11: ('Alep.Protocol', 'update'),
   12: ('Alep.Protocol', 'disperse'),
   13: ('openalea.data structure', 'int'),
   14: ('Alep.Models', 'RandomDispersal'),
   15: ('openalea.data structure.string', 'string'),
   16: ('Alep.Test_nodes', 'scene_from_g'),
   17: ('openalea.flow control', 'annotation'),
   18: ('openalea.python method', 'eval'),
   19: ('openalea.python method', 'eval'),
   20: ('openalea.flow control', 'iter'),
   21: ('openalea.flow control', 'pool setdefault'),
   23: ('openalea.flow control', 'iter')},
                             elt_connections={  20306968: (15, 0, 12, 3),
   20306980: (4, 0, 3, 2),
   20306992: (7, 0, 11, 2),
   20307004: (20, 0, 10, 4),
   20307016: (11, 0, 12, 0),
   20307028: (3, 0, 5, 0),
   20307040: (2, 0, 3, 0),
   20307052: (5, 0, 8, 0),
   20307064: (21, 0, 10, 0),
   20307076: (19, 0, 20, 0),
   20307088: (6, 0, 5, 1),
   20307100: (14, 0, 12, 2),
   20307112: (16, 0, 12, 1),
   20307124: (9, 0, 8, 2),
   20307136: (10, 0, 11, 0),
   20307148: (8, 0, 21, 1),
   20307172: (23, 0, 11, 5),
   20307184: (11, 0, 16, 0),
   20307196: (13, 0, 11, 1),
   20307208: (13, 0, 10, 1),
   20307220: (18, 0, 23, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'wheat',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x071BBD90> : "wheat"',
         'hide': True,
         'id': 2,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -64.12718287457903,
         'posy': -137.0236964308275,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   3: {  'block': False,
         'caption': 'set_properties_node',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x071BBDD0> : "set_properties_node"',
         'hide': True,
         'id': 3,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -59.47200198324889,
         'posy': -104.37494152168192,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   4: {  'block': False,
         'caption': 'dict',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x088010F0> : "dict"',
         'hide': True,
         'id': 4,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 13.944303570971968,
         'posy': -135.01835381289874,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   5: {  'block': False,
         'caption': 'distribute_dispersal_units',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x071BBE50> : "distribute_dispersal_units"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -39.24283092615882,
         'posy': -53.89214534907848,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': '10',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x07C752B0> : "int"',
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 95.08360729950847,
         'posy': -121.91094687099283,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   7: {  'block': False,
         'caption': 'NoPriorityGrowthControl',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x07CFF5D0> : "NoPriorityGrowthControl"',
         'hide': True,
         'id': 7,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 132.48964624818092,
         'posy': 220.30146830782957,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   8: {  'block': False,
         'caption': 'set_properties_node',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x071BBDD0> : "set_properties_node"',
         'hide': True,
         'id': 8,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': -29.72953347337817,
         'posy': 37.43577298463505,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   9: {  'block': False,
         'caption': 'dict',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x088010F0> : "dict"',
         'hide': True,
         'id': 9,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 67.28910864785185,
         'posy': -3.865355676956611,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'infect',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x0C672890> : "infect"',
          'hide': True,
          'id': 10,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': 0.31364761819369136,
          'posy': 201.21563194488053,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   11: {  'block': False,
          'caption': 'update',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x0C672870> : "update"',
          'hide': True,
          'id': 11,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': 24.759960955987026,
          'posy': 259.34314702867994,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   12: {  'block': False,
          'caption': 'disperse',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x0C672830> : "disperse"',
          'hide': True,
          'id': 12,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': 87.19318306286668,
          'posy': 424.407951671825,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   13: {  'block': False,
          'caption': '1',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x07C752B0> : "int"',
          'hide': True,
          'id': 13,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 50.216179730665075,
          'posy': 74.67003963046031,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   14: {  'block': False,
          'caption': 'RandomDispersal',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x07CFF790> : "RandomDispersal"',
          'hide': True,
          'id': 14,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 146.39327506396464,
          'posy': 298.1175694449287,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   15: {  'block': False,
          'caption': '\'"powdery_mildew"\'',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x07C86AD0> : "string"',
          'hide': True,
          'id': 15,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 245.32083688088994,
          'posy': 298.4853444481432,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   16: {  'block': False,
          'caption': 'scene_from_g',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x071BBDF0> : "scene_from_g"',
          'hide': True,
          'id': 16,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': 62.95203163306603,
          'posy': 297.3220457467305,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   17: {  'factory': '<openalea.core.node.NodeFactory object at 0x07074070> : "annotation"',
          'id': 17,
          'posx': -98.80968254968715,
          'posy': 154.45008631553037,
          'txt': u'To loop'},
   18: {  'block': False,
          'caption': 'eval',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x083BD290> : "eval"',
          'hide': True,
          'id': 18,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 270.2846884830301,
          'posy': 126.67934311308245,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   19: {  'block': False,
          'caption': 'eval',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x083BD290> : "eval"',
          'hide': True,
          'id': 19,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 157.45191712092839,
          'posy': 51.030098677127896,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   20: {  'block': False,
          'caption': 'iter',
          'delay': 1,
          'factory': '<openalea.core.node.NodeFactory object at 0x07074170> : "iter"',
          'hide': True,
          'id': 20,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 159.18548324675922,
          'posy': 85.05133389655823,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   21: {  'block': False,
          'caption': 'g',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0x07074250> : "pool setdefault"',
          'hide': True,
          'id': 21,
          'lazy': False,
          'port_hide_changed': set(),
          'posx': -54.72455110922016,
          'posy': 97.4889252517754,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   23: {  'block': False,
          'caption': 'iter',
          'delay': 1,
          'factory': '<openalea.core.node.NodeFactory object at 0x07074170> : "iter"',
          'hide': True,
          'id': 23,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 272.01825460886096,
          'posy': 160.7005783325128,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 0,
                'posy': 0,
                'priority': 0,
                'use_user_color': True,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 0,
                 'posy': 0,
                 'priority': 0,
                 'use_user_color': True,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  2: [(0, "'adel_mtg2'")],
   3: [(1, "'LeafElement'")],
   4: [  (  0,
            "{'healthy_surface': 5.0, 'age': 0.0, 'position_senescence': None, 'surface': 5.0}")],
   5: [(2, "'powdery_mildew'")],
   6: [(0, '10')],
   7: [],
   8: [(1, "'LeafElement'")],
   9: [  (  0,
            "{'rain_duration': 0.0, 'wind_speed': 0.2, 'temp': 22.0, 'wetness': True, 'rain_intensity': 0.0, 'relative_humidity': 85.0, 'age': 1}")],
   10: [(1, '1'), (2, 'None'), (3, "'LeafElement'")],
   11: [(3, 'None'), (4, "'LeafElement'")],
   12: [(4, "'LeafElement'"), (5, 'True')],
   13: [(0, '1')],
   14: [],
   15: [(0, '\'"powdery_mildew"\'')],
   16: [],
   17: [],
   18: [(0, "'[0]*5+[1]*15'")],
   19: [(0, "'[0,1,1,1,0,0,0,1,1,1]*5'")],
   20: [],
   21: [(0, "'g'")],
   23: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  2: {  'position': [-64.12718287457903, -137.0236964308275],
         'useUserColor': False,
         'userColor': None},
   3: {  'position': [-59.47200198324889, -104.37494152168192],
         'useUserColor': False,
         'userColor': None},
   4: {  'position': [13.944303570971968, -135.01835381289874],
         'useUserColor': False,
         'userColor': None},
   5: {  'position': [-39.24283092615882, -53.89214534907848],
         'useUserColor': False,
         'userColor': None},
   6: {  'position': [95.08360729950847, -121.91094687099283],
         'useUserColor': False,
         'userColor': None},
   7: {  'position': [132.48964624818092, 220.30146830782957],
         'useUserColor': False,
         'userColor': None},
   8: {  'position': [-29.72953347337817, 37.43577298463505],
         'useUserColor': False,
         'userColor': None},
   9: {  'position': [67.28910864785185, -3.865355676956611],
         'useUserColor': False,
         'userColor': None},
   10: {  'position': [0.31364761819369136, 201.21563194488053],
          'useUserColor': False,
          'userColor': None},
   11: {  'position': [24.759960955987026, 259.34314702867994],
          'useUserColor': False,
          'userColor': None},
   12: {  'position': [87.19318306286668, 424.407951671825],
          'useUserColor': False,
          'userColor': None},
   13: {  'position': [50.216179730665075, 74.67003963046031],
          'useUserColor': False,
          'userColor': None},
   14: {  'position': [146.39327506396464, 298.1175694449287],
          'useUserColor': False,
          'userColor': None},
   15: {  'position': [245.32083688088994, 298.4853444481432],
          'useUserColor': False,
          'userColor': None},
   16: {  'position': [62.95203163306603, 297.3220457467305],
          'useUserColor': False,
          'userColor': None},
   17: {  'color': None,
          'position': [-98.80968254968715, 154.45008631553037],
          'rectP2': (466.78093257249276, 320.11626652763243),
          'text': u'To loop',
          'textColor': None,
          'visualStyle': 1},
   18: {  'position': [270.2846884830301, 126.67934311308245],
          'useUserColor': False,
          'userColor': None},
   19: {  'position': [157.45191712092839, 51.030098677127896],
          'useUserColor': False,
          'userColor': None},
   20: {  'position': [159.18548324675922, 85.05133389655823],
          'useUserColor': False,
          'userColor': None},
   21: {  'position': [-54.72455110922016, 97.4889252517754],
          'useUserColor': False,
          'userColor': None},
   22: {  'position': [77.637457363799, 484.9776116285419],
          'useUserColor': False,
          'userColor': None},
   23: {  'position': [272.01825460886096, 160.7005783325128],
          'useUserColor': False,
          'userColor': None},
   '__in__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None},
   '__out__': {  'position': [0, 0], 'useUserColor': True, 'userColor': None}},
                             lazy=True,
                             eval_algo='DiscreteTimeEvaluation',
                             )




