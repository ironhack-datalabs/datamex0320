import numpy as np

def fix_colnames(array:list):
    '''
    This function will retunr a list containng more trackeable names for the columns. 
    '''
    
    new_colnames = []
    
    for c in array:
        if (':' not in c) and (c.lower().endswith(' ')): 
            new_colnames.append(c.lower().replace('.', '')[:-1])
        elif ':' not in c:
            new_colnames.append(c.lower().replace('.', ''))
        else:
            new_colnames.append(c.lower().replace('unnamed:', 'col'))
            
    return new_colnames


def activity_mask(activity):
    
    if isinstance(activity, float) or (isinstance(activity,str) and (len(activity) < 6)):
        return 0
    else:
        return activity



def location_mask(location):
    
    if isinstance(location, float) or (isinstance(location, str) and (len(location) < 4)):
        return 0
    else:
        return location



def time_mask(time):
    
    if isinstance(time, float) or (isinstance(time, str) and (len(time) < 4)):
        return 0
    else:
        return time




def date_mask(date):
    
    if date != '':
        return date



def sex_mask(sex):
    
    if sex == 'M ':
        sex = 'M'
        
    if sex not in ['F', 'M']:
        return 0
    else:
        return sex




def area_mask(area):
    
    if isinstance(area, float) or (isinstance(area, str) and (len(area) < 3)):
        return 0
    else:
        return area




def row_relevance(row):
    
    act = loc = t = dt = s = a = y = 0
    
    if activity_mask(row['activity']) != 0:
        act = 5
        
    if location_mask(row['location']) != 0:
        loc = 4
        
    if time_mask(row['time']) != 0:
        t = 3
        
    if date_mask(row['date']) != 0:
        dt = 3
        
    if sex_mask(row['sex']) != 0:
        s = 2
        
    if area_mask(row['area']) != 0:
        a = 2
        
    if row['year'] != np.nan:
        y = 1
    
    return act + loc + t + dt + s + a + y




def clean_case_number(entry):
    if isinstance(entry, float):
        return "Not specified"
    else:
        return str(entry)





def clean_species(entry):
    
    
    if isinstance(entry, float) or (len(entry.split(" ")) == 1):
        return "Not identified"
    else:
        species = entry.split(' ')
        s = " ".join([species[i] for i in range(len(species)-1) if species[i+1] == 'shark' or species[i+1] == 'shark,'])
        
        if len(s) < 3:
            return "Not identified"
        elif ord(s[0].lower()) not in range(ord('a'), ord('z')):
            return "Not identified"
        else:
            return s



def clean_date(entry):
    
    if isinstance(entry, float) or len(entry)<8:
        return "Not found"
    
    else:
        
        date = entry.split(" ")
        
        if len(date) > 1 and all([len(s) > 0 for s in date]):
            if [s for s in date if ord(s[0]) in range(ord('0'), ord('9')+1)] != []:
                date = [s for s in date if ord(s[0]) in range(ord('0'), ord('9')+1)]
                return date[0]
            else:
                return "Not found"
        else:
            return date[0]
    



def clean_type(entry):
    if isinstance(entry, float) or entry == 'Invalid' or entry == 'Boatomg' or entry == 'Boating' or entry == 'Questionable' or entry == 'Boat':
        return "Not found"
    else:
        return str(entry)



def clean_country(entry):
    if isinstance(entry, float):
        return "UNKNOWN"
    else:
        if entry.endswith('?') or ('/' in entry) or ('SEA' in entry) or ('Coast' in entry) or ('ATLANTIC' in entry) or ('MID-' in entry) or ('PACIFIC' in entry) or entry == 'DIEGO GARCIA':
            return "UNKNOWN"
        else:
            return entry


def clean_area(entry):
    if isinstance(entry, float):
        return "UNKNOWN"
    else:
    	return entry



def clean_location(entry):
    if isinstance(entry, float):
        return "UNKNOWN"
    else:
    	return entry


def clean_activity(entry):
    if isinstance(entry, float):
        return "UNKNOWN"
    else:
    	return entry




def clean_name(entry):
    if isinstance(entry, float):
        return "Unidentified"
    else:
        if len(entry.split(" "))>4 or ('male' in entry) or ('female' in entry) or ('unknown' in entry) or ('a' in entry) or ('child' in entry) or ('sailor' in entry) or ('boy' in entry) or ('Anonymous' in entry) or ('fishermen' in entry) or ('girl' in entry) or ('Unknown' in entry) or ('women' in entry) or ('men' in entry) or ('dinghy' in entry) or ('M.C.' in entry):
            return "Unidentified"
        else:
            return entry



def clean_sex(entry):
	if entry == 'M ':
		entry = 'M'

	if isinstance(entry, float) or entry not in ['F', 'M']:
		return "Not specified"
	else:
		return str(entry)



def clean_age(entry):
    if isinstance(entry, float):
        return "UNKNOWN"
    else:
    	return entry



def clean_injury(entry):
    if isinstance(entry, float) or entry == 'FATAL' or entry == 'Survived' or ('No injury' in entry) or ('FATAL, body' in entry):
        return "No details"
    else:
        return entry



def clean_fatality(entry):

	if entry == 'N ' or entry == ' N':
		entry = 'N'

	if isinstance(entry, float) or entry not in ['N', 'Y']:
		return "UNKNOWN"

	else:
		return entry



def clean_time(entry):
	if isinstance(entry, float):
		return "UNKNOWN"
	else:
		return entry



def clean_invs(entry):
	if isinstance(entry, float):
		return "UNKNOWN"
	else:
		return entry




def clean_href_f(entry):
	if isinstance(entry, float):
		return "UNKNOWN"
	else:
		return entry




