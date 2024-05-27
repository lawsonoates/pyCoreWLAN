from typing import List, Optional

from .CoreWLANTypes import *
from .CWInterface import *

class CWWiFiClient:
    """
    @class

    @abstract
    The interface to the Wi-Fi subsystem on OS X.
     
    @discussion 
    Provides access to all Wi-Fi interfaces and allows Wi-Fi clients to setup event notifications.
     
    CWWiFiClient objects are heavy objects, therefore, clients of the CoreWLAN framework should use a single, 
    long-running instance rather than creating several short-lived instances.  
    For convenience, +[CWWiFiClient sharedWiFiClient] can be used to return a singleton instance.
    
    The CWWiFiClient object should be used to instantiate CWInterface objects rather than using a CWInterface
    initializer directly.
    """

    def delegate(self) -> None:
        """
        @property

        @abstract
        Sets the delegate to the specified object, which may implement CWWiFiEventDelegate protocol for Wi-Fi event handling.

        @discussion
        Clients may register for specific Wi-Fi events using -[CWWiFiClient startMonitoringEventWithType:error:].
        """
        ...

    def sharedWiFiClient(cls) -> CWWiFiClient:
        """
        @method

        @abstract 
        Returns the shared CWWiFiClient instance. There is a single shared instance per process.
        """
        ...
    
    def init(self) -> None:
        """
        @method

        @abstract
        Initializes a CWWiFiClient object.
        """
        ...

    def interface(self) -> Optional[CWInterface]:
        """
        @method

        @abstract
        Returns the CWInterface object for the default Wi-Fi interface.
        """
        ...

    def interfaceNames(cls) -> Optional[List[NSString]]:
        """
        @method

        @result 
        An NSArray of NSString objects corresponding to Wi-Fi interface names.

        @abstract
        Returns the list of available Wi-Fi interface names (e.g. "en0").

        @discussion
        If no Wi-Fi interfaces are available, this method will return an empty array.
        Returns nil if an error occurs.
        """
        ...

    def interfaceWithName_(self, interfaceName: Optional[NSString]) -> Optional[CWInterface]:
        """
        @method

        @param interfaceName
        The name of an available Wi-Fi interface.

        @abstract
        Get the CWInterface object bound to the Wi-Fi interface with a specific interface name.

        @discussion
        Use +[CWWiFiClient interfaceNames] to get a list of available Wi-Fi interface names.
        Returns a CWInterface object for the default Wi-Fi interface if no interface name is specified.
        """
        ...

    def interfaces(self) -> Optional[List[CWInterface]]:
        """
        @method

        @result 
        An NSArray of CWInterface objects.

        @abstract 
        Returns all available Wi-Fi interfaces.

        @discussion 
        If no Wi-Fi interfaces are available, this method will return an empty array.
        Returns nil if an error occurs.
        """
        ...

    def startMonitoringEventWithType_error_(self, type: CWEventType, error: Optional[NSError] = None) -> bool:
        """
        @method

        @param type
        A CWEventType value.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract 
        Register for specific Wi-Fi event notifications.
        """
        ...

    def stopMonitoringEventWithType_error_(self, type: CWEventType, error: Optional[NSError] = None) -> bool:
        """
        @method

        @param type
        A CWEventType value.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract
        Unregister for specific Wi-Fi event notifications.
        """
        ...

    def stopMonitoringAllEventsAndReturnError_(self, error: Optional[NSError] = None) -> bool:
        """
        @method

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract
        Unregister for all Wi-Fi event notifications.
        """
        ...