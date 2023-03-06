package com.android.chaquopybug;

import android.os.Bundle;
import android.os.Looper;
import android.util.Log;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import java.util.Objects;

public class MainActivity extends AppCompatActivity {
    Button button_start;
    TextView textview_output_messages;
    Python py;
    Thread thread;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        button_start = findViewById(R.id.button_start);
        textview_output_messages = findViewById(R.id.textview_output_messages);

        button_start.setOnClickListener(view -> {
            textview_output_messages.setText("");
            showProgressBar();
        });

    }

    private void showProgressBar() {
        thread = null;
        thread = new Thread(() -> {
            if (Looper.myLooper() == null) {
                Looper.prepare();
            }

            try {
                if (!Python.isStarted()) {
                    Python.start(new AndroidPlatform(MainActivity.this));
                    py = Python.getInstance();
                }

                // CALLING PYTHON SCRIPT test.py
                PyObject pyObjProgressBar = py.getModule("test").callAttr(
                        "show_progress_bar",
                        MainActivity.this, textview_output_messages);

            }
            catch (Exception e) {
                Log.e("Exception: ", Objects.requireNonNull(e.getMessage()));
                e.printStackTrace();
            }
        });
        thread.start();
    }


}
