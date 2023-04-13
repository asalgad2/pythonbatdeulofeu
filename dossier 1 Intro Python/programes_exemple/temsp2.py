from time import gmtime,localtime,strftime
print('Data i hora en formats habituals')
format_curt=strftime('%d/%m/%y',localtime())
print('Data en format curt:',format_curt)
format_dataihora=strftime('%d/%m/%y  %H:%M:%S',localtime())
print('Data i hora:',format_dataihora)