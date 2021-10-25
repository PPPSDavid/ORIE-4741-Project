import pandas as pd
import numpy as np

# DataFrame structure
columns_of_interest = ['Year', 
                       'Quarter', 
                       'Month', 
                       'DayofMonth', 
                       'DayOfWeek', 
                       'FlightDate', 
                       'Reporting_Airline', 
                       'DOT_ID_Reporting_Airline', 
                       'Flight_Number_Reporting_Airline', 
                       'Origin', 
                       'OriginCityName', 
                       'OriginState', 
                       'Dest', 
                       'DestCityName', 
                       'DestState', 
                       'CRSDepTime', 
                       'DepTime', 
                       'DepDelay', 
                       'TaxiOut', 
                       'WheelsOff', 
                       'WheelsOn', 
                       'TaxiIn', 
                       'CRSArrTime',
                       'ArrTime',
                      'ArrDelay',
                       'CRSElapsedTime',
                      'Cancelled',
                      'CancellationCode',
                      'Diverted',
                       'Flights',
                       'Distance',
                       'DivArrDelay',
                       'DivActualElapsedTime'
                      ]
column_dtypes =  {'Year' : 'int', 
                   'Quarter': 'int', 
                   'Month': 'int', 
                   'DayofMonth': 'int', 
                   'DayOfWeek': 'int', 
                   'FlightDate': 'str', 
                   'Reporting_Airline': 'str', 
                   'DOT_ID_Reporting_Airline': 'int', 
                   'Flight_Number_Reporting_Airline': 'int', 
                   'Origin': 'str', 
                   'OriginCityName': 'str', 
                   'OriginState': 'str', 
                   'Dest': 'str', 
                   'DestCityName': 'str', 
                   'DestState': 'str', 
                   'CRSDepTime': 'str', 
                   'DepTime': 'str', 
                   'DepDelay': 'float', 
                   'TaxiOut': 'float', 
                   'WheelsOff': 'str', 
                   'WheelsOn': 'str', 
                   'TaxiIn': 'float', 
                   'CRSArrTime': 'str',
                   'ArrTime': 'str',
                   'ArrDelay': 'float',
                   'CRSElapsedTime': 'float',
                   'Cancelled': 'float',
                   'CancellationCode': 'str',
                   'Diverted': 'float',
                   'Flights': 'float',
                   'Distance': 'float',
                   'DivArrDelay': 'float',
                   'DivActualElapsedTime': 'float'
                 }

# US State Time Zones 
us_states_timezones = {
    'NY' : 'US/Eastern',
    'ME' : 'US/Eastern',
    'VT' : 'US/Eastern',
    'NH' : 'US/Eastern',
    'MA' : 'US/Eastern',
    'CT' : 'US/Eastern',
    'RI' : 'US/Eastern',
    'NJ' : 'US/Eastern',
    'DE' : 'US/Eastern',
    'MD' : 'US/Eastern',
    'DC' : 'US/Eastern',
    'WV' : 'US/Eastern',
    'VA' : 'US/Eastern',
    'NC' : 'US/Eastern',
    'SC' : 'US/Eastern',
    'GA' : 'US/Eastern',
    'FL' : 'US/Eastern',
    'OH' : 'US/Eastern',
    'MI' : 'US/Eastern',
    'IN' : 'US/Eastern',
    'PA' : 'US/Eastern',
    'CA' : 'US/Pacific',
    'OR' : 'US/Pacific',
    'WA' : 'US/Pacific',
    'NV' : 'US/Pacific',
    'ID' : 'US/Mountain',
    'MT' : 'US/Mountain',
    'WY' : 'US/Mountain',
    'CO' : 'US/Mountain',
    'UT' : 'US/Mountain',
    'NM' : 'US/Mountain',
    'AZ' : 'US/Arizona',
    'AK' : 'US/Alaska',
    'HI' : 'US/Hawaii',
    'ND' : 'US/Central',
    'SD' : 'US/Central',
    'NE' : 'US/Central',
    'KS' : 'US/Central',
    'OK' : 'US/Central',
    'TX' : 'US/Central',
    'MN' : 'US/Central',
    'IA' : 'US/Central',
    'MO' : 'US/Central',
    'AR' : 'US/Central',
    'LA' : 'US/Central',
    'WI' : 'US/Central',
    'IL' : 'US/Central',
    'KY' : 'US/Central',
    'TN' : 'US/Central',
    'MS' : 'US/Central',
    'AL' : 'US/Central',
    'PR' : 'America/Puerto_Rico',
    'VI' : 'America/Puerto_Rico',
    'TT' : 'America/Puerto_Rico',
}

# List of US Largest Airports
list_of_airports = set(['ATL', 'DFW', 'DEN', 'ORD', 'LAX', 'CLT', 'LAS', 'PHX', 'MCO', 'SEA'])

# Time-related helper functions
def cleanup_hhmm_time(s):
  """Parse time in corrputed HHMM format to Correct Form
  Args:
    s (str): Corrputed time in HHMM format

  Returns:
    str: time in HHMM format
  """
  if len(s) == 4:
      res =  s
  elif len(s) == 3:
      res = '0' + s
  elif len(s) == 2:
      res = '00' + s
  elif len(s) == 1:
      res = '000' + s
  assert len(res) == 4
  return res

def agg_datetime(date, time):
  """Aggregate date and time to  YYYY-MM-DD HH:MM:SS format
  Args:
    date (str): Date in YYYY-MM-DD format
    time (str): Time in HHMM format
  
  Returns:
    str: DateTime in YYYY-MM-DD-HHMM format

  """
    return str(date) + '-' + str(time)

def to_datetime(s):
  """Convert time in YYYY-MM-DD-HHMM format to datetime
  Args:
    s : Strings or Pandas Series of Strings in YYYY-MM-DD-HHMM format

  Returns:
    datetime: Time in Pandas datetime object
  """
  return pd.to_datetime(s, format = '%Y-%m-%d-%H%M', errors='coerce')

def to_utc(local_time, local_tz):
  """Convert local time to UTC
  Args:
    local_time (str): time in Pandas DateTime format
  
  Returns:
    UTC_time: UTC-ed time in Pandas DateTime format
  """
  UTC_time = local_time.tz_localize(local_tz, ambiguous=False).tz_convert("UTC")
  return UTC_time