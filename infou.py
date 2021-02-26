import psutil
import time
import eel

def infou():
    cpu_perc = '<span class = \'number\'>' + str(psutil.cpu_percent(1)) + '%' + '</span>' + ' CPU Usage'
    memr = '<span class = \'number\'>' + str(round(psutil.virtual_memory().used / 1073741824, 2)) + 'GB ' + '</span>' + ' Memory Usage'
    disc = '<span class = \'number\'>' + str(round(psutil.disk_usage('/').free / 1073741824, 2)) + 'GB ' + '</span>' + ' of Disk Space Available'
    eel.display(cpu_perc, memr, disc)

eel.init('Web')
eel.start('index.html', size = (1584, 790), block = False)

while True:
    infou()
    eel.sleep(2)
