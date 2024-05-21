from typing import NewType

from .FoundationTypes import *

# Error Codes

CWErr = NewType('CWErr', NSInteger)
"""
Error codes corresponding to the CWErrorDomain domain.
"""

kCWNoErr: CWErr = 0
"""Success."""

kCWEAPOLErr: CWErr = 1
"""EAPOL-related error."""

kCWInvalidParameterErr: CWErr = -3900
"""Parameter error."""

kCWNoMemoryErr: CWErr = -3901
"""Memory allocation failed."""

kCWUnknownErr: CWErr = -3902
"""Unexpected error condition encountered for which no error code exists."""

kCWNotSupportedErr: CWErr = -3903
"""Operation not supported."""

kCWInvalidFormatErr: CWErr = -3904
"""Invalid protocol element field detected."""

kCWTimeoutErr: CWErr = -3905
"""Operation timed out."""

kCWUnspecifiedFailureErr: CWErr = -3906
"""Access point did not specify a reason for authentication/association failure."""

kCWUnsupportedCapabilitiesErr: CWErr = -3907
"""Access point cannot support all requested capabilities."""

kCWReassociationDeniedErr: CWErr = -3908
"""Reassociation was denied because the access point was unable to determine that an association exists."""

kCWAssociationDeniedErr: CWErr = -3909
"""Association was denied for an unspecified reason."""

kCWAuthenticationAlgorithmUnsupportedErr: CWErr = -3910
"""Specified authentication algorithm is not supported."""

kCWInvalidAuthenticationSequenceNumberErr: CWErr = -3911
"""Authentication frame received with an authentication sequence number out of expected sequence."""

kCWChallengeFailureErr: CWErr = -3912
"""Authentication was rejected because of a challenge failure."""

kCWAPFullErr: CWErr = -3913
"""Access point is unable to handle another associated station."""

kCWUnsupportedRateSetErr: CWErr = -3914
"""Interface does not support all of the rates in the basic rate set of the access point."""

kCWShortSlotUnsupportedErr: CWErr = -3915
"""Association denied because short slot time option is not supported by requesting station."""

kCWDSSSOFDMUnsupportedErr: CWErr = -3916
"""Association denied because DSSS-OFDM is not supported by requesting station."""

kCWInvalidInformationElementErr: CWErr = -3917
"""Invalid information element included in association request."""

kCWInvalidGroupCipherErr: CWErr = -3918
"""Invalid group cipher requested."""

kCWInvalidPairwiseCipherErr: CWErr = -3919
"""Invalid pairwise cipher requested."""

kCWInvalidAKMPErr: CWErr = -3920
"""Invalid authentication selector requested."""

kCWUnsupportedRSNVersionErr: CWErr = -3921
"""Invalid WPA/WPA2 version specified."""

kCWInvalidRSNCapabilitiesErr: CWErr = -3922
"""Invalid RSN capabilities specified in association request."""

kCWCipherSuiteRejectedErr: CWErr = -3923
"""Cipher suite rejected due to network security policy."""

kCWInvalidPMKErr: CWErr = -3924
"""PMK rejected by the access point."""

kCWSupplicantTimeoutErr: CWErr = -3925
"""WPA/WPA2 handshake timed out."""

kCWHTFeaturesNotSupportedErr: CWErr = -3926
"""Association was denied because the requesting station does not support HT features."""

kCWPCOTransitionTimeNotSupportedErr: CWErr = -3927
"""Association was denied because the requesting station does not support the PCO transition time required by the AP."""

kCWReferenceNotBoundErr: CWErr = -3928
"""No interface is bound to the CWInterface object."""

kCWIPCFailureErr: CWErr = -3929
"""Error communicating with a separate process."""

kCWOperationNotPermittedErr: CWErr = -3930
"""Calling process does not have permission to perform this operation."""

kCWErr: CWErr = -3931
"""Generic error, no specific error code exists to describe the error condition."""

# Physical Layer Modes

CWPHYMode = NewType('CWPHYMode', NSInteger)
"""
Type describing the IEEE 802.11 physical layer mode.
"""

kCWPHYModeNone: CWPHYMode = 0

kCWPHYMode11a: CWPHYMode = 1
"""IEEE 802.11a physical layer mode."""

kCWPHYMode11b: CWPHYMode  = 2
"""IEEE 802.11b physical layer mode."""

kCWPHYMode11g: CWPHYMode = 3
"""IEEE 802.11g physical layer mode."""

kCWPHYMode11n: CWPHYMode = 4
"""IEEE 802.11n physical layer mode."""

kCWPHYMode11ac: CWPHYMode = 5
"""IEEE 802.11ac physical layer mode."""

kCWPHYMode11ax: CWPHYMode = 6
"""IEEE 802.11ax physical layer mode."""

# Wi-Fi Interface Operating Modes

CWInterfaceMode = NewType('CWInterfaceMode', NSInteger)
"""Wi-Fi interface operating modes returned by -[CWInterface interfaceMode]."""

kCWInterfaceModeNone: CWInterfaceMode = 0
"""Interface is not in any mode."""

kCWInterfaceModeStation: CWInterfaceMode = 1
"""Interface is participating in an infrastructure network as a non-AP station."""

kCWInterfaceModeIBSS: CWInterfaceMode = 2
"""Interface is participating in an IBSS network."""

kCWInterfaceModeHostAP: CWInterfaceMode = 3
"""Interface is participating in an infrastructure network as an access point."""

# Wi-Fi Security Types

CWSecurity = NewType('CWSecurity', NSInteger)
"""Wi-Fi security types."""

kCWSecurityNone: CWSecurity = 0
"""Open System authentication."""

kCWSecurityWEP: CWSecurity = 1
"""WEP security."""

kCWSecurityWPAPersonal: CWSecurity = 2
"""WPA Personal authentication."""

kCWSecurityWPAPersonalMixed: CWSecurity = 3
"""WPA/WPA2 Personal authentication."""

kCWSecurityWPA2Personal: CWSecurity = 4
"""WPA2 Personal authentication."""

kCWSecurityPersonal: CWSecurity = 5
"""Alias for WPA/WPA2 Personal authentication."""

kCWSecurityDynamicWEP: CWSecurity = 6
"""Dynamic WEP security."""

kCWSecurityWPAEnterprise: CWSecurity = 7
"""WPA Enterprise authentication."""

kCWSecurityWPAEnterpriseMixed: CWSecurity = 8
"""WPA/WPA2 Enterprise authentication."""

kCWSecurityWPA2Enterprise: CWSecurity = 9
"""WPA2 Enterprise authentication."""

kCWSecurityEnterprise: CWSecurity = 10
"""Alias for WPA/WPA2 Enterprise authentication."""

kCWSecurityWPA3Personal: CWSecurity = 11
"""WPA3 Personal authentication."""

kCWSecurityWPA3Enterprise: CWSecurity = 12
"""WPA3 Enterprise authentication."""

kCWSecurityWPA3Transition: CWSecurity = 13
"""WPA3 Transition (WPA3/WPA2 Personal) authentication."""

kCWSecurityOWE: CWSecurity = 14
"""OWE security."""

kCWSecurityOWETransition: CWSecurity = 15
"""OWE Transition."""

kCWSecurityUnknown: CWSecurity = NSIntegerMax
"""Unknown security type."""

# IBSS Mode Security Types

CWIBSSModeSecurity = NewType('CWIBSSModeSecurity', NSInteger)
"""IBSS security types used in ad-hoc (IBSS) Wi-Fi networks."""

kCWIBSSModeSecurityNone: CWIBSSModeSecurity = 0
"""Open System authentication, no security."""

kCWIBSSModeSecurityWEP40: CWIBSSModeSecurity = 1
"""WEP 40-bit security."""

kCWIBSSModeSecurityWEP104: CWIBSSModeSecurity = 2
"""WEP 104-bit security."""

# Channel Width Types

CWChannelWidth = NewType('CWChannelWidth', NSInteger)
"""Channel width values."""

kCWChannelWidthUnknown: CWChannelWidth = 0
"""Unknown channel width."""

kCWChannelWidth20MHz: CWChannelWidth = 1
"""20MHz channel width."""

kCWChannelWidth40MHz: CWChannelWidth = 2
"""40MHz channel width."""

kCWChannelWidth80MHz: CWChannelWidth = 3
"""80MHz channel width."""

kCWChannelWidth160MHz: CWChannelWidth = 4
"""160MHz channel width."""

# Channel Band Types

CWChannelBand = NewType('CWChannelBand', NSInteger)
"""Channel band values."""

kCWChannelBandUnknown: CWChannelBand = 0
"""Unknown channel band."""

kCWChannelBand2GHz: CWChannelBand = 1
"""2.4GHz channel band."""

kCWChannelBand5GHz: CWChannelBand = 2
"""5GHz channel band."""

kCWChannelBand6GHz: CWChannelBand = 3
"""6GHz channel band."""

# Cipher Key Flags

CWCipherKeyFlags = NewType('CWCipherKeyFlags', NSUInteger)
"""Cipher key flags for wireless security."""

kCWCipherKeyFlagsNone: CWCipherKeyFlags = 0
"""No flags."""

kCWCipherKeyFlagsUnicast: CWCipherKeyFlags = 1 << 1
"""Cipher key for unicast packets."""

kCWCipherKeyFlagsMulticast: CWCipherKeyFlags = 1 << 2
"""Cipher key for multicast packets."""

kCWCipherKeyFlagsTx: CWCipherKeyFlags = 1 << 3
"""Cipher key for transmitted packets."""

kCWCipherKeyFlagsRx: CWCipherKeyFlags = 1 << 4
"""Cipher key for received packets."""

# Keychain Domain Types

CWKeychainDomain = NewType('CWKeychainDomain', NSInteger)
"""Keychain domain types used by CoreWLAN keychain methods."""

kCWKeychainDomainNone: CWKeychainDomain = 0
"""No keychain domain specified."""

kCWKeychainDomainUser: CWKeychainDomain = 1
"""The user keychain domain, potentially including iCloud keychain."""

kCWKeychainDomainSystem: CWKeychainDomain = 2
"""The system keychain domain."""

# Wi-Fi Event Types

CWEventType = NewType('CWEventType', NSInteger)
"""Wi-Fi event types used for monitoring Wi-Fi interface changes."""

kCWEventTypeNone: CWEventType = 0
"""No event type specified."""

kCWEventTypePowerDidChange: CWEventType = 1
"""Posted when the power state of any Wi-Fi interface changes."""

kCWEventTypeSSIDDidChange: CWEventType = 2
"""Posted when the current SSID of any Wi-Fi interface changes."""

kCWEventTypeBSSIDDidChange: CWEventType = 3
"""Posted when the current BSSID of any Wi-Fi interface changes."""

kCWEventTypeCountryCodeDidChange: CWEventType = 4
"""Posted when the adopted country code of any Wi-Fi interface changes."""

kCWEventTypeLinkDidChange: CWEventType = 5
"""Posted when the link state for any Wi-Fi interface changes."""

kCWEventTypeLinkQualityDidChange: CWEventType = 6
"""Posted when the RSSI or transmit rate for any Wi-Fi interface changes."""

kCWEventTypeModeDidChange: CWEventType = 7
"""Posted when the operating mode of any Wi-Fi interface changes."""

kCWEventTypeScanCacheUpdated: CWEventType = 8
"""Posted when the scan cache of any Wi-Fi interface is updated with new scan results."""

kCWEventTypeBtCoexStats: CWEventType = 9
"""Posted when Bluetooth coexistence statistics are updated."""

kCWEventTypeUnknown: CWEventType = NSIntegerMax
"""Unknown event type."""
