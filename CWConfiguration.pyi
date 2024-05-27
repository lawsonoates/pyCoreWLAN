from .CoreWLANTypes import *
from .CWNetworkProfile import *

class CWConfiguration:
    """
    @class

    @abstract 
    Encapsulates the system configuration for a given Wi-Fi interface.

    @discussion
    The CWConfiguration class contains basic network configuration settings and also the list of preferred networks.
    CWConfiguration is an immutable object. For changing configuration settings and/or the preferred networks list, see CWMutableConfiguration.
    """

    def networkProfiles(self) -> NSOrderedSet[CWNetworkProfile]:
        """
        @property

        @result
        An NSOrderedSet of CWNetworkProfile objects.

        @abstract
        Returns the preferred networks list.

        @discussion 
        The order of the ordered set corresponds to the order the preferred networks list.
        """
        ...

    def requireAdministratorForAssociation(self) -> bool:
        """
        @property

        @result
        YES if the preference is enabled, NO otherwise.

        @abstract 
        Returns the preference to require an administrator password to change networks.

        @discussion
        If YES, the user may be prompted to enter an administrator password upon attempting to join a Wi-Fi network.
        This preference is enforced at the API layer.
        """
        ...

    def requireAdministratorForPower(self) -> bool:
        """
        @property

        @result
        YES if the preference is enabled, NO otherwise.

        @abstract 
        Returns the preference to require an administrator password to change the interface power state.

        @discussion
        If YES, the user may be prompted to enter an administrator password upon attempting to turn Wi-Fi on or off.
        This preference is enforced at the API layer.
        """
        ...

    def requireAdministratorForIBSSMode(self) -> bool:
        """
        @property

        @result
        YES if the preference is enabled, NO otherwise.

        @abstract
        Returns the preference to require an administrator password to create a computer-to-computer network.

        @discussion
        If YES, the user may be prompted to enter an administrator password upon attempting to create an IBSS network.
        This preference is enforced at the API layer.
        """
        ...

    def rememberJoinedNetworks(self) -> bool:
        """
        @property

        @result
        YES if the preference is enabled, NO otherwise.

        @abstract
        Returns the preference to remember all Wi-Fi networks joined unless otherwise specified by the user when joining a particular Wi-Fi network.
        """
        ...

    def configuration(cls) -> CWConfiguration:
        """
        @method

        @abstract 
        Convenience method for getting a CWConfiguration object.
        """
        ...

    def init(self) -> None:
        """
        @method

        @abstract 
        Initializes a CWConfiguration object.
        """
        ...

    def initWithConfiguration_(self, configuration: CWConfiguration) -> CWConfiguration:
        """
        @method

        @param configuration 
        A CWConfiguration object.

        @result 
        A CWConfiguration object.

        @abstract 
        Initializes a CWConfiguration object with the properties of an existing CWConfiguration object.
        """
        ...

    def configurationWithConfiguration_(cls, configuration: CWConfiguration) -> CWConfiguration:
        """
        @method

        @param configuration
        A CWConfiguration object.

        @result
        A CWConfiguration object.

        @abstract
        Convenience method for getting a CWConfiguration object initialized with the properties of an existing CWConfiguration object.
        """
        ...

    def isEqualToConfiguration_(self, configuration: CWConfiguration) -> bool:
        """
        @method

        @param configuration 
        The CWConfiguration with which to compare the receiver.

        @result 
        YES if the objects are equal, NO otherwise.

        @abstract 
        Determine CWConfiguration equality.

        @discussion 
        CWConfiguration objects are considered equal if all their corresponding properties are equal.
        """
        ...

class CWMutableConfiguration(CWConfiguration):
    """
    @class

    @abstract
    Mutable subclass of CWConfiguration.  Use this class for changing configuration settings and/or the preferred networks list.

    @discussion
    To commit configuration changes, use -[CWInterface commitConfiguration:authorization:error:].
    """

    def networkProfiles(self) -> NSOrderedSet[CWNetworkProfile]:
        """
        @property

        @abstract
        Add, remove, or update the preferred networks list.
        """
        ...

    def requireAdministratorForAssociation(self) -> bool:
        """
        @property

        @abstract
        Set the preference to require an administrator password to change networks.
        """
        ...

    def requireAdministratorForPower(self) -> bool:
        """
        @property

        @abstract
        Set the preference to require an administrator password to change the interface power state.
        """
        ...

    def requireAdministratorForIBSSMode(self) -> bool:
        """
        @property

        @abstract
        Set the preference to require an administrator password to create a computer-to-computer network.
        """
        ...

    def rememberJoinedNetworks(self) -> bool:
        """
        @property

        @abstract
        Set the preference to require an administrator password to change networks.
        """
        ...