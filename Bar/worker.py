from revent import Worker

worker = Worker()

@worker.on('foo', "update")
def test(bar, test=False):
    if bool(test) == False:
        print('test')
    else:
        print('tested')

if __name__ == "__main__":
    worker.listen(host='127.0.0.1', port=6379, db=0)