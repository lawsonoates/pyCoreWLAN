from typing import Optional, Set

from .CoreWLANTypes import *
from .CWChannel import *

## confirm that option is used in code as null

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

    def interfaceNames() -> Optional[Set[str]]:
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

    def interfaceWithName(name: Optional[str]) -> CWInterface:
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

    def initWithInterfaceName(self, name: Optional[str]) -> 'CWInterface':
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

        ######### here

    def setPower(self, power: bool, error: Optional[object] = None) -> bool:
        """
        Sets the Wi-Fi interface power state.

        Args:
            power (bool): A BOOL value indicating Wi-Fi power state. Specify YES to turn on the Wi-Fi interface.
            error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

        Returns:
            bool: YES upon success, or NO if an error occurred.
        """
        ...

    def setWLANChannel(self, channel: 'CWChannel', error: Optional[object] = None) -> bool:
        """
        Sets the Wi-Fi interface channel.

        Args:
            channel (CWChannel): A CWChannel object.
            error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

        Returns:
            bool: YES upon success, or NO if an error occurred.
        """
        ...

    def setPairwiseMasterKey(self, key: Optional[bytes], error: Optional[object] = None) -> bool:
        """
        Sets the Wi-Fi interface pairwise master key (PMK).

        Args:
            key (Optional[bytes]): An NSData object containing the pairwise master key (PMK). Passing nil clears the PMK for the Wi-Fi interface.
            error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

        Returns:
            bool: YES upon success, or NO if an error occurred.
        """
        ...

    def setWEPKey(self, key: Optional[bytes], flags: CWCipherKeyFlags, index: int, error: Optional[object] = None) -> bool:
        """
        Sets the Wi-Fi interface WEP key.

        Args:
            key (Optional[bytes]): An NSData object containing the WEP key. Passing nil clears the WEP key for the Wi-Fi interface.
            flags (CWCipherKeyFlags): A bitmask indicating which CWCipherKeyFlags to use for the specified WEP key.
            index (int): An NSInteger indicating which default key index (1-4) to use for the specified key.
            error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

        Returns:
            bool: YES upon success, or NO if an error occurred.
        """
        ...

    def scanForNetworksWithSSID(self, ssid: Optional[bytes], error: Optional[object] = None) -> Optional[Set[CWNetwork]]:
        """
        Performs a scan for Wi-Fi networks and returns scan results to the caller.

        Args:
            ssid (Optional[bytes]): Probe request SSID. Pass an SSID to perform a directed scan for hidden Wi-Fi networks. This parameter is optional.
            error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

        Returns:
            Optional[Set[CWNetwork]]: An NSSet of CWNetwork objects, or None if an error occurs.
        """
        ...

    def scanForNetworksWithSSID_includeHidden(self, ssid: Optional[bytes], includeHidden: bool, error: Optional[object] = None) -> Optional[Set[CWNetwork]]:
        """
        Performs a scan for Wi-Fi networks and returns scan results to the caller.

        Args:
            ssid (Optional[bytes]): Probe request SSID. Pass an SSID to perform a directed scan for hidden Wi-Fi networks. This parameter is optional.
            includeHidden (bool): Indicate whether or not hidden networks should not be filtered from the returned scan results.
            error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

        Returns:
            Optional[Set[CWNetwork]]: An NSSet of CWNetwork objects, or None if an error occurs.
        """
        ...

    def scanForNetworksWithName(self, networkName: Optional[str], error: Optional[object] = None) -> Optional[Set[CWNetwork]]:
        """
        Performs a scan for Wi-Fi networks and returns scan results to the caller.

        Args:
            networkName (Optional[str]): Probe request SSID, encoded as an UTF-8 string. Pass a networkName to perform a directed scan for hidden Wi-Fi networks. This parameter is optional.
            error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

        Returns:
            Optional[Set[CWNetwork]]: An NSSet of CWNetwork objects, or None if an error occurs.
        """
        ...

    def scanForNetworksWithName_includeHidden(self, networkName: Optional[str], includeHidden: bool, error: Optional[object] = None) -> Optional[Set[CWNetwork]]:
        """
        Performs a scan for Wi-Fi


#     def setPower(self, power: bool, error: Optional[object] = None) -> bool:
#         """
#         Sets the Wi-Fi interface power state.

#         Args:
#             power (bool): A BOOL value indicating Wi-Fi power state. Specify YES to turn on the Wi-Fi interface.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             bool: YES upon success, or NO if an error occurred.
#         """
#         ...

#     def setWLANChannel(self, channel: 'CWChannel', error: Optional[object] = None) -> bool:
#         """
#         Sets the Wi-Fi interface channel.

#         Args:
#             channel (CWChannel): A CWChannel object.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             bool: YES upon success, or NO if an error occurred.
#         """
#         ...

#     def setPairwiseMasterKey(self, key: Optional[bytes], error: Optional[object] = None) -> bool:
#         """
#         Sets the Wi-Fi interface pairwise master key (PMK).

#         Args:
#             key (Optional[bytes]): An NSData object containing the pairwise master key (PMK). Passing nil clears the PMK for the Wi-Fi interface.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             bool: YES upon success, or NO if an error occurred.
#         """
#         ...

#     def setWEPKey(self, key: Optional[bytes], flags: CWCipherKeyFlags, index: int, error: Optional[object] = None) -> bool:
#         """
#         Sets the Wi-Fi interface WEP key.

#         Args:
#             key (Optional[bytes]): An NSData object containing the WEP key. Passing nil clears the WEP key for the Wi-Fi interface.
#             flags (CWCipherKeyFlags): A bitmask indicating which CWCipherKeyFlags to use for the specified WEP key.
#             index (int): An NSInteger indicating which default key index (1-4) to use for the specified key.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             bool: YES upon success, or NO if an error occurred.
#         """
#         ...

#     def scanForNetworksWithSSID(self, ssid: Optional[bytes], error: Optional[object] = None) -> Optional[Set[CWNetwork]]:
#         """
#         Performs a scan for Wi-Fi networks and returns scan results to the caller.

#         Args:
#             ssid (Optional[bytes]): Probe request SSID. Pass an SSID to perform a directed scan for hidden Wi-Fi networks. This parameter is optional.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             Optional[Set[CWNetwork]]: An NSSet of CWNetwork objects, or None if an error occurs.
#         """
#         ...

#     def scanForNetworksWithSSID_includeHidden(self, ssid: Optional[bytes], includeHidden: bool, error: Optional[object] = None) -> Optional[Set[CWNetwork]]:
#         """
#         Performs a scan for Wi-Fi networks and returns scan results to the caller.

#         Args:
#             ssid (Optional[bytes]): Probe request SSID. Pass an SSID to perform a directed scan for hidden Wi-Fi networks. This parameter is optional.
#             includeHidden (bool): Indicate whether or not hidden networks should not be filtered from the returned scan results.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             Optional[Set[CWNetwork]]: An NSSet of CWNetwork objects, or None if an error occurs.
#         """
#         ...

#     def scanForNetworksWithName(self, networkName: Optional[str], error: Optional[object] = None) -> Optional[Set[CWNetwork]]:
#         """
#         Performs a scan for Wi-Fi networks and returns scan results to the caller.

#         Args:
#             networkName (Optional[str]): Probe request SSID, encoded as an UTF-8 string. Pass a networkName to perform a directed scan for hidden Wi-Fi networks. This parameter is optional.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             Optional[Set[CWNetwork]]: An NSSet of CWNetwork objects, or None if an error occurs.
#         """
#         ...

#     def scanForNetworksWithName_includeHidden(self, networkName: Optional[str], includeHidden: bool, error: Optional[object] = None) -> Optional[Set[CWNetwork]]:
#         """
#         Performs a scan for Wi-Fi networks and returns scan results to the caller.

#         Args:
#             networkName (Optional[str]): Probe request SSID, encoded as an UTF-8 string. Pass a networkName to perform a directed scan for hidden Wi-Fi networks. This parameter is optional.
#             includeHidden (bool): Indicate whether or not hidden networks should not be filtered from the returned scan results.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             Optional[Set[CWNetwork]]: An NSSet of CWNetwork objects, or None if an error occurs.
#         """
#         ...

#     def associateToNetwork_password(self, network: CWNetwork, password: Optional[str], error: Optional[object] = None) -> bool:
#         """
#         Associates to a Wi-Fi network using the specified passphrase.

#         Args:
#             network (CWNetwork): The network to which the Wi-Fi interface will associate.
#             password (Optional[str]): The network passphrase or key. Required for association to WEP, WPA Personal, and WPA2 Personal networks.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             bool: YES upon success, or NO if an error occurred.
#         """
#         ...

#     def disassociate(self) -> None:
#         """
#         Disassociates from the current Wi-Fi network.
#         """
#         ...

#     def associateToEnterpriseNetwork_identity_username_password(self, network: CWNetwork, identity: Optional[SecIdentityRef], username: Optional[str], password: Optional[str], error: Optional[object] = None) -> bool:
#         """
#         Associates to an enterprise Wi-Fi network using the specified 802.1X credentials.

#         Args:
#             network (CWNetwork): The network to which the Wi-Fi interface will associate.
#             identity (Optional[SecIdentityRef]): The identity to use for IEEE 802.1X authentication. Holds the corresponding client certificate.
#             username (Optional[str]): The username to use for 802.1X authentication.
#             password (Optional[str]): The password to use for 802.1X authentication.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             bool: YES upon success, or NO if an error occurred.
#         """
#         ...

#     def startIBSSModeWithSSID_security_channel_password(self, ssidData: bytes, security: CWIBSSModeSecurity, channel: int, password: Optional[str], error: Optional[object] = None) -> bool:
#         """
#         Creates a computer-to-computer (IBSS) network.

#         Args:
#             ssidData (bytes): The SSID to use for the IBSS network. Pass nil to use the machine name as the IBSS network name.
#             security (CWIBSSModeSecurity): The CWIBSSModeSecurity type.
#             channel (int): The channel on which the IBSS network will be created.
#             password (Optional[str]): The password to be used. This paramter is required for kCWIBSSModeSecurityWEP40 or kCWIBSSModeSecurityWEP104 security types.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             bool: YES upon success, or NO if an error occurred.
#         """
#         ...

#     def commitConfiguration_authorization(self, configuration: CWConfiguration, authorization: Optional[SFAuthorization], error: Optional[object] = None) -> bool:
#         """
#         Commits a CWConfiguration for the given Wi-Fi interface.

#         Args:
#             configuration (CWConfiguration): The Wi-Fi configuration to commit to disk.
#             authorization (Optional[SFAuthorization]): An SFAuthorization object to use for authorizing the commit. This parameter is optional.
#             error (Optional[object]): An NSError object passed by reference, which upon return will contain the error if an error occurs. This parameter is optional.

#         Returns:
#             bool: YES upon success, or NO if an error occurred.
#         """
#         ...
