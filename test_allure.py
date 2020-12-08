import _thread
import logging
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)
loops=[2,4]
def loop(nloop,nsec,lock):
    logging.info("start loop " + nloop + "at" + ctime())
    sleep(4)
    logging.info("end loop0 " + nloop + "at" + ctime())
    lock.release()

def main():
    logging.info("start all at " + ctime())
    locks=[]
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1,())
    sleep(6)
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()






