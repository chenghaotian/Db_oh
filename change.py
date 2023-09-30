# -*- coding: utf-8 -*-
et_dict = {
    "0": "000",
    "1": "001",
    "2": "010",
    "3": "011",
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111",
    ".": "."
}
st_dict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
    ".": "."
}


def tw(input_data):
    if "." in input_data:
        return input_data
    else:
        return input_data + ".0"


def et(input_data):
    if "." in input_data:
        start_out_list = []
        for i in input_data:
            start_out_list.append(et_dict[i])
        start_out = "".join(start_out_list).replace("0", " ").strip().replace(" ", "0")
        if start_out[-1] == ".":
            start_out += "0"
        return start_out
    else:
        out_list = []
        for i in input_data:
            out_list.append(et_dict[i])
        out = "".join(out_list).replace("0", " ").lstrip().replace(" ", "0")+".0"
        if out == ".0":
            return "0.0"
        else:
            return out


def tn(input_data):
    if "." in input_data:
        input_list = input_data.partition(".")
        start_data = input_list[0]
        end_data = input_list[2]
        start_data = int(start_data)
        b = []
        while True:
            if start_data <= 0:
                b.append("0")
                break
            if start_data % 2 == 1:
                start_data = (start_data - 1) / 2
                b.append("1")
            else:
                start_data = start_data / 2
                b.append("0")
        b.reverse()
        start_out_text = "".join(b).replace("0", " ").lstrip().replace(" ", "0")
        if start_out_text == "":
            start_out_text = "0"
        end_data = float("0." + end_data)
        end_b = []
        n = 0
        while True:
            end_data *= 2
            if n == 36:
                break
            if end_data <= 0:
                break
            if str(end_data)[0] == "1":
                end_data -= 1
                end_b.append("1")
            else:
                end_b.append("0")
            n += 1
        end_out_text = "".join(end_b).replace("0", " ").rstrip().replace(" ", "0")
    else:
        start_data = int(input_data)
        b = []
        while True:
            if start_data <= 0:
                b.append("0")
                break
            if start_data % 2 == 1:
                start_data = (start_data - 1) / 2
                b.append("1")
            else:
                start_data = start_data / 2
                b.append("0")
        b.reverse()
        start_out_text = "".join(b).replace("0", " ").lstrip().replace(" ", "0")
        if start_out_text == "":
            start_out_text = "0"
        end_out_text = "0"
    out = start_out_text + "." + end_out_text
    if out[-1] == ".":
        out += "0"
    return out


def st(input_data):
    if input_data == "0":
        return "0.0"
    out_list = []
    for i in input_data:
        out_list.append(st_dict[i])
    out = "".join(out_list)
    if "." in out:
        out = out.replace("0", " ").strip().replace(" ", "0")
        if out[-1] == ".":
            out += "0"
        if out[0] == ".":
            out = "0" + out
        return out
    else:
        return out.replace("0", " ").lstrip().replace(" ", "0") + ".0"


if __name__ == '__main__':
    print(st("F.A"))
