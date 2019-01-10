def num_to_words(num):
    num_dict = {
            0: '',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            100: 'one hundred',
            1000: 'one thousand'
            }

    if num in num_dict.keys():
        return("{}".format(num_dict[num]))
    else:
        ones = num % 10
        tens = ((num % 100) - ones)
        huns = (num % 1000) - tens - ones

        if huns > 0:
            huns_ones = huns/100
        else:
            huns_ones = 0

        if huns_ones > 0 and (tens == 0 and ones == 0):
            return("{} hundred".format(num_dict[huns_ones]))
        elif huns_ones > 0 and tens > 0 and ones == 0:
            return("{} hundred and {}".format(num_dict[huns_ones],num_dict[tens]))
        elif huns_ones > 0 and tens == 0 and ones > 0:
            return("{} hundred and {}".format(num_dict[huns_ones],num_dict[ones]))
        elif huns_ones > 0 and tens > 0 and ones > 0:
            if tens < 20:
                return("{} hundred and {}".format(num_dict[huns_ones],num_dict[tens+ones]))
            else:
                return("{} hundred and {} {}".format(num_dict[huns_ones],num_dict[tens],num_dict[ones]))
        elif huns_ones == 0 and tens >= 20 and ones > 0:
            return("{} {}".format(num_dict[tens],num_dict[ones]))


def main():
    total = 0
    for x in range(1,1001):
        total += len(num_to_words(x).replace(" ",""))
    print(total)


if __name__ == '__main__':
    main()
