import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final cameras = await availableCameras();
  runApp(MyApp(cameras: cameras));
}

class MyApp extends StatelessWidget {
  final List<CameraDescription> cameras;
  const MyApp({Key? key, required this.cameras}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Live Color Detection',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: CameraScreen(cameras: cameras),
    );
  }
}

class CameraScreen extends StatefulWidget {
  final List<CameraDescription> cameras;
  const CameraScreen({Key? key, required this.cameras}) : super(key: key);

  @override
  State<CameraScreen> createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;
  String detectedColor = "Renk Bekleniyor...";

  @override
  void initState() {
    super.initState();
    _controller = CameraController(
      widget.cameras[0],
      ResolutionPreset.medium,
    );
    _initializeControllerFuture = _controller.initialize();
    _startColorDetection();
  }

  Future<void> _startColorDetection() async {
    // Periyodik olarak renk tespiti isteği gönder
    Timer.periodic(Duration(seconds: 2), (timer) async {
      await _detectColor();
    });
  }

  Future<void> _detectColor() async {
    try {
      // Güncellenmiş IP adresi ve port
      final response =
          await http.get(Uri.parse('http://10.0.2.2:5001/detect-color'));

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        setState(() {
          final color = data['detected_color'];
          detectedColor =
              "R: ${color['red']}, G: ${color['green']}, B: ${color['blue']}";
        });
      } else {
        setState(() {
          detectedColor = "Renk tespiti başarısız";
        });
      }
    } catch (e) {
      setState(() {
        detectedColor = "Bağlantı hatası";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Canlı Renk Tespiti'),
      ),
      body: FutureBuilder<void>(
        future: _initializeControllerFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return Stack(
              children: [
                CameraPreview(_controller),
                // Kare çizmek için CustomPaint ekliyoruz
                CustomPaint(
                  size: Size.infinite,
                  painter: SquarePainter(),
                ),
                Positioned(
                  bottom: 20,
                  left: 20,
                  child: Container(
                    padding: EdgeInsets.all(10),
                    color: Colors.white.withOpacity(0.8),
                    child: Text(
                      detectedColor,
                      style: TextStyle(fontSize: 20, color: Colors.black),
                    ),
                  ),
                ),
              ],
            );
          } else {
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
    );
  }
}

class SquarePainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.red
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke;

    // Ekranın ortasında bir kare oluştur
    final rect = Rect.fromCenter(
      center: Offset(size.width / 2, size.height / 2),
      width: 100, // Kare genişliği
      height: 100, // Kare yüksekliği
    );

    // Kareyi çiz
    canvas.drawRect(rect, paint);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) {
    return false;
  }
}
