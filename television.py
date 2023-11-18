class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to set default values of Television Object
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        method to toggle whether the tv is on or off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        method to toggle the mute status of the TV between muted or not muted
        """
        if self.__muted:
            self.__muted = False
        else:
            self.__muted = True

    def channel_up(self) -> None:
        """
        method to increase channel number
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        method to decrease Channel number
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        method to increase TV volume
        """
        if self.__muted:
            self.__muted = False
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        method to decrease TV volume
        """
        if self.__muted:
            self.__muted = False
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        method to get current tv status
        :return: status of the TV's current power, channel, and volume
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
