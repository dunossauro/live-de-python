from requests import get
from shutil import copyfileobj

base_url = 'http://www.tjms.jus.br/cdje/downloadCaderno.do?dtDiario=08/08/2017&cdCaderno=-1&tpDownload=D'
file_ = 'teste.pdf'

xpto = get(base_url, stream=True)
with open(file_, 'wb') as f:
    copyfileobj(xpto.raw, f)
