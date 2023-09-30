# -*- coding: utf-8 -*-
import re
et_dict = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7",
    ".": "."
}
st_dict = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
    ".": "."
}


def tw(input_data: str):
    return input_data


def et(input_data: str):
    input_list = input_data.partition(".")
    start_data = input_list[0]
    end_data = input_list[2]
    start_data = "0" * (3-(len(start_data) % 3)) + start_data
    start_data_list = re.findall(r'.{3}', start_data)
    start_data_out = ""
    for i in start_data_list:
        start_data_out += et_dict[i]
    end_data = end_data + "0" * (3-(len(end_data) % 3))
    end_data_list = re.findall(r'.{3}', end_data)
    end_data_out = ""
    for i in end_data_list:
        end_data_out += et_dict[i]
    out = start_data_out + "." + end_data_out
    if out[0:1] == "0.":
        return out
    else:
        out = out.replace("0", " ").strip().replace(" ", "0")
        if out[-1] == ".":
            return out + "0"
        else:
            return out


def tn(input_data: str):
    data_list = input_data.partition(".")
    start_num = data_list[0]
    end_num = data_list[2]
    end_float = 0
    start_int = 0
    for i in range(0, len(end_num)):
        end_float += (int(end_num[i]) * (2 ** (-1 - i)))
    for i in range(0, len(start_num)):
        start_int += (int(start_num[-(1 + i)])) * (2 ** i)
    out = str(end_float + start_int)
    return out


def st(input_data: str):
    input_list = input_data.partition(".")
    start_data = input_list[0]
    end_data = input_list[2]
    start_data = "0" * (4-(len(start_data) % 4)) + start_data
    start_data_list = re.findall(r'.{4}', start_data)
    start_data_out = ""
    for i in start_data_list:
        start_data_out += st_dict[i]
    end_data = end_data + "0" * (4-(len(end_data) % 4))
    end_data_list = re.findall(r'.{4}', end_data)
    end_data_out = ""
    for i in end_data_list:
        end_data_out += st_dict[i]
    out = start_data_out + "." + end_data_out
    if out[0:1] == "0.":
        return out
    else:
        out = out.replace("0", " ").strip().replace(" ", "0")
        if out[-1] == ".":
            return out + "0"
        else:
            return out


if __name__ == '__main__':
    print(tn("0.0"))
