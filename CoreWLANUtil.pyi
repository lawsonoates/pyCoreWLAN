from typing import Optional

from .CoreWLANTypes import *

def CWKeychainFindWiFiPassword(domain: CWKeychainDomain, ssid: NSData, password: Optional[NSString] = None) -> OSStatus:
    """
    @method

    @param domain 
    The keychain domain, which determines which keychain will be used.

    @param ssid
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @param password 
    An NSString passed by reference, which upon return will contain the Wi-Fi keychain password for the specified SSID.
    This parameter is optional.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Finds and returns (by reference) the password for the specified SSID and keychain domain.
    """
    ...

def CWKeychainSetWiFiPassword(domain: CWKeychainDomain, ssid: NSData, password: NSString) -> OSStatus:
    """
    @method

    @param domain 
    The keychain domain, which determines which keychain will be used.

    @param ssid
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @param password 
    The Wi-Fi network password.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Sets the Wi-Fi network keychain password for the specified SSID and keychain domain.
    """
    ...

def CWKeychainDeleteWiFiPassword(domain: CWKeychainDomain, ssid: NSData) -> OSStatus:
    """
    @method

    @param domain
    The keychain domain, which determines which keychain will be used.

    @param ssid
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Deletes the password for the specified SSID and keychain domain.
    """
    ...

def CWKeychainFindWiFiEAPUsernameAndPassword(domain: CWKeychainDomain, ssid: NSData, username: Optional[NSString] = None, password: Optional[NSString] = None) -> OSStatus:
    """
    @method

    @param domain
    The keychain domain, which determines which keychain will be used.

    @param ssid
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @param username 
    An NSString passed by reference, which upon return will contain the 802.1X username for the specified SSID.
    This parameter is optional.

    @param password
    An NSString passed by reference, which upon return will contain the 802.1X password for the specified SSID.
    This parameter is optional.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Finds and returns the 802.1X username and password stored for the specified SSID and keychain domain.
    """
    ...

def CWKeychainSetWiFiEAPUsernameAndPassword(domain: CWKeychainDomain, ssid: NSData, username: Optional[NSString] = None, password: Optional[NSString] = None) -> OSStatus:
    """
    @method

    @param domain
    The keychain domain, which determines which keychain will be used.

    @param ssid
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @param username
    The 802.1X username.

    @param password
    The 802.1X password. This parameter is optional.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Sets the 802.1X username and password for the specified SSID and keychain domain.
    """
    ...

def CWKeychainDeleteWiFiEAPUsernameAndPassword(domain: CWKeychainDomain, ssid: NSData) -> OSStatus:
    """
    @method

    @param domain
    The keychain domain, which determines which keychain will be used.

    @param ssid
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Deletes the 802.1X username and password for the specified SSID and keychain domain.
    """
    ...

def CWKeychainCopyWiFiEAPIdentity(domain: CWKeychainDomain, ssid: NSData, identity: Optional[SecIdentityRef] = None) -> OSStatus:
    """
    @method

    @param domain
    The keychain domain, which determines which keychain will be used.

    @param ssid
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @param identity 
    A SecIdentityRef passed by reference, which upon return will contain the SecIdentityRef associated with the specified SSID.
    This parameter is optional.  The returned value must be released by the caller.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Finds and returns the identity stored for the specified SSID and keychain domain.
    """
    ...

def CWKeychainSetWiFiEAPIdentity(domain: CWKeychainDomain, ssid: NSData, identity: Optional[SecIdentityRef] = None) -> OSStatus:
    """
    @method

    @param domain
    The keychain domain, which determines which keychain will be used.

    @param ssid
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @param identity 
    The identity containing the certificate to use for 802.1X authentication.
    Passing nil clears any identity association for the specified SSID.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Associates an identity to the specified SSID and keychain domain.
    """
    ...

def CWKeychainCopyEAPIdentityList(identityList: Optional[CFArrayRef] = None) -> OSStatus:
    """
    @method

    @param identityList 
    A CFArrayRef passed by reference, which upon return will be populated with a list of SecIdentityRef objects.
    This parameter is optional.  The returned value must be released by the caller.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract 
    Finds and returns all available identities.
    """
    ...

def CWKeychainCopyEAPUsernameAndPassword(ssidData: CFDataRef, username: Optional[CFStringRef] = None, password: Optional[CFStringRef] = None) -> OSStatus:
    """
    @method

    @param ssidData
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @param username
    A CFStringRef passed by reference, which upon return will contain the 802.1X username for the specified SSID.
    This parameter is optional.  The returned value must be released by the caller.

    @param password
    A CFStringRef passed by reference, which upon return will contain the 802.1X password for the specified SSID.
    This parameter is optional.  The returned value must be released by the caller.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract
    Finds and returns the 802.1X username and password stored for the specified SSID.
    The keychain used is determined by the SecPreferencesDomain of the caller as returned by SecKeychainGetPreferenceDomain().
    """
    ...

def CWKeychainSetEAPUsernameAndPassword(ssidData: CFDataRef, username: Optional[CFStringRef] = None, password: Optional[CFStringRef] = None) -> OSStatus:
    """
    @method

    @param ssidData
    The service set identifier (SSID) which is used to uniquely identify the keychain item.

    @param username
    The 802.1X username.

    @param password
    The 802.1X password. This parameter is optional.

    @result
    An OSStatus error code indicating whether or not a failure occurred.
    <i>errSecSuccess</i> indicates no error occurred.

    @abstract
    Sets the 802.1X username and password
    """
    ...