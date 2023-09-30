# -*- coding: utf-8 -*-
import change
import figure
import collections

tw = ["1", "0", "."]
et = ["0", "1", "2", "3", "4", "5", "6", "7", "."]
tn = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ""]
st = ["0", "1", "2", "3", "4", "5", "6", "7",
      "8", "9", "A", "B", "C", "D", "E", "F", "."]
sn_list = [tw, et, tn, st]


def main(input_text: str, input_type: int):
    if input_text == "":
        return ["0", "0", "0", "0", False]
    text = input_text.upper()
    for i in text:
        if i not in sn_list[input_type]:
            return ["0", "0", "0", "0", False]
        elif collections.Counter(text)['.'] >= 2:
            return ["0", "0", "0", "0", False]
    if input_type == 0:
        tw_data = change.tw(text)
    elif input_type == 1:
        tw_data = change.et(text)
    elif input_type == 2:
        tw_data = change.tn(text)
    else:
        tw_data = change.st(text)
    tw_out = figure.tw(tw_data)
    et_out = figure.et(tw_data)
    tn_out = figure.tn(tw_data)
    st_out = figure.st(tw_data)
    return [tw_out, et_out, tn_out, st_out, True]
