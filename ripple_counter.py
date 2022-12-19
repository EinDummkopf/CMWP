from time import sleep
from ram import latch

class Counter:
    def __init__(self, bit_quantity:int) -> None:
        self.Q = [latch() for i in range(bit_quantity-1)]
        self.trigger = True
        self._counter()

    def _counter(self):
        Clk = False
        while self.trigger:
            # Oscillator
            Clk = not(Clk)
            sleep(0.3)
            
    def output(self, Clk_bar):
        pass
