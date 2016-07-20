import sys
import json
import commands
import fuzzy


HOT_RECONFIG_CMD = "sudo haproxy -f /etc/haproxy/haproxy.cfg -p /var/run/haproxy.pid -sf $(cat /var/run/haproxy.pid)"
IP_REGEX = " | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}:[0-9]\{1,5\}'"


def read_input_json():
    content = str()
    with open("/home/ubuntu/data.json", "r") as f:
        content += f.read()
    return json.loads(content)


def get_cfg_ip(ip):
    cfg_ip = ip
    get_cfg_line = commands.getoutput("cat /etc/haproxy/haproxy.cfg | grep " + ip)
    if get_cfg_line.find(':') > 0:
        cfg_ip = commands.getoutput("cat /etc/haproxy/haproxy.cfg | grep " + ip + IP_REGEX)
    return cfg_ip


def change_config(input_data):
    for key, value in input_data.iteritems():
        element1 = int(round(value[0][0]))
        element2 = int(round(value[0][1]))
        weight = fuzzy.fuzzy_algorithm(element1, element2, 'element-1.csv', 'element-2.csv')
        print element1, element2, weight
        if value[0][2].find(':') >= 0:
            get_cfg_line = commands.getoutput("cat /etc/haproxy/haproxy.cfg | grep " + value[0][2])
            pre_weight = int(get_cfg_line.split("weight")[1].split("maxconn")[0])
            if pre_weight != weight:
                changed = get_cfg_line.split("weight")[0] + 'weight ' + str(weight) + ' maxconn -1'
                replace_command = "sudo sed -i 's/" + get_cfg_line + "/" + changed + "/g'" + " /etc/haproxy/haproxy.cfg"
                commands.getoutput(replace_command)
                # print replace_command
    commands.getoutput(HOT_RECONFIG_CMD)


def main():
    input_data = dict()
    for key, value in read_input_json().iteritems():
        if sys.argv[1] == 'host':
            if key not in input_data:
                input_data[key] = []
            input_data[key].append([value['system_status']['cpu_used'],
                                    value['system_status']['mem_free'],
                                    get_cfg_ip(value['ip_addr'])])
        elif sys.argv[1] == 'docker':
            for docker_id, docker_status in value['container_status'].iteritems():
                if docker_status['ports'] != '':
                    docker_ipaddr = get_cfg_ip(value['ip_addr'])
                else:
                    docker_ipaddr = value['ip_addr']
                if docker_id not in input_data:
                    input_data[docker_id] = []
                input_data[docker_id].append([docker_status['cpu_used'],
                                              docker_status['mem_free'],
                                              docker_ipaddr])
    # print("{}".format(json.dumps(input_data, indent=4, sort_keys=True)))
    if bool(input_data):
        change_config(input_data)


if __name__ == '__main__':
    main()
