import json
import ijson
import re
from shutil import copyfile


'''
В списках User-Agent(UA), которые раздаются бесплатно, можно легко напороться на User-Agent ботов и устаревшие UA.
Системы защиты популярных ресурсов гарантировано блокируют запросы с теми версиями ОС, браузеров и их движков в User-Agent, которые вышли более 5 лет назад.
Поэтому при создании списка валидных/настоящих UA нужно отсеить мусорные строки. Для этого удобно использовать регулярки. Этим и занимается ф-я garbage_sort()
Известные мне на момент 25.07.2026 критерии UA настоящих пользователей:
1. Минорные версии Chrome начиная со 101 заморожены в формате Major.0.0.0 (например, Chrome/146.0.0.0 или Chrome/150.0.0.0)
2. Версии Chrome ниже 101.0 - это всегда боты
3. У всех пользователей, заходящих с Windows, в UA всегда установлена версия этой ОС 10 (Windows NT 10.0)
!!! - 4. Начиная с iOS 26 и iPadOS 26 актуальное значение в строке жёстко заморожено на iPhone OS 18_6 (или 18_7) с 2025 года для всех пользователей,
соответственно заморозка не коснулась пользователей устройств на iOS и iPadOS ниже 26. По этой заморозке окончательного решения в Apple не принято, 
поэтому в итоговом списке я пока оставил UA с iPhone OS 26 и 27
5. Для всех пользователей macOS версия этой ОС в UA так же заморожена (уже давно) на версии Mac OS X 10_15_7 (или Mac OS X 10.15 в Firefox)
6. В UA пользователей Mac и iPhone меняется только версия браузера Safari: актуальные Version/26.x и Version/27.x, а Version/18.x - старая (ниже 18 - устаревшие)
7. Браузеры Apple и Firefox не отправляют Client Hints - то есть при запросе отправляется только UA этих пользователей
8. Версия Firefox всегда оканчивается на .0 (Firefox/153.0 - актуальная на июль 2026, есть также 115 для старых ОС и 140), а его движок Gecko всегда на версии 20100101 
(Gecko/20100101) для настольных ОС (Windows, macOS, Linux). Для Android версия Gecko равна версии Firefox, а для iOS/iPhone имеет собственную метку FxiOS/<version>
9. Версия Android в Chromium-браузерах всегда Android 10, а модель всегда K (Linux; Android 10; K), а настоящие версия и модель отправляются 
в Sec-CH-UA-Platform-Version и Sec-CH-UA-Model. В Firefox в UA настоящая версия, а модель: Tablet или Mobile (Android 15; Mobile; rv:153.0)
10. Версия Microsoft Edge как и Chrome всегда оканчивается на 0.0.0 (Edg/150.0.0.0 - актуальная), а для iOS EdgA/<version> или EdgiOS/<version>
11. Версия Opera как и Chrome всегда оканчивается на 0.0.0 (OPR/133.0.0.0 - актуальная), для iOS OPT/<version>, 
а геймерская версия на мобильных OPX/<version> (актуальная на мобилках - 100.0.0.0)
'''
#^(?:(?!Chrome/)(?!Edg/)(?!OPR/)(?!OPX/)(?!OPT/)(?!Version/)(?!Firefox/)(?!GSA/)(?!CriOS/)(?!FxiOS/)(?!iPhone).)*$
def garbage_sort(name1 = r'C:\Users\%USERPROFILE%\Desktop\user-agents.json', name2 = r'C:\Users\%USERPROFILE%\Desktop\user-agents1.json'):
    ofr1 = open(name1, 'r', encoding='utf-8')
    ofw1 = open(name2, 'w', encoding='utf-8')
    novalid = 0
    valid = 0
    first = True
    ofw1.write('[')
    for n1 in ijson.items(ofr1, 'item', use_float=True):
        if re.search(r'Chrome/1[0-9]{2}(?!\.0\.0\.0)|Chrome/[3-9]|Windows NT [^1][^0]|Mac OS.+Version/1[1-7]|Mac OS X (?!10_15_7|10.15)', n1["userAgent"]):  #|iPhone OS 18_(?:[^7]|7[^ ])
            novalid += 1
            continue
        if not first:
            ofw1.write(',\n')
        ofw1.write(json.dumps(n1, ensure_ascii='False'))
        valid += 1
        first = False
    ofr1.close()
    ofw1.write(']')
    ofw1.close()
    print(f'Боты и устаревшие UA: {novalid}')
    print(f'Валидные UA: {valid}')
    print(f'Всего строк: {novalid+valid}')





def record_new(name1 = r'C:\Users\%USERPROFILE%\Desktop\user-agents1.json', name2 = r'C:\Users\%USERPROFILE%\Desktop\tUAintoli.json', uniq_ua=False):
    unusual_ua(name1)
    ofr1 = open(name2, 'r', encoding='utf-8')
    orig = list(ijson.items(ofr1, 'item', use_float=True))
    ofr1.close()
    if not uniq_ua:
        ofr3 = open(name1, 'r', encoding='utf-8')
        new_data = 0
        for n1 in ijson.items(ofr3, 'item', use_float=True):
            if not n1 in orig:
                orig.append(n1)
                new_data += 1
        ofr3.close()
    else:
        ofr2 = open(name2, 'r', encoding='utf-8')
        origUA = list(ijson.items(ofr2, 'item.userAgent', use_float=True))
        ofr2.close()

        ofr3 = open(name1, 'r', encoding='utf-8')
        new_data = 0
        for n1 in ijson.items(ofr3, 'item', use_float=True):
            if not n1['userAgent'] in origUA:
                origUA.append(n1['userAgent'])
                orig.append(n1)
                new_data += 1
        ofr3.close()

    ofw1 = open(name2, 'w', encoding='utf-8')
    ofw1.write('[')
    first = True
    total = 0
    if not uniq_ua:
        for n2 in orig:
            if not first:
                ofw1.write(',\n')
            ofw1.write(json.dumps(n2, ensure_ascii='False'))
            total += 1
            first = False
    else:
        for n2 in orig:
            if not first:
                ofw1.write(',\n')
            ofw1.write(json.dumps(n2, ensure_ascii='False'))
            total += 1
            first = False
    ofw1.write(']')
    ofw1.close()

    if uniq_ua:
        print(f'Новых UA: {new_data}')
        print(f'Итого оригинальных UA-строк: {total}')
    else:
        print(f'Новых данных: {new_data}')
        print(f'Итого данных в конечном файле: {total}')





def remove_duplicates(name1 = r'C:\Users\%USERPROFILE%\Desktop\tUAintoli.json', uniq_ua=False):
    ofr1 = open(name1, 'r', encoding='utf-8')
    total = list(ijson.items(ofr1, 'item', use_float=True))
    ofr1.close()

    ofw1 = open(name1, 'w', encoding='utf-8')
    ofw1.write('[')
    first = True
    res = 0
    dupl = 0
    origUA = []
    if uniq_ua:
        for n1 in total:
            if not n1['userAgent'] in origUA:
                origUA.append(n1['userAgent'])
                if not first:
                    ofw1.write(',\n')
                ofw1.write(json.dumps(n1, ensure_ascii='False'))
                res += 1
                first = False
            else:
                dupl += 1
    else:
        for n1 in total:
            if not n1 in origUA:
                origUA.append(n1)
                if not first:
                    ofw1.write(',\n')
                ofw1.write(json.dumps(n1, ensure_ascii='False'))
                res += 1
                first = False
            else:
                dupl += 1
    ofw1.write(']')
    ofw1.close()

    if uniq_ua:
        print(f'UA-дубликатов: {dupl}')
        print(f'Итого оригинальных UA-строк: {res}')
    else:
        print(f'Дубликатов: {dupl}')
        print(f'Итого оригинальных данных: {res}')





def unusual_ua(fname):  #Удаляет (по выбору) необычные UA
    with open(fname, 'r', encoding='utf-8') as ofr1:
        total = list(ijson.items(ofr1, 'item', use_float=True))

    with open(fname, 'w', encoding='utf-8') as ofw1:
        ofw1.write('[')
        first = True
        unusUA = []
        for n1 in total:
            if re.fullmatch(r'^(?:(?!Chrome/)(?!Version/)(?!Firefox/)(?!GSA/)(?!CriOS/)(?!FxiOS/)(?!iPhone)(?!Macintosh)(?!iPad).)*$', n1['userAgent']) and not n1['userAgent'] in unusUA:
                print('Обнаружен необычный User-Agent')
                print(n1['userAgent'])
                unusUA.append(n1['userAgent'])
                answer = input('Удалить или оставить(1) его? Ответ(ничего/1): ')
                if not answer:
                    continue
            if not first:
                ofw1.write(',\n')
            ofw1.write(json.dumps(n1, ensure_ascii=False))
            first = False
        ofw1.write(']')

    
    
    












if __name__ == '__main__':
    garbage_sort()    #Создаёт новый файл, в который записывает только данные с валидными UA из скаченного списка intoli 
    #record_new()   #Из созданного файла с валидными UA записывает новые данные в основной файл (во временную версию)
    #remove_duplicates()    #Удалить во временном файле (копии основного) все дубликаты
    #copyfile(r'C:\Users\%USERPROFILE%\Desktop\tUAintoli.json', r'C:\Users\%USERPROFILE%\Desktop\UAintoli.json')    #Перезаписывает основной файл, записывая в него содержимое из временной версии


    #garbage_sort(r'C:\Users\%USERPROFILE%\Desktop\UAintoli.json', r'C:\Users\%USERPROFILE%\Desktop\tUAintoli.json')     #Если ужесточится сортировка, то можно использовать для обновления временного файла. После этого для изменения основного нужно воспользоваться предыдущим copyfile()
    #remove_duplicates(r'C:\Users\%USERPROFILE%\Desktop\tuniqUA.json', True)  #Нужно применить к КОПИИ основного (или временного) файла с тысячими данных с UA, дав копии любое уникальное имя (например, "uniqUA.json"). Сохранятся ТОЛЬКО данные с уникальными UA

    record_new(uniq_ua=True)    #Из созданного файла с валидными UA записывает новые данные с уникальными UA в основной файл (во временную версию)
    record_new(name2 = r'C:\Users\%USERPROFILE%\Desktop\tuniqUA.json', uniq_ua=True)    #Из созданного файла с новыми валидными UA записывает новые данные во временный файл уникальных UA
    copyfile(r'C:\Users\%USERPROFILE%\Desktop\tUAintoli.json', r'C:\Users\%USERPROFILE%\Desktop\UAintoli.json')
    copyfile(r'C:\Users\%USERPROFILE%\Desktop\tuniqUA.json', r'C:\Users\%USERPROFILE%\Desktop\uniqUA.json')
    pass