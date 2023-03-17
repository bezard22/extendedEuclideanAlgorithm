class ExtendedEuclideanAlgorithm:
    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self.r = []
        self.s = []
        self.t = []

    def eea(self, r0: int, r1: int) -> int:
        self.r = [r0, r1]
        while r1 > 0:
            r1, r0 = r0 % r1, r1
            self.r.append(r1)
            
        return r0
