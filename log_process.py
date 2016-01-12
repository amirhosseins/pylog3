
import re
import csv
import sqlite3
import argparse
import sys
import time, datetime, aniso8601
from functions import *



###########################################


parser = argparse.ArgumentParser()
parser.add_argument(
     'input',
     type = argparse.FileType('r'),
     default = sys.stdin,
     nargs = '?',
     help = "File to parse; will read from stdin otherwise")

parser.add_argument('-c', '--counter', action='store_true', help='Download Counters')
parser.add_argument('-i', '--ip', action='store_true', help='ip/uuid remove redundent IPs')
parser.add_argument('-z', '--isp', action='store_true', help='Show ISP dl traffic')
parser.add_argument('-s', '--stat', action='store_true', help='Show stat (time, processed lines, ...')
parser.add_argument('-l', '--location', help='Location')
parser.add_argument('-t', '--table', help='Sql format for output')

args = parser.parse_args()


start = time.time()

########################################################

line_dl = re.compile(r"""(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}),\-,(?P<date>\d{4}\-\d{2}\-\d{2})T(?P<hour>\d{2}):\d{2}:\d{2}(\+|\-)\d{2}:\d{2},((?P<method>GET|POST|HEAD) )(?P<url>(\/dl\/|\/preview\/.+?) (http\/\d\.\d)),(?P<statuscode>\d{3}),(?P<bytessent>\d+),(.*)""", re.IGNORECASE)

uuid_pattern = re.compile(r'.+\/(?P<uuid>(\w{10}|\w{8}\-\w{4}\-\w{4}-\w{4}\-\w{12}))\/.+')

# ignore_preview = re.compile(r'.+\/preview\/.+\/(small|medium|large)\/.+', re.IGNORECASE)

########################################################

loation = "NA"
if args.location:
    location = args.location


table = "NA"
if args.table:
    table= args.table

########################################################

skipped_lines = 0
line_count = 0

########################################################

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('CREATE TABLE logs (dateandtime text, ip text, isp text, uuid text, size int)')

########################################################

loation = "NA"
if args.location:
    location = args.location

########################################################

for line in args.input:
    line_count += 1
    line = line.strip()


    match = line_dl.match(line)
#    if match:
#         print ("OK: " + line + "\n" )
    if not match:
         skipped_lines += 1
#         print ("SKIPPED" + line + "\n" )
         continue


    line2 = match.groupdict()

    url = line2['url']

    uuid_match = uuid_pattern.match(url)

    if not uuid_match:
        skipped_lines += 1
        continue

    #code = line2['statuscode']
    #method = line2['method']
    ip = line2['ip']

    isp = isp_lookup(ip)

    date = line2['date']
    hour = line2['hour']
 
    dateandtime = date + ' ' + hour + ":00:00" 

    #epoch = int(time.mktime(aniso8601.parse_datetime(dateandtime).timetuple()))
    #epoch_rounded = epoch - (epoch%3600)

    url = line2 ['url']
    bytessent = line2['bytessent']

    uuid = uuid_match.groupdict()['uuid']
    
    #print (ip,",", isp,",",uuid,",", bytessent )

    c.execute('INSERT INTO logs VALUES (?,?,?,?,?)', (dateandtime, ip, isp, uuid, bytessent) )


c.execute('''CREATE VIEW group1 AS
             SELECT dateandtime, ip, isp, uuid, sum(size) as sum_dl
             FROM logs GROUP BY  ip, uuid ''')

#####################################################################
if args.isp:
    # per ISP traffic
    c.execute('''CREATE VIEW group0 AS
                 SELECT isp, sum(size) as sum_dl
                 FROM logs GROUP BY isp ''')
    
    print ("---ISP Traffic----------------------------")
    
    for isp, total_dl in c.execute('''
        SELECT isp, sum_dl
        FROM group0 '''):
             print (isp, total_dl) 
#####################################################################    
if args.ip:    

    # merge redundant downloads per IP (in one hour as assumed)
    
    first_line = "INSERT INTO "+ table + " (dateandtime, location, ip, isp, uuid, size) VALUES "

    print (first_line)

    my_list = c.execute (''' SELECT dateandtime, ip, isp, uuid, sum_dl FROM group1 ''')

    #row0 = my_list.fetchone()
    #print (row0)

    for dateandtime, ip, isp, uuid, total_dl in my_list :
             insert= " ('" + dateandtime + "','" + location + "','" + ip + "','" + isp + "','" + uuid + "','" + str(total_dl) + "'),"
             print (insert)
    
    
    #for dateandtime, ip, isp, uuid, total_dl in row0 :
    #         insert2= " ('" + dateandtime + "','" + location + "','" + ip + "','" + isp + "','" + uuid + "','" + str(total_dl) + "');"
    #         print (insert2)
    #print (row0)
    
#####################################################################    
if args.counter:
    # find downloads for each file
    first_line = "INSERT INTO "+ table + " (location, uuid, count_dl) VALUES "
    c.execute('''CREATE VIEW group2 AS
                 SELECT uuid, count(uuid) as count_dl
                 FROM group1 GROUP BY uuid ''')
    
    #print ("--UUID ------ #Downloads Count-----------------------")
    for uuid, count_dl in c.execute('''
        SELECT uuid, count_dl
        FROM group2 '''):
             print (" ('" + location + "','" + uuid + "','" + str(count_dl) + "'),") 

############################################################################
if args.stat:
    print ('Duration: ', time.time() - start)
    print ('Lines: ', line_count)
    print ('Skipped Lines: ', skipped_lines )

