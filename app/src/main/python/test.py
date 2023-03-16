import time
from java import dynamic_proxy
from java.lang import Runnable

from java import static_proxy, jvoid, Override, method
from androidx.appcompat.app import AppCompatActivity
from androidx.appcompat.widget import AppCompatTextView
from android.os import Bundle
from android.app import Activity
from com.android.chaquopybug import R

def show_progress_bar(activity, textview_debug):
    for i in range(100):
        static_proxy_progressBar(i, 100, "Test : ", activity, textview_debug)
    static_proxy_progressBar(100, 100, "Test : ", activity, textview_debug)


#THIS FUNCTION GOT ERROR com.chaquo.python.PyException: NotImplementedError: com.chaquo.python.PyProxy._chaquopyGetDict is abstract and cannot be called
def not_working_progressBar(count_value, total, prefix, activity, textview_debug):
    bar_length = 10
    filled_up_Length = int(round(bar_length*count_value/(total)))
    percentage = round(100.0 * count_value/(total),1)
    bar = '█' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    strings = ('%s|%10s|%3s%s\r' %(prefix, bar, int(percentage), '%'))

    class R(dynamic_proxy(Runnable)):
        @Override(jvoid, [])
        def run(self):
            textview_debug.setText(strings)
    activity.runOnUiThread(R())


# THIS FUNCTION IS WORKING BUT WE HAVE TO USE 'BARRIERS' TO SLOWING DOWN THE CALL TO class R()
def working_progressBar(count_value, total, prefix, activity, textview_debug):
    bar_length = 10
    filled_up_Length = int(round(bar_length*count_value/(total)))
    percentage = round(100.0 * count_value/(total),1)
    bar = '█' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    strings = ('%s|%10s|%3s%s\r' %(prefix, bar, int(percentage), '%'))

    if (int(percentage) % 10 == 0): # 'BARRIER' TO SLOWING DOWN THE CALL
        time.sleep(1) # 'BARRIER' TO SLOWING DOWN THE CALL
        class R(dynamic_proxy(Runnable)):
            def run(self):
                textview_debug.setText(strings)
        activity.runOnUiThread(R())


# THIS IS THE BEST SOLUTION TO UPDATE THE TEXTVIEW WITHOUT USING ANY BARRIERS
# BUT REMEMBER TO CHANGE build.gradle ON app FOLDER AS DESCRIBED AT
# https://chaquo.com/chaquopy/doc/current/python.html#static-proxy
def static_proxy_progressBar(count_value, total, prefix, activity, textview_debug):
    bar_length = 10
    filled_up_Length = int(round(bar_length*count_value/(total)))
    percentage = round(100.0 * count_value/(total),1)
    bar = '█' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    strings = ('%s|%10s|%3s%s\r' %(prefix, bar, int(percentage), '%'))
    activity.runOnUiThread(S(textview_debug, strings))


class S(static_proxy(None, Runnable)):
    def __init__(self, textview_debug, strings):
        super(S, self).__init__()
        self.textview_debug = textview_debug
        self.strings = strings

    @Override(jvoid, [])
    def run(self):
        self.textview_debug.setText(self.strings)

