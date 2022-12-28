class latch:
    def __init__(self) -> None:
        self.q = 0
        self.q_bar = 0
        self.D_type_latch()

    def R_S_flip_flop(self, R, S):
        self.q_bar = int(not(S or self.q))
        self.q = int(not(R or self.q_bar))
        self.q_bar = int(not(S or self.q))
        # print(f"Q: {self.q}, Q-bar: {self.q_bar} \n -----------")

    def D_type_latch(self, D=0, Clk=0):
        R=int(not(D) and Clk)
        S=int(D and Clk)
        # print(f"R: {R}, S: {S}")
        self.R_S_flip_flop(R, S)

class RAM:
    # 8x1 RAM
    def __init__(self) -> None:
        self._8bit_latch = [latch() for i in range(8)]
        self.__D_part = [i.q for i in self._8bit_latch]
    
    def __call__(self, s2, s1, s0, D, W):
        O = self.ECO_DEMUX(s2, s1, s0, W)
        for i, j in zip(self._8bit_latch, O):
            i.D_type_latch(D=D, Clk=j)
        self.__D_part = [i.q for i in self._8bit_latch]
        return self.ECO_MUX(self.__D_part, s2, s1, s0)
        # print(f"OUTPUT: {self.ECO_MUX(self.D_part, s2, s1, s0)}")

    # 8:1 MUX
    @staticmethod
    def ECO_MUX(D:list, s2, s1, s0) -> int:
        return int(any([D[0] & (not s0) & (not s1) & (not s2),
                        D[1] & s0 & (not s1) & (not s2),
                        D[2] & s1 & (not s0) & (not s2),
                        D[3] & s0 & s1 & (not s2),
                        D[4] & s2 & (not s0) & (not s1),
                        D[5] & s0 & s2 & (not s1),
                        D[6] & s1 & s2 & (not s0),
                        D[7] & s0 & s1 & s2]))     
    
    #  3-8 DECODER
    @staticmethod
    def ECO_DEMUX(s2, s1, s0, D) -> list:
        return [D & (not s0) & (not s1) & (not s2),
                D & s0 & (not s1) & (not s2),
                D & s1 & (not s0) & (not s2),
                D & s0 & s1 & (not s2),
                D & s2 & (not s0) & (not s1),
                D & s0 & s2 & (not s1),
                D & s1 & s2 & (not s0),
                D & s0 & s1 & s2]
    
if __name__ == "__main__":
    M = RAM()
    M(0, 0, 0, 1, 1)
    print(f"Data parts: {list(reversed(M.__D_part))}")

# L = latch()
# print(L.q, L.q_bar)
# L.D_type_latch(1, 1)
# print(L.q, L.q_bar)