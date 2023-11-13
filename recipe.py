from rgsync import RGWriteBehind, RGWriteThrough # RGJSONWriteBehind 
from rgsync.Connectors import MySqlConnector, MySqlConnection # MongoConnector, MongoConnection

'''
Create MySQL connection object
'''
connection = MySqlConnection('demouser', 'Password123!', 'localhost:3306/test')

'''
Create MySQL persons connector
'''
personsConnector = MySqlConnector(connection, 'persons', 'person_id')

personsMappings = {
	'first_name':'first',
	'last_name':'last',
	'age':'age'
}

RGWriteBehind(GB,  keysPrefix='person', mappings=personsMappings, connector=personsConnector, name='PersonsWriteBehind',  version='99.99.99')

# '''
# Create MySQL cars connector
# '''
# carsConnector = MySqlConnector(connection, 'cars', 'car_id')

# carsMappings = {
# 	'id':'id',
# 	'color':'color'
# }

# RGWriteBehind(GB, keysPrefix='car', mappings=carsMappings, connector=carsConnector, name='CarsWriteBehind', version='99.99.99')



