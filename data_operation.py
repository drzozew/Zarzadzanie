from datetime import timedelta


def time_paras(time_list):
    try:
        time_sum = timedelta(0)
        for time in time_list:
            time_from_list = time
            hour, minute, second = map(int, time_from_list.split(':'))
            get_time = timedelta(hours=hour, minutes=minute, seconds=second)
            time_sum += get_time
        return time_sum
    except TypeError:
        mesage = 0
        return mesage


def money_for_time(time_list, money_per_hour):
    try:
        time_sum = 0
        for time in time_list:
            time_from_list = time
            hour, minute, second = map(int, time_from_list.split(':'))
            get_time = (hour*3600)+(minute*60)+second
            time_sum += get_time
        time_value = (time_sum * (money_per_hour/3600))
        return time_value
    except TypeError:
        mesage = 0
        return mesage


def money_left(cash_out_list, money_for_time):
    try:
        cash_out = 0
        for cash in cash_out_list:
            cash_out += int(cash)
        output = money_for_time - cash_out
        print(f"Możesz jeszcze wypłacić {round(output, 2)} zł.")
    except TypeError:
        mesage = 0
        return mesage


def time_in_mins_list(time_list):
    time_value = []
    try:
        for time in time_list:
            time_from_list = time
            hour, minute, second = map(int, time_from_list.split(':'))
            get_time = ((hour*3600)+(minute*60)+second)//60
            time_value.append(get_time)
        return time_value
    except TypeError:
        mesage = 0
        return mesage
