
# coding: utf-8

# In[ ]:


from socketIO_client import SocketIO, LoggingNamespace
from datetime import datetime


# In[ ]:


ttime_file = datetime.now().strftime('%Y-%m-%d_%H-%M')
save_file_name_current = 'current_' + ttime_file + '.txt'

def m_current(resString):
    ttime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(ttime + 'current :', str(resString))
    with open(save_file_name_current, 'a') as f:
        f.write(str(resString) + '\n')

    
def connect_current():
    with SocketIO('https://streamer.cryptocompare.com', 0) as socket:
        print('Connected')
        socket.emit('SubAdd', {'subs': ['2~Poloniex~ETH~USD']})
        socket.on('m', m_current)
        socket.wait(60)

while True:
    try:
        connect_current()
    except Exception as err:
        print('ERROR:', str(err))


# In[ ]:




