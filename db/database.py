#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
create_engine() 用来初始化数据库连接。
    SQLAlchemy用一个字符串表示连接信息：
        '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    #Windows
        engine = create_engine('sqlite:///C:\\path\\to\\foo.db')
'''


from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, Integer, DateTime, Boolean

import os

# 创建对象的基类:
Base = declarative_base()

class Database():
    """
    1. 创建一个数据库, 存在则不创建.
    2. 创建表, 存在则会报错.
    3. 创建连接. 一个可操作数据库的连接.
    4. 创建会话. 一个可操作数据库的会话.
    5. 之后的增删查改都要通过会话提交
    """
    def __init__(self, projectPath):
        databaseName = u"data.db"
        self.engine = create_engine(u"sqlite:///{0}\{1}".format(projectPath, databaseName), echo=False)     # 建立数据库连接
        Base.metadata.create_all(self.engine)                               # 先检查data库表的存在性，如果不存在的话会执行表的创建工作 //是具体什么样的表与继承Base类相关
        DBSession = sessionmaker(bind=self.engine)                          # 创建一个可操作数据库的连接
        self.session = DBSession()                                          # 从engine所维护的连接池中取出一个连接来操作数据库。这个连接在我们应用有所更改或者关闭Session时会被释放。

    def addIpInfo(self, ip, country, region, city, idc):
        newIpInfo = IpInfo(ip=ip, country=country, region=region, city=city, idc=idc)                  # 创建新IpInfo对象:
        self.session.add(newIpInfo)                                         # 添加到session:
        self.session.commit()                                               # 提交即保存到数据库:
        self.session.close()                                                # 关闭session:

    def queryIpInfo(self, ip):
        query_result = self.session.query(IpInfo).filter(IpInfo.ip == ip).all()  # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        self.session.close()
        return query_result

    def addReverseIpInfo(self, ip, row, s_domain, date):
        newReverseIpInfo = ReverseIpInfo(ip=ip, row=row, s_domain=s_domain, date=date)
        self.session.add(newReverseIpInfo)
        self.session.commit()
        self.session.close()

    def queryReverseIpInfo(self, ip):
        query_result = self.session.query(ReverseIpInfo).filter(ReverseIpInfo.ip == ip).all()
        self.session.close()
        return query_result

    def addNmapResult(self, ip, command, result):
        newNmapResult = NmapResult(ip=ip, command=command, result=result)
        self.session.add(newNmapResult)
        self.session.commit()
        self.session.close()

    def queryNmapResult(self, ip):
        query_result = self.session.query(NmapResult).filter(NmapResult.ip == ip).all()
        self.session.close()
        return query_result

    def addDomainToIpInfo(self, domain, ip):
        newDomainToIpInfo = DomainToIpInfo(domain=domain, ip=ip)
        self.session.add(newDomainToIpInfo)
        self.session.commit()
        self.session.close()

    def queryDomainToIpInfo(self, domain):
        query_result = self.session.query(DomainToIpInfo).filter(DomainToIpInfo.domain == domain).all()
        self.session.close()
        return query_result

    def addWhois(self, domain, r_name, r_e_mail, r_phone, country, province, city, r_date, e_date, s_registrar):
        newWhois = Whois(domain=domain, r_name=r_name, r_e_mail=r_e_mail, r_phone=r_phone, country=country, province=province, city=city, r_date=r_date, e_date=e_date, s_registrar=s_registrar)
        self.session.add(newWhois)
        self.session.commit()
        self.session.close()

    def queryWhois(self, domain):
        query_result = self.session.query(Whois).filter(Whois.domain == domain).all()
        self.session.close()
        return query_result

    def addSubDomain(self, domain, row, sub_domain, title):
        newSubDomainInfo = SubDomainInfo(domain=domain, row=row, sub_domain=sub_domain, title=title)
        self.session.add(newSubDomainInfo)
        self.session.commit()
        self.session.close()

    def querySubDomain(self, domain):
        query_result = self.session.query(SubDomainInfo).filter(SubDomainInfo.domain == domain).all()
        self.session.close()
        return query_result


class IpInfo(Base):
    # 表的名字:
    __tablename__ = u'ip_info'

    # 表的结构:
    ip = Column(String(15), primary_key=True)
    country = Column(String)
    region = Column(String)
    city = Column(String)
    idc = Column(String)

class ReverseIpInfo(Base):
    # 表的名字:
    __tablename__ = u'reverse_ip_info'

    # 表的结构:
    ip = Column(String(15))
    row = Column(Integer)
    s_domain = Column(String, primary_key=True)
    date = Column(String)

class NmapResult(Base):
    # 表的名字:
    __tablename__ = u'nmap_results'

    # 表的结构:
    ip = Column(String(15), primary_key=True)
    command = Column(String)
    result = Column(String)

class DomainToIpInfo(Base):
    # 表的名字:
    __tablename__ = u'domain_to_ip_info'

    # 表的结构:
    domain = Column(String)
    ip = Column(String(15), primary_key=True)

class Whois(Base):
    # 表的名字:
    __tablename__ = u'whois'

    # 表的结构:
    domain = Column(String, primary_key=True)
    r_name = Column(String)
    r_e_mail = Column(String(50))
    r_phone = Column(String(25))
    country = Column(String(30))
    province = Column(String(30))
    city = Column(String(30))
    r_date = Column(String(30))
    e_date = Column(String(30))
    s_registrar = Column(String)

class  SubDomainInfo(Base):
    # 表的名字:
    __tablename__ = u'subdomain_info'

    # 表的结构:
    domain = Column(String)
    row = Column(Integer)
    sub_domain = Column(String, primary_key=True)
    title = Column(String)


if __name__ == "__main__":
    projectPath = r"{0}\project\{1}".format(os.path.abspath('..'), u"test")
    #print(projectPath)
    database = Database(projectPath)
    database.addIpInfo("192.168.0.8", "中国", "广东", "广州", "电信")
    #database.queryIpInfo("192.168.0.1")
    print("success")
    """
    databaseName = u"data.db"
    projectPath2 = u"sqlite:///{0}\{1}".format(projectPath, databaseName)
    print(projectPath2)
    """