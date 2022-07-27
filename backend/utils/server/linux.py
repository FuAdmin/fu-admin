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
# linux系统命令工具类封装
# ------------------------------
import os, sys, re, time, json
import psutil
from django.core.cache import cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PUBLIC_DICT = os.path.join(BASE_DIR, 'public.json')


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


def get_preexec_fn(run_user):
    '''
        @name 获取指定执行用户预处理函数
        @author hwliang<2021-08-19>
        @param run_user<string> 运行用户
        @return 预处理函数
    '''
    import pwd
    pid = pwd.getpwnam(run_user)
    uid = pid.pw_uid
    gid = pid.pw_gid

    def _exec_rn():
        os.setgid(gid)
        os.setuid(uid)

    return _exec_rn


def get_error_info():
    import traceback
    errorMsg = traceback.format_exc()
    return errorMsg


def ExecShell(cmdstring, timeout=None, shell=True, cwd=None, env=None, user=None):
    '''
        @name 执行命令
        @author hwliang<2021-08-19>
        @param cmdstring 命令 [必传]
        @param timeout 超时时间
        @param shell 是否通过shell运行
        @param cwd 进入的目录
        @param env 环境变量
        @param user 执行用户名
        @return 命令执行结果
    '''
    a = ''
    e = ''
    import subprocess, tempfile
    preexec_fn = None
    tmp_dir = '/dev/shm'
    if user:
        preexec_fn = get_preexec_fn(user)
        tmp_dir = '/tmp'
    try:
        rx = md5(cmdstring)
        succ_f = tempfile.SpooledTemporaryFile(max_size=4096, mode='wb+', suffix='_succ', prefix='btex_' + rx,
                                               dir=tmp_dir)
        err_f = tempfile.SpooledTemporaryFile(max_size=4096, mode='wb+', suffix='_err', prefix='btex_' + rx,
                                              dir=tmp_dir)
        sub = subprocess.Popen(cmdstring, close_fds=True, shell=shell, bufsize=128, stdout=succ_f, stderr=err_f,
                               cwd=cwd, env=env, preexec_fn=preexec_fn)
        if timeout:
            s = 0
            d = 0.01
            while sub.poll() == None:
                time.sleep(d)
                s += d
                if s >= timeout:
                    if not err_f.closed: err_f.close()
                    if not succ_f.closed: succ_f.close()
                    return 'Timed out'
        else:
            sub.wait()

        err_f.seek(0)
        succ_f.seek(0)
        a = succ_f.read()
        e = err_f.read()
        if not err_f.closed: err_f.close()
        if not succ_f.closed: succ_f.close()
    except:
        return '', get_error_info()
    try:
        # 编码修正
        if type(a) == bytes: a = a.decode('utf-8')
        if type(e) == bytes: e = e.decode('utf-8')
    except:
        a = str(a)
        e = str(e)

    return a, e


def ReadFile(filename, mode='r'):
    """
    读取文件内容
    @filename 文件名
    return string(bin) 若文件不存在，则返回None
    """
    import os
    if not os.path.exists(filename): return False
    fp = None
    try:
        fp = open(filename, mode)
        f_body = fp.read()
    except Exception as ex:
        if sys.version_info[0] != 2:
            try:
                fp = open(filename, mode, encoding="utf-8")
                f_body = fp.read()
            except:
                fp = open(filename, mode, encoding="GBK")
                f_body = fp.read()
        else:
            return False
    finally:
        if fp and not fp.closed:
            fp.close()
    return f_body


def readFile(filename, mode='r'):
    '''
        @name 读取指定文件数据
        @author hwliang<2021-06-09>
        @param filename<string> 文件名
        @param mode<string> 文件打开模式，默认r
        @return string or bytes or False 如果返回False则说明读取失败
    '''
    return ReadFile(filename, mode)


# xss 防御
def xsssec(text):
    return text.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')


def get_os_version():
    '''
        @name 取操作系统版本
        @author hwliang<2021-08-07>
        @return string
    '''
    p_file = '/etc/.productinfo'
    if os.path.exists(p_file):
        s_tmp = readFile(p_file).split("\n")
        if s_tmp[0].find('Kylin') != -1 and len(s_tmp) > 1:
            version = s_tmp[0] + ' ' + s_tmp[1].split('/')[0].strip()
    else:
        version = readFile('/etc/redhat-release')
    if not version:
        version = readFile('/etc/issue').strip().split("\n")[0].replace('\\n', '').replace('\l', '').strip()
    else:
        version = version.replace('release ', '').replace('Linux', '').replace('(Core)', '').strip()
    v_info = sys.version_info
    try:
        version = "{} {}(Py{}.{}.{})".format(version, os.uname().machine, v_info.major, v_info.minor, v_info.micro)
    except:
        version = "{} (Py{}.{}.{})".format(version, v_info.major, v_info.minor, v_info.micro)
    return xsssec(version)


def GetSystemVersion():
    # 取操作系统版本
    key = 'lybbn_sys_version'
    version = cache.get(key)
    if version: return version
    version = get_os_version()
    cache.set(key, version, 10000)
    return version


def GetLoadAverage():
    try:
        c = os.getloadavg()
    except:
        c = [0, 0, 0]
    data = {}
    data['one'] = float(c[0])
    data['five'] = float(c[1])
    data['fifteen'] = float(c[2])
    data['max'] = psutil.cpu_count() * 2
    data['limit'] = data['max']
    data['safe'] = data['max'] * 0.75
    temppercent = round(data['one'] / data['max'] * 100)
    data['percent'] = 100 if temppercent > 100 else temppercent
    return data


# 取内存信息
def GetMemInfo():
    mem = psutil.virtual_memory()
    memInfo = {}
    # memInfo['percent'] = mem.percent
    memInfo2 = {'memTotal': int(mem.total / 1024 / 1024), 'memFree': int(mem.free / 1024 / 1024),
                'memBuffers': int(mem.buffers / 1024 / 1024), 'memCached': int(mem.cached / 1024 / 1024)}
    memInfo['total'] = round(float(mem.total) / 1024 / 1024 / 1024, 2)
    memInfo['free'] = round((memInfo2['memFree'] + memInfo2['memBuffers'] + memInfo2['memCached']) / 1024, 2)
    memInfo['used'] = round(float(mem.used) / 1024 / 1024 / 1024, 2)
    memInfo['percent'] = round((int(mem.used) / 1024 / 1024) / memInfo2['memTotal'] * 100, 1)
    # memInfo['realUsed'] = round((memInfo2['memTotal'] - memInfo2['memFree'] - memInfo2['memBuffers'] - memInfo2['memCached']) / 1024,2)  # memRealUsed
    return memInfo


# 获取磁盘IO开销数据
def get_disk_iostat():
    iokey = 'iostat'
    diskio = cache.get(iokey)
    mtime = int(time.time())
    if not diskio:
        diskio = {}
        diskio['info'] = None
        diskio['time'] = mtime
    diskio_1 = diskio['info']
    stime = mtime - diskio['time']
    if not stime: stime = 1
    diskInfo = {}
    diskInfo['ALL'] = {}
    diskInfo['ALL']['read_count'] = 0
    diskInfo['ALL']['write_count'] = 0
    diskInfo['ALL']['read_bytes'] = 0
    diskInfo['ALL']['write_bytes'] = 0
    diskInfo['ALL']['read_time'] = 0
    diskInfo['ALL']['write_time'] = 0
    diskInfo['ALL']['read_merged_count'] = 0
    diskInfo['ALL']['write_merged_count'] = 0
    try:
        if os.path.exists('/proc/diskstats'):
            diskio_2 = psutil.disk_io_counters(perdisk=True)
            if not diskio_1:
                diskio_1 = diskio_2
            for disk_name in diskio_2.keys():
                diskInfo[disk_name] = {}
                diskInfo[disk_name]['read_count'] = int(
                    (diskio_2[disk_name].read_count - diskio_1[disk_name].read_count) / stime)
                diskInfo[disk_name]['write_count'] = int(
                    (diskio_2[disk_name].write_count - diskio_1[disk_name].write_count) / stime)
                diskInfo[disk_name]['read_bytes'] = int(
                    (diskio_2[disk_name].read_bytes - diskio_1[disk_name].read_bytes) / stime)
                diskInfo[disk_name]['write_bytes'] = int(
                    (diskio_2[disk_name].write_bytes - diskio_1[disk_name].write_bytes) / stime)
                diskInfo[disk_name]['read_time'] = int(
                    (diskio_2[disk_name].read_time - diskio_1[disk_name].read_time) / stime)
                diskInfo[disk_name]['write_time'] = int(
                    (diskio_2[disk_name].write_time - diskio_1[disk_name].write_time) / stime)
                diskInfo[disk_name]['read_merged_count'] = int(
                    (diskio_2[disk_name].read_merged_count - diskio_1[disk_name].read_merged_count) / stime)
                diskInfo[disk_name]['write_merged_count'] = int(
                    (diskio_2[disk_name].write_merged_count - diskio_1[disk_name].write_merged_count) / stime)

                diskInfo['ALL']['read_count'] += diskInfo[disk_name]['read_count']
                diskInfo['ALL']['write_count'] += diskInfo[disk_name]['write_count']
                diskInfo['ALL']['read_bytes'] += diskInfo[disk_name]['read_bytes']
                diskInfo['ALL']['write_bytes'] += diskInfo[disk_name]['write_bytes']
                if diskInfo['ALL']['read_time'] < diskInfo[disk_name]['read_time']:
                    diskInfo['ALL']['read_time'] = diskInfo[disk_name]['read_time']
                if diskInfo['ALL']['write_time'] < diskInfo[disk_name]['write_time']:
                    diskInfo['ALL']['write_time'] = diskInfo[disk_name]['write_time']
                diskInfo['ALL']['read_merged_count'] += diskInfo[disk_name]['read_merged_count']
                diskInfo['ALL']['write_merged_count'] += diskInfo[disk_name]['write_merged_count']

            cache.set(iokey, {'info': diskio_2, 'time': mtime})
    except:
        return diskInfo
    return diskInfo


# 获取网卡数据
def GetNetWork():
    cache_timeout = 86400
    otime = cache.get("lybbn_otime")
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
        networkIo = networkIo_list[net_key][:4]
        up_key = "{}_up".format(net_key)
        down_key = "{}_down".format(net_key)
        otime_key = "lybbn_otime"

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
        networkInfo['network'][net_key]['up'] = round(float(networkIo[0] - up) / 1024 / (ntime - otime), 2)
        networkInfo['network'][net_key]['down'] = round(float(networkIo[1] - down) / 1024 / (ntime - otime), 2)
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
    networkInfo['iostat'] = get_disk_iostat()

    return networkInfo


# 取系统启动时间
def GetBootTime():
    key = 'lybbn_sys_time'
    sys_time = cache.get(key)
    if sys_time: return sys_time
    import math
    conf = readFile('/proc/uptime').split()
    tStr = float(conf[0])
    min = tStr / 60
    hours = min / 60
    days = math.floor(hours / 24)
    hours = math.floor(hours - (days * 24))
    min = math.floor(min - (days * 60 * 24) - (hours * 60))
    sys_time = "{}天".format(int(days))
    cache.set(key, sys_time, 1800)
    return sys_time


# 取CPU类型
def getCpuType():
    cpuinfo = open('/proc/cpuinfo', 'r').read()
    rep = "model\s+name\s+:\s+(.+)"
    tmp = re.search(rep, cpuinfo, re.I)
    cpuType = ''
    if tmp:
        cpuType = tmp.groups()[0]
    else:
        cpuinfo = ExecShell('LANG="en_US.UTF-8" && lscpu')[0]
        rep = "Model\s+name:\s+(.+)"
        tmp = re.search(rep, cpuinfo, re.I)
        if tmp: cpuType = tmp.groups()[0]
    return cpuType


# 取CPU信息
def GetCpuInfo(interval=1):
    # 取CPU信息
    cpuCount = psutil.cpu_count()
    cpuNum = psutil.cpu_count(logical=False)
    c_tmp = readFile('/proc/cpuinfo')
    d_tmp = re.findall("physical id.+", c_tmp)
    cpuW = len(set(d_tmp))
    import threading
    p = threading.Thread(target=get_cpu_percent_thead, args=(interval,))
    # p.setDaemon(True)
    p.start()

    used = cache.get('lybbn_cpu_used_all')
    if not used: used = get_cpu_percent_thead(interval)

    used_all = psutil.cpu_percent(percpu=True)
    cpu_name = getCpuType() + " * {}".format(cpuW)

    return used, cpuCount, used_all, cpu_name, cpuNum, cpuW


def get_cpu_percent_thead(interval):
    used = psutil.cpu_percent(interval)
    cache.set('lybbn_cpu_used_all', used, 10)
    return used


def get_cpu_time():
    cpu_time = 0.00
    cpu_times = psutil.cpu_times()
    for s in cpu_times: cpu_time += s
    return cpu_time


def GetDiskInfo(human=True):
    # 取磁盘分区信息
    key = 'lybbn_sys_disk'
    diskInfo = cache.get(key)
    if diskInfo: return diskInfo
    if human:
        temp = ExecShell("df -hT -P|grep '/'|grep -v tmpfs|grep -v 'snap/core'|grep -v udev")[0]
    else:
        temp = ExecShell("df -T -P|grep '/'|grep -v tmpfs|grep -v 'snap/core'|grep -v udev")[0]
    tempInodes = ExecShell("df -i -P|grep '/'|grep -v tmpfs|grep -v 'snap/core'|grep -v udev")[0]
    temp1 = temp.split('\n')
    tempInodes1 = tempInodes.split('\n')
    diskInfo = []
    n = 0
    cuts = ['/mnt/cdrom', '/boot', '/boot/efi', '/dev', '/dev/shm', '/run/lock', '/run', '/run/shm', '/run/user']
    for tmp in temp1:
        n += 1
        try:
            inodes = tempInodes1[n - 1].split()
            disk = re.findall(
                r"^(.+)\s+([\w\.]+)\s+([\w\.]+)\s+([\w\.]+)\s+([\w\.]+)\s+([\d%]{2,4})\s+(/.{0,100})$", tmp.strip())
            if disk: disk = disk[0]
            if len(disk) < 6: continue
            if disk[2].find('M') != -1: continue
            if disk[2].find('K') != -1: continue
            if len(disk[6].split('/')) > 10: continue
            if disk[6] in cuts: continue
            if disk[6].find('docker') != -1: continue
            if disk[1].strip() in ['tmpfs']: continue
            arr = {}
            arr['filesystem'] = disk[0].strip()
            arr['type'] = disk[1].strip()
            arr['path'] = disk[6].replace('/usr/local/lighthouse/softwares/btpanel', '/www')
            tmp1 = [disk[2], disk[3], disk[4], disk[5].split('%')[0]]
            arr['size'] = tmp1
            arr['inodes'] = [inodes[1], inodes[2], inodes[3], inodes[4]]
            diskInfo.append(arr)
        except Exception as ex:
            continue
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
        @author hwliang<hwl@bt.cn>
        @param status  返回状态
        @param msg  返回消息
        @return dict  {"status":bool,"msg":string}
    """
    log_message = json.loads(ReadFile(PUBLIC_DICT))
    keys = log_message.keys()
    if type(msg) == str:
        if msg in keys:
            msg = log_message[msg]
            for i in range(len(args)):
                rep = '{' + str(i + 1) + '}'
                msg = msg.replace(rep, args[i])
    return {'status': status, 'msg': msg}


def returnMsg(status, msg, args=()):
    """
        @name 取通用dict返回
        @author hwliang<hwl@bt.cn>
        @param status  返回状态
        @param msg  返回消息
        @return dict  {"status":bool,"msg":string}
    """
    return ReturnMsg(status, msg, args)


def RestartServer():
    ExecShell("sync && init 6 &")
    return returnMsg(True, 'SYS_REBOOT')
