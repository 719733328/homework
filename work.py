# -*- coding: utf-8 -*-
import  threading
import queue
import schedule
import time
work_queue = queue.Queue(10)



def job():
    if not work_queue.empty():
        sql_update = """
            UPDATE works SET status = '1' WHERE status='0' && id = '%s'
        """
        w = work_queue.get(block=False)
        if w:

            print("执行 %s" % (str(w), ))
            cur.execute(sql_update % (w,))
            db.commit()

            time.sleep(10)
            sql_update = """
                UPDATE works SET status = '2' WHERE status = '1' && id = '%s'
            """
            cur.execute(sql_update % (w, ))
            db.commit()
            work_queue.task_done()
        # work_queue.task_done()


def add_job(work):
    print("add job")
    print(work)
    work_queue.put(str(work))
    print(work_queue.qsize())


def work_threading():
    while True:
        print("正在运行")
        schedule.run_pending()
        time.sleep(1)


def init_works(cur):
    sql = """select id,status,title from works where status='0' or  status='1' """
    cur.execute(sql)
    results = cur.fetchall()
    for x in results:
        add_job(x[0])

    schedule.every(5).seconds.do(job)
    worker_thread = threading.Thread(target=work_threading)
    worker_thread.start()



