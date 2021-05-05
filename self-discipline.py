import os
import datetime as dt
import time

forbidden_hours = {0, 1, 2, 3, 4, 5, 6, 7, 8, 23}
blacklist_hosts = ["www.bilibili.com", "www.zhihu.com"]
host_file = "/etc/hosts"


def check_blacklist_website(blacklist_host):
    forbidden_string = os.popen("cat {} | grep '\<127.0.0.1' | grep {}".format(host_file, blacklist_host)).read()
    if len(forbidden_string) == 0:
        os.system("echo \"127.0.0.1 {}\" >> {}".format(blacklist_host, host_file))


if __name__ == '__main__':
    while True:
        time.sleep(5)
        hour = dt.datetime.now().hour
        if hour in forbidden_hours:
            os.system("pkill Safari")
            for host in blacklist_hosts:
                check_blacklist_website(host)
        else:
            for host in blacklist_hosts:
                os.system("sed -i \"\" \"/127.0.0.1 {}/d\" {}".format(host, host_file))

