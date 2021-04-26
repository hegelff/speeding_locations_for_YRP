'''
Created on Mar 16, 2021

@author: FengF
'''

conn_str = 'Driver={SQL Server};\
            Server=YKR-DEV-DBS-DW\SQLDB1;\
            Database=CCS_Analysis;\
            Trusted_Connection=yes;'

#getting location list and other information from this file
#roads name,geoid,ns or ew, pspl,studydat, dow(sun is 1), 
roads_info='''roads_info.csv'''

#chart output folder
chart_out_dir='''charts/'''
