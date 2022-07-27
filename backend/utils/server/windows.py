#!/bin/python
# coding: utf-8
# +-------------------------------------------------------------------
# | django-vue3-lyadmin
# +-------------------------------------------------------------------
# | Author: lybbn
# +-------------------------------------------------------------------
# | QQ: 1042594286
# +-------------------------------------------------------------------

# ------------------------------
# windows系统命令工具类封装
# ------------------------------

import platform
import os, time, re, json, socket
import psutil
import winreg
from random import Random
from django.core.cache import cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PUBLIC_DICT = os.path.join(BASE_DIR, 'public.json')


def ReadFile(filename, mode='r'):
    """
    读取文件内容
    @filename 文件名
    return string(bin) 若文件不存在，则返回None
    """

    import os, chardet
    if not os.path.exists(filename): return False
    if not os.path.isfile(filename): return False

    f_body = '';
    try:
        fp = open(filename, mode)
        f_body = fp.read()
    except:
        try:
            fp.close()
        except:
            pass

        try:
            encoding = 'utf8'
            fp = open(filename, mode, encoding=encoding)
            f_body = fp.read()
        except:
            try:
                fp.close()
            except:
                pass
            try:
                encoding = 'gbk'
                fp = open(filename, mode, encoding=encoding)
                f_body = fp.read()
            except:
                try:
                    fp.close()
                except:
                    pass

                encoding = 'ansi'
                fp = open(filename, mode, encoding=encoding)
                f_body = fp.read()

    try:
        if f_body[0] == '\ufeff':
            # 处理带bom格式
            new_code = chardet.detect(f_body.encode(encoding))["encoding"]
            f_body = f_body.encode(encoding).decode(new_code);
    except:
        pass

    fp.close()
    return f_body


def readFile(filename, mode='r'):
    return ReadFile(filename, mode)


def ReadReg(path, key):
    """
    读取注册表
    @path 注册表路径
    @key 注册表键值
    """
    import winreg
    try:
        newKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        value, type = winreg.QueryValueEx(newKey, key)
        return value
    except:
        return False


def DelReg(path, key):
    """
    删除注册表
    @path 注册表路径
    @key 注册表键值
    """
    import winreg
    try:
        newKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        winreg.DeleteKey(newKey, key)
        return True
    except:
        return False


def WriteReg(path, key, value, type=winreg.REG_SZ):
    """
    写入/创建注册表
    @path 注册表路径
    @key 注册表键值
    @value 注册表值
    @type 注册表值类型
    """
    import winreg
    try:
        newKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_ALL_ACCESS)
    except:
        newKey = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, path)
    try:
        # SetValue 只支持字符串，其他类型使用SetValueEx
        if isinstance(value, int):
            winreg.SetValueEx(newKey, key, 0, winreg.REG_DWORD, value)
        else:
            winreg.SetValueEx(newKey, key, 0, type, value)
        return True
    except Exception as ex:

        return False


def get_mac_address():
    """
    获取mac
    """
    import uuid
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def process_exists(pname, exe=None):
    """
    检查进程是否存在
    @pname 进程名称
    @exe 进程路径
    """
    try:
        pids = psutil.pids()
        for pid in pids:
            try:
                p = psutil.Process(pid)
                if p.name() == pname:
                    if not exe:
                        return True;
                    else:
                        if p.exe() == exe: return True
            except:
                pass
        return False
    except:
        return True


def GetRandomString(length):
    """
       @name 取随机字符串
       @author hwliang<hwl@bt.cn>
       @param length 要获取的长度
       @return string(length)
    """
    strings = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    chrlen = len(chars) - 1
    random = Random()
    for i in range(length):
        strings += chars[random.randint(0, chrlen)]
    return strings


def Md5(strings):
    """
        @name 生成MD5
        @author hwliang<hwl@bt.cn>
        @param strings 要被处理的字符串
        @return string(32)
    """
    if type(strings) != bytes:
        strings = strings.encode()
    import hashlib
    m = hashlib.md5()
    m.update(strings)
    return m.hexdigest()


def md5(strings):
    return Md5(strings)


def ExecShell(cmdstring, cwd=None, timeout=None, shell=True):
    """
    通过管道执行SHELL
    @cmdstring 需要执行的cmd命令
    @cwd 设置工作目录
    @timeout 超时时间
    @shell 是否通过shell输出
    @output 是否通过文件重定向输出结果（当结果数据量过大必须使用此参数，否则造成管道阻塞）
    """
    import shlex
    import datetime
    import subprocess
    import time, tempfile

    a = ''
    e = ''
    try:
        rx = md5(cmdstring)
        succ_f = tempfile.SpooledTemporaryFile(max_size=4096000, mode='wb+', suffix='_succ', prefix='btex_' + rx)
        err_f = tempfile.SpooledTemporaryFile(max_size=4096000, mode='wb+', suffix='_err', prefix='btex_' + rx)

        sub = subprocess.Popen(cmdstring, shell=shell, bufsize=128, stdout=succ_f, stderr=err_f)
        sub.wait()

        err_f.seek(0)
        succ_f.seek(0)
        a = succ_f.read()
        e = err_f.read()

        if not err_f.closed: err_f.close()
        if not succ_f.closed: succ_f.close()
    except:
        pass

    if type(a) == bytes:
        try:
            a = a.decode('utf-8')
        except:
            try:
                a = a.decode('gb2312')
            except:
                try:
                    a = a.decode('utf-16')
                except:
                    a = a.decode('gb2312', 'ignore')

    if type(e) == bytes:
        try:
            e = e.decode('utf-8')
        except:
            try:
                a = a.decode('utf-16')
            except:
                e = e.decode('gb2312', 'ignore')
    return a, e


class ExcepError(Exception):
    '''
    通用异常对像
    '''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ("运行时发生错误: {}".format(repr(self.value)))


def exists_args(args, get):
    '''
        @name 检查参数是否存在
        @author hwliang<2021-06-08>
        @param args<list or str> 参数列表 允许是列表或字符串
        @param get<dict_obj> 参数对像
        @return bool 都存在返回True，否则抛出KeyError异常
    '''
    if type(args) == str:
        args = args.split(',')
    for arg in args:
        if not arg in get:
            raise KeyError('缺少必要参数: {}'.format(arg))
    return True


# xss 防御
def xssencode(text):
    from html import escape, unescape
    list = ['`', '~', '&', '#', '*', '$', '@', '<', '>', '\"', '\'', ';', '%', ',', '\\u']
    ret = []
    for i in text:
        if i in list:
            i = ''
        ret.append(i)
    str_convert = ''.join(ret)
    text2 = escape(str_convert, quote=True)
    return text2


def path_safe_check(path, force=True):
    """
    校验路径安全
    @path 校验路径
    @force
    """
    if len(path) > 256: return False
    checks = ['..', './', '\\', '%', '$', '^', '&', '*', '~', '#', '"', "'", ';', '|', '{', '}', '`']
    for c in checks:
        if path.find(c) != -1: return False
    if force:
        rep = r"^[\w\s\.\/-]+$"
        if not re.match(rep, path): return False
    return True


def is_ipv4(ip):
    """
    判断是否IPV4地址
    @ip ip地址
    return bool
    """
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except AttributeError:
        try:
            socket.inet_aton(ip)
        except socket.error:
            return False
        return ip.count('.') == 3
    except socket.error:
        return False
    return True


def is_ipv6(ip):
    """
    判断是否IPV6地址
    @ip ip地址
    return bool
    """
    try:
        socket.inet_pton(socket.AF_INET6, ip)
    except socket.error:
        return False
    return True


def to_size(size):
    """
    字节单位转换
    @size 字节大小
    return 返回带单位的格式(如：1 GB)
    """
    if not size: return '0.00 b'
    size = float(size)

    d = ('b', 'KB', 'MB', 'GB', 'TB');
    s = d[0];
    for b in d:
        if size < 1024: return ("%.2f" % size) + ' ' + b;
        size = size / 1024;
        s = b;
    return ("%.2f" % size) + ' ' + b;


# 取通用对象
re_key_match = re.compile(r'^[\w\s\[\]\-]+$')
re_key_match2 = re.compile(r'^\.?__[\w\s[\]\-]+__\.?$')
key_filter_list = ['get', 'set', 'get_items', 'exists', '__contains__', '__setitem__', '__getitem__', '__delitem__',
                   '__delattr__', '__setattr__', '__getattr__', '__class__']


class dict_obj:
    def __contains__(self, key):
        return getattr(self, key, None)

    def __setitem__(self, key, value):
        if key in key_filter_list:
            raise ExcepError("错误的字段名")
        if not re_key_match.match(key) or re_key_match2.match(key):
            raise ExcepError("错误的字段名")
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key, None)

    def __delitem__(self, key):
        delattr(self, key)

    def __delattr__(self, key):
        delattr(self, key)

    def get_items(self):
        return self

    def exists(self, keys):
        return exists_args(keys, self)

    def set(self, key, value):
        if not isinstance(value, str) or not isinstance(key, str): return False
        if key in key_filter_list:
            raise ExcepError("错误的字段名")
        if not re_key_match.match(key) or re_key_match2.match(key):
            raise ExcepError("错误的字段名")
        return setattr(self, key, value)

    def get(self, key, default='', format='', limit=[]):
        '''
            @name 获取指定参数
            @param key<string> 参数名称，允许在/后面限制参数格式，请参考参数值格式(format)
            @param default<string> 默认值，默认空字符串
            @param format<string>  参数值格式(int|str|port|float|json|xss|path|url|ip|ipv4|ipv6|letter|mail|phone|正则表达式|>1|<1|=1)，默认为空
            @param limit<list> 限制参数值内容
            @param return mixed
        '''
        if key.find('/') != -1:
            key, format = key.split('/')
        result = getattr(self, key, default)
        if isinstance(result, str): result = result.strip()
        if format:
            if format in ['str', 'string', 's']:
                result = str(result)
            elif format in ['int', 'd']:
                try:
                    result = int(result)
                except:
                    raise ValueError("参数：{}，要求int类型数据".format(key))
            elif format in ['float', 'f']:
                try:
                    result = float(result)
                except:
                    raise ValueError("参数：{}，要求float类型数据".format(key))
            elif format in ['json', 'j']:
                try:
                    result = json.loads(result)
                except:
                    raise ValueError("参数：{}, 要求JSON字符串".format(key))
            elif format in ['xss', 'x']:
                result = xssencode(result)
            elif format in ['path', 'p']:
                if not path_safe_check(result):
                    raise ValueError("参数：{}，要求正确的路径格式".format(key))
                result = result.replace('//', '/')
            elif format in ['url', 'u']:
                regex = re.compile(
                    r'^(?:http|ftp)s?://'
                    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                    r'localhost|'
                    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                    r'(?::\d+)?'
                    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
                if not re.match(regex, result):
                    raise ValueError('参数：{}，要求正确的URL格式'.format(key))
            elif format in ['ip', 'ipaddr', 'i', 'ipv4', 'ipv6']:
                if format == 'ipv4':
                    if not is_ipv4(result):
                        raise ValueError('参数：{}，要求正确的ipv4地址'.format(key))
                elif format == 'ipv6':
                    if not is_ipv6(result):
                        raise ValueError('参数：{}，要求正确的ipv6地址'.format(key))
                else:
                    if not is_ipv4(result) and not is_ipv6(result):
                        raise ValueError('参数：{}，要求正确的ipv4/ipv6地址'.format(key))
            elif format in ['w', 'letter']:
                if not re.match(r'^\w+$', result):
                    raise ValueError('参数：{}，要求只能是英文字母或数据组成'.format(key))
            elif format in ['email', 'mail', 'm']:
                if not re.match(r"^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$)", result):
                    raise ValueError("参数：{}，要求正确的邮箱地址格式".format(key))
            elif format in ['phone', 'mobile', 'p']:
                if not re.match("^[0-9]{11,11}$", result):
                    raise ValueError("参数：{}，要求手机号码格式".format(key))
            elif format in ['port']:
                result_port = int(result)
                if result_port > 65535 or result_port < 0:
                    raise ValueError("参数：{}，要求端口号为0-65535".format(key))
                result = result_port
            elif re.match(r"^[<>=]\d+$", result):
                operator = format[0]
                length = int(format[1:].strip())
                result_len = len(result)
                error_obj = ValueError("参数：{}，要求长度为{}".format(key, format))
                if operator == '=':
                    if result_len != length:
                        raise error_obj
                elif operator == '>':
                    if result_len < length:
                        raise error_obj
                else:
                    if result_len > length:
                        raise error_obj
            elif format[0] in ['^', '(', '[', '\\', '.'] or format[-1] in ['$', ')', ']', '+', '}']:
                if not re.match(format, result):
                    raise ValueError("指定参数格式不正确, {}:{}".format(key, format))

        if limit:
            if not result in limit:
                raise ValueError("指定参数值范围不正确, {}:{}".format(key, limit))
        return result


def is_64bitos():
    """
    判断是否x64系统(windows)
    """
    bites = {'AMD64': 64, 'x86_64': 64, 'i386': 32, 'x86': 32}
    info = platform.uname()
    if bites.get(info.machine) == 64:
        return True
    return False


def get_registry_value(key, subkey, value):
    """
    读取注册表信息
    @key 注册表类型
    @subkey 注册表路径
    @value 注册表具体key值
    """
    key = getattr(winreg, key)
    handle = winreg.OpenKey(key, subkey)
    (value, type) = winreg.QueryValueEx(handle, value)
    return value


def GetSystemVersion():
    """
    取操作系统版本
    """
    try:
        key = 'lybbn_sys_version'
        version = cache.get(key)
        if version: return version
        bit = 'x86';
        if is_64bitos(): bit = 'x64'

        def get(key):
            return get_registry_value("HKEY_LOCAL_MACHINE", "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", key)

        os = get("ProductName")
        build = get("CurrentBuildNumber")

        version = "%s (build %s) %s (Py%s)" % (os, build, bit, platform.python_version())
        cache.set(key, version, 10000)
        return version
    except Exception as ex:
        version = "未知系统版本."
        cache.set(key, version, 10000)
        return version


# 取负载信息
def GetLoadAverage():
    data = {}
    data['one'] = 0
    data['five'] = 0
    data['fifteen'] = 0
    data['max'] = psutil.cpu_count() * 2
    data['limit'] = data['max']
    data['safe'] = data['max'] * 0.75
    data['percent'] = 0
    return data


# 取内存信息
def GetMemInfo():
    mem = psutil.virtual_memory()
    memInfo = {}
    memInfo['percent'] = mem.percent
    memInfo['total'] = round(float(mem.total) / 1024 / 1024 / 1024, 2)
    memInfo['free'] = round(float(mem.free) / 1024 / 1024 / 1024, 2)
    memInfo['used'] = round(float(mem.used) / 1024 / 1024 / 1024, 2)
    return memInfo


# 获取网卡信息
def GetNetWork():
    cache_timeout = 86400
    otime = cache.get("otime")
    ntime = time.time()
    networkInfo = {}
    networkInfo['network'] = {}
    networkInfo['upTotal'] = 0
    networkInfo['downTotal'] = 0
    networkInfo['up'] = 0
    networkInfo['down'] = 0
    networkInfo['downPackets'] = 0
    networkInfo['upPackets'] = 0
    networkIo_list = psutil.net_io_counters(pernic=True)

    for net_key in networkIo_list.keys():
        if net_key.find('Loopback') >= 0 or net_key.find('Teredo') >= 0 or net_key.find('isatap') >= 0: continue

        networkIo = networkIo_list[net_key][:4]
        up_key = "{}_up".format(net_key)
        down_key = "{}_down".format(net_key)
        otime_key = "otime"

        if not otime:
            otime = time.time()

            cache.set(up_key, networkIo[0], cache_timeout)
            cache.set(down_key, networkIo[1], cache_timeout)
            cache.set(otime_key, otime, cache_timeout)

        networkInfo['network'][net_key] = {}
        up = cache.get(up_key)
        down = cache.get(down_key)
        if not up:
            up = networkIo[0]
        if not down:
            down = networkIo[1]
        networkInfo['network'][net_key]['upTotal'] = networkIo[0]
        networkInfo['network'][net_key]['downTotal'] = networkIo[1]
        try:
            networkInfo['network'][net_key]['up'] = round(float(networkIo[0] - up) / 1024 / (ntime - otime), 2)
            networkInfo['network'][net_key]['down'] = round(float(networkIo[1] - down) / 1024 / (ntime - otime), 2)
        except:
            networkInfo['up'] = 0
            networkInfo['down'] = 0

            networkInfo['network'][net_key]['up'] = 0
            networkInfo['network'][net_key]['down'] = 0

        networkInfo['network'][net_key]['downPackets'] = networkIo[3]
        networkInfo['network'][net_key]['upPackets'] = networkIo[2]

        networkInfo['upTotal'] += networkInfo['network'][net_key]['upTotal']
        networkInfo['downTotal'] += networkInfo['network'][net_key]['downTotal']
        networkInfo['up'] += networkInfo['network'][net_key]['up']
        networkInfo['down'] += networkInfo['network'][net_key]['down']
        networkInfo['downPackets'] += networkInfo['network'][net_key]['downPackets']
        networkInfo['upPackets'] += networkInfo['network'][net_key]['upPackets']

        cache.set(up_key, networkIo[0], cache_timeout)
        cache.set(down_key, networkIo[1], cache_timeout)
        cache.set(otime_key, time.time(), cache_timeout)

    networkInfo['up'] = round(float(networkInfo['up']), 2)
    networkInfo['down'] = round(float(networkInfo['down']), 2)
    networkInfo['iostat'] = {}

    return networkInfo


# 取系统启动时间
def GetBootTime():
    key = 'lybbn_sys_time'
    sys_time = cache.get(key)
    if sys_time: return sys_time
    import math
    tStr = time.time() - psutil.boot_time()
    min = tStr / 60;
    hours = min / 60;
    days = math.floor(hours / 24);
    hours = math.floor(hours - (days * 24));
    min = math.floor(min - (days * 60 * 24) - (hours * 60));
    sys_time = "{}天".format(int(days))
    cache.set(key, sys_time, 1800)
    return sys_time


def getCpuType():
    """
    取CPU类型
    """
    try:
        cpuType = ReadReg(r'HARDWARE\DESCRIPTION\System\CentralProcessor\0', 'ProcessorNameString')
    except:
        cpuType = ''
    return cpuType;


# 取CPU详细信息
def GetCpuInfo(interval=1):
    cpuCount = psutil.cpu_count()
    cpuNum = psutil.cpu_count(logical=False)

    import threading
    p = threading.Thread(target=get_cpu_percent_thead, args=(interval,))
    # p.setDaemon(True)
    p.start()

    used = cache.get('lybbn_cpu_used_all')
    if not used: used = get_cpu_percent_thead(interval)

    used_all = psutil.cpu_percent(percpu=True)

    used_total = 0
    for x in used_all: used_total += x

    ret = ExecShell('wmic cpu get NumberOfCores')[0]
    cpuW = 0

    arrs = ret.strip().split('\r\n')
    for x in arrs:
        val = x.strip()
        if not val: continue;
        try:
            val = int(val)
            cpuW += 1;
        except:
            pass
    try:
        cpu_name = '{} * {}'.format(
            ReadReg(r'HARDWARE\DESCRIPTION\System\CentralProcessor\0', 'ProcessorNameString').strip(), cpuW);
    except:
        cpu_name = ''

    tmp = 0
    if cpuW: tmp = cpuNum / cpuW

    used = 0
    if used_total:  used = round(used_total / cpuCount, 2)
    return used, cpuCount, used_all, cpu_name, tmp, cpuW


def get_cpu_percent_thead(interval):
    used = psutil.cpu_percent(interval)
    cache.set('lybbn_cpu_used_all', used, 10)
    return used


# 取磁盘分区信息
def GetDiskInfo():
    key = 'lybbn_sys_disk'
    diskInfo = cache.get(key)
    if diskInfo: return diskInfo
    try:
        diskIo = psutil.disk_partitions();
    except:
        import string
        diskIo = []
        for c in string.ascii_uppercase:
            disk = c + ':'
            if os.path.isdir(disk):
                data = dict_obj()
                data['mountpoint'] = disk + '/'
                diskIo.append(data)

    diskInfo = []
    for disk in diskIo:
        try:
            tmp = {}
            tmp['path'] = disk.mountpoint.replace("\\", "/")
            usage = psutil.disk_usage(disk.mountpoint)
            tmp['size'] = [to_size(usage.total), to_size(usage.used), to_size(usage.free), usage.percent]
            tmp['inodes'] = False
            diskInfo.append(tmp)
        except:
            pass
    cache.set(key, diskInfo, 10)
    return diskInfo


def GetMsg(key, args=()):
    """
    根据key获取内置消息返回
    @key 指定消息的key
    @args 消息内容中的参数
    """
    try:
        log_message = json.loads(ReadFile(PUBLIC_DICT));
        keys = log_message.keys();
        msg = None;
        if key in keys:
            msg = log_message[key];
            for i in range(len(args)):
                rep = '{' + str(i + 1) + '}'
                msg = msg.replace(rep, args[i]);
        return msg;
    except:
        return key


def getMsg(key, args=()):
    return GetMsg(key, args)


def ReturnMsg(status, msg, args=()):
    """
        @name 取通用dict返回
        @param status  返回状态
        @param msg  返回消息
        @return dict  {"status":bool,"msg":string}
    """
    log_message = json.loads(ReadFile(PUBLIC_DICT));

    keys = log_message.keys();
    if type(msg) == str:
        if msg in keys:
            msg = log_message[msg];
            for i in range(len(args)):
                rep = '{' + str(i + 1) + '}'
                msg = msg.replace(rep, args[i]);
    return {'status': status, 'msg': msg}


def returnMsg(status, msg, args=()):
    return ReturnMsg(status, msg, args)


# 重启系统
def RestartServer():
    try:
        os.system("shutdown /r /f /t 0");
    except:
        pass
    return returnMsg(True, 'SYS_REBOOT');
