from time import sleep

# Oscillator
Clk = False
while True:
    print(int(Clk))
    Clk = not(Clk)
    sleep(0.3)