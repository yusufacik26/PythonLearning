// lib/services/native_color_detection.dart
import 'package:flutter/services.dart';

class NativeColorDetection {
  static const platform = MethodChannel('com.example/colorDetection');

  Future<String> getColorFromCamera() async {
    try {
      final String color = await platform.invokeMethod('getColor');
      return color;
    } on PlatformException catch (e) {
      return "Failed to get color: '${e.message}'.";
    }
  }
}
