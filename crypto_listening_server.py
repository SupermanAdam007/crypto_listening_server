from socketIO_client import SocketIO, LoggingNamespace

def m(resString):
	print(str(resString))


def conn(resString):
	print(str(resString))

with SocketIO('https://streamer.cryptocompare.com', 0) as socket:
	print('prdel')
	socket.emit('SubAdd', {'subs': '0~Poloniex~ETH~USD'}, conn)
	print('prdel1')
	socket.on('m', m)



