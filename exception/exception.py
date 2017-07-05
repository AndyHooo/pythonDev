#coding: utf-8
##异常处理
import logging
logging.basicConfig(logging.INFO)
try:
    10 / 0
except ZeroDivisionError, e:
    #print 'oops,exception:',e
    #logging.debug("出错了")
    logging.info("出错了")
    #logging.exception("程序出错了")
finally:
    print 'END'