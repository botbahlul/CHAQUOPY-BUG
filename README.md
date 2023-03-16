# CHAQUOPY-BUG

JUST AN EXAMPLE OF A BUG IN CHAQUOPY WHEN WE CALL dynamic_proxy(Runnable) CLASS REPEATLY IN A LOOP

    --------- beginning of crash
E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.android.chaquopybug, PID: 18871
    com.chaquo.python.PyException: NotImplementedError: com.chaquo.python.PyProxy._chaquopyGetDict is abstract and cannot be called
        at <python>.java.chaquopy.JavaMethod.__call__(class.pxi:781)
        at <python>.java.chaquopy.JavaMethod.__get__.lambda2(class.pxi:775)
        at <python>.java.chaquopy.set_this(class.pxi:341)
        at <python>.java.chaquopy.set_this(class.pxi:334)
        at <python>.java.chaquopy.JavaClass.__call__(class.pxi:133)
        at <python>.java.chaquopy.JavaClass.__call__(class.pxi:111)
        at <python>.java.chaquopy.DynamicProxyClass.__call__(proxy.pxi:58)
        at <python>.java.chaquopy.j2p(conversion.pxi:94)
        at <python>.chaquopy_java.Java_com_chaquo_python_PyObject_fromJavaNative(chaquopy_java.pyx:176)
        at com.chaquo.python.PyObject.fromJavaNative(Native Method)
        at com.chaquo.python.PyObject.fromJava(PyObject.java:87)
        at com.chaquo.python.PyInvocationHandler.invoke(PyInvocationHandler.java:27)
        at java.lang.reflect.Proxy.invoke(Proxy.java:1006)
        at $Proxy1.run(Unknown Source)
        at android.os.Handler.handleCallback(Handler.java:938)
        at android.os.Handler.dispatchMessage(Handler.java:99)
        at android.os.Looper.loop(Looper.java:223)
        at android.app.ActivityThread.main(ActivityThread.java:7656)
        at java.lang.reflect.Method.invoke(Native Method)
        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:592)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:947)
I/Process: Sending signal. PID: 18871 SIG: 9

Temporary solution to updating a textview without using any 'barriers' is by using static_proxy
```
class S(static_proxy(None, Runnable)):
    def __init__(self, textview_debug, strings):
        super(S, self).__init__()
        self.textview_debug = textview_debug
        self.strings = strings

    @Override(jvoid, [])
    def run(self):
        self.textview_debug.setText(self.strings)
```

and then call it with : 

```
activity.runOnUiThread(S(textview_debug, strings))
```
