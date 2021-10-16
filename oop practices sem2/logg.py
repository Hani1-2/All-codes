###Slide 12
##
##import logging
##logging.critical('This is a critical message')



###Slide 13
##
# import logging
# logging.debug("Harmless debug Message")
# logging.info("Just an information")
# logging.warning("It is a Warning")
# logging.error("Did you try to divide by zero")
# logging.critical("Internet is down")



###Slide 16
# ##
# import logging
# # logging.basicConfig(format='%(asctime)s - %(message)s')
# logging.basicConfig(filename='test.log', format='%(asctime)s - %(message)s')
# logging.warning('Admin logged out')



###Slide 17
##
# import logging
# logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')
# l=logging.getLogger('myLogger')
# l.critical('This is a critical message')


### Slide 19
# ##
# import logging
# logging.basicConfig(level=logging.INFO,filename='value.log', format='%(asctime)s - %(message)s')
# try:
#    value=int(input('Enter an integer: '))
#    logging.info(value)
#
# except:
#    logging.exception('Error')
#    logging.critical('exception occur')