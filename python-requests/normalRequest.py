import threading, requests, time, sys, commands, os, random

connect_url = sys.argv[1]
requestRate = int(sys.argv[2])
request_stats = []
request_times = []
request_count = dict()

def client_notify(msg):
    return time.time(), threading.current_thread().name, msg


def generate_req(reqSession):
    start_time = time.time()
    response = reqSession.get(connect_url)
    end_time = time.time()
    elapsed = end_time - start_time
    request_times.append(elapsed)
    if response.text.split('<br/>')[0] not in request_count:
        request_count[response.text.split('<br/>')[0]] = []
    request_count[response.text.split('<br/>')[0]].append(elapsed)
    if response.status_code == 200:
        client_notify('Success')
        request_stats.append('Success')
    else:
        client_notify('Fail')
        request_stats.append('Fail')


def random_propability(propabilitys, values):
    index = random.randint(1, 100)
    output = 0.1
    if index <= propabilitys[0]:
        output = random.uniform(values[0], values[1])
    elif index <= (propabilitys[0] + propabilitys[1]):
        output = random.uniform(values[1], values[2])
    else:
        output = random.uniform(values[2], values[3])
    # print output
    return output


def main():
    start_time = time.time()
    delay_time = 0;
    rq_num = int(random_propability([70, 20, 10], [10, 30, 70, 100]))
    # print '1 -> ', rq_num
    print "Progress..."
    for i in range(requestRate):
        s1 = requests.session()
        th = threading.Thread(
            target=generate_req, args=(s1,),
            name='thread-{:03d}'.format(i),
        )
        th.start()
        # progress
        if (i+1) >= 100 and ((i+1) % 100 == 0):
            print("Completed {} requests".format(
                i+1,
            ))

        # delay
        if i == rq_num:
            delay = random_propability([80, 15, 5], [0, 2, 5, 10])
            # print 'delay -> ', delay
            rq_num = rq_num + int(random_propability([70, 20, 10], [10, 30, 70, 100]))
            # print '2 -> ', rq_num
            time.sleep(delay)

    for th in threading.enumerate():
        if th != threading.current_thread():
            th.join()

    # total time
    end_time = time.time()
    elapsed = end_time - start_time
    print '\ntask total time : ', elapsed


    for key, value in request_count.iteritems():
        each_total_time = 0
        for key_value in value:
            each_total_time += key_value
        print("{} -> {} , {} , {}".format(
            key,
            len(value),
            each_total_time,
            each_total_time / len(value),
        ))

    total_time = 0
    for each_time in request_times:
        total_time += each_time

    fail_counter = 0
    for stats in request_stats:
        if stats == 'Fail':
            fail_counter += 1

    print("total requests : {}\nfail requests : {}\ntotal time : {}\naverage time : {}".format(
        len(request_stats),
        fail_counter,
        total_time,
        total_time / requestRate,
    ))


if __name__=='__main__':
    main()
