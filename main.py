import re
ss = []
while True:
    a = input('Введите число или нажмите "Enter": ')
    r = re.search(r'^[2-5]', a)
    if len(a) == 0:
        if len(ss) != 0:
            print(f"Ваши оценки: {''.join(str(ss)).replace('[', '').replace(']', '')}")
            print(f"Итоговая оценка: {sum(ss) / len(ss)}")
        input()
        break
    elif r and len(a) == 1:
        ss.append(int(a))
    else:
        print("Неккоректная оценка")