from collections import defaultdict

class ExtendedEuclideanAlgorithm:
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self.steps = []
        self.explanation = []
        self.subs = {}
        self.subStr = {}
    
    def linearBreakdown(self, dividend: int, modulus: int, remainder: int, quotient: int) -> None:
        rep = {dividend: 1, modulus: -quotient}
        while True:
            if sorted(rep.keys()) == sorted([self.dividend, self.modulus]):
                expStr0 = f"{remainder}"
                expStr1 = "".join([f"[{rep[key]}] * {key} + " for key in rep.keys()])[:-3]
                self.explanation[-1][1].append(expStr0 + " = " + expStr1)
                self.subs[remainder] = rep
                self.subStr[remainder] = expStr1
                return rep[self.dividend], rep[self.modulus]
            else:
                expStr0 = f"{remainder}"
                expStr1 = "".join([f"{rep[key]} * {key} + " for key in rep.keys()])[:-3]
                self.explanation[-1][1].append(expStr0 + " = " + expStr1)
                newRep = defaultdict(int)
                for key in rep.keys():
                    if key in self.subs.keys():
                        expStr1 = expStr1.replace(f"* {key}", f"* ({self.subStr[key]})")
                        for newKey in self.subs[key]:
                            newRep[newKey] += self.subs[key][newKey] * rep[key]
                    else:
                        newRep[key] += rep[key]
                self.explanation[-1][1].append(expStr0 + " = " + expStr1)
                rep = newRep
    
    def formatExplanation(self) -> None:
        expStr = ""
        for step in self.explanation:
            for substep in step[1]:
                expStr += f"{step[0]}\t| {substep}\n"
        return expStr

    def eea(self, dividend: int, modulus: int) -> int:
        self.reset
        self.dividend = dividend
        self.modulus = modulus
        s = None
        t= None
        while modulus > 0:
            remainder = dividend % modulus
            quotient = int(dividend / modulus)
            self.explanation.append([f"{dividend} = {quotient} * {modulus} + {remainder}", []])
            if remainder > 0:
                s, t = self.linearBreakdown(dividend, modulus, remainder, quotient)
            self.steps.append((dividend, modulus, quotient, remainder))
            modulus, dividend = remainder, modulus
        return dividend, s, t