
# coding: utf-8

# In[1]:


from socketIO_client import SocketIO, LoggingNamespace
from datetime import datetime


# In[2]:


ttime_file = datetime.now().strftime('%Y-%m-%d_%H-%M')
save_file_name_trade = 'trade_' + ttime_file + '.txt'


# In[3]:


def m_trade(resString):
    ttime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(ttime + 'trade :', str(resString))
    with open(save_file_name_trade, 'a') as f:
        f.write(str(resString) + '\n')


# In[ ]:


def connect_trade():
    with SocketIO('https://streamer.cryptocompare.com', 0) as socket:
        print('Connected')
        socket.emit('SubAdd', {'subs': ['0~Poloniex~ETH~USD']})
        socket.on('m', m_trade)
        socket.wait(60)


# In[ ]:


while True:
    try:
        connect_trade()
    except Exception as err:
        print('ERROR:', str(err))


# In[ ]:




