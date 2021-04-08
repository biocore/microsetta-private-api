import secrets

# 4.5 bits of entropy per character,
# need ~15 to get 64 bits entropy:
# 1/(2^32) chance of collision by
# birthday paradox
CHARSET22 = "ACEFHJKLMNPRTUVWXY3479"


class ActivationCode:
    @classmethod
    def generate(cls):
        prefix = "TMI"
        part1 = "".join([secrets.choice(CHARSET22) for i in range(5)])
        part2 = "".join([secrets.choice(CHARSET22) for i in range(5)])
        part3 = "".join([secrets.choice(CHARSET22) for i in range(5)])
        return "-".join([prefix, part1, part2, part3])
