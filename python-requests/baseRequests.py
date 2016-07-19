import threading, requests, time, sys

connect_url = sys.argv[1]
requestRate = int(sys.argv[2])
request_stats = []
request_times = []

def client_notify(msg):
  return time.time(), threading.current_thread().name, msg


def generate_req(reqSession):
  start_time = time.time()
  response = reqSession.get(connect_url)
  end_time = time.time()
  elapsed = end_time - start_time
  request_times.append(elapsed)
  if response.status_code == 200:
    client_notify('Success')
    request_stats.append('Success')
  else:
    client_notify('Fail')
    request_stats.append('Fail')


def main():
  for i in range(requestRate):
    # if i % 40 == 0:
    #     time.sleep(1)
    s1 = requests.session()
    th = threading.Thread(
      target=generate_req, args=(s1,),
      name='thread-{:03d}'.format(i),
    )
    th.start()

  for th in threading.enumerate():
    if th != threading.current_thread():
      th.join()

  total_time = 0
  for each_time in request_times:
     total_time += each_time

  fail_counter = 0
  for stats in request_stats:
    if stats == 'Fail':
      fail_counter += 1

  print("total requests:{}\nfail requests:{}\ntotal time:{}\naverage time:{}".format(
    len(request_stats),
    fail_counter,
    total_time,
    total_time / requestRate,
  ))


if __name__=='__main__':
  main()
