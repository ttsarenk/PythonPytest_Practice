import re


def get_eid(log):
    log_file = open(log, "r")
    log_list = log_file.readlines()
    pattern = "D:TUpdaterController::SetUniqueParam\(429\): eid: "
    eid_list = []
    for x in log_list:
        if re.search(pattern, x):
            eid_list.append(x[(x.find("PDO")):])
        else:
            continue
    log_file.close()
    # найти в логе две последние записи eid
    upd_list = eid_list[-2:]

    # вывести в консоль две строки "Предпоследние eid: " и "Последние eid: "
    print("\nPlease, find 2 last eid strings below >>\n")
    for x in upd_list:
        print(x)

    # найти отличия в ключах и значениях в последнем и предпоследнем словарях eid
    dict1 = dict((a.strip(), int(b.strip()))
                 for a, b in (element.split('.')
                              for element in upd_list[0].split(';')))
    dict2 = dict((a.strip(), int(b.strip()))
                 for a, b in (element.split('.')
                              for element in upd_list[1].split(';')))
    set1 = set(dict1.items())
    set2 = set(dict2.items())
    # print("More details:", set1 ^ set2) #uncomment for more details
    return dict(set1 ^ set2)


if __name__ == '__main__':
    try:
        dictDif = get_eid("yupdate-exec-yabrowser.log")
    except FileNotFoundError:
        print("The log file wasn't found. Try again.")
    except Exception as err3:
        print("Error:", err3)
    else:
        print("\nThe difference in values between the previous and the last eid:\n", dictDif)
