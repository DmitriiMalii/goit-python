from datetime import datetime, timedelta


def congratulate(user):
    """
    displaying a list of colleagues who need to be congratulated on their birthday
    """

    m = ['Monday:']
    t = ['Tuesday:']
    w = ['Wednesday:']
    th = ['Thursday:']
    f = ['Friday:']
    result = ''

    d1 = datetime.now().date()
    # d1 = datetime(year=2021, month=12, day=28).date() //manual setting the current date
    delta = timedelta(days=5-d1.weekday())
    start = d1 + delta                          # beginning and end of the week
    end = start + timedelta(days=7)

    for colleague in user:
        # checking the conditions for changing the year
        if colleague['birthday'].month == 1 and d1.month == 12:
            d2 = datetime(year=d1.year+1, month=colleague['birthday'].month, day=colleague['birthday'].day)
        else:
            d2 = datetime(year=d1.year, month=colleague['birthday'].month, day=colleague['birthday'].day)
        if start < d2.date() < end:
            if d2.strftime('%A') == 'Monday':
                m.append(colleague['name'])
            elif d2.strftime('%A') == 'Tuesday':
                t.append(colleague['name'])
            elif d2.strftime('%A') == 'Wednesday':
                w.append(colleague['name'])
            elif d2.strftime('%A') == 'Thursday':
                th.append(colleague['name'])
            elif d2.strftime('%A') == 'Friday':
                f.append(colleague['name'])
            else:
                m.append(colleague['name'])

    for i in m, t, w, th, f:
        if len(i) > 1:
            result = result + ' '.join(i) + '\n'

    return result


Anton = {
    'name': 'Anton',
    'birthday': datetime(year=1986, month=1, day=3)
}

Serg = {
    'name': 'Serg',
    'birthday': datetime(year=1991, month=5, day=21)
}


user = [Anton, Serg]
print(congratulate(user))
