import os

for fl in [y for y in os.listdir() if '.html' in y]:
    with open('result.html', 'w', encoding='utf8') as result:
        with open(fl, 'r', encoding='utf8') as file:
            text = file.read()
            _temp_links = text.split("\"/thumb/2/")[1:]
            links = ['/thumb/2/' + x.split("\"")[0] for x in _temp_links]
            # print(links, len(links))
            for link in links:
                true_link = '/thumb/2/' + link.split('/')[-1]
                text = text.replace(link, true_link)
            result.write(text)

    with open('result.html', 'r', encoding='utf8') as result:
        with open(fl, 'w', encoding='utf8') as file:
            file.write(result.read())