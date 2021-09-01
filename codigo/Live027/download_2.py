from requests import get
from shutil import copyfileobj
from uteis import days

days = list(map(lambda day: str(day) if len(str(day)) > 1 else '0' + str(day),
                days))

base_url = 'http://www.tjms.jus.br/cdje/downloadCaderno.do'
full_url = '{}?dtDiario=DAY/10/2017&cdCaderno=3&tpDownload=D'.format(base_url)

files_list = [full_url.replace('DAY', day) for day in days]


def download_file(name, url):
    xpto = get(url, stream=True)
    with open(name, 'wb') as f:
        copyfileobj(xpto.raw, f)


for day, file_ in zip(days, files_list):
    print(file_)
    download_file('{}.pdf'.format(day), file_)
