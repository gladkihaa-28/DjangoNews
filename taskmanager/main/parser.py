import requests
from bs4 import BeautifulSoup


def get_news():
    dict = {}
    try:
        cookies = {
            'is_mobile': '0',
            'lids': '482274F8DC14AA0F',
            'lid': 'vAsAAFJwb2T4dKkbAdkfVwB=',
            'user-id_1.0.5_lr_lruid': 'pQ8AAFFwb2TKL9qxAWWK9AA%3D',
            'adtech_uid': '030c2bd3-261a-4dda-ac92-f0dd2eb416fb%3Alenta.ru',
            'ab-4335': '1',
            'tmr_lvid': 'ec0d7a7bb96e9220d8c9738402099793',
            'tmr_lvidTS': '1685024849819',
            '_ga': 'GA1.2.783759520.1685024850',
            '_gid': 'GA1.2.465741777.1685024850',
            'top100_id': 't1.80674.532917976.1685024849931',
            '_ym_uid': '1685024850359562511',
            '_ym_d': '1685024850',
            'sspjs_38.25.0_af_lpdid': '%7B%22DATE%22%3A1685024850369%2C%22ID%22%3A%2258787%3A17147%22%7D',
            '_ym_isad': '2',
            'detect_count': '0',
            'vpuid': '1685024857.333-330208995',
            't3_sid_4422985': 's1.1963991357.1685024856427.1685025507654.1.24',
            't3_sid_7356279': 's1.694999838.1685024857369.1685025507656.1.61',
            't3_sid_7643964': 's1.485879761.1685024857377.1685025507658.1.34',
            '_gat': '1',
            'last_visit': '1685014708064%3A%3A1685025508064',
            'tmr_detect': '0%7C1685025510563',
            't3_sid_80674': 's1.682600896.1685024849935.1685025524102.1.67',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'is_mobile=0; lids=482274F8DC14AA0F; lid=vAsAAFJwb2T4dKkbAdkfVwB=; user-id_1.0.5_lr_lruid=pQ8AAFFwb2TKL9qxAWWK9AA%3D; adtech_uid=030c2bd3-261a-4dda-ac92-f0dd2eb416fb%3Alenta.ru; ab-4335=1; tmr_lvid=ec0d7a7bb96e9220d8c9738402099793; tmr_lvidTS=1685024849819; _ga=GA1.2.783759520.1685024850; _gid=GA1.2.465741777.1685024850; top100_id=t1.80674.532917976.1685024849931; _ym_uid=1685024850359562511; _ym_d=1685024850; sspjs_38.25.0_af_lpdid=%7B%22DATE%22%3A1685024850369%2C%22ID%22%3A%2258787%3A17147%22%7D; _ym_isad=2; detect_count=0; vpuid=1685024857.333-330208995; t3_sid_4422985=s1.1963991357.1685024856427.1685025507654.1.24; t3_sid_7356279=s1.694999838.1685024857369.1685025507656.1.61; t3_sid_7643964=s1.485879761.1685024857377.1685025507658.1.34; _gat=1; last_visit=1685014708064%3A%3A1685025508064; tmr_detect=0%7C1685025510563; t3_sid_80674=s1.682600896.1685024849935.1685025524102.1.67',
            'Referer': 'https://lenta.ru/?ysclid=li38c8o4ts468090458',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        cookies2 = {
            'is_mobile': '0',
            'lids': '482274F8DC14AA0F',
            'lid': 'vAsAAFJwb2T4dKkbAdkfVwB=',
            'user-id_1.0.5_lr_lruid': 'pQ8AAFFwb2TKL9qxAWWK9AA%3D',
            'adtech_uid': '030c2bd3-261a-4dda-ac92-f0dd2eb416fb%3Alenta.ru',
            'ab-4335': '1',
            'tmr_lvid': 'ec0d7a7bb96e9220d8c9738402099793',
            'tmr_lvidTS': '1685024849819',
            '_ga': 'GA1.2.783759520.1685024850',
            '_gid': 'GA1.2.465741777.1685024850',
            'top100_id': 't1.80674.532917976.1685024849931',
            '_ym_uid': '1685024850359562511',
            '_ym_d': '1685024850',
            'sspjs_38.25.0_af_lpdid': '%7B%22DATE%22%3A1685024850369%2C%22ID%22%3A%2258787%3A17147%22%7D',
            '_ym_isad': '2',
            'detect_count': '0',
            'vpuid': '1685024857.333-330208995',
            'chash': '2OxiizxMhk',
            'last_visit': '1685015311337%3A%3A1685026111337',
            '_gat': '1',
            'rchainid': '%7B%22message%22%3A%22need%20session%22%2C%22code%22%3A-4000%2C%22details%22%3A%7B%22method%22%3A%22%2Fsession%2FgetRsidx%22%2C%22requestId%22%3A%22ridli391h23fcpiyi1so%22%7D%7D',
            'tmr_detect': '0%7C1685026114276',
            't3_sid_80674': 's1.682600896.1685024849935.1685026133788.1.107',
            't3_sid_4422985': 's1.1963991357.1685024856427.1685026133791.1.34',
            't3_sid_7356279': 's1.694999838.1685024857369.1685026133794.1.73',
            't3_sid_7643964': 's1.485879761.1685024857377.1685026133808.1.42',
        }
        headers2 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'is_mobile=0; lids=482274F8DC14AA0F; lid=vAsAAFJwb2T4dKkbAdkfVwB=; user-id_1.0.5_lr_lruid=pQ8AAFFwb2TKL9qxAWWK9AA%3D; adtech_uid=030c2bd3-261a-4dda-ac92-f0dd2eb416fb%3Alenta.ru; ab-4335=1; tmr_lvid=ec0d7a7bb96e9220d8c9738402099793; tmr_lvidTS=1685024849819; _ga=GA1.2.783759520.1685024850; _gid=GA1.2.465741777.1685024850; top100_id=t1.80674.532917976.1685024849931; _ym_uid=1685024850359562511; _ym_d=1685024850; sspjs_38.25.0_af_lpdid=%7B%22DATE%22%3A1685024850369%2C%22ID%22%3A%2258787%3A17147%22%7D; _ym_isad=2; detect_count=0; vpuid=1685024857.333-330208995; chash=2OxiizxMhk; last_visit=1685015311337%3A%3A1685026111337; _gat=1; rchainid=%7B%22message%22%3A%22need%20session%22%2C%22code%22%3A-4000%2C%22details%22%3A%7B%22method%22%3A%22%2Fsession%2FgetRsidx%22%2C%22requestId%22%3A%22ridli391h23fcpiyi1so%22%7D%7D; tmr_detect=0%7C1685026114276; t3_sid_80674=s1.682600896.1685024849935.1685026133788.1.107; t3_sid_4422985=s1.1963991357.1685024856427.1685026133791.1.34; t3_sid_7356279=s1.694999838.1685024857369.1685026133794.1.73; t3_sid_7643964=s1.485879761.1685024857377.1685026133808.1.42',
            'If-None-Match': 'W/"0b3cd278b1bf252640abe88ed7d43526"',
            'Referer': 'https://lenta.ru/parts/news/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.get('https://lenta.ru/parts/news/', cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        for link in soup.find_all('a', class_='card-full-news _parts-news'):
            if "http" in link.get('href'):
                pass
            else:
                card_link = f"https://lenta.ru{link.get('href')}"
                res = requests.get(card_link, cookies=cookies2, headers=headers2)
                sp = BeautifulSoup(res.text, 'lxml')
                news_title = sp.find('span', class_='topic-body__title').text
                news_text = sp.find('div', class_='topic-body__content').text
                dict[news_title] = news_text

    except:
        pass

    return dict


