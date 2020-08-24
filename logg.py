# Write a Python Program to create a log file and write WARNING and Higher level messages?

import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
print('loggin demo')
logging.debug("debug message")
logging.critical("critical message")
logging.info("information")
logging.error("error message")
logging.warning('warning Information')
#o/p WARNING:root:warning Information
# ERROR:root:error Information
# CRITICAL:root:critical Information
# Note:
# In the above program only WARNING and higher level messages will be written to the log file



# If we set level as DEBUG then all messages 	will be written to the log file.
logging.basicConfig(filename='log1.txt' ,level=logging.DEBUG)
print ('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')




logging.basicConfig(filename='log2.txt')#by default level is WARNING
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')


# logging.basicConfig(filename='log3.txt',filemode='a')# if we will run the file multiple time then the data will be added
# # at the last of the previous data
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')


# logging.basicConfig(filename='log4.txt',filemode='w')# if we will run the file multiple time then the  previous data
# # will beoverwritten by the new data
#
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')



#we are not specifying the file name the message will be printed on the  console
logging.basicConfig(filemode='w')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')



#only level name will display
logging.basicConfig(format='%(levelname)s')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')

# only message will display
logging.basicConfig(format='%(message)s')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')



#both level and message
logging.basicConfig(format='%(levelname)s:%(message)s')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')



#time stamp
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')


#changing the format of date and time
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y  %I:%M:%S %p')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')


# logging.basicConfig(filename='log5.txt',level=logging.INFO)
logging.info("A new request came")
try:
    x=int(input("Enter the first number :"))
    y=int(input("Enter second number :"))
    print(x/y)
except ZeroDivisionError as msg:
    print("not divisible by 0")
    logging.exception(msg)
except ValueError as msg:
    print("Enter only int values")
    logging.exception(msg)
logging.info("Request completed")



logging.basicConfig(filename='student.log',level=logging.INFO)
logging.info('info message from student module')



