from .CoreWLANTypes import *

class CWChannel:
    """
    @class

    @abstract
    Represents an IEEE 802.11 channel.

    @discussion
    The CWChannel class is used by both CWInterface and CWNetwork as a representation of an IEEE 802.11 Wi-Fi channel.
    """

    def channelNumber(self) -> NSInteger:
        """
        @property

        @abstract 
        The channel number represented as an integer value.
        """
        ...

    def channelWidth(self) -> CWChannelWidth:
        """
        @property

        @abstract 
        The channel width as indicated by the CWChannelWidth type.
        """
        ...

    def channelBand(self) -> CWChannelBand:
        """
        @property

        @abstract
        The channel band as indicated by the CWChannelBand type.
        """
        ...

    def isEqualToChannel_(self, channel: CWChannel) -> bool:
        """
        @method

        @param channel
        The CWChannel with which to compare the receiver.

        @result 
        YES if the objects are equal, otherwise NO.

        @abstract 
        Determine CWChannel equality.

        @discussion 
        CWChannel objects are considered equal if all their corresponding properties are equal.
        """
        ...