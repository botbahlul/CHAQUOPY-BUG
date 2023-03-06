import time
from com.chaquo.python import Python
from java import dynamic_proxy
from java.lang import Runnable


def show_progress_bar(activity, textview_debug):
    for i in range(100):
        not_working_progressBar(i, 100, "Test : ", activity, textview_debug)
    not_working_progressBar(100, 100, "Test : ", activity, textview_debug)


#THIS FUNCTION GOT ERROR com.chaquo.python.PyException: NotImplementedError: com.chaquo.python.PyProxy._chaquopyGetDict is abstract and cannot be called
def not_working_progressBar(count_value, total, prefix, activity, textview_debug):
    bar_length = 10
    filled_up_Length = int(round(bar_length*count_value/(total)))
    percentage = round(100.0 * count_value/(total),1)
    bar = '█' * filled_up_Length + '-' * (bar_length - filled_up_Length)

    class R(dynamic_proxy(Runnable)):
        def run(self):
            textview_debug.setText('%s|%10s|%3s%s\r' %(prefix, bar, int(percentage), '%'))
    activity.runOnUiThread(R())



# THIS FUNCTION IS WORKING
def working_progressBar(count_value, total, prefix, activity, textview_debug):
    bar_length = 10
    filled_up_Length = int(round(bar_length*count_value/(total)))
    percentage = round(100.0 * count_value/(total),1)
    bar = '█' * filled_up_Length + '-' * (bar_length - filled_up_Length)

    if (int(percentage) % 10 == 0): # 'BARRIER' TO SLOWING DOWN THE CALL
        time.sleep(1) # 'BARRIER' TO SLOWING DOWN THE CALL
        class R(dynamic_proxy(Runnable)):
            def run(self):
                textview_debug.setText('%s|%10s|%3s%s\r' %(prefix, bar, int(percentage), '%'))
        activity.runOnUiThread(R())
