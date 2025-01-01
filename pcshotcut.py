
import csv
import random
from colorama import Back, Fore
with open(r"input_arbID.csv") as f:
    reader = csv.reader(f)
    out_str = ""
    for x, y in zip(reader, range(1, 100)):
        arbid = int(x[0], 16)  # (''.join(x))
        # to_decimal=int(arbid,16)
        data_from = "C"
        list_data = [random.choice(data_from) for x in range(16)]
        # print(list_data)
        data = (str(y)+("".join(list_data)))
        # print(y)
        out_str += (Back.WHITE + Fore.BLACK+"ID="+(str(arbid)) +
                    ","+"Type=D"+","+"Length=8"+","+"Data="+(data[0:16]) +
                    ","+"CycleTime=1000"+","+"IDFormat=hex"+Fore.RESET+Back.RESET + "\n")
    print(out_str)
