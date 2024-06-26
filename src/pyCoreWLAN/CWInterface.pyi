from typing import Optional, Set

from .FoundationTypes import *
from .CWChannel import *
from .CWNetwork import *

class CWInterface:
    """
    @class

    @abstract 
    Control and query a Wi-Fi interface on OS X.

    @discussion 
    All actions performed by a CWInterface object are executed on the Wi-Fi
    device with the corresponding interface name.
    """

    def interfaceName(self) -> Optional[NSString]:
        """
        @property

        @abstract
        Returns the BSD name of the Wi-Fi interface (e.g. "en0").
        """
        ...

    def powerOn(self) -> bool:
        """
        @method

        @result
        YES if the Wi-Fi interface is on, NO otherwise.

        @abstract
        Indicates the Wi-Fi interface power state.

        @discussion
        Returns NO if an error occurs.
        """
        ...

    def supportedWLANChannels(self) -> Optional[Set[CWChannel]]:
        """
        @method

        @result
        An NSSet of CWChannel objects.

        @abstract 
        Returns the set of channels supported by the Wi-Fi interface for the currently adopted country code.
        
        @discussion
        Returns nil if an error occurs.
        """
        ...

    def wlanChannel(self) -> Optional[CWChannel]:
        """
        @method

        @abstract
        Returns the current channel of the Wi-Fi interface.

        @discussion
        Returns nil if an error occurs.
        """
        ...

    def activePHYMode(self) -> CWPHYMode:
        """
        @method

        @abstract
        Returns the currently active physical layer (PHY) mode of the Wi-Fi
        interface.

        @discussion
        Returns kCWPHYModeNone if an error occurs.
        """
        ...

    def ssid(self) -> Optional[NSString]:
        """
        @method

        @abstract 
        Returns the current service set identifier (SSID) of the Wi-Fi
        interface, encoded as a string.

        @discussion 
        Returns nil if an error occurs, or if the interface is not participating
        in a Wi-Fi network, or if the SSID can not be encoded as a valid UTF-8
        or WinLatin1 string.
        """
        ...

    def ssidData(self) -> Optional[NSData]:
        """
        @method

        @abstract 
        Returns the current service set identifier (SSID) for the interface,
        encapsulated in an NSData object.

        @discussion 
        Returns nil if an error occurs, or if the interface is not participating
        in a Wi-Fi network.
        """
        ...

    def bssid(self) -> Optional[NSString]:
        """
        @method

        @abstract 
        Returns the current basic service set identifier (BSSID) of the Wi-Fi
        interface, returned as an UTF-8 string.

        @discussion 
        Returns a UTF-8 string using hexadecimal characters formatted as
        XX:XX:XX:XX:XX:XX.
        Returns nil if an error occurred, or if the interface is not
        participating in a Wi-Fi network.

        @note
        BSSID information is not available unless Location Services is enabled
        and the user has authorized the calling app to use location services.

        @seealso
        CLLocationManager
        """
        ...

    def rssiValue(self) -> NSInteger:
        """
        @method

        @abstract 
        Returns the current received signal strength indication (RSSI)
        measurement (dBm) for the Wi-Fi interface.

        @discussion 
        Returns 0 if an error occurs, or if the interface is not participating
        in a Wi-Fi network.
        """
        ...

    def noiseMeasurement(self) -> NSInteger:
        """
        @method

        @abstract 
        Returns the current noise measurement (dBm) for the Wi-Fi interface.

        @discussion 
        Returns 0 if an error occurs, or if the interface is not participating
        in a Wi-Fi network.
        """
        ...

    def security(self) -> CWSecurity:
        """
        @method

        @abstract
        Returns the current security type of the Wi-Fi interface.

        @discussion 
        Returns kCWSecurityUnknown if an error occurs, or if the interface is
        not participating in a Wi-Fi network.
        """
        ...

    def transmitRate(self) -> float:
        """
        @method

        @abstract 
        Returns the current transmit rate (Mbps) for the Wi-Fi interface.

        @discussion 
        Returns 0 if an error occurs, or if the interface is not participating
        in a Wi-Fi network.
        """
        ...

    def countryCode(self) -> Optional[NSString]:
        """
        @method

        @abstract 
        Returns the currently adopted country code (ISO/IEC 3166-1:1997) for the
        Wi-Fi interface.

        @discussion 
        Returns nil if an error occurs, or if the Wi-Fi interface is off.
        """
        ...

    def interfaceMode(self) -> CWInterfaceMode:
        """
        @method

        @abstract 
        Returns the current operating mode for the Wi-Fi interface.

        @discussion
        Returns kCWInterfaceModeNone if an error occurs, or if the interface is
        not participating in a Wi-Fi network.
        """
        ...

    def transmitPower(self) -> NSInteger:
        """
        @method

        @abstract 
        Returns the current transmit power (mW) for the Wi-Fi interface.

        @discussion 
        Returns 0 if an error occurs.
        """
        ...

    def hardwareAddress(self) -> Optional[NSString]:
        """
        @method

        @abstract 
        Returns the hardware media access control (MAC) address for the Wi-Fi
        interface, returned as an UTF-8 string.

        @discussion 
        The standard format for printing a MAC-48 address XX:XX:XX:XX:XX:XX is
        used to represent
        the MAC address as a string. 
        Returns nil if an error occurs.
        """
        ...

    def serviceActive(self) -> bool:
        """
        @method

        @result
        YES if the corresponding network service is active, NO otherwise.

        @abstract 
        Indicates the network service state of the Wi-Fi interface.

        @discussion 
        Returns NO if an error occurs.
        """
        ...

    def cachedScanResults(self) -> Optional[Set[CWNetwork]]:
        """
        @method

        @result
        An NSSet of CWNetwork objects.

        @abstract 
        Returns the scan results currently in the scan cache for the Wi-Fi
        interface.

        @discussion 
        Returns nil if an error occurs.
        """
        ...

    def configuration(self) -> Optional[CWConfiguration]:
        """
        @method

        @abstract 
        Returns the current configuration for the Wi-Fi interface.

        @discussion
        Returns nil if an error occurs.
        """
        ...

    def interfaceNames() -> Optional[Set[NSString]]:
        """
        @method

        @result
        An NSSet of NSString objects.

        @abstract 
        Returns the list of available Wi-Fi interface names (e.g. "en0").

        @discussion 
        Returns an empty NSArray object if no Wi-Fi interfaces exist.
        Returns nil if an error occurs.
        """
        ...

    def interface() -> CWInterface:
        """
        @method

        @abstract 
        Convenience method for getting a CWInterface object for the default
        Wi-Fi interface.
        """
        ...

    def interfaceWithName_(name: Optional[NSString]) -> CWInterface:
        """
        @method

        @param name 
        The name of an available Wi-Fi interface.

        @abstract 
        Convenience method for getting a CWInterface object bound to the Wi-Fi
        interface with a specific interface name.

        @discussion 
        Use +[CWInterface interfaceNames] to get a list of available Wi-Fi
        interface names.
        Returns a CWInterface object for the default Wi-Fi interface if no
        interface name is specified.
        """
        ...

    def initWithInterfaceName_(self, name: Optional[NSString]) -> CWInterface:
        """
        @method

        @param name 
        The name of an available Wi-Fi interface.

        @abstract 
        Convenience method for getting a CWInterface object bound to the Wi-Fi
        interface with a specific interface name.

        @discussion 
        Use +[CWInterface interfaceNames] to get a list of available Wi-Fi
        interface names.
        Returns a CWInterface object for the default Wi-Fi interface if no
        interface name is specified.
        """
        ...

    def setPower_error_(self, power: bool, error: Optional[NSError] = None) -> bool:
        """
        @method
        
        @param power 
        A BOOL value indicating Wi-Fi power state. Specify YES to turn on the Wi-Fi interface.
        
        @param error 
        An NSError object passed by reference, which upon return will contain the error if an error occurs. 
        This parameter is optional.
        
        @result 
        Returns YES upon success, or NO if an error occurred.
        
        @abstract 
        Sets the Wi-Fi interface power state.
        """
        ...

    def setWLANChannel_error_(self, channel: CWChannel, error: Optional[NSError] = None) -> bool:
        """
        @method

        @param channel
        A CWChannel object.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract 
        Sets the Wi-Fi interface channel.

        @discussion 
        Setting the channel while the interface is associated to a Wi-Fi network is not permitted.
        """
        ...

    def setPairwiseMasterKey_error_(self, key: Optional[NSData], error: Optional[NSError] = None) -> bool:
        """
        @method

        @param key 
        An NSData object containing the pairwise master key (PMK).
        Passing nil clear the PMK for the Wi-Fi interface.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract 
        Sets the Wi-Fi interface pairwise master key (PMK).

        @discussion
        The specified key must be exactly 32 octets.
        """
        ...

    def setWEPKey_flags_index_error_(self, key: Optional[NSData], flags: CWCipherKeyFlags, index: NSInteger, error: Optional[NSError] = None) -> bool:
        """
        @method

        @param key 
        An NSData object containing the WEP key.
        Passing nil clears the WEP key for the Wi-Fi interface.

        @param flags 
        A bitmask indicating which CWCipherKeyFlags to use for the specified WEP key.

        @param index 
        An NSInteger indicating which default key index (1-4) to use for the specified key.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract 
        Sets the Wi-Fi interface WEP key.
        """
        ...

    def scanForNetworksWithSSID_error_(self, ssid: Optional[NSData], error: Optional[NSError] = None) -> Optional[Set[CWNetwork]]:
        """
        @method

        @param ssid
        Probe request SSID.  
        Pass an SSID to perform a directed scan for hidden Wi-Fi networks.
        This parameter is optional.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        An NSSet of CWNetwork objects, or nil if an error occurs.

        @abstract 
        Performs a scan for Wi-Fi networks and returns scan results to the caller.

        @discussion 
        This method will block for the duration of the scan.

        @note
        Returned networks will not contain BSSID information unless Location Services is enabled and the user has authorized the calling app to use location services.

        @seealso
        CLLocationManager
        """
        ...

    def scanForNetworksWithSSID_includeHidden_error_(self, ssid: Optional[NSData], includeHidden: bool, error: Optional[NSError] = None) -> Optional[Set[CWNetwork]]:
        """
        @method

        @param ssid
        Probe request SSID.
        Pass an SSID to perform a directed scan for hidden Wi-Fi networks.
        This parameter is optional.

        @param includeHidden
        Indicate whether or not hidden networks should not be filtered from the returned scan results.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        An NSSet of CWNetwork objects, or nil if an error occurs.

        @abstract
        Performs a scan for Wi-Fi networks and returns scan results to the caller.

        @discussion
        This method will block for the duration of the scan.

        @note
        Returned networks will not contain BSSID information unless Location Services is enabled and the user has authorized the calling app to use location services.

        @seealso
        CLLocationManager
        """
        ...

    def scanForNetworksWithName_error_(self, networkName: Optional[NSString], error: Optional[NSError] = None) -> Optional[Set[CWNetwork]]:
        """
        @method

        @param networkName
        Probe request SSID, encoded as an UTF-8 string.
        Pass a networkName to perform a directed scan for hidden Wi-Fi networks.
        This parameter is optional.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        An NSSet of CWNetwork objects, or nil if an error occurs.

        @abstract
        Performs a scan for Wi-Fi networks and returns scan results to the caller.

        @discussion
        This method will block for the duration of the scan.

        @note
        Returned networks will not contain BSSID information unless Location Services is enabled and the user has authorized the calling app to use location services.

        @seealso
        CLLocationManager
        """
        ...

    def scanForNetworksWithName_includeHidden_error_(self, networkName: Optional[NSString], includeHidden: bool, error: Optional[NSError] = None) -> Optional[Set[CWNetwork]]:
        """
        @method

        @param networkName
        Probe request SSID, encoded as an UTF-8 string.
        Pass a networkName to perform a directed scan for hidden Wi-Fi networks.
        This parameter is optional.

        @param includeHidden
        Indicate whether or not hidden networks should not be filtered from the returned scan results.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        An NSSet of CWNetwork objects, or nil if an error occurs.

        @abstract
        Performs a scan for Wi-Fi networks and returns scan results to the caller.

        @discussion
        This method will block for the duration of the scan.

        @note
        Returned networks will not contain BSSID information unless Location Services is enabled and the user has authorized the calling app to use location services.

        @seealso
        CLLocationManager
        """

    def associateToNetwork_password_error_(self, network: CWNetwork, password: Optional[NSString], error: Optional[NSError] = None) -> bool:
        """
        @method

        @param network
        The network to which the Wi-Fi interface will associate.

        @param password
        The network passphrase or key. Required for association to WEP, WPA Personal, and WPA2 Personal networks.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract 
        Associates to a W-Fi network using the specified passphrase.

        @discussion 
        This method will block for the duration of the association.
        """
        ...

    def disassociate(self) -> None:
        """
        @method

        @abstract 
        Disassociates from the current Wi-Fi network.

        @discussion
        """
        ...

    def associateToEnterpriseNetwork_identity_username_password_error_(self, network: CWNetwork, identity: Optional[SecIdentityRef], username: Optional[NSString], password: Optional[NSString], error: Optional[NSError] = None) -> bool:
        """
        @method

        @param network
        The network to which the Wi-Fi interface will associate.

        @param username 
        The username to use for 802.1X authentication.

        @param password 
        The password to use for 802.1X authentication.

        @param identity 
        The identity to use for IEEE 802.1X authentication. Holds the corresponding client certificate.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract
        Associates to an enterprise W-Fi network using the specified 802.1X credentials.

        @discussion
        This method will block for the duration of the association.
        """
        ...

    def startIBSSModeWithSSID_security_channel_password_error_(self, ssidData: NSData, security: CWIBSSModeSecurity, channel: NSUInteger, password: Optional[NSString], error: Optional[NSError] = None) -> bool:
        """
        @method

        @param ssidData
        The SSID to use for the IBSS network.
        Pass nil to use the machine name as the IBSS network name.

        @param security 
        The CWIBSSModeSecurity type.

        @param channel 
        The channel on which the IBSS network will be created.

        @param password 
        The password to be used. This paramter is required for kCWIBSSModeSecurityWEP40 or kCWIBSSModeSecurityWEP104 security types.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract
        Creates a computer-to-computer (IBSS) network.
        """
        ...

    def commitConfiguration_authorization_error_(self, configuration: CWConfiguration, authorization: Optional[SFAuthorization], error: Optional[NSError] = None) -> bool:
        """
        @method

        @param configuration
        The Wi-Fi configuration to commit to disk.

        @param authorization
        An SFAuthorization object to use for authorizing the commit.
        This parameter is optional.

        @param error
        An NSError object passed by reference, which upon return will contain the error if an error occurs.
        This parameter is optional.

        @result
        Returns YES upon success, or NO if an error occurred.

        @abstract 
        Commits a CWConfiguration for the given Wi-Fi interface.

        @discussion 
        This method requires the caller have root privileges
        or obtain administrator privileges using the SFAuthorization API.
        """
        ...
