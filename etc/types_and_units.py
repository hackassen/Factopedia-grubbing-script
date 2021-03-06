'''
    units for properties
'''

units={

    'Product code':['text', ''],
    'Model':['text', ''],
    'Part number':['text', ''],
    'Brand':['text', ''],
    'Model name':['text', ''],
    'Display diagonal':['dec', 'inch'],
    'Release date':['int', 'year'],
    'Form factor':['text', ''],
    'Internal memory':['int', 'GB'],
    'Maximum internal memory':['text', ''],
    'Total storage capacity':['int', 'GB'],
    'Storage media':['text', ''],
    'Processor family':['text', ''],
    'Processor model':['text', '']    ,
    'Processor (link)':['object', ''],
    'Discrete graphics adapter model (link)':['object', '']    ,
    'Depth':['dec', 'mm'],
    'Width':['dec', 'mm'],
    'Height':['dec', 'mm'],
    'Numeric keypad':['bool', ''],
    'On-board graphics adapter':['bool', ''],
    'Processor cores':['int', ''],
    'On-board graphics adapter model':['text', ''],
    'Operating system installed':['text', ''],
    'Front camera':['bool', ''],
    'Processor cache':['int', 'MB'],
    'Internal memory type':['text', ''],
    'Bluetooth':['bool', ''],
    'Discrete graphics adapter':['bool', ''],
    'Display resolution':['text', ''],
    'Wi-Fi standards':['array', ''],
    'Pointing device':['text', ''],
    'Discrete graphics adapter model':['text', ''],
    'Weight':['dec', 'kg'],
    'Built-in microphone':['bool', ''],
    'Card reader integrated':['bool', ''],
    'Processor frequency':['dec', 'GHz'],
    'Touchscreen':['bool', ''],
    'Ethernet LAN':['bool', ''],
    'Processor boost frequency':['dec', 'GHz'],
    'Family':['text', ''],
    'Product colour':['text', ''],
    'HD type':['text', ''],
    'LED backlight':['bool', ''],
    'HDMI ports quantity':['int', ''],
    'Combo headphone/mic port':['bool', ''],
    'AC adapter power':['dec', 'W'],
    'Number of SSDs installed':['int', ''],
    'Bluetooth version':['text', ''],
    'SSD capacity':['dec', 'GB'],
    'Operating system architecture':['int', 'bit'],
    'Wi-Fi':['bool', ''],
    'Memory clock speed':['int', 'MHz'],
    'Processor threads':['int', ''],
    'Processor lithography':['int', 'nm'],
    'Cable lock slot':['bool', ''],
    'Ethernet LAN data rates':['array', 'Mbit/s'],
    'On-board graphics adapter base frequency':['dec', 'MHz'],
    'Battery capacity (Watt-hours)':['dec', 'Wh'],
    'Battery capacity':['int', 'mAh'],
    'Password protection':['bool', ''],
    'Front camera HD type':['text', ''],
    'Processor socket':['text', ''],
    'Speaker power':['dec', 'W'],
    'Processor manufacturer':['text', ''],
    'Maximum on-board graphics adapter memory':['int', 'GB'],
    'Keyboard backlit':['bool', ''],
    'Panel type':['text', ''],
    'USB 3.x Type-A ports':['int', ''],
    'USB 3.x Type-C ports':['int', ''],
    'USB Type-C Thunderbolt 3 ports',
    'USB 2.0 ports':['int', ''],
    'USB 2.0 Type-C ports':['int', ''],
    'USB Sleep-and-Charge':['bool', ''],
    'Front camera resolution':['text', ''],
    'Discrete graphics adapter memory':['int', 'GB'],
    '4G':['bool', ''],
    '3G':['bool', ''],
    'Fingerprint reader':['bool', ''],
    'Battery life (max)':['dec', 'h'],
    'Discrete graphics memory type':['text', ''],
    'SSD form factor':['text', ''],
    'Trusted Platform Module (TPM)':['bool', ''],
    'Password protection type':['text', ''],
    'Market positioning':['text', ''],
    'Front camera resolution (numeric)':['dec', 'MP'],
    'Audio chip':['text', ''],
    'Dual-screen':['bool', ''],
    'Full-size keyboard':['bool', ''],
    'Maximum refresh rate':['int', 'Hz'],
    'HDD capacity':['dec', 'GB'],
    'Docking connector':['bool', ''],
    'DVI port':['bool', ''],
    }

pos=[
    'Model', 
    'Product code', 

    'Brand', 
    'Part number', 
    'Model name', 
    'Family', 
    'Market positioning', 
    'Release date', 
    'Product colour', 
    'Form factor', 

    'Processor socket', 
    'Processor (link)', 
    'Processor manufacturer', 
    'Processor model', 
    'Processor family', 
    'Processor lithography', 
    'Processor boost frequency', 
    'Processor cache', 
    'Processor cores', 
    'Processor threads', 
    'Processor frequency', 

    'Maximum internal memory', 
    'Memory clock speed', 
    'Internal memory', 
    'Internal memory type', 

    'Display diagonal', 
    'Touchscreen', 
    'Panel type', 
    'Led backlight', 
    'Dual-screen', 
    'Display resolution', 
    'Maximum refresh rate', 
    'Hd type', 

    'Discrete graphics adapter', 
    'On-board graphics adapter', 
    'On-board graphics adapter model', 
    'Discrete graphics adapter model', 
    'Discrete graphics adapter model (link)', 
    'On-board graphics adapter base frequency', 
    'Maximum on-board graphics adapter memory', 
    'Discrete graphics memory type', 
    'Discrete graphics adapter memory', 

    'Storage media', 
    'Card reader integrated', 
    'Ssd capacity', 
    'Number of ssds installed', 
    'Total storage capacity', 
    'Ssd form factor', 
    'Hdd capacity', 

    '3g', 
    'Bluetooth version', 
    'Ethernet lan', 
    '4g', 
    'Bluetooth', 
    'Wi-fi standards', 
    'Wi-fi', 
    'Ethernet lan data rates', 


    
    'Docking connector', 
    'Usb 2.0 type-c ports', 
    'Usb 3.x type-a ports', 
    'Dvi port', 
    'Combo headphone/mic port', 
    'Usb 2.0 ports', 
    'Usb sleep-and-charge', 
    'Usb type-c thunderbolt 3 ports', 
    'Usb 3.x type-c ports', 

    'Speaker power', 
    'Audio chip', 
    'Built-in microphone', 

    'Front camera hd type', 
    'Front camera resolution (numeric)', 
    'Front camera resolution', 
    'Front camera', 

    'Pointing device', 
    'Numeric keypad', 
    'Keyboard backlit', 
    'Full-size keyboard', 

    'Operating system architecture', 
    'Operating system installed', 

    'Battery capacity (watt-hours)', 
    'Battery capacity', 
    'Battery life (max)', 

    'Width', 
    'Height', 
    'Depth', 
    'Weight', 

    'Ac adapter power', 

    'Cable lock slot', 
    'Password protection', 
    'Fingerprint reader', 
    'Password protection type', 
    'Trusted platform module (tpm)',     
]

s='HDMI ports quantity (IT stuff)'
import my_process
