"""
   Copyright 2006-2008 SpringSource (http://springsource.com), All Rights Reserved

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.       
"""

# JMS constants

DELIVERY_MODE_NON_PERSISTENT = 1
DELIVERY_MODE_PERSISTENT = 2

RECEIVE_TIMEOUT_INDEFINITE_WAIT = 0
RECEIVE_TIMEOUT_NO_WAIT = -1

DEFAULT_DELIVERY_MODE = DELIVERY_MODE_PERSISTENT
DEFAULT_TIME_TO_LIVE = 0

class JMSException(Exception):
    """ Base class for all JMS-related exceptions.
    """

class NoMessageAvailableException(JMSException):
    """ Raised when the jms_template's call to receive returned no message
    in the expected wait interval.
    """
    pass

class WebSphereMQJMSException(JMSException):
    """ Class for exceptions related to WebSphereMQ only.
    """
    def __init__(self, exc=None):
        
        if exc == None:
            exc_message = ""
        else:
            # XXX: comp/reason tests
            if not isinstance(exc, basestring):
                exc_message = "An exception has occured, completion_code='%s', reason_code='%s'" % (
                        exc.comp, exc.reason)
            else:
                exc_message = exc 
        
        super(JMSException, self).__init__(exc_message)
        
        self.completion_code = None
        self.reason_code = None
        
        if exc:
            from pymqi import MQMIError
            
            if isinstance(exc, MQMIError):
                self.completion_code = exc.comp
                self.reason_code = exc.reason
