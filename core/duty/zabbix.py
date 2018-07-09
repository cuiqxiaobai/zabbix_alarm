"""zabbix:host be added groups ;host be removed groups ; get the relationship between user,usergroup,hostgroup """

from pyzabbix import ZabbixAPI
import setting
print(setting.zURL)
"""zapi is  global variable"""
zabbix_url =
username, passwd =
zapi = ZabbixAPI(zabbix_url)
zapi.login(username, passwd)

class Objzabbix(object):
    def __init__(self):
        pass

    def getHostID(self,hosts=[]):
        pass
    def getGroupID(self,group=''):
        pass
    def addGroup(self,hosts=[],group=''):
        pass
    def removeGroup(self):
        pass
    def getUserGroup(self):
        pass

