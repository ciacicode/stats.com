import unittest
from config import Config
from stats import EPLRequest
import pdb


class TestEPLMethods(unittest.TestCase):        
    
    def test_instantiate(self):
        EPL_request = EPLRequest(Config)
        print "Asserting instantiation"
        assert hasattr(EPL_request, 'config')
        assert hasattr(EPL_request, 'api_key')
        assert hasattr(EPL_request, 'secret')
        assert hasattr(EPL_request, 'format')
        print "Instantiation Terminated"
                        
    def test_get_teams(self):
        # tests the output of a get_teams request
        #last season teams
        print "Testing get_teams"
        EPL_request = EPLRequest(Config)
        params = {'season':'2015'}
        teams = EPL_request.get_teams(params)
        assert type(teams) is dict
                                            
    def test_get_events(self):
        #test output of get_events request
        print "Testing get_events with start and end date"
        EPL_request = EPLRequest(Config)
        params = {'startDate':'20160812', 'endDate':'20160819'}
        events = EPL_request.get_events(params)
        assert type(events) is dict
        
if __name__ == '__main__':
    unittest.main()
    
    