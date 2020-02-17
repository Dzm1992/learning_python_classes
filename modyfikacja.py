#9.13
"""slownik w kolejnosci z biblioteki domyslnej."""

from collections import OrderedDict

glosariusz = OrderedDict()

glosariusz['Boolean'] = 'True/False'
glosariusz['Integer'] = '2'
glosariusz['PEP8'] = 'Formatowanie' 
glosariusz['Tuple'] = 'Krotka'
glosariusz['Float'] = '1.5'

for k, v in glosariusz.items():
	print(k,":",v)

