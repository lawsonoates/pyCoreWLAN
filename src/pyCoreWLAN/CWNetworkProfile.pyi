from typing import Optional

from .CoreWLANTypes import *
from .CWChannel import *

class CWNetworkProfile:
    """
    @class

    @abstract 
    Encapsulates a preferred network entry.
    """

    def ssid(self) -> Optional[NSString]:
        """
        @property

        @abstract
        Returns the service set identifier (SSID) for the Wi-Fi network profile,
        encoded as a string.

        @discussion 
        Returns nil if the SSID can not be encoded as a valid UTF-8 or WinLatin1
        string.
        """
        ...

    def ssidData(self) -> Optional[NSData]:
        """
        @property

        @abstract 
        Returns the service set identifier (SSID) for the Wi-Fi network profile,
        encapsulated in an NSData object.

        @discussion
        The SSID is 1-32 octets.
        """
        ...

    def security(self) -> CWSecurity:
        """
        @property

        @abstract 
        Returns the security type of the Wi-Fi network profile.
        """
        ...

    def networkProfile(cls) -> CWNetworkProfile:
        """
        @method

        @abstract 
        Convenience method for getting a CWNetworkProfile object.
        """
        ...

    def init(self) -> None:
        """
        @method

        @abstract 
        Initializes a CWNetworkProfile object.
        """
        ...

    def initWithNetworkProfile_(self, networkProfile: CWNetworkProfile) -> CWNetworkProfile:
        """
        @method

        @param networkProfile 
        A CWNetworkProfile object.

        @result 
        A CWNetworkProfile object.

        @abstract 
        Initializes a CWNetworkProfile object with the properties of an existing
        CWNetworkProfile object.
        """
        ...

    def networkProfileWithNetworkProfile_(cls, networkProfile: CWNetworkProfile) -> CWNetworkProfile:
        """
        @method

        @param networkProfile
        A CWNetworkProfile object.

        @result
        A CWNetworkProfile object.

        @abstract
        Convenience method for getting a CWNetworkProfile object initialized
        with the properties of an existing CWNetworkProfile object.
        """
        ...

    def isEqualToNetworkProfile_(self, networkProfile: CWNetworkProfile) -> bool:
        """
        @method

        @param networkProfile
        A CWNetworkProfile object.

        @result
        YES if the objects are equal, NO otherwise.

        @abstract
        Determine CWNetworkProfile equality.

        @discussion
        CWNetworkProfile objects are considered equal if their corresponding
        <i>ssidData</i> and <i>security</i> properties are equal.
        """
        ...


class CWMutableNetworkProfile(CWNetworkProfile):
    """
    @class

    @abstract
    Mutable subclass of CWNetworkProfile. Use this class for changing profile
    properties.

    @discussion
    To commit Wi-Fi network profile changes, use
    -[CWMutableConfiguration setNetworkProfiles:] and 
    -[CWInterface commitConfiguration:authorization:error:].
    """

    def ssidData(self) -> Optional[NSData]:
        """
        @property

        @abstract
        Set the service set identifier (SSID).
        """
        ...

    def security(self) -> CWSecurity:
        """
        @property

        @abstract
        Set the security type.
        """
        ...