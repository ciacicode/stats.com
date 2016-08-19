import hashlib
import requests
from config import Config
import time
import pdb


class EPLRequest:
    """ Stats.com Request object"""
    def __init__(self,config):
        """ 
        config: object containing api_key, secret and format
        """
        self.config = config
        self.api_key = config.API_KEY
        self.secret = config.SECRET
        self.format = config.FORMAT
    
    def sign_parameters(self, parameters):
        """
        parameters: dict with optional parameters
        returns full dict of parameters + signature parameters
        """
        epoch = str(int(time.time()))
        parameters['api_key'] = self.api_key
        parameters['accept'] = self.format
        parameters['eventTypeId'] = '1'
        sig = hashlib.sha256(self.api_key + self.secret + epoch).hexdigest()
        parameters['sig'] = sig
        return parameters
                
    def get_teams(self, params):
        """
        params: dict with the following optional parameters:
            startDate: YYYYMMDD
            endDate: YYYYMMDD
            date: YYYYMMDD
            season: YYYY
            eventId: int
            linescore: boolean
            box: boolean, requires eventId if true
            pbp: boolean, requires eventId if true
            touches: boolean, requires eventId if true
            breakdowns: boolean, requires eventId if true   
        returns: team details for the league
        """
        teams_url = self.config.ENDPOINTS['teams']
        payload = self.sign_parameters(params)
        response = requests.get(teams_url, params=payload)
        return response.json()
    
    def get_events(self, params):
        """
        params: dict with the following optional parameters:
            startDate: YYYYMMDD
            endDate: YYYYMMDD
            date: YYYYMMDD
            season: YYYY
            eventId: int
            linescore: boolean
            box: boolean as str, requires eventId if true
            pbp: boolean as str, requires eventId if true
            touches: boolean as str, requires eventId if true
            breakdowns: boolean str, requires eventId if true   
        returns: event details for the given date
        """
        events_url = self.config.ENDPOINTS['events']
        payload = self.sign_parameters(params)
        if payload['eventId'] is not None:
            event_id = str(payload['eventId'])
            response = requests.get(events_url + event_id, params=payload)
        else:
            response = requests.get(events_url, params=payload)
        return response.json()
        
    
        
    def __repr__(self):
        print self.config
        
        
        