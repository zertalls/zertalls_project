import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import math, random
from tkinter import *
from tkinter import ttk, scrolledtext
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.ttk import Combobox

taskList = []
graphListTask = []

graphIntervalResult = []
rangeInterval = []

graphList = []
graphListFind = []

wordList = []
axInWindow = []

find = 0

x0_axis, x1_axis = 0, 14
y0_axis, y1_axis = 0, None


def retrunInterval(interval):

    interval = interval.replace(' ', '')
    intervals, xToSend, intervalToSend = [], [], []
    i, j = -1, -1
    for el in interval:
        i += 1
        if el == '(':
            first = i
        elif el == ')':
            last = i
            for el in interval[first + 1:last]:
                j += 1
                if el == ',':
                    intervals.append(interval[first + 1:first + 1 + j])
                    intervals.append(interval[first + 2 + j:last])
            else:
                j = -1
    else:
        intervals = list(map(int, intervals))
        for x in range(1, len(intervals), 2):
            x0, x1 = intervals[x - 1], intervals[x]
            rangeInterval.append(x1-x0)
            xToSend.append(np.linspace(x0, x1, 500))
            intervalToSend.append([x0, x1])

    return intervals, intervalToSend, xToSend

def createLine(k, b, time=None, param=None):
    X1 = []
    Y1 = []
    if time == None:
        for x in np.linspace(x0_axis, x1_axis, 500):
            y = k * x + b
            X1.append(x)
            Y1.append(y)
        else:
            if param == 'CREATE':
                return Y1
            elif type(param) == list and param[0] == 'INTERVAL':
                intervals, interval, intervalsX = retrunInterval(param[1])
                for x0y0 in interval:
                    graphIntervalResult.append(['line', k, b, x0y0])
                valInterval = []
                for x in intervalsX:
                    y = k * x + b
                    valInterval.append(y)
                else:
                    k = 1
                    for y in valInterval:
                        x = np.linspace(0, intervals[k] - intervals[k-1], 500)
                        if len(param) == 2:
                            plt.plot(x, y, label='line, interval [{}, {}]'.format(intervals[k - 1], intervals[k]))
                            plt.legend()
                            k += 2
                        else:
                            param[2].plot(x, y, label='line, interval [{}, {}]'.format(intervals[k - 1], intervals[k]))
                            param[2].legend()
                            k += 2

            elif type(param) == list and param[0] == 'WORD':
                axInWindow.append(param[1])
                param[1].plot(X1, Y1, label='line')
                param[1].legend()
            else:
                plt.plot(X1, Y1, label='line')
                plt.legend()
    elif time == 'not in range':
        return 'Неопределено'
    else:
        return k * time + b


def createSinus(A, w, f, time=None, param=None):

    if time == None:
        x = np.linspace(x0_axis, x1_axis, 500)
        y = A * np.sin(w * x + f)
        if param == 'CREATE':
            return y
        elif type(param) == list and param[0] == 'INTERVAL':
            intervals, interval, intervalsX = retrunInterval(param[1])
            for x0y0 in interval:
                graphIntervalResult.append(['sin', A, w, f, x0y0])
            valInterval = []
            for x in intervalsX:
                y = A * np.sin(w * x + f)
                valInterval.append(y)
            else:
                k = 1
                for y in valInterval:
                    x = np.linspace(0, intervals[k] - intervals[k-1], 500)
                    if len(param) == 2:
                        plt.plot(x, y, label='sinus, interval [{}, {}]'.format(intervals[k - 1], intervals[k]))
                        plt.legend()
                        k += 2
                    else:
                        param[2].plot(x, y, label='sinus, interval [{}, {}]'.format(intervals[k - 1], intervals[k]))
                        param[2].legend()
                        k += 2
        elif type(param) == list and param[0] == 'WORD':
            axInWindow.append(param[1])
            param[1].plot(x, y, label='sinus')
            param[1].legend()

        else:
            plt.plot(x, y, label='sinus')
            plt.legend()
    elif time == 'not in range':
        return 'Неопределено'
    else:
        return A * np.sin(w * time + f)


def createCosinus(A, w, f, time=None, param=None):

    if time == None:
        x = np.linspace(x0_axis, x1_axis, 500)
        y = A * np.cos(w * x + f)
        if param == 'CREATE':
            return y
        elif type(param) == list and param[0] == 'INTERVAL':
            intervals, interval, intervalsX = retrunInterval(param[1])
            for x0y0 in interval:
                graphIntervalResult.append(['cos', A, w, f, x0y0])
            valInterval = []
            for x in intervalsX:
                y = A * np.sin(w * x + f)
                valInterval.append(y)
            else:
                k = 1
                for y in valInterval:
                    x = np.linspace(0, intervals[k] - intervals[k-1], 500)
                    if len(param) == 2:
                        plt.plot(x, y, label='cosinus, interval [{}, {}]'.format(intervals[k - 1], intervals[k]))
                        plt.legend()
                        k += 2
                    else:
                        param[2].plot(x, y, label='cosinus, interval [{}, {}]'.format(intervals[k - 1], intervals[k]))
                        param[2].legend()
                        k += 2

        elif type(param) == list and param[0] == 'WORD':

            axInWindow.append(param[1])
            param[1].plot(x, y, label='cosinus')
            param[1].legend()
        else:
            plt.plot(x, y, label='cosinus')
            plt.legend()
    elif time == 'not in range':
        return 'Неопределено'
    else:
        return A * np.cos(w * time + f)

def createWord(param):
        #WORD_CREATOR =[опция, сабплот, имя, дик, х]
    if type(param) == list and param[0] == 'WORD_CREATOR':
        k = - 1
        razriad = ''
        for val in param[3]:
            k -= 10
            razriad = razriad + str(val) + ' '
            param[1].hlines(-1 + k, 0, param[3][val], label=val)
            param[1].vlines(param[3][val], -1 + k, k + 5)
            param[1].hlines(k + 5, param[3][val], param[4])
        else:
            axInWindow.append(param[1])
            razriad = razriad.rstrip().replace(' ', ', ')
            param[1].set_title(param[2] + '\n(Неисправные разряды: {})'.format(razriad))
            param[1].get_yaxis().set_visible(False)


def createNewSignal(name, formula, graphs, time=None, param=None):
    primaryGraphs = []

    if time == None:
        for graph in graphs:
            if graph[0] == 'line':
                line = createLine(graph[1], graph[2], param='CREATE')
                print(line)
                primaryGraphs.append(line)
            elif graph[0] == 'sin':
                sinus = list(createSinus(graph[1], graph[2], graph[3], param='CREATE'))
                print(sinus)
                primaryGraphs.append(sinus)
            elif graph[0] == 'cos':
                cosinus = list(createCosinus(graph[1], graph[2], graph[3], param='CREATE'))
                print(cosinus)
                primaryGraphs.append(cosinus)
    else:
        for graph in graphs:
            if graph[0] == 'line':
                line = createLine(graph[1], graph[2], time)
                print(line)
                primaryGraphs.append(line)
            elif graph[0] == 'sin':
                sinus = float(createSinus(graph[1], graph[2], graph[3], time))
                print(sinus)
                primaryGraphs.append(sinus)
            elif graph[0] == 'cos':
                cosinus = float(createCosinus(graph[1], graph[2], graph[3], time))
                print(cosinus)
                primaryGraphs.append(cosinus)

    paramFunc = []
    intervalValues = {}
    names = ['d', 'e', 'f', 'g', 'h', 'i', 'z']

    def ind_calc(state, a, b):

        def identificate(a=None, first=None, last=None):

            # sign = ['+', '-', '*', '/']

            def calculate(a, b, sign):

                if sign == '+':
                    if time == None:
                        if type(a) == list and type(b) == list:
                            return list(map(lambda x, y: x + y, a, b))
                        elif type(a) == list:
                            return list(map(lambda x: x + b, a))
                        else:
                            return list(map(lambda x: x + a, b))
                    else:
                        return a + b

                elif sign == '-':
                    if time == None:
                        if type(a) == list and type(b) == list:
                            return list(map(lambda x, y: x - y, a, b))
                        elif type(a) == list:
                            return list(map(lambda x: x - b, a))
                        else:
                            return list(map(lambda x: x - a, b))
                    else:
                        return a - b

                elif sign == '*':
                    if time == None:
                        if type(a) == list and type(b) == list:
                            return list(map(lambda x, y: x * y, a, b))
                        elif type(a) == list:
                            return list(map(lambda x: x * b, a))
                        else:
                            return list(map(lambda x: x * a, b))
                    else:
                        return a * b

                elif sign == '/':
                    if time == None:
                        if type(a) == list and type(b) == list:
                            return list(map(lambda x, y: x / y, a, b))
                        elif type(a) == list:
                            return list(map(lambda x: x / b, a))
                        else:
                            return list(map(lambda x: x / a, b))
                    else:
                        return a / b


            if a == 'a':
                a = primaryGraphs[0]
            elif a == 'b':
                a = primaryGraphs[1]
            elif a == 'c':
                a = primaryGraphs[2]
            elif a in sign:
                a = sign[sign.index(a)]
            elif a == None:
                pass
            else:
                if '.' in a:
                    a = float(a)
                elif a in intervalValues:
                    a = intervalValues[a]
                else:
                    a = int(a)

            paramFunc.append(a)

            nonlocal func, names
            if last != None:
                try:
                    if func[first - 1] == '(' or func[last + 1] == ')':
                        intervalValues.update({names[0]: paramFunc[0]})
                        func = func.replace(func[first - 1:last + 1], names[0])
                        names.pop(0)
                    else:
                        intervalValues.update({names[0]: paramFunc[0]})
                        func = func.replace(func[first:last], names[0])
                        names.pop(0)
                    paramFunc.clear()
                except IndexError:
                    intervalValues.update({names[0]: paramFunc[0]})
                    func = func.replace(func[first:last], names[0])
                    names.pop(0)
                    paramFunc.clear()

            elif len(paramFunc) == 3:
                print('calc: {} {} {}'.format(paramFunc[0], paramFunc[2], paramFunc[1]))
                result = calculate(paramFunc[0], paramFunc[2], paramFunc[1])
                print('res {}'.format(result))
                paramFunc.clear()
                paramFunc.append(result)

        sign = ['+', '-', '*', '/', ')', '(']
        if state == 'bracket':
            first = a
            while a < b:
                if func[a] not in sign:
                    try:
                        if func[a + 1] not in sign:
                            identificate(func[a] + func[a + 1])
                            a += 2
                        else:
                            identificate(func[a])
                            a += 1
                    except IndexError:
                        identificate(func[a])
                        a += 1
                else:
                    identificate(func[a])
                    a += 1
            else:
                identificate(first=first, last=a)

        elif state == 'division' or state == 'multiplication' or state == 'plus/minus':

            k = a + 1
            val0, val1 = '', ''
            while func[a] not in sign and a >= 0:
                val0 = a
                a -= 1
            else:
                identificate(func[val0:k])
                identificate(func[k])
                try:
                    while func[b] not in sign and b < len(func):
                        val1 = b
                        b += 1
                    else:
                        identificate(func[k + 1:val1 + 1])
                        identificate(first=val0, last=val1 + 1)
                except IndexError:
                    identificate(func[k + 1:val1 + 1])
                    identificate(first=val0, last=val1 + 1)

    func = formula
    func = func.replace(' ', '')
    print(func)
    j = 0
    while j < len(func):
        if func[j] == '(':
            start = j + 1
            j += 1
        elif func[j] == ')':
            end = j
            ind_calc('bracket', start, end)
            j = 0
        else:
            j += 1
    else:
        j = 0
        while j < len(func):

            if func[j] == '/':

                ind_calc('division', j - 1, j + 1)
                j = 0
            else:
                j += 1
        else:
            j = 0
            while j < len(func):
                if func[j] == '*':
                    ind_calc('multiplication', j - 1, j + 1)
                    j = 0
                else:
                    j += 1
            else:
                j = 0
                while j < len(func):
                    if func[j] == '+' or func[j] == '-':
                        print(func[0:j])
                        ind_calc('plus/minus', j - 1, j + 1)
                        j = 0
                    else:
                        j += 1

        for y in intervalValues:
            pass
        else:
            if time == None:
                plt.plot(np.linspace(x0_axis, x1_axis, 500), intervalValues[y], label=name)
            else:
                return intervalValues[y]

def click_acceptParam(list, listBox=None):
    if list in graphList or list[0] == 'task' or list == graphListFind or list == graphList:
        pass
    else:
        graphList.insert(0, list)

    if list[0] == 'line':
        if list[1] == 0:
            listBox.insert(0, 'y = {}'.format(list[2]))
        elif list[2] == 0:
            listBox.insert(0, 'y = {} * x'.format(list[1]))
        else:
            listBox.insert(0, 'y = {} * x + {}'.format(list[1], list[2]))

    elif list[0] == 'sin' or list[0] == 'cos':
        if list[1] == 1:
            if list[2] == 0:
                listBox.insert(0, 'y = {})'.format(list[3]))
            else:
                listBox.insert(0, 'y = {}({}x + {})'.format(list[0], list[1], list[2], list[3]))
        elif list[2] == 0:
            listBox.insert(0, 'y = {}'.format(list[3]))
        elif list[3] == 0:
            listBox.insert(0, 'y = {}({}x'.format(list[0], list[1], list[2], list[3]))
        else:
            listBox.insert(0, 'y = {} * {}({}x + {})'.format(list[1], list[0], list[2], list[3]))

    elif list[0] == 'step':
        listBox.insert(0, 'Cтупенька (H = {}, lenght = ({}, {}))'.format(list[3], list[1], list[2]))

    elif list[0] == 'mass':
        listBox.insert(0, 'Массив от {} до {}'.format(list[1], list[2]))

    elif list[0] == 'task':
        taskList.insert(0, list)
        values = []
        for task in taskList:
            for value in task[1:]:
                if value == list[2]:
                    break
                values.append(value)

        comboTask.config(values=values)
        listBoxTask.delete(0, listBoxTask.size())
        graphListTask.clear()
        comboTask.current(0)

    elif list[0] == 'word':

        wordList.insert(0, list)
        listBox.insert(0, 'Слово "{}"'.format(list[2]))

    elif list[0] == 'newSig':
        listBox.insert(0, '{}'.format(list[1]))



def click_openFile():
    def deleteNone(a):
        list = []
        for i in a[::]:
            list.append(i)
        else:
            list2 = []
            for j in list:
                if (j != '_'):
                    list2.append(j)
            else:
                return ''.join(list2)

    file = askopenfile(mode='r', filetypes=[('Text files', '*.txt')])

    click_deleteSignals()
    wordList.clear()
    for line in file:
        nameOfGraph = deleteNone(line[0:8])

        if nameOfGraph == 'line':
            click_acceptParam(['line', int(deleteNone(line[8:11])), int(deleteNone(line[11:14]))], listBox)

        elif nameOfGraph == 'sin':
            click_acceptParam(['sin', int(deleteNone(line[8:11])), int(deleteNone(line[11:14])),
                               int(deleteNone(line[14:17]))], listBox)
        elif nameOfGraph == 'cos':
            click_acceptParam(['cos', int(deleteNone(line[8:11])), int(deleteNone(line[11:14])),
                               int(deleteNone(line[14:17]))], listBox)
        elif nameOfGraph == 'step':
            click_acceptParam(['step', int(deleteNone(line[8:11])), int(deleteNone(line[11:14])),
                               int(deleteNone(line[14:17]))], listBox)
        elif nameOfGraph == 'mass':
            click_acceptParam(['mass', int(deleteNone(line[8:11])), int(deleteNone(line[11:14]))], listBox)

        elif nameOfGraph == 'word':
            print(line[8:11])
            print(line[12:45])
            print(line[45:55])
            print(line[5:])
            if deleteNone(line[45:55]) == 'correct':
                click_acceptParam(['word', int(deleteNone(line[8:11])), deleteNone(line[12:45]),
                                   deleteNone(line[45:55]).strip()], listBox)

                # click_acceptParam(['word', int(deleteNone(line[8:11])), deleteNone(line[11:19]),
                #                    deleteNone(line[19:28]).strip()], listBox)
            else:
                capVal = []
                num = ''
                for i in line[55:]:
                    if i != '_':
                        num = num + i

                    else:
                        capVal.append(int(num))
                        num = ''
                else:
                    newWord = {}
                    for cap in range(0, int(len(capVal) / 2)):
                        newWord.setdefault(capVal[cap], capVal[cap +int(len(capVal)/2)])
                    capVal = newWord

                click_acceptParam(['word', int(deleteNone(line[8:11])), deleteNone(line[12:45]),
                                   deleteNone(line[45:55]).strip(), capVal], listBox)

def click_createGraph():
    lineDig = None
    currentTime = None
    active = None

    def graphDig(time, active, option=None):

        if time == None or time > x1_axis or time < x0_axis:
            return 0

        nonlocal lineDig, currentTime
        try:
            if type(lineDig) == list:
                for ax in lineDig:
                    lineDig = ax
                    lineDig.remove()
            else:
                lineDig.remove()

        except AttributeError:
            pass
        finally:
            values = []
            num = 0
            currentTime = time

            output.delete(1.0, END)

            if option == 'WORD_IN':
                lineDig = []
                for axx in axInWindow:
                    ymin, ymax = axx.get_ylim()
                    axx.set_ylim(ymin, ymax)
                    lineDig.append(axx.vlines(time, ymin, ymax))

            else:
                ymin, ymax = plt.ylim()
                lineDig = plt.vlines(time, ymin, ymax)


            output.delete(1.0, END)
            k = 0
            if active == 'default':
                signals = graphListTask
            else:
                signals = graphIntervalResult

            TheRealTime = []
            TheRealTime.append(time)
            for graph in signals:
                time0 = TheRealTime[0]
                if graph[0] == 'line':
                    if signals == graphIntervalResult:
                        if time0 > graph[3][1] - graph[3][0] or time0 < 0:
                            time0 = 'not in range'
                            k = ''
                        else:
                            k = graph[3][0]
                        text = 'Линия на интервале [{}, {}]\n'.format(graph[3][0], graph[3][1])
                    else:
                        text = 'GraphLine №{}\n'.format(num+1)
                    value = createLine(graph[1], graph[2], time0 + k)
                    values.append(text + 'Значение = {}\n\n'.format(value))
                elif graph[0] == 'sin':
                    if signals == graphIntervalResult:
                        if time0 > graph[4][1] - graph[4][0] or time0 < 0:
                            time0 = 'not in range'
                            k = ''
                        else:
                            k = graph[4][0]
                        text = 'Синус на интервале [{}, {}]\n'.format(graph[4][0], graph[4][1])
                    else:
                        text = 'GraphSinus №{}\n'.format(num+1)
                    value = createSinus(graph[1], graph[2], graph[3], time0 + k)
                    values.append(text + 'Значение = {}\n\n'.format(value))
                elif graph[0] == 'cos':
                    if signals == graphIntervalResult:
                        if time0 > graph[4][1] - graph[4][0] or time0 < 0:
                            time0 = 'not in range'
                            k = ''
                        else:
                            k = graph[4][0]
                        text = 'Косинус на интервале [{}, {}]\n'.format(graph[4][0], graph[4][1])
                    else:
                        text = 'GraphCosinus №{}\n'.format(num+1)
                    value = createCosinus(graph[1], graph[2], graph[3], time0 + k)
                    values.append(text + 'Значение = {}\n\n'.format(value))
                elif graph[0] == 'newSig':
                    value = createNewSignal(graph[1], graph[2], graph[3], time)
                    values.append(('{}\nЗначение = {}\n\n'.format(graph[1], value)))

                num += 1

            else:
                toolbar.draw()
                values.reverse()
                for value in values:
                    output.insert(1.0, value)
                else:
                    output.insert(1.0, 'Оцифровка по уровню\n\n')
                    values.clear()

    def graphOpen(mode=None, x=None, k=0, gs=None, incorrWords=None, scaling=None):
        global y0_axis, y1_axis, x1_axis, active
        if mode == 'default':
            if k == 0:
                x1_axis = 14
                option = ['DEFAULT']
            else:
                x1_axis = x
                ax = fig.add_subplot(gs[0:3, :])
                gs.update(wspace=0.5, hspace=0.5)
                plt.subplots_adjust(left=0.07, bottom=0.04, right=0.98, top=0.98)
                option = ['WORD', ax]

                j = 3
                i = 0
                m = 0
                while i <= 3:
                    if i % 3 == 0 and i > 0:
                        j += 1
                        i = 0
                        continue
                    else:
                        pass

                    if m == k:
                        break
                    else:
                        ax = fig.add_subplot(gs[j, i])
                        wordParam = ['WORD_CREATOR', ax, incorrWords[m][2], incorrWords[m][4], x]
                        createWord(param=wordParam)
                        i += 1
                        m += 1

            for listOfParam in graphListTask:
                if listOfParam[0] == 'line':
                    createLine(listOfParam[1], listOfParam[2], param=option)
                elif listOfParam[0] == 'sin':
                    createSinus(listOfParam[1], listOfParam[2], listOfParam[3], param=option)
                elif listOfParam[0] == 'cos':
                    createCosinus(listOfParam[1], listOfParam[2], listOfParam[3], param=option)
                elif listOfParam[0] == 'newSig':
                    createNewSignal(listOfParam[1], listOfParam[2], listOfParam[3], param=option)

            else:
                active = 'default'
                if scaling == None:
                    if y0_axis == 0 and y1_axis == None:
                        ymin, ymax = plt.ylim()
                        plt.ylim(ymin, ymax)
                    else:
                        plt.ylim(y0_axis, y1_axis)
                else:
                    plt.xlim()
                    plt.ylim(scaling[2], scaling[3])


        elif mode == 'interval':
            if numOfWords >= 1:
                axInWindow[len(axInWindow) - 1].cla()
            else:
                plt.cla()

            for index in graphInterval:
                if graphInterval[index][1] == '':
                    pass
                else:
                    paramForInter = ['INTERVAL', graphInterval[index][1]] if numOfWords == 0 else\
                        ['INTERVAL', graphInterval[index][1], axInWindow[len(axInWindow) - 1]]

                    if graphInterval[index][0] == 'line':
                        createLine(graphListTask[index][1], graphListTask[index][2],
                                   param=paramForInter)
                    elif graphInterval[index][0] == 'sin':
                        createSinus(graphListTask[index][1], graphListTask[index][2], graphListTask[index][3],
                                    param=paramForInter)
                    elif graphInterval[index][0] == 'cos':
                        createCosinus(graphListTask[index][1], graphListTask[index][2], graphListTask[index][3],
                                     param=paramForInter)
            else:
                active = 'interval'
                if numOfWords == 0:
                    if y0_axis == 0 and y1_axis == None:
                        ymin, ymax = plt.ylim()
                        plt.ylim(ymin, ymax)
                    else:
                        plt.ylim(y0_axis, y1_axis)

                    rangeInterval.sort()
                    plt.xlim(0, rangeInterval[len(rangeInterval) - 1])
                    toolbar.draw()
                else:
                    if y0_axis == 0 and y1_axis == None:
                        ymin, ymax = axInWindow[len(axInWindow) - 1].get_ylim()
                        axInWindow[len(axInWindow) - 1].set_ylim(ymin, ymax)
                    else:
                        axInWindow[len(axInWindow) - 1].set_ylim(y0_axis, y1_axis)

                    rangeInterval.sort()
                    axInWindow[len(axInWindow) - 1].set_xlim(0, rangeInterval[len(rangeInterval) - 1])
                    toolbar.draw()


                #if numOfWords == 0:


                # else:
                #     if y0_axis == 0 and y1_axis == None:
                #         ymin, ymax = axInWindow[len(axInWindow) - 1].get_ylim()
                #         axInWindow[len(axInWindow) - 1].set_ylim(ymin, ymax)
                #     else:
                #         axInWindow[len(axInWindow) - 1].set_ylim(y0_axis, y1_axis)
                #
                #     rangeInterval.sort()
                #     axInWindow[len(axInWindow) - 1].set_xlim(0, rangeInterval[len(rangeInterval) - 1])
                #     toolbar.draw()




    # def pan__zoom(event):
    #     nonlocal currentTime
    #     if toolbar.mode == 'pan/zoom':
    #         if event.button == 1 or event.button == 3:
    #             graphDig(currentTime)
    #             return toolbar.draw()

    def selectTime(event):
       global active
       if toolbar.mode == 'pan/zoom':
        def pan__zoom(event):
            nonlocal currentTime
            if event.button == 1 or event.button == 3:
                graphDig(currentTime, active)


            return toolbar.draw()

        cid1 = fig.canvas.mpl_connect('motion_notify_event', pan__zoom)

       else:
           if numOfWords >= 1:
                return graphDig(event.xdata, active, option='WORD_IN')
           else:
               return graphDig(event.xdata, active)

    def changeAxis(x1, y1, x2, y2):
        global y0_axis, y1_axis, x0_axis, x1_axis, active

        x0_axis, x1_axis = int(x1), int(x2)
        y0_axis, y1_axis = int(y1), int(y2)

        plt.cla()

        if active == 'default':
            graphOpen(mode='default', scaling=[x0_axis, x1_axis, y0_axis, y1_axis])
        elif active == 'interval':
            graphOpen(mode='interval')

        toolbar.draw()
        #window.destroy()

    def cancelAxis(status=None):
        global y0_axis, y1_axis, x0_axis, x1_axis, active

        plt.cla()

        if active == 'default' or status == 'default':
            x0_axis, x1_axis = 0, 14
            y0_axis, y1_axis = 0, None
            graphOpen(mode='default')

        elif active == 'interval':
            graphOpen(mode='interval')

        toolbar.draw()

        # if window == None:
        #     pass
        # else:
        #     window.destroy()

    # def click_optionDig():
    #
    #     window6 = Tk()
    #     window6.title('Отображение сигналов')
    #     w = (window6.winfo_screenwidth() // 2) - 510
    #     h = (window6.winfo_screenheight() // 2) - 500
    #     window6.geometry('200x150+{}+{}'.format(w, h))
    #     window6.resizable(width=False, height=False)
    #
    #     labelOpt_dig = Label(window6, text='Масштабирование', font=("Arial", 10))
    #     labelOpt_dig.place(x=0, y=0)
    #
    #     labelOpt_x = Label(window6, text='По оси X от:', font=("Arial", 10))
    #     labelOpt_x.place(x=10, y=20)
    #
    #     integer_x = IntVar()
    #     intOpt_x = Entry(window6, width=5, textvariable=integer_x)
    #     intOpt_x.place(x=90, y=22)
    #
    #     labelOpt_x2 = Label(window6, text='до', font=("Arial", 10))
    #     labelOpt_x2.place(x=126, y=20)
    #
    #     integer_x2 = IntVar()
    #     intOpt_x2 = Entry(window6, width=5, textvariable=integer_x2)
    #     intOpt_x2.place(x=150, y=22)
    #
    #     labelOpt_y = Label(window6, text='По оси Y от:', font=("Arial", 10))
    #     labelOpt_y.place(x=10, y=40)
    #
    #     integer_y = IntVar()
    #     intOpt_y = Entry(window6, width=5, textvariable=integer_y)
    #     intOpt_y.place(x=90, y=42)
    #
    #     labelOpt_y2 = Label(window6, text='до', font=("Arial", 10))
    #     labelOpt_y2.place(x=126, y=40)
    #
    #     integer_y2 = IntVar()
    #     intOpt_y2 = Entry(window6, width=5, textvariable=integer_y2)
    #     intOpt_y2.place(x=150, y=42)
    #
    #     btnOpt_acc = Button(window6, text='Принять', command=lambda: changeAxis(window6, intOpt_x.get(), intOpt_y.get(),
    #                                                                             intOpt_x2.get(), intOpt_y2.get()))
    #     btnOpt_acc.place(x=0, y=100)
    #
    #     btnOpt_cancel = Button(window6, text='Сброс', command=lambda: cancelAxis(window6, status='default'))
    #     btnOpt_cancel.place(x=60, y=100)

    def setInterval(event):

        def setInterval():
            txtSigName['state'] = 'normal'
            txtSigName.delete(0, END)
            txtSigInter.delete(0, END)
            txtSigInter['state'] = 'normal'

            select = list(listBoxTaskInter.curselection())[0]
            click_acceptParam(graphListTask[select], txtSigName)
            txtSigName['state'] = 'disabled'
            if graphInterval[select] != '':
                txtSigInter.insert(0, graphInterval[select][1])
            return select

        nonlocal lastIndex

        if lastIndex == None:
            lastIndex = setInterval()
        else:
            graphInterval[lastIndex][1] = txtSigInter.get()
            lastIndex = setInterval()


    def createInterval(mode=None):
        if mode == 'default':
            if len(rangeInterval) == 0:
                pass
            else:
                rangeInterval.clear()
                graphIntervalResult.clear()
            if txtSigInter.get() != None:
                select = list(listBoxTaskInter.curselection())[0]
                if graphInterval[select][1] == '' or graphInterval[select][1] != txtSigInter.get():
                    graphInterval[select][1] = txtSigInter.get()
                    graphOpen(mode='interval')
                elif graphInterval[select][1] == txtSigInter.get():
                    graphOpen(mode='interval')
            else:
                pass

        elif mode == 'delete':
            cancelAxis()


    def intervalInp(inp):
        try:
            lastSymbol = inp[len(inp) - 1]
        except IndexError:
            lastSymbol = ' '

        key = ord(lastSymbol)

        if key in range(48, 57) or key in [32, 40, 41, 44]:
            return True
        else:
            return False

    numOfWords, valsX, words, option = 0, [], [], None

    fig = plt.figure(figsize=(11, 11))

    for listOfParam in graphListTask:
        if listOfParam[0] == 'word':
            if listOfParam[3] != 'correct':
                numOfWords += 1
                words.append(listOfParam)
                valsX.extend(listOfParam[4].values())
    else:
        if numOfWords == 0:
            graphOpen(mode='default')
        else:
            valsX.sort()
            X = valsX[len(valsX) - 1] + 10
            gs = None
            if numOfWords <= 3:
                gs = gridspec.GridSpec(4, numOfWords)
            elif numOfWords < 6:
                gs = gridspec.GridSpec(5, 3)

            graphOpen(mode='default', x=X, k=numOfWords, gs=gs, incorrWords=words)

    try:
        window5 = Tk()
        window5.title('Оцифровка сигналов по времени')
        window5.state('zoomed')

        output = scrolledtext.ScrolledText(window5, width=99, height=60)
        output.place(x=5, y=190)

        # mainmenu5 = Menu(window5)
        # window5.config(menu=mainmenu5)
        # option_dig = Menu(mainmenu5, tearoff=0)
        # option_dig.add_command(label='Отображение сигналов', command=click_optionDig)
        # mainmenu5.add_cascade(label='Настройка', menu=option_dig)

        frameTop = LabelFrame(window5, text='Масштабирование', font=("Arial", 10))
        frameTop.place(x=500, y=0)
        l0 = Label(frameTop)
        l0.pack(side=LEFT, padx=153, pady=70)

        labelOpt_x = Label(window5, text='По оси X от:', font=("Arial", 10))
        labelOpt_x.place(x=505, y=25)

        integer_x = IntVar()
        intOpt_x = Entry(window5, width=5, textvariable=integer_x)
        intOpt_x.place(x=585, y=25)

        labelOpt_x2 = Label(window5, text='до', font=("Arial", 10))
        labelOpt_x2.place(x=621, y=25)

        integer_x2 = IntVar()
        intOpt_x2 = Entry(window5, width=5, textvariable=integer_x2)
        intOpt_x2.place(x=643, y=25)

        labelOpt_y = Label(window5, text='По оси Y от:', font=("Arial", 10))
        labelOpt_y.place(x=505, y=55)

        integer_y = IntVar()
        intOpt_y = Entry(window5, width=5, textvariable=integer_y)
        intOpt_y.place(x=585, y=55)

        labelOpt_y2 = Label(window5, text='до', font=("Arial", 10))
        labelOpt_y2.place(x=621, y=55)

        integer_y2 = IntVar()
        intOpt_y2 = Entry(window5, width=5, textvariable=integer_y2)
        intOpt_y2.place(x=643, y=55)
        #
        btnOpt_acc = Button(window5, text='Принять', font=("Arial", 10), command=lambda: changeAxis(intOpt_x.get(), intOpt_y.get(),
                                                                                intOpt_x2.get(), intOpt_y2.get()))
        btnOpt_acc.place(x=704, y=147)

        btnOpt_cancel = Button(window5, text='Сброс', font=("Arial", 10), command=lambda: cancelAxis(status='default'))
        btnOpt_cancel.place(x=765, y=147)




        frameTop = LabelFrame(window5, text='Задание и построение интервалов исследоваемого сигнала', font=("Arial", 10))
        frameTop.place(x=5, y=0)
        l0 = Label(frameTop)
        l0.pack(side=LEFT, padx=239, pady=70)

        labelInter = Label(window5, text='Текущие сигналы:', font=("Arial", 10))
        labelInter.place(x=10, y=25)

        listBoxTaskInter = Listbox(window5, width=30, height=8, exportselection=False)
        listBoxTaskInter.place(x=10, y=45)
        listBoxTaskInter.bind('<<ListboxSelect>>', setInterval)

        labelSig = Label(window5, text='Выбранный сигнал:', font=("Arial", 10))
        labelSig.place(x=220, y=25)

        labelSigInter = Label(window5, text='Заданный интервал:', font=("Arial", 10))
        labelSigInter.place(x=220, y=55)

        butCreateInter = Button(window5, text='Построить', command=lambda: createInterval(mode='default'),
                                font=("Arial", 10))
        butCreateInter.place(x=365, y=147)

        butCreateInter = Button(window5, text='Сброс', command=lambda: createInterval(mode='delete'),
                                font=("Arial", 10))
        butCreateInter.place(x=438, y=147)

        textSigName = StringVar()
        txtSigName = Entry(window5, width=20, textvariable=textSigName, state='disabled')
        txtSigName.place(x=350, y=27)

        textSigInter = StringVar()
        txtSigInter = Entry(window5, width=20, textvariable=textSigInter, state='disabled')
        txtSigInter.place(x=350, y=57)
        reg = window5.register(intervalInp)
        txtSigInter.config(validate='key', validatecommand=(reg, '%P'))

        graphInterval = {}
        lastIndex = None
        i = 0

        graphListTask.reverse()
        for sig in graphListTask:
            click_acceptParam(sig, listBoxTaskInter)
        else:
            graphListTask.reverse()

        for sig in graphListTask:
            graphInterval.setdefault(i, [sig[0], ''])
            i += 1

        canvas = FigureCanvasTkAgg(fig, window5)
        canvas.draw()
        canvas.get_tk_widget().pack(side=RIGHT)

        toolbar = NavigationToolbar2Tk(canvas, window5)
        #cancelAxis()
        toolbar.update()

        canvas._tkcanvas.pack(side=RIGHT)

        cid = fig.canvas.mpl_connect('button_press_event', selectTime)

    except TclError:
        pass
        #plt.close(fig)
        #click_createGraph()


def click_deleteSignals():
    graphList.clear()
    listBox.delete(0, listBox.size())

def click_acceptFind(getComboCurent, window):
    global find
    find = 1

    count = 0

    listBox.delete(0, listBox.size())

    for graph in graphList:
        if getComboCurent == 0:
            if graph[0] == 'line':
                graphListFind.append(graph)
                click_acceptParam(graph, listBox)
                count += 1
                continue
            else:
                continue
        elif getComboCurent == 1:
            if graph[0] == 'sin':
                graphListFind.append(graph)
                click_acceptParam(graph, listBox)
                count += 1
                continue
            else:
                continue
        elif getComboCurent == 2:
            if graph[0] == 'cos':
                graphListFind.append(graph)
                click_acceptParam(graph, listBox)
                count += 1
                continue
            else:
                continue
        elif getComboCurent == 3:
            if graph[0] == 'step':
                graphListFind.append(graph)
                click_acceptParam(graph, listBox)
                count += 1
                continue
            else:
                continue

    window.destroy()


def click_rejectFind():
    listBox.delete(0, listBox.size())
    global find
    find = 0
    graphList.reverse()
    for graph in graphList:
        if graph[0] == 'line':
            click_acceptParam(['line', graph[1], graph[2]], listBox)
        elif graph[0] == 'sin':
            click_acceptParam(['sin', graph[1], graph[2], graph[3]], listBox)
        elif graph[0] == 'cos':
            click_acceptParam(['cos', graph[1], graph[2], graph[3]], listBox)
        elif graph[0] == 'step':
            click_acceptParam(['step', graph[1], graph[2], graph[3]], listBox)
        elif graph[0] == 'mass':
            click_acceptParam(['mass', graph[1], graph[2], graph[3]], listBox)
        elif graph[0] == 'word':
            click_acceptParam(['word', graph[1], graph[2]], listBox)
        elif graph[0] == 'newSig':
            click_acceptParam(['newSig', graph[1]], graph[2]. graph[3], listBox)

    else:
        graphList.reverse()


def click_findGraph():
    try:
        z = graphList[0]
    except IndexError:
        messagebox.showinfo('Ошибка!', 'Сначала загрузите файл!')
    else:
        window4 = Tk()
        window4.title('Поиск сигнала в списке')
        w = (window4.winfo_screenwidth() // 2) - 100
        h = (window4.winfo_screenheight() // 2) - 100
        window4.geometry('350x95+{}+{}'.format(w, h))
        window4.resizable(width=False, height=False)

        labelFind = Label(window4, text='Поиск по типу:', font=("Arial", 10))
        labelFind.place(x=0, y=0)

        labelFind1 = Label(window4, text='Поиск по идентификатору:', font=("Arial", 10))
        labelFind1.place(x=0, y=30)

        nameInd = Text(window4, width=21, height=1)
        nameInd.place(x=163, y=30)

        comboFind = Combobox(window4)
        comboFind['value'] = ('Линейный', 'Синусоидальный', 'Косинусоидальный', 'Слово')
        comboFind.place(x=163, y=2)

        btnAcceptFind = Button(window4, text='Принять', command=lambda: click_acceptFind(comboFind.current(), window4))
        btnAcceptFind.place(x=163, y=55)

        btnRejectFind = Button(window4, text='Сбросить поиск', command=click_rejectFind)
        btnRejectFind.place(x=223, y=55)

        window4.mainloop()


def click_createTask():
    def click():
        click_acceptParam(['task', txt_Name.get(), txtInfo.get(0.0, END)])
        window3.destroy()

    window3 = Tk()
    window3.title('Создание нового задания')
    w = (window3.winfo_screenwidth() // 2) - 100
    h = (window3.winfo_screenheight() // 2) - 100
    window3.geometry('350x125+{}+{}'.format(w, h))
    window3.resizable(width=False, height=False)

    label = Label(window3, text='Наименование:', font=("Arial", 10))
    label.place(x=0, y=0)

    txtName = StringVar()
    txt_Name = Entry(window3, width=30, textvariable=txtName)
    txt_Name.place(x=100, y=3)

    label1 = Label(window3, text='Описание:', font=("Arial", 10))
    label1.place(x=0, y=30)

    txtInfo = Text(window3, width=30, height=3)
    txtInfo.place(x=100, y=35)

    btn = Button(window3, text='Создать', command=click)
    btn.place(x=291, y=90)

    window3.mainloop()


def click_deleteGraphListBoxTask(event):
    select = list(listBoxTask.curselection())
    listBoxTask.delete(select[0])
    graphListTask.remove(graphListTask[select[0]])
    taskList[comboTask.current()].pop(select[0] + 3)


def click_deleteAllListBoxTask():
    listBoxTask.delete(0, listBoxTask.size())
    for graph in graphListTask:
        taskList[comboTask.current()].remove(graph)
    graphListTask.clear()

#  window5.destroy()
# window5 = Tk()
# window5.geometry('800x800')
# window5.mainloop()


def click_addToTask(event):
    select = listBox.curselection()

    if comboTask.current() == -1:
        messagebox.showinfo('Ошибка!', 'Отсутствует задание! Создайте его.')
    else:
        try:
            if listBox.get(0)[0] == '':
                pass
        except IndexError:
            messagebox.showinfo('Ошибка!', 'Не выбран сигнал!')

    if comboTask.current() >= 0:

        global find
        if find == 0:
            taskList[comboTask.current()].insert(3, graphList[select[0]])
            graphListTask.insert(0, graphList[select[0]])
            click_acceptParam(graphList[select[0]], listBoxTask)
        else:
            taskList[comboTask.current()].insert(3, graphListFind[select[0]])
            graphListTask.insert(0, graphListFind[select[0]])
            click_acceptParam(graphListFind[select[0]], listBoxTask)

def click_changeTask():

    def returnInfo(event):
        txtTaskName.delete(0, END)
        textTaskInfo.delete(1.0, END)
        listBoxCurrTask.delete(0, END)
        def getVals(index):
            i = -1
            txtTaskName.insert(0, taskList[index][1])
            textTaskInfo.insert(1.0, taskList[index][2])
            for signal in taskList[index][3:]:
                i += 1
                click_acceptParam(signal, listBoxCurrTask)

        if event == 'default':
            getVals(0)
        else:
            select = listBoxChangeTask.curselection()
            getVals(select[0])

    windowTaskChange = Tk()
    windowTaskChange.title('Редактирование заданий')
    windowTaskChange.resizable(width=False, height=False)
    windowTaskChange.geometry('700x700')

    labelTask = Label(windowTaskChange, text='Список заданий:', font=("Arial", 10))
    labelTask.place(x=0, y=0)

    listBoxChangeTask = Listbox(windowTaskChange, width=30, height=15)
    listBoxChangeTask.place(x=1, y=20)
    listBoxChangeTask.bind('<Button-1>', returnInfo)

    frameTop = LabelFrame(windowTaskChange, font=("Arial", 10))
    frameTop.place(x=200, y=20)
    l0 = Label(frameTop)
    l0.pack(side=LEFT, padx=190, pady=110)

    labelTaskName = Label(windowTaskChange, text='Имя задания: ', font=("Arial", 10))
    labelTaskName.place(x=205, y=25)

    textTaskName = StringVar()
    txtTaskName = Entry(windowTaskChange, width=30, textvariable=textTaskName)
    txtTaskName.place(x=330, y=27)

    labelTaskInfo = Label(windowTaskChange, text='Описание задания:', font=("Arial", 10))
    labelTaskInfo.place(x=205, y=45)

    textTaskInfo = Text(windowTaskChange, width=30, height=3)
    textTaskInfo.place(x=330, y=50)

    labelTaskSig = Label(windowTaskChange, text='Сигналы задния:', font=("Arial", 10))
    labelTaskSig.place(x=205, y=105)

    listBoxCurrTask = Listbox(windowTaskChange, width=40, height=7)
    listBoxCurrTask.place(x=329, y=105)

    i = -1
    for task in taskList:
        i += 1
        listBoxChangeTask.insert(i, task[1])
    else:
        listBoxChangeTask.selection_set(0)
        returnInfo('default')



def click_wordAnalyzer():
    windowWord = Tk()
    windowWord.title('Отчет по словам')
    windowWord.geometry('825x900')

    windowWord.resizable(width=False, height=False)


    outputWord = scrolledtext.ScrolledText(windowWord, width=99, height=55)
    outputWord.place(x=0, y=0)

    i, k, failure = 0, 0, []



    # БЛОКИ ПИТАНИЯ
    BPP_VY_27 = {1: [], 2: [], 3: [], 4: [], 'RESULT': 'None'}
    BPP_VY_9 = {1: [], 2: [], 3: [], 4: [], 'RESULT': 'None'}
    BPP_VY_MVS2_5 = {1: [], 2: [], 3: [], 4: [], 'RESULT': 'None'}
    BPP_VY_MVS4_5 = {1: [], 2: [], 3: [], 4: [], 'RESULT': 'None'}

    BPP_VYS_YSDK_27 = []

    YSDK_Right = []
    YSDK_Left = []



    # РПД
    RPD_Eleron_Left = {1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 'RESULT': 'None'}
    RPD_Eleron_Right = {1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 'RESULT': 'None'}
    RPD_Stab_Left = {1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 'RESULT': 'None'}
    RPD_Stab_Right = {1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 'RESULT': 'None'}
    RPD_Wheel_Left = {1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 'RESULT': 'None'}
    RPD_Wheel_Right = {1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 'RESULT': 'None'}
                    # ЭГУ-СС-ЭГУ-N, ССК3-1-N [ЭГУ, ЗОЛ, ШТОК]

    # ДАТЧИКИ
    IBD = {1: [[0, 0, 0], 0], 2: [[0, 0, 0], 0],
           3: [[0, 0, 0], 0], 4: [[0, 0, 0], 0], 'RESULT': 'None'}  # ССK1-1-N (17-19), ССK2-1-N (14),

    DPR = {1: [[0, 0, 0, 0], [x - x for x in range(0, 9)]],
           2: [[0, 0, 0, 0], [x - x for x in range(0, 9)]],
           3: [[0, 0, 0, 0], [x - x for x in range(0, 9)]],
           4: [[0, 0, 0, 0], [[x - x for x in range(0, 9)]]],
           'RESULT': 'None'}  # ССK1-1-N (26-29), ССK2-1-N (19-27)

    DDAD = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 'RESULT': 'None'}  # ССK2-1-N (17-18)

    Nxy = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 'RESULT': 'None'}  # ССK1-1-N (20-21)


    while i >= 0:
        if k < 1:
            if wordList[i][2] == 'ССК0-ХЗ-1-1' or wordList[i][2] == 'ССК0-ХЗ-2-2':
                if wordList[i][3] == 'correct':
                    pass
                else:
                    canal = int(wordList[i][2][len(wordList[i][2]) - 1])
                    for dig in wordList[i][4]:
                        if dig == 8:
                            mistake = 'Нет связи с МВС 2КР в {} канале'.format(canal)
                            BPP_VY_MVS2_5[canal].append(mistake)
                        elif dig == 9:
                            mistake = 'Нет связи с МВС 4КР в {} канале'.format(canal)
                            BPP_VY_MVS4_5[canal].append(mistake)
                        elif dig == 10:
                            mistake = 'Отказ {} канала САУ'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                        elif dig == 11:
                            mistake = 'Отказ ИМАТ в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS2_5[canal].append(mistake)
                        elif dig == 12:
                            mistake = 'Отказ управления закрылками в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS2_5[canal].append(mistake)
                    else:
                        k += 0.5
                        i = 0 if k == 1 else i + 1
                        continue
            else:
                i += 1
                continue

        elif k < 2 and k >= 1:
            if wordList[i][2] == 'ССК1-1-1' or wordList[i][2] == 'ССК1-2-2':
                if wordList[i][3] == 'correct':
                    pass
                else:
                    canal = int(wordList[i][2][len(wordList[i][2]) - 1])
                    for dig in wordList[i][4]:
                        if dig == 17:
                            mistake = 'Неисправность датчика угловой скорости крена в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            IBD[canal][0].pop(0); IBD[canal][0].insert(0, mistake)
                        elif dig == 18:
                            mistake = 'Неисправность датчика угловой скорости рысканья в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            IBD[canal][0].pop(1); IBD[canal][0].insert(1, mistake)
                        elif dig == 19:
                            mistake = 'Неисправность датчика угловой скорости тангажа в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            IBD[canal][0].pop(2); IBD[canal][0].insert(2, mistake)
                        elif dig == 20:
                            mistake = 'Неисправность датчика перегрузки продольной в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            Nxy[canal].pop(0); Nxy[canal].insert(0, mistake)
                        elif dig == 21:
                            mistake = 'Неисправность датчика перегрузки нормальной в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            Nxy[canal].pop(1); Nxy[canal].insert(1, mistake)
                        elif dig == 26:
                            mistake = 'Несправность ДПР носка корневого левого в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            BPP_VY_9[canal].append(mistake)
                            DPR[canal][0].pop(0); DPR[canal][0].insert(0, mistake)
                        elif dig == 27:
                            mistake = 'Несправность ДПР носка корневого правого в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            BPP_VY_9[canal].append(mistake)
                            DPR[canal][0].pop(1); DPR[canal][0].insert(1, mistake)
                        elif dig == 28:
                            mistake = 'Несправность ДПР носка концевого левого в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            BPP_VY_9[canal].append(mistake)
                            DPR[canal][0].pop(2); DPR[canal][0].insert(2, mistake)
                        elif dig == 29:
                            mistake = 'Несправность ДПР носка концевого правого в {} канале'.format(canal)
                            BPP_VY_27[canal].append(mistake)
                            BPP_VY_MVS4_5[canal].append(mistake)
                            BPP_VY_9[canal].append(mistake)
                            DPR[canal][0].pop(3); DPR[canal][0].insert(3, mistake)
                    else:
                        k += 0.5
                        i = 0 if k == 2 else i + 1
                        continue

            else:
                i += 1
                continue
        elif k < 3 and k >= 2:
            if wordList[i][2] == 'ССК2-1-1' or wordList[i][2] == 'ССК2-2-2':
                canal = int(wordList[i][2][len(wordList[i][2]) - 1])
                for dig in wordList[i][4]:
                    if dig == 14:
                        mistake = 'Нет связи с ИБД в {} канале'.format(canal)
                        IBD[canal].pop(1)
                        IBD[canal].insert(1, mistake)
                    elif dig == 16:
                        mistake = 'Отказ {} канала СДУ ВУ'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                    elif dig == 17:
                        mistake = 'Неисправность датчика давления статического в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        DDAD[canal].pop(0)
                        DDAD[canal].insert(0, mistake)
                    elif dig == 18:
                        mistake = 'Неисправность датчика давления динамического в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        DDAD[canal].pop(1)
                        DDAD[canal].insert(1, mistake)
                    elif dig == 19:
                        mistake = 'Неисправность ДПР РУС тангажа в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(0)
                        DPR[canal][1].insert(0, mistake)
                    elif dig == 20:
                        mistake = 'Неисправность ДПР РУС крена в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(1)
                        DPR[canal][1].insert(1, mistake)
                    elif dig == 21:
                        mistake = 'Неисправность ДПР педалей в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(2)
                        DPR[canal][1].insert(2, mistake)
                    elif dig == 22:
                        mistake = 'Несправность ДПР триммера тангажа в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(3)
                        DPR[canal][1].insert(3, mistake)
                    elif dig == 23:
                        mistake = 'Несправность ДПР триммера крена в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(4)
                        DPR[canal][1].insert(4, mistake)
                    elif dig == 24:
                        mistake = 'Несправность ДПР триммера направления в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(5)
                        DPR[canal][1].insert(5, mistake)
                    elif dig == 25:
                        mistake = 'Несправность ДПР закрылка левого в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(6)
                        DPR[canal][1].insert(6, mistake)
                    elif dig == 26:
                        mistake = 'Несправность ДПР закрылка правого в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(7)
                        DPR[canal][1].insert(7, mistake)
                    elif dig == 27:
                        mistake = 'Несправность ДПР тормозного щитка в {} канале'.format(canal)
                        BPP_VY_27[canal].append(mistake)
                        BPP_VY_MVS4_5[canal].append(mistake)
                        BPP_VY_9[canal].append(mistake)
                        DPR[canal][1].pop(8)
                        DPR[canal][1].insert(8, mistake)
                else:
                    k += 0.5
                    i = 0 if k == 2 else i + 1
                    continue

            else:
                i += 1
                continue

        elif k < 4 and k >= 3:
             if wordList[i][2] == 'ССК3-1-1' or wordList[i][2] == 'ССК3-2-2' or wordList[i][2] == 'ССК3-3-3' or \
                     wordList[i][2] == 'ССК3-4-4':
                 canal = int(wordList[i][2][len(wordList[i][2]) - 1])
                 for dig in wordList[i][4]:
                     if dig == 18:
                         mistake = 'Неисправность датчика штока левого элерона в {} канале'.format(canal)
                         RPD_Eleron_Left[canal].pop(2)
                         RPD_Eleron_Left[canal].insert(2, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Left.append(mistake)
                     elif dig == 19:
                         mistake = 'Неисправность датчика штока правого элерона в {} канале'.format(canal)
                         RPD_Eleron_Right[canal].pop(2)
                         RPD_Eleron_Right[canal].insert(2, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Right.append(mistake)
                     elif dig == 20:
                         mistake = 'Неисправность датчика штока левого руля направления в {} канале'.format(canal)
                         RPD_Wheel_Left[canal].pop(2)
                         RPD_Wheel_Left[canal].insert(2, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Left.append(mistake)
                     elif dig == 21:
                         mistake = 'Неисправность датчика штока правого руля направления в {} канале'.format(canal)
                         RPD_Wheel_Right[canal].pop(2)
                         RPD_Wheel_Right[canal].insert(2, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Right.append(mistake)
                     elif dig == 22:
                         mistake = 'Неисправность датчика штока левого стабилизатора в {} канале'.format(canal)
                         RPD_Stab_Left[canal].pop(2)
                         RPD_Stab_Left[canal].insert(2, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Left.append(mistake)
                     elif dig == 23:
                         mistake = 'Неисправность датчика штока правого стабилизатора в {} канале'.format(canal)
                         RPD_Stab_Right[canal].pop(2)
                         RPD_Stab_Right[canal].insert(2, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Right.append(mistake)
                     elif dig == 24:
                         mistake = 'Неисправность датчика золотника левого элерона в {} канале'.format(canal)
                         RPD_Eleron_Left[canal].pop(1)
                         RPD_Eleron_Left[canal].insert(1, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Left.append(mistake)
                     elif dig == 25:
                         mistake = 'Неисправность датчика золотника правого элерона в {} канале'.format(canal)
                         RPD_Eleron_Right[canal].pop(1)
                         RPD_Eleron_Right[canal].insert(1, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Right.append(mistake)
                     elif dig == 26:
                         mistake = 'Неисправность датчика золотника левого руля направления в {} канале'.format(canal)
                         RPD_Wheel_Left[canal].pop(1)
                         RPD_Wheel_Left[canal].insert(1, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Left.append(mistake)
                     elif dig == 27:
                         mistake = 'Неисправность датчика золотника правого руля направления в {} канале'.format(canal)
                         RPD_Wheel_Right[canal].pop(1)
                         RPD_Wheel_Right[canal].insert(1, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Right.append(mistake)
                     elif dig == 28:
                         mistake = 'Неисправность датчика золотника левого стабилизатора в {} канале'.format(canal)
                         RPD_Stab_Left[canal].pop(1)
                         RPD_Stab_Left[canal].insert(1, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Left.append(mistake)
                     elif dig == 29:
                         mistake = 'Неисправность датчика золотника правого стабилизатора в {} канале'.format(canal)
                         RPD_Stab_Right[canal].pop(1)
                         RPD_Stab_Right[canal].insert(1, mistake)
                         BPP_VYS_YSDK_27.append(mistake)
                         YSDK_Right.append(mistake)
                 else:
                     k += 0.25
                     i = 0 if k == 4 else i + 1
             else:
                 i += 1
        elif k < 5 and k >= 4:
            if wordList[i][2] == 'ЭГУ-СС-ЭГУ-1' or wordList[i][2] == 'ЭГУ-СС-ЭГУ-2':
                canal = int(wordList[i][2][len(wordList[i][2]) - 1])
                canal = 3 if canal == 2 else 1

                for dig in wordList[i][4]:
                    if dig == 18:
                        mistake = 'Отказ ЭГУ левого элерона в {} канале'.format(canal)
                        RPD_Eleron_Left[canal].pop(0)
                        RPD_Eleron_Left[canal].insert(0, mistake)
                    elif dig == 19:
                        mistake = 'Отказ ЭГУ правого элерона в {} канале'.format(canal)
                        RPD_Eleron_Right[canal].pop(0)
                        RPD_Eleron_Right[canal].insert(0, mistake)
                    elif dig == 20:
                        mistake = 'Отказ ЭГУ левого руля направления в {} канале'.format(canal)
                        RPD_Wheel_Left[canal].pop(0)
                        RPD_Wheel_Left[canal].insert(0, mistake)
                    elif dig == 21:
                        mistake = 'Отказ ЭГУ правого руля направления в {} канале'.format(canal)
                        RPD_Wheel_Right[canal].pop(0)
                        RPD_Wheel_Right[canal].insert(0, mistake)
                    elif dig == 22:
                        mistake = 'Отказ ЭГУ левого стабилизатора в {} канале'.format(canal)
                        RPD_Stab_Left[canal].pop(0)
                        RPD_Stab_Left[canal].insert(0, mistake)
                    elif dig == 23:
                        mistake = 'Отказ ЭГУ правого стабилизатора в {} канале'.format(canal)
                        RPD_Stab_Right[canal].pop(0)
                        RPD_Stab_Right[canal].insert(0, mistake)
                    elif dig == 24:
                        mistake = 'Отказ ЭГУ левого элерона в {} канале'.format(canal + 1)
                        RPD_Eleron_Left[canal + 1].pop(0)
                        RPD_Eleron_Left[canal + 1].insert(0, mistake)
                    elif dig == 25:
                        mistake = 'Отказ ЭГУ правого элерона в {} канале'.format(canal + 1)
                        RPD_Eleron_Right[canal + 1].pop(0)
                        RPD_Eleron_Right[canal + 1].insert(0, mistake)
                    elif dig == 26:
                        mistake = 'Отказ ЭГУ левого руля направления в {} канале'.format(canal + 1)
                        RPD_Wheel_Left[canal + 1].pop(0)
                        RPD_Wheel_Left[canal + 1].insert(0, mistake)
                    elif dig == 27:
                        mistake = 'Отказ ЭГУ правого руля направления в {} канале'.format(canal + 1)
                        RPD_Wheel_Right[canal + 1].pop(0)
                        RPD_Wheel_Right[canal + 1].insert(0, mistake)
                    elif dig == 28:
                        mistake = 'Отказ ЭГУ левого стабилизатора в {} канале'.format(canal + 1)
                        RPD_Stab_Left[canal + 1].pop(0)
                        RPD_Stab_Left[canal + 1].insert(0, mistake)
                    elif dig == 29:
                        mistake = 'Отказ ЭГУ правого стабилизатора в {} канале'.format(canal + 1)
                        RPD_Stab_Right[canal + 1].pop(0)
                        RPD_Stab_Right[canal + 1].insert(0, mistake)

                else:
                    k += 0.5
                    if k == 5:
                        break
                    else:
                        i += 1
            else:
                i += 1
        else:
            i += 1




    # print('BPP VY 27: {}'.format(BPP_VY_27))
    # print('BPP VY MVS2_5: {}'.format(BPP_VY_MVS2_5))
    # print('BPP VY MVS4_5: {}'.format(BPP_VY_MVS4_5))
    # print('BPP VY 9: {}'.format(BPP_VY_9))



    # print('BPP_VY_27')
    # for x in BPP_VY_27:
    #     print(len(BPP_VY_27[x]))
    #     for y in BPP_VY_27[x]:
    #         print(y)
    #
    # print('BPP_VY_9\n')
    # for x in BPP_VY_9:
    #     print(len(BPP_VY_9[x]))
    #     for y in BPP_VY_9[x]:
    #         print(y)
    #
    # print('BPP_VY_MVS2_5\n')
    # for x in BPP_VY_MVS2_5:
    #     print(len(BPP_VY_MVS2_5[x]))
    #     for y in BPP_VY_MVS2_5[x]:
    #         print(y)
    #
    # print('BPP_VY_MVS4_5\n')
    # for x in BPP_VY_MVS4_5:
    #     print(len(BPP_VY_MVS4_5[x]))
    #     for y in BPP_VY_MVS4_5[x]:
    #         print(y)



    print('RPD_eleron left\n')
    for x in RPD_Eleron_Left:
        print(RPD_Eleron_Left[x])
    else:
        print('\n')

    print('RPD_eleron right\n')
    for x in RPD_Eleron_Right:
        print(RPD_Eleron_Right[x])
    else:
        print('\n')


    print('RPD_stab left\n')
    for x in RPD_Stab_Left:
        print(RPD_Stab_Left[x])
    else:
        print('\n')

    print('RPD_stab right\n')
    for x in RPD_Stab_Right:
        print(RPD_Stab_Right[x])
    else:
        print('\n')


    print('RPD_wHEEL left\n')
    for x in RPD_Wheel_Left:
        print(RPD_Wheel_Left[x])
    else:
        print('\n')

    print('RPD_wHEEL right\n')
    for x in RPD_Wheel_Right:
        print(RPD_Wheel_Right[x])
    else:
        print('\n')





    #
    # print('RPD_Stab_right\n')
    # for x in RPD_Stab_Right:
    #     #print(len(RPD_Stab_Right[x]))
    #     for y in RPD_Stab_Right[x]:
    #         print(y)

    # print('RPD_Stab\n')
    # for x in RPD_Stab_Right:
    #     #print(len(RPD_Stab_Right[x]))
    #     for y in RPD_Stab_Right[x]:
    #         print(y)

    # АНАЛИЗ КСЭ

    # БПП ВУ (27, 5, 9) в 1 и 2 канале

    if len(BPP_VY_27[1]) == 24 or len(BPP_VY_27[2]) == 24:
        outputWord.insert(END, 'Состояние БПП ВУ: \n\n')
        if len(BPP_VY_27[1]) == 24:
            outputWord.insert(END, '\tОтказ БПП ВУ 27В в 1 канале на {} секунде\n'.format(345))
            outputWord.insert(END, '\tСнижение надежности\n\n')
        if len(BPP_VY_27[2]) == 24:
            outputWord.insert(END, '\tОтказ БПП ВУ 27В в 2 канале на {} секунде\n'.format(613))
            outputWord.insert(END, '\tСнижение надежности\n\n')

    if len(BPP_VY_9[1]) == 13 or len(BPP_VY_9[2]) == 13:
        if len(BPP_VY_9[1]) == 13:
            outputWord.insert(END, '\tОтказ БПП ВУ 9В в 1 канале на {} секунде\n'.format(145))
            outputWord.insert(END, '\tСнижение надежности\n\n')
        if len(BPP_VY_9[2]) == 13:
            outputWord.insert(END, '\tОтказ БПП ВУ 9В в 2 канале на {} секунде\n'.format(1245))
            outputWord.insert(END, '\tСнижение надежности\n\n')

    # if len(BPP_VY_MVS2_5[1]) == 3 or len(BPP_VY_MVS2_5[2]) == 3:
    #     if len(BPP_VY_MVS2_5[1]) == 3:
    #         outputWord.insert(END, '\tОтказ БПП ВУ 5В МВС2 в 1 канале\n')
    #     if len(BPP_VY_MVS2_5[2]) == 3:
    #         outputWord.insert(END, '\tОтказ БПП ВУ 5В МВС2 в 2 канале\n\n')
    #
    # if len(BPP_VY_MVS4_5[1]) == 21 or len(BPP_VY_MVS4_5[2]) == 21:
    #         if len(BPP_VY_MVS4_5[1]) == 21:
    #             outputWord.insert(END, '\tОтказ БПП ВУ 5В МВС4 в 1 канале\n')
    #             outputWord.insert(END, '\tСнижение надежности\n\n')
    #         if len(BPP_VY_MVS4_5[2]) == 21:
    #             outputWord.insert(END, '\tОтказ БПП ВУ 5В МВС4 в 2 канале\n')
    #             outputWord.insert(END, '\tСнижение надежности\n\n')


    # РПД
    RPD = [RPD_Eleron_Left]
    forBPP_VYS_27 = {1: [], 2: [], 3: [], 4: []}
    forMVS_VYS_5 = {1: [], 2: [], 3: [], 4: []}
    YS_Left = {1: [], 2: [], 3: [], 4: []}
    YS_Right = {1: [], 2: [], 3: [], 4: []}
    outputWord.insert(END, 'Состояние РПД ВУС: \n\n')

    for rpd in RPD:
        if rpd == RPD_Eleron_Left:
            rpdIs = 'левого элерона'
        elif rpd == RPD_Eleron_Right:
            rpdIs = 'правого элерона'
        elif rpd == RPD_Stab_Left:
            rpdIs = 'левого стабилизатора'
        elif rpd == RPD_Stab_Right:
            rpdIs = 'правого стабилизатора'
        elif rpd == RPD_Wheel_Left:
            rpdIs = 'левого руля направления'
        elif rpd == RPD_Wheel_Right:
            rpdIs = 'правого руля направления'

        a, b, c, d = rpd[1], rpd[2], rpd[3], rpd[4]

        j, i = 0, 0
        outputWord.insert(END, 'РПД {}:\n'.format(rpdIs))
        while i < 3:
            ysIs = YS_Left if 'левого' in rpdIs else YS_Right
            if (a[i] != 0 and b[i] != 0 and c[i] != 0 and d[i] != 0) and j == 0:

                if i == 0:
                    outputWord.insert(END, '\tОтказ {} в канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                    outputWord.insert(END, '\tСнижение надежности\n')
                    outputWord.insert(END, '\tНет резерва\n\n')
                    if rpdIs == RPD_Stab_Left or rpdIs == RPD_Stab_Right:
                        outputWord.insert(END, '\tОтказ КСУ\n\n')


                elif i == 1:
                    outputWord.insert(END, '\tОтказ {} в канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                    outputWord.insert(END, '\tСнижение надежности\n')
                    outputWord.insert(END, '\tНет резерва\n\n')
                    if rpdIs == RPD_Stab_Left or rpdIs == RPD_Stab_Right:
                        outputWord.insert(END, '\tОтказ КСУ\n')

                elif i == 2:
                    outputWord.insert(END, '\tОтказ {} в канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                    outputWord.insert(END, '\tСнижение надежности\n')
                    outputWord.insert(END, '\tНет резерва\n\n')
                    if rpdIs == RPD_Stab_Left or rpdIs == RPD_Stab_Right:
                        outputWord.insert(END, '\tОтказ КСУ\n')

                i += 1
                if i == 3:
                    j, i = 1, 0
                    continue

            else:

                if i == 3 and j == 0:
                    j, i = 1, 0
                    continue
                elif j == 0:
                    if i == 2:
                        j, i = 1, 0
                        continue
                    else:
                        i += 1

            if ((a[i] != 0 and b[i] != 0 and c[i] != 0 and d[i] == 0) or (
                    a[i] == 0 and b[i] != 0 and c[i] != 0 and d[i] != 0) or (
                          a[i] != 0 and b[i] == 0 and c[i] != 0 and d[i] != 0)) and j == 1:

                if d[i] == 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 1, 2 и 3 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')
                        forMVS_VYS_5[4].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 1, 2 и 3 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 1, 2 и 3 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')


                    forBPP_VYS_27[4].append(0)

                    ysIs[4].append(0)

                elif a[i] == 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 2, 3 и 4 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')
                        forMVS_VYS_5[1].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 2, 3 и 4 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 2, 3 и 4 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    forBPP_VYS_27[1].append(0)

                    ysIs[1].append(0)

                elif b[i] == 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 1, 3 и 4 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')
                        forMVS_VYS_5[2].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 1, 3 и 4 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность{} в 1, 3 и 4 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    forBPP_VYS_27[2].append(0)

                    ysIs[2].append(0)

                i += 1
                if i == 3:
                    j, i = 2, 0
                    continue
            else:
                if i >= 3 and j == 1:
                    j, i = 2, 0
                    continue
                elif j == 1:
                    if i == 2:
                        j, i = 2, 0
                        continue
                    else:
                        i += 1

            if ((a[i] != 0 and b[i] != 0 and c[i] == 0 and d[i] == 0) or (
                    a[i] == 0 and b[i] == 0 and c[i] != 0 and d[i] != 0) or (
                          a[i] != 0 and b[i] == 0 and c[i] != 0 and d[i] == 0) or (
                          a[i] == 0 and b[i] != 0 and c[i] != 0 and d[i] == 0)) and j == 2:

                if c[i] == 0 and d[i] == 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 1 и 2 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')
                        forMVS_VYS_5[3].append(0)
                        forMVS_VYS_5[4].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 1 и 2 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')


                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 1 и 2 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    forBPP_VYS_27[3].append(0)
                    forBPP_VYS_27[4].append(0)

                    ysIs[3].append(0)
                    ysIs[4].append(0)

                elif a[i] == 0 and b[i] == 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 3 и 4 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')
                        forMVS_VYS_5[1].append(0)
                        forMVS_VYS_5[2].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 3 и 4 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 3 и 4 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    forBPP_VYS_27[1].append(0)
                    forBPP_VYS_27[2].append(0)

                    ysIs[1].append(0)
                    ysIs[2].append(0)

                elif b[i] == 0 and d[i] == 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 1 и 3 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')
                        forMVS_VYS_5[2].append(0)
                        forMVS_VYS_5[4].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 1 и 3 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 1 и 3 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    forBPP_VYS_27[2].append(0)
                    forBPP_VYS_27[4].append(0)

                    ysIs[2].append(0)
                    ysIs[4].append(0)

                elif a[i] == 0 and d[i] == 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 2 и 3 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')
                        forMVS_VYS_5[1].append(0)
                        forMVS_VYS_5[4].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 2 и 3 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 2 и 3 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n')
                        outputWord.insert(END, '\tНет резерва\n\n')

                    forBPP_VYS_27[1].append(0)
                    forBPP_VYS_27[4].append(0)

                    ysIs[1].append(0)
                    ysIs[4].append(0)

                i += 1
                if i == 3:
                    j, i = 3, 0
                    continue

            else:
                if i == 3 and j == 2:
                    j, i = 3, 0
                    continue
                elif j == 2:
                    if i == 2:
                        j, i = 3, 0
                        continue
                    else:
                        i += 1

            if ((a[i] != 0 and b[i] == 0 and c[i] == 0 and d[i] == 0) or (
                    a[i] == 0 and b[i] != 0 and c[i] == 0 and d[i] == 0) or (
                          a[i] == 0 and b[i] == 0 and c[i] != 0 and d[i] == 0) or (
                          a[i] == 0 and b[i] == 0 and c[i] == 0 and d[i] != 0)) and j == 3:

                if a[i] != 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 1 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')
                        forMVS_VYS_5[2].append(0)
                        forMVS_VYS_5[3].append(0)
                        forMVS_VYS_5[4].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 1 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 1 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')

                    forBPP_VYS_27[2].append(0)
                    forBPP_VYS_27[3].append(0)
                    forBPP_VYS_27[4].append(0)

                    ysIs[2].append(0)
                    ysIs[3].append(0)
                    ysIs[4].append(0)

                elif b[i] != 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 2 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')
                        forMVS_VYS_5[1].append(0)
                        forMVS_VYS_5[3].append(0)
                        forMVS_VYS_5[4].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 2 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 2 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')

                    forBPP_VYS_27[1].append(0)
                    forBPP_VYS_27[3].append(0)
                    forBPP_VYS_27[4].append(0)

                    ysIs[1].append(0)
                    ysIs[3].append(0)
                    ysIs[4].append(0)


                elif c[i] != 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 3 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')
                        forMVS_VYS_5[1].append(0)
                        forMVS_VYS_5[2].append(0)
                        forMVS_VYS_5[4].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 3 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 3 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')

                    forBPP_VYS_27[1].append(0)
                    forBPP_VYS_27[2].append(0)
                    forBPP_VYS_27[4].append(0)

                    ysIs[1].append(0)
                    ysIs[2].append(0)
                    ysIs[4].append(0)

                elif d[i] != 0:
                    if i == 0:
                        outputWord.insert(END, '\tНеисправность {} в 4 канале ЭГУ на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')
                        forMVS_VYS_5[1].append(0)
                        forMVS_VYS_5[2].append(0)
                        forMVS_VYS_5[3].append(0)

                    elif i == 1:
                        outputWord.insert(END, '\tНеисправность {} в 4 канале ДОС золотника на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')

                    elif i == 2:
                        outputWord.insert(END, '\tНеисправность {} в 4 канале ДОС штока на {} секунде\n'.format(rpdIs, random.randint(500, 1500)))
                        outputWord.insert(END, '\tСнижение надежности\n\n')

                    forBPP_VYS_27[1].append(0)
                    forBPP_VYS_27[2].append(0)
                    forBPP_VYS_27[3].append(0)

                    ysIs[1].append(0)
                    ysIs[2].append(0)
                    ysIs[3].append(0)

                i += 1
                if i == 3:
                     break

            else:
                if i == 3 and j == 3:
                    break
                elif j == 3:
                    if i == 2:
                        break
                    else:
                        i += 1

    if len(YSDK_Right) == 24:
        outputWord.insert(END, 'Отказ правого УЗДК\n\n')

    if len(YSDK_Left) == 24:
        outputWord.insert(END, 'Отказ левого УЗДК\n\n')

    if len(BPP_VYS_YSDK_27) == 48:
        outputWord.insert(END, 'Отказ БПП ВУС УЗДК\n')
        outputWord.insert(END, 'Снижение надежности\n\n')

    print(YS_Left)
    print(YS_Right)

    # ПРОВЕРКА БПП ВУС 27В, МВС ВУС 5В, правого и левого УС
    for x in range(1, 5):
        if 0 in forBPP_VYS_27[x]:
            forBPP_VYS_27.pop(x)

        if 0 in forMVS_VYS_5[x]:
            forMVS_VYS_5.pop(x)

        if 0 in YS_Left[x]:
            YS_Left.pop(x)

        if 0 in YS_Right[x]:
            YS_Right.pop(x)
    else:
        if bool(forBPP_VYS_27) == False and bool(forMVS_VYS_5) == False:
            pass
        else:
            def output(nameKSS, KSS):
                string = ''
                for x in KSS.keys():
                    string = string + str(x) + ' '
                else:
                    string = string.rstrip().replace(' ', ', ')
                    outputWord.insert(END, '{} в {} канале\n'.format(nameKSS, string))
                    if len(KSS) > 1:
                        outputWord.insert(END, 'Снижение надежности\n')
                        outputWord.insert(END, 'Нет связи\n\n')
                    else:
                        outputWord.insert(END, 'Снижение надежности\n\n')

            if bool(forBPP_VYS_27) != False:
                output('Отказ БПП ВУС 27В', forBPP_VYS_27)
            if bool(forMVS_VYS_5) != False:
                output('Отказ МВС ВУС 5В', forMVS_VYS_5)
            if bool(YS_Left) != False:
                output('Отказ левого УС (5, 15В)', YS_Left)
            if bool(YS_Right) != False:
                output('Отказ правого УС (5, 15В)', YS_Right)


    outputWord.configure(state=DISABLED)
    windowWord.mainloop()

def click_signalCreator():

    i = 1
    k = 1
    graphListToChange = []
    listOfEntry = []

    def click_accFind(val, comboCurr=None, name=None):

        listBoxOfSig.delete(0, END)
        graphList.reverse()
        if val == 1 and name == '' and comboCurr > 0:
            listOfSystem = ['', 'line', 'sin', 'cos']
            for graph in graphList:
                if graph[0] == listOfSystem[comboCurr]:
                    click_acceptParam(graph, listBoxOfSig)
            else:
                graphList.reverse()
        elif val == 1 and name != '' and comboCurr == 0:
            for graph in graphList:
                if graph[0] == name:
                    click_acceptParam(graph, listBoxOfSig)
            else:
                graphList.reverse()
        elif val == 0 or comboCurr == 0:
            for graph in graphList:
                click_acceptParam(graph, listBoxOfSig)
            else:
                graphList.reverse()

    def clearTextFunc(event, var, num):
        nonlocal k
        var.delete(0, END)
        graphListToChange.pop(num)
        graphListToChange.insert(num, '')
        k += 1

    def varB_varC(step):

        nonlocal listOfEntry, i
        if step == 1:
            i = 1
            listOfEntry.clear()

            varB = StringVar()
            b = Entry(frameBot, textvariable=varB)
            b.bind('<Button-3>', lambda event, var=b, num=1: clearTextFunc(event, var, num))

            varC = StringVar()
            c = Entry(frameBot, textvariable=varC)
            c.bind('<Button-3>', lambda event, var=c, num=2: clearTextFunc(event, var, num))

            listOfEntry = [a, b, c]

        else:
            i = 2
            listOfEntry.remove(listOfEntry[2])

            varC = StringVar()
            c = Entry(frameBot, textvariable=varC)
            c.bind('<Button-3>', lambda event, var=c: clearTextFunc(event, var))

            listOfEntry.append(c)

    def selectFunc(event):
        nonlocal i, k

        numGraph = listBoxOfSig.curselection()

        if k > 0:
            for j in range(0, i):
                if listOfEntry[j].get() == '':
                    click_acceptParam(graphList[numGraph[0]], listOfEntry[j])
                    for graph in graphListToChange:
                        if graph == '':
                            graphListToChange.insert(graphListToChange.index(graph), graphList[numGraph[0]])
                            graphListToChange.remove(graph)
                            break
                    else:
                        graphListToChange.append(graphList[numGraph[0]])
                        break
                    break

        k -= 1

    def refreshSpinBox():
        nonlocal listOfEntry, i, k
        if i < int(numOfSigSpin.get()):
            try:
                if i == 1:
                    labelB.config(text='b:')
                    listOfEntry[1].place(x=30, y=120)
                elif i == 2:
                    labelC.config(text='c:')
                    try:
                        listOfEntry[2].place(x=30, y=140)
                    except TclError:
                        varB_varC(2)
                        refreshSpinBox()
                        return 0
                i += 1
                k = i
            except TclError:
                varB_varC(1)
                refreshSpinBox()
                return 0

        elif i > int(numOfSigSpin.get()):

            if i == 3:
                listOfEntry[2].destroy()
                labelC.config(text='')
                if len(graphListToChange) == i:
                    graphListToChange.pop(i-1)
            elif i == 2:
                listOfEntry[1].destroy()
                labelB.config(text='')
                if len(graphListToChange) == i:
                    graphListToChange.pop(i - 1)
            i -= 1
            k = i

    def funcFormula(inp):
        try:
            lastSymbol = inp[len(inp) - 1]
        except IndexError:
            lastSymbol = ' '

        key = ord(lastSymbol)

        nonlocal i
        b = i
        symbols = [97]
        while b > 1:
            symbols.append(symbols[len(symbols) - 1] + 1)
            b -= 1

        if key in range(48, 57) or key in [32, 40, 41, 42, 43, 45, 46, 47, 127, 8] or key in symbols:
            return True
        else:
            return False

    windowSignalCreator = Tk()
    windowSignalCreator.geometry('550x375')
    windowSignalCreator.title('Создание нового сигнапа')

    frameTop = LabelFrame(windowSignalCreator, text='Поиск по файлу', font=("Arial", 10))
    frameTop.place(x=5, y=10)

    l0 = Label(frameTop)
    l0.pack(side=LEFT, padx=150, pady=45)

    label1 = Label(frameTop, text='По типу сигнала:', font=("Arial", 10))
    label1.place(x=5, y=5)

    comboBox = Combobox(frameTop)
    comboBox['value'] = ('', 'Линейный', 'Синусоидальный', 'Косинусоидальный')
    comboBox.place(x=122, y=7)
    comboBox.bind('<<ComboboxSelected>>', lambda event: txtName.delete(0, END))

    label2 = Label(frameTop, text='По имени сигнала:', font=("Arial", 10))
    label2.place(x=5, y=35)

    txt = StringVar()
    txtName = Entry(frameTop, width=23, textvariable=txt)
    txtName.place(x=122, y=37)
    txtName.bind('<Key>', lambda event: comboBox.current(0))

    buttAcc = Button(frameTop, text='Принять', command=lambda: click_accFind(1, comboBox.current(), txtName.get()))
    buttAcc.place(x=10, y=75)

    buttCan = Button(frameTop, text='Сбросить', command=lambda: click_accFind(0))
    buttCan.place(x=75, y=75)

    frameBot = LabelFrame(windowSignalCreator, text='Создание нового сигнала на основе имеющихся', font=("Arial", 10))
    frameBot.place(x=5, y=150)

    l_ = Label(frameBot)
    l_.pack(side=LEFT, padx=150, pady=90)

    label3 = Label(frameBot, text='Количество сигналов:', font=("Arial", 10))
    label3.place(x=5, y=10)

    numOfSigSpin = Spinbox(frameBot, from_=1, to=3, width=5, command=refreshSpinBox)
    numOfSigSpin.place(x=170, y=11)


    label5 = Label(frameBot, text='Функция преобразования:', font=("Arial", 10))
    label5.place(x=5, y=30)

    txt2 = StringVar()
    txtFunc = Entry(frameBot, textvariable=txt2)
    txtFunc.place(x=170, y=31)
    reg = frameBot.register(funcFormula)
    txtFunc.config(validate='key', validatecommand=(reg, '%P'))

    label6 = Label(frameBot, text='Наименование функции:', font=("Arial", 10))
    label6.place(x=5, y=50)

    txt3 = StringVar()
    txtNameFunc = Entry(frameBot, textvariable=txt3)
    txtNameFunc.place(x=170, y=51)

    label4 = Label(frameBot, text='Отобранные сигналы:', font=("Arial", 10))
    label4.place(x=5, y=79)

    varA = StringVar()
    a = Entry(frameBot, textvariable=varA)
    labelA = Label(frameBot, text='a:', font=("Arial", 10))
    labelA.place(x=5, y=100)
    a.place(x=30, y=100)
    a.bind('<Button-3>', lambda event, var=a, num=0: clearTextFunc(event, var, num))

    labelB = Label(frameBot, font=("Arial", 10))
    labelB.place(x=5, y=120)

    labelC = Label(frameBot, font=("Arial", 10))
    labelC.place(x=5, y=140)

    varB_varC(1)

    frameRight = Frame(windowSignalCreator)
    frameRight.place(x=315, y=30)

    label5 = Label(windowSignalCreator, text='Общий список сигналов', font=("Arial", 10))
    label5.place(x=355, y=5)

    l__ = Label(frameRight)
    l__.pack(side=LEFT, padx=106, pady=160)

    listBoxOfSig = Listbox(windowSignalCreator, width=34, height=21)
    listBoxOfSig.place(x=325, y=30)
    listBoxOfSig.bind('<Double-Button-1>', selectFunc)

    scroll = Scrollbar(frameRight, command=listBoxOfSig.yview)
    scroll.pack(side=RIGHT, fill=Y)
    listBoxOfSig.config(yscrollcommand=scroll.set)

    buttNewSig = Button(frameBot, text='Создать', command=lambda: click_acceptParam(['newSig',
                                                                                     txtNameFunc.get(), txtFunc.get(),
                                                                                     graphListToChange], listBox))
    buttNewSig.place(x=5, y=170)

    graphList.reverse()
    for graph in graphList:
        click_acceptParam(graph, listBoxOfSig)
    else:
        graphList.reverse()

    windowSignalCreator.mainloop()


            ###### КОМПОНЕНТЫ ГЛАВНОГО ОКНА ######


###### БЛОК НАСТРОЙКИ ОКНА ######
window = Tk()
window.title('Обработчик сигналов')
w = (window.winfo_screenwidth() // 2) - 200
h = (window.winfo_screenheight() // 2) - 200
window.geometry('700x250+{}+{}'.format(w, h))
window.resizable(width=False, height=False)

###### БЛОК "ЗАДАНИЕ" ######
label2 = Label(window, text='Выберите задачу:', font=('Arial', 10))
label2.place(x=320, y=0)

label3 = Label(window, text='Список сигналов задания:', font=('Arial', 10))
label3.place(x=320, y=25)

listBoxTask = Listbox(width=35, height=12)
listBoxTask.place(x=320, y=50)
listBoxTask.bind('<Button-3>', click_deleteGraphListBoxTask)

def refreshListBoxTask(event):
    listBoxTask.delete(0, listBoxTask.size())
    graphListTask.clear()
    for task in [taskList[comboTask.current()]]:
        for graph in task[3:]:
            graphListTask.append(graph)
        else:
            graphListTask.reverse()
            for graphToListBoxTask in graphListTask:
                click_acceptParam(graphToListBoxTask, listBoxTask)
            else:
                graphListTask.reverse()


comboTask = Combobox(window)
comboTask.place(x=430, y=2)
comboTask.bind("<<ComboboxSelected>>", refreshListBoxTask)


btnDelAll = Button(window, text='Очистить', command=click_deleteAllListBoxTask)
btnDelAll.place(x=540, y=50)

###### БЛОК СИГНАЛОВ ######
label1 = Label(window, text='Обший список сигналов:', font=("Arial", 10)).place(x=0, y=0, anchor=NW)

listBox = Listbox(width=35, height=13)
listBox.place(x=0, y=25)
listBox.bind('<Double-Button-1>', click_addToTask)

btnCreate = Button(window, text='Построить', command=click_createGraph)
btnCreate.place(x=540, y=205)

btnFind = Button(window, text='Поиск', command=click_findGraph)
btnFind.place(x=215, y=25)

###### БЛОК МЕНЮ ######

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Создать')
filemenu.add_command(label="Открыть", command=click_openFile)
filemenu.add_separator()
filemenu.add_command(label='Анализ слов', command=click_wordAnalyzer)
filemenu.add_command(label='Создание нового сигнала', command=click_signalCreator)
mainmenu.add_cascade(label="Файл", menu=filemenu)

taskmenu = Menu(mainmenu, tearoff=0)
taskmenu.add_command(label='Создать задание', command=click_createTask)
mainmenu.add_cascade(label='Задание', menu=taskmenu)

window.mainloop()

