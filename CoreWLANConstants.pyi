from typing import Optional
from .CoreWLANTypes import *

CWErrorDomain: Optional[NSString] = None
"""
@constant CWErrorDomain

@abstract 
Error domain corresponding to the CWErr type.
"""

CWPowerDidChangeNotification: Optional[NSString] = None
"""
@constant CWPowerDidChangeNotification

@abstract
Posted when the power state of the Wi-Fi interface changes.

@discussion
The <i>object</i> for this notification is the corresponding Wi-Fi interface name.
This notification does not contain a <i>userInfo</i> dictionary.
"""

CWSSIDDidChangeNotification: Optional[NSString] = None
"""
@constant CWSSIDDidChangeNotification

@abstract
Posted when the SSID of the Wi-Fi interface changes.

@discussion 
The <i>object</i> for this notification is the corresponding Wi-Fi interface name.
This notification does not contain a <i>userInfo</i> dictionary.
"""

CWBSSIDDidChangeNotification: Optional[NSString] = None
"""
@constant CWBSSIDDidChangeNotification

@abstract
Posted when the BSSID of the Wi-Fi interface changes.

@discussion
The <i>object</i> for this notification is the corresponding Wi-Fi interface name.
This notification does not contain a <i>userInfo</i> dictionary.
"""

CWLinkDidChangeNotification: Optional[NSString] = None
"""
@constant CWLinkDidChangeNotification

@abstract
Posted when the link of the Wi-Fi interface changes.

@discussion
The <i>object</i> for this notification is the corresponding Wi-Fi interface name.
This notification does not contain a <i>userInfo</i> dictionary.
"""

CWModeDidChangeNotification: Optional[NSString] = None
"""
@constant CWModeDidChangeNotification

@abstract
Posted when the operating mode of the Wi-Fi interface changes.

@discussion
The <i>object</i> for this notification is the corresponding Wi-Fi interface name.
This notification does not contain a <i>userInfo</i> dictionary.
"""

CWCountryCodeDidChangeNotification: Optional[NSString] = None
"""
@constant CWCountryCodeDidChangeNotification

@abstract
Posted when the adopted country code of the Wi-Fi interface changes.

@discussion
The <i>object</i> for this notification is the corresponding Wi-Fi interface name.
This notification does not contain a <i>userInfo</i> dictionary.
"""

CWScanCacheDidUpdateNotification: Optional[NSString] = None
"""
@constant CWScanCacheDidUpdateNotification

@abstract
Posted when the scan cache of the Wi-Fi interface is updated with new scan results.

@discussion
The <i>object</i> for this notification is the corresponding Wi-Fi interface name.
This notification does not contain a <i>userInfo</i> dictionary.
"""

CWLinkQualityDidChangeNotification: Optional[NSString] = None
"""
@constant CWLinkQualityDidChangeNotification

@abstract
Posted when the link quality of the current Wi-Fi association changes.

@discussion
The <i>object</i> for this notification is the corresponding Wi-Fi interface name.
This notification does not contain a <i>userInfo</i> dictionary.
"""

CWLinkQualityNotificationRSSIKey: Optional[NSString] = None
"""
@constant CWLinkQualityNotificationRSSIKey

@abstract
NSNumber containing the current RSSI value for the Wi-Fi interface.

@discussion
Found in the <i>userInfo</i> dictionary for the <i>CWLinkQualityChangedNotification</i>.
"""

CWLinkQualityNotificationTransmitRateKey: Optional[NSString] = None
"""
@constant CWLinkQualityNotificationTransmitRateKey

@abstract
NSNumber containing the current transmit rate for the Wi-Fi interface.

@discussion
Found in the <i>userInfo</i> dictionary for the <i>CWLinkQualityChangedNotification</i>.
"""