// lib/main.dart
import 'package:flutter/material.dart';
import 'services/native_color_detection.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Renk Algılama',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ColorDetectionScreen(),
    );
  }
}

class ColorDetectionScreen extends StatefulWidget {
  @override
  _ColorDetectionScreenState createState() => _ColorDetectionScreenState();
}

class _ColorDetectionScreenState extends State<ColorDetectionScreen> {
  String _detectedColor = "Bilinmiyor";
  final NativeColorDetection _colorDetection = NativeColorDetection();

  Future<void> _getColorFromCamera() async {
    String color = await _colorDetection.getColorFromCamera();
    setState(() {
      _detectedColor = color;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Renk Algılama"),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(
                "Algılanan Renk: $_detectedColor",
                style: TextStyle(fontSize: 24),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _getColorFromCamera,
                child: Text("Rengi Algıla"),
              ),
            ],
          ),
        ));
  }
}
