import secrets

# 4.5 bits of entropy per character,
# need ~15 to get 64 bits entropy:
# 1/(2^32) chance of collision by
# birthday paradox
CHARSET22 = "ACEFHJKLMNPRTUVWXY3479"


class ActivationCode:
    @staticmethod
    def generate_code():
        prefix = "TMI"
        part1 = "".join([secrets.choice(CHARSET22) for i in range(5)])
        part2 = "".join([secrets.choice(CHARSET22) for i in range(5)])
        part3 = "".join([secrets.choice(CHARSET22) for i in range(5)])
        return "-".join([prefix, part1, part2, part3])

    def __init__(self, email, code, activated=False):
        self.email = email
        self.code = code
        self.activated = activated

    def to_api(self):
        return {
            "email": self.email,
            "code": self.code,
            "activated": self.activated
        }

    @classmethod
    def from_dict(cls, row):
        return cls(row["email"], row["code"], row["activated"])

