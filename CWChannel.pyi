from .CoreWLANTypes import *

class CWChannel:
    """
    Represents an IEEE 802.11 channel.
    """
    
    # def __init__(self, info: Dict[str, str]):
    #         self._info = info

    def channelNumber(self) -> NSInteger:
        """
        The channel number represented as an integer value.
        """
        ...

    def channelWidth(self) -> CWChannelWidth:
        """
        The channel width as indicated by the CWChannelWidth type.
        """
        ...

    # @property
    def channelBand(self) -> CWChannelBand:
        """
        The channel band as indicated by the CWChannelBand type.
        """
        ...

    def isEqualToChannel_(self, channel: CWChannel) -> bool:
        """
        Determine CWChannel equality.

        Args:
            channel (CWChannel): The CWChannel with which to compare the
            receiver.

        Returns:
            bool: YES if the objects are equal, otherwise NO.
        """
        ...