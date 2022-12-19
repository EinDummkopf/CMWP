from time import sleep
from ram import latch

class Counter:
    def __init__(self, bit_quantity:int) -> None:
        self.Q = [latch() for i in range(bit_quantity-1)]
        [self.Q[i].D_type_latch() for i in range(bit_quantity-1)]
        self.Clk = False
        self.Oscillator()
        
    def Oscillator(self):
        self.Clk = not(self.Clk)
        sleep(0.5)
        print(self._counter(int(self.Clk)))
        self.Oscillator()

    def _counter(self, clk):
        self.Q[0].D_type_latch(Clk=clk, D=self.Q[0].q_bar)
        self.Q[1].D_type_latch(Clk=self.Q[0].q_bar, D=self.Q[1].q_bar)

        return [self.Q[1].q, self.Q[0].q]
        # self.Q[2].D_type_latch(Clk=self.Q[1].q_bar, D=self.Q[2].q_bar)
        # return [self.Q[2].q ,self.Q[1].q, self.Q[0].q, int(not(clk))]

Counter(3)