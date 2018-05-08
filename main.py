# -----------------------------------
# 名称：日历小程序
# 描述：控制台程序   Windows平台编写
# 时间：2017.8.9
# 作者：mr.zhu
# -----------------------------------


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthdays = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']


def main():
    rilititle()
    year = int(input('输入年：'))
    rpyear = monthdaysnum(year)
    if rpyear == 1:
        monthdays[1] = 29
    else:
        monthdays[1] = 28
    month_mod = input('查看多个月份的日历？（y/n）：')
    if month_mod == 'n':
        start_month = end_month = int(input('输入月份：'))
    else:
        start_month = int(input('输入起始月份：'))
        end_month = int(input('输入结束月份：'))
    for month in range(start_month, end_month+1):
        startweek = daysweek(year, month, 1)
        if startweek == 0:
            startweek = 7
        monthP(months[month-1], startweek, monthdays[month-1])
    input('回车退出')


def rilititle():
    print('***************************************************************\n'
          '                |========|      |==========                    \n'
          '                ||      ||      ||   ||                        \n'
          '                ||______||      || ==||===|                    \n'
          '                ||------||      ||   //  ||                    \n'
          '                ||      ||      ||  //   ||                    \n'
          '                |========|      || //    ||                    \n'
          '***************************************************************')


def monthdaysnum(year):
    if year % 400 == 0:
        return 1
    if year % 4 == 0:
        if year % 100 != 0:
            return 1
        else:
            return 0
    else:
        return 0


def daysweek(year, month, day):
    year_one,year_two = int(str(year)[:2]), int(str(year)[2:])
    if month == 1 or month == 2:
        return(year_two-1 + (year_two-1)//4 + year_one//4 - 2*year_one + 26*(month+12 + 1)//10 + day-1)%7
    return (year_two + year_two//4 + year_one//4 - 2*year_one + 26*(month+1)//10 + day-1)%7


def monthP(months, startweek, days):
    print('\n\n%12s%s' % (' ', months))
    for week in weeks:
        print(' %s ' % week, end='')
    print('\n----------------------------')
    flg = startweek
    for space in range(1, startweek):
        print('    ', end='')
    for day in range(1, days+1):
        print(' %02d ' % day, end='')
        if flg % 7 == 0:
            print()
        flg += 1
    print('\n')


if __name__ == '__main__':
    main()
