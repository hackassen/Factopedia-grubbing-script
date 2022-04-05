

'''
    !!! написать мануал к этим настройкам
'''
# boolean fields regex
bool_YES_regex=['^[Yy]es$', '^Y$']
bool_NO_regex=['^[Nn]o$', '^N$']



value_proc_settings={
    'Numeric keypad':{'bool':True},
    'On-board graphics adapter':{'bool':True},
    'Front camera':{'bool':True},
    'Bluetooth':{'bool':True},
    'Discrete graphics adapter':{'bool':True},
    'Built-in microphone':{'bool':True},
    'Card reader integrated':{'bool':True},
    'Touchscreen':{'bool':True},
    'Ethernet LAN':{'bool':True},
    'LED backlight':{'bool':True},
    'Combo headphone/mic port':{'bool':True},
    'Wi-Fi':{'bool':True},
    'Combo headphone/mic port':{'bool':True},
    'Combo headphone/mic port':{'bool':True},
    'Combo headphone/mic port':{'bool':True},
    'Combo headphone/mic port':{'bool':True},
    'Combo headphone/mic port':{'bool':True},

    
    'Display diagonal':{'reg':'([0-9\,\.]+)\s?inch', 'precision': 1},
    'Release date':{'reg':'([0-9]{4})', 'precision': 0},    
    'Internal memory':{'reg':'([0-9]+)\s?GB', 'precision': 0},
    'Total storage capacity':{'reg':'([0-9]+)\s?GB', 'precision': 0},    
    'Depth':{'reg':'([0-9\.]+)\s?mm', 'precision': 1},
    'Width':{'reg':'([0-9\.]+)\s?mm', 'precision': 1},
    'Height':{'reg':'([0-9\.]+)\s?mm', 'precision': 1},
    'Processor cache':{'reg':'([0-9]+)\s?MB', 'precision': 0},
    'Wi-Fi standards': {'reg':'([a-zA-Z\-\(\)\s0-9\.]+)', 'list':True, 'unique':True},    
    'Weight':{'reg':'([0-9\.]+)\s?[Kk]g', 'precision': 2},    
    'Processor frequency':{'reg':'([0-9\.]+)\s?GHz', 'precision': 1},
    'Processor boost frequency':{'reg':'([0-9\.]+)\s?GHz', 'precision': 1},
    'AC adapter power':{'reg':'([0-9\,\.]+)\s?[Ww]', 'precision': 0},
    'SSD capacity':{'reg':'([0-9]+)\s?GB', 'precision': 0},    
    'Operating system architecture':{'reg':'([0-9]{1:2})\s?', 'precision': 0},
    'Memory clock speed':{'reg':'([0-9\,]+)\s?MHz', 'precision': 0},
    'Processor lithography':{'reg':'([0-9]+)\s?nm', 'precision': 0},

    
    'Display diagonal':{'reg':'([0-9\,\.]+)\s?inch', 'precision': 1},
    'Display diagonal':{'reg':'([0-9\,\.]+)\s?inch', 'precision': 1},
    'Display diagonal':{'reg':'([0-9\,\.]+)\s?inch', 'precision': 1},


    
    #'Country':            {'reg':'([^\(\)]+)'},
    #'HDI':            {'reg':'(0\.[0-9]+)',     'precision':3},
    #'Official language(s)':            {'reg':'([\[\(]?[a-zA-Z]+[\]\)]?)', 'list':True, 'unique':True, 'repl':'([\[\(][^\)\]]+?[\]\)])|(and)|(\\xa0\w+)', 'replto':''},    
    'Max cruise speed': {'reg':'([0-9\,]+)\s?Km/h', 'precision': 0},
    'Approach speed': {'reg':'([0-9\,]+)\s?knots', 'precision': 0, 'MultK': 1.852},
    'Travel range': {'reg':'([0-9\,]+)\s?Kilometers', 'precision': 0},
    'Fuel economy': {'reg':'([0-9\,\.]+)\s?kilometres\s/\slitre', 'precision': 3},
    'Service ceiling': {'reg':'([0-9\,]+)\s?feet', 'precision': 0, 'MultK': 0.3048},
    'Rate of climb': {'reg':'([0-9\,\.]+)\s?metre\s/\ssecond', 'precision': 2},
    'Take off distance': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 0},
    'Landing distance': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 0},
    'Max take off weight': {'reg':'([0-9\,\.]+)\s?Kg', 'precision': 0},
    'Max landing weight': {'reg':'([0-9\,\.]+)\s?Kg', 'precision': 0},
    'Max payload': {'reg':'([0-9\,\.]+)\s?Kg', 'precision': 0},
    'Fuel tank capacity': {'reg':'([0-9\,\.]+)\s?litre', 'precision': 0},
    'Baggage volume': {'reg':'([0-9\,\.]+)\s?m3', 'precision': 2},
    'Seats': {'reg':'([0-9]+)', 'precision': 0},
    'Seats - business class': {'reg':'([0-9]+)', 'precision': 0},
    'Seats - first class': {'reg':'([0-9]+)', 'precision': 0},
    'Cabin height': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 2},
    'Cabin width': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 2},
    'Cabin length': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 2},
    'Exterior length': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 2},
    'Tail height': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 2},
    'Fuselage diameter': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 2},
    'Wing span': {'reg':'([0-9\,\.]+)\s?metre', 'precision': 2},
    'Manufactured from': {'reg':'([0-9]{4})'},
    'Manufactured to': {'reg':'([0-9]{4})'},
        
   
    }

