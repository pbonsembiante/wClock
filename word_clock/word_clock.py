from datetime import datetime

from num2words import num2words as n2w


class WordClock(object):
    __O_CLOCK = "o'clock"
    __DEFAULT_SECONDS = "ish"

    def get_time(self, in_time=None):
        if in_time is None:
            in_time = datetime.now().time()
        return " ".join(self.get_clock_info(in_time)).strip()

    def get_clock_info(self, in_time):
        hours = self.__get_hours(in_time)
        minutes = self.__get_minutes(in_time)
        seconds = self.__get_seconds(in_time)
        return hours, minutes, seconds

    @staticmethod
    def __get_hours(in_time):
        return n2w(in_time.hour).title()

    @staticmethod
    def __get_seconds(in_time):
        return WordClock.__DEFAULT_SECONDS \
            if in_time.second is not 0 and in_time.minute is not 0 \
            else ""

    @staticmethod
    def __get_minutes(in_time):
        return WordClock.__O_CLOCK \
            if in_time.minute is 0 \
            else n2w(in_time.minute)
