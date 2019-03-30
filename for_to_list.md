>通过一下这种写法实现两组字串列表的互相拼接，很巧妙
```
In [1]: a =            [tran + side
   ...:             for tran in 'TCP UNIX SSL UNIXDatagram'.split()
   ...:             for side in 'Server Client'.split()]

In [2]: a
Out[2]:
['TCPServer',
 'TCPClient',
 'UNIXServer',
 'UNIXClient',
 'SSLServer',
 'SSLClient',
 'UNIXDatagramServer',
 'UNIXDatagramClient']

In [3]:
```
