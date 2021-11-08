import os
import requests
from dotenv import load_dotenv
load_dotenv()

def make_pair(x, y):
    return lambda n: x if n == 0 else y


def first(p):
    return p(0)


def second(p):
    return p(1)

if __name__ == '__main__':
    url = f"https://api.miro.com/v1/boards/{os.getenv('MIRO_BOARD_ID')}/widgets/?widgetType=shape"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('MIRO_API_TOKEN')}"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.json())



    realres = []
    # вывод всех текстов
    for i in range(0, len(response.json()['data'])):
        p = make_pair(response.json()['data'][i]['id'], response.json()['data'][i]['text'])
        print(f'{first(p)} : {second(p)}')
        if response.json()['data'][i]['style']['backgroundColor'] == "#e6e6e6":
            j = 1
            L = []
            listY = []
            while response.json()['data'][i+j]['style']['backgroundColor'] == "#5396e6" or response.json()['data'][i+j]['style']['backgroundColor'] == "#ffffff":
                if i+j == len(response.json()['data'])-1:
                    if response.json()['data'][i+j]['style']['backgroundColor'] == "#5396e6" or response.json()['data'][i+j]['style']['backgroundColor'] == "#ffffff":
                        listY.append(float(response.json()['data'][i + j]['y']))
                        L.append(response.json()['data'][i + j]['text'][3:len(response.json()['data'][i+j]['text'])-4])
                    break
                listY.append(float(response.json()['data'][i+j]['y']))
                L.append(response.json()['data'][i+j]['text'][3:len(response.json()['data'][i+j]['text'])-4])

                j += 1
            d = {}

            for g in range(0, len(listY)):
                if listY[g] in d.keys():
                    d[listY[g]].append(L[g])
                else:
                    d[listY[g]] = list()
                    d[listY[g]].append(L[g])
            res = []
            list_keys = list(d.keys())
            list_keys.sort()
            for v in list_keys:
                res.append(d[v])
            realres.append(res)

    print()

    for i in realres:
        print(i)
        #print()



    print('\n\n\n')

    url_widget = f"https://api.miro.com/v1/boards/{os.getenv('MIRO_BOARD_ID')}/widgets/?widgetType=line"
    response_widget = requests.request("GET", url_widget, headers=headers)

    # вывод всех текстов
    for i in range(0, len(response_widget.json()['data'])):
        p = make_pair(response_widget.json()['data'][i]['startWidget'], response_widget.json()['data'][i]['endWidget'])

        print(f'{first(p)} -> {second(p)}')

