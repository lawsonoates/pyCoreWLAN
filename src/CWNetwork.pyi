from typing import Optional

from .CoreWLANTypes import *
from .CWChannel import *

class CWNetwork:
    """
    @class

    @abstract 
    Represents a device participating in a Wi-Fi network, providing accessors to
    various network attributes.
    """

    def ssid(self) -> Optional[NSString]:
        """
        @property

        @abstract
        Returns the service set identifier (SSID) for the Wi-Fi network device,
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
        Returns the service set identifier (SSID) for the Wi-Fi network device,
        encapsulated in an NSData object.

        @discussion
        The SSID is defined as 1-32 octets.
        """
        ...

    def bssid(self) -> Optional[NSString]:
        """
        @property

        @abstract 
        Returns the basic service set identifier (BSSID) for the Wi-Fi network
        device, returned as UTF-8 string.

        @discussion
        Returns a UTF-8 string using hexadecimal characters formatted as
        XX:XX:XX:XX:XX:XX.

        @note
        BSSID information is not available unless Location Services is enabled
        and the user has authorized the calling app to use location services.

        @seealso
        CLLocationManager
        """
        ...

    def wlanChannel(self) -> Optional[CWChannel]:
        """
        @property

        @abstract 
        The operating channel of the Wi-Fi device.
        """
        ...

    def rssiValue(self) -> NSInteger:
        """
        @property

        @abstract 
        Returns the received signal strength indication (RSSI) measurement (dBm)
        for the Wi-Fi device.
        """
        ...

    def noiseMeasurement(self) -> NSInteger:
        """
        @property

        @abstract 
        Returns the noise measurement (dBm) for the Wi-Fi device.
        """
        ...

    def informationElementData(self) -> Optional[NSData]:
        """
        @property

        @abstract 
        Returns information element data included in beacon or probe response
        frames.
        """
        ...

    def countryCode(self) -> Optional[NSString]:
        """
        @property

        @abstract 
        Returns the advertised country code (ISO/IEC 3166-1:1997) for the Wi-Fi
        device.
        """
        ...

    def beaconInterval(self) -> NSInteger:
        """
        @property

        @abstract
        Returns the beacon interval (ms) for the Wi-Fi device.
        """
        ...

    def ibss(self) -> bool:
        """
        @property

        @result
        YES if the Wi-Fi device is part of an IBSS network, NO otherwise.

        @abstract
        Indicates whether or not the Wi-Fi device is participating in an
        independent basic service set (IBSS), or ad-hoc Wi-Fi network.
        """
        ...

    def isEqualToNetwork_(self, network: CWNetwork) -> bool:
        """
        @method

        @param network 
        A CWNetwork object.

        @result
        YES if the objects are equal, NO otherwise.

        @abstract 
        Determine CWNetwork equality.

        @discussion
        CWNetwork objects are considered equal if their corresponding
        <i>ssidData</i> and <i>bssid</i> properties are equal.
        """
        ...

    def supportsSecurity_(self, security: CWSecurity) -> bool:
        """
        @method

        @param security
        A CWSecurity type value.

        @result
        <i>YES</i> if the Wi-Fi device supports the specified security type,
        <i>NO</i> otherwise.

        @abstract 
        Determine which security types a Wi-Fi device supports.
        """
        ...

    def supportsPHYMode_(self, phyMode: CWPHYMode) -> bool:
        """
        @method

        @param phyMode
        A CWPHYMode type value.

        @result 
        YES if the Wi-Fi device supports the specified PHY mode, NO otherwise.

        @abstract
        Determine which PHY modes a Wi-Fi device supports.
        """
        ...
