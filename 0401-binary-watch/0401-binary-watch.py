class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        possible_time = []
        for hour_hand in range(12):
            for minute_hand in range(60):
                if hour_hand.bit_count() + minute_hand.bit_count() == turnedOn:
                    print(f"hour: {hour_hand} and bit_count: {hour_hand.bit_count()}")
                    print(f"minute: {minute_hand} and bit_count: {minute_hand.bit_count()}")
                    if minute_hand < 10:
                        minute = "0" + str(minute_hand)
                        time = str(hour_hand) + ":" + str(minute)
                    else:
                        time = str(hour_hand) + ":" + str(minute_hand)
                    possible_time.append(time)

        return possible_time