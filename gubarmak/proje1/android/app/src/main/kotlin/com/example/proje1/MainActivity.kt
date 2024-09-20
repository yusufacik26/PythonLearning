// android/app/src/main/kotlin/com/example/your_project/MainActivity.kt
package com.example.your_project

import android.os.Bundle
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import org.opencv.android.BaseLoaderCallback
import org.opencv.android.LoaderCallbackInterface
import org.opencv.android.OpenCVLoader
import org.opencv.core.Core
import org.opencv.core.Mat
import org.opencv.imgproc.Imgproc

class MainActivity: FlutterActivity() {
    private val CHANNEL = "com.example/colorDetection"

    private val mLoaderCallback: BaseLoaderCallback = object : BaseLoaderCallback(this) {
        override fun onManagerConnected(status: Int) {
            when (status) {
                LoaderCallbackInterface.SUCCESS -> {
                    // OpenCV başarıyla yüklendi
                }
                else -> {
                    super.onManagerConnected(status)
                }
            }
        }
    }

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler { call, result ->
            if (call.method == "getColor") {
                val color = detectColor()
                if (color != null) {
                    result.success(color)
                } else {
                    result.error("UNAVAILABLE", "Color detection failed.", null)
                }
            } else {
                result.notImplemented()
            }
        }
    }

    override fun onResume() {
        super.onResume()
        if (!OpenCVLoader.initDebug()) {
            OpenCVLoader.initAsync(OpenCVLoader.OPENCV_VERSION, this, mLoaderCallback)
        } else {
            mLoaderCallback.onManagerConnected(LoaderCallbackInterface.SUCCESS)
        }
    }

    private fun detectColor(): String? {
        // Buraya OpenCV ile renk algılama kodunuzu ekleyin
        // Örneğin, kamera görüntüsünü alıp renk tespiti yapabilirsiniz
        // Basit bir örnek olarak sabit bir renk döndürüyoruz
        return "Red"
    }
}
