import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'dart:typed_data';
import 'package:image/image.dart' as img;

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
      title: 'Renk Tespiti',
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
  String detectedColorName = "Renk Bekleniyor...";
  bool isDetecting = false;

  @override
  void initState() {
    super.initState();
    _controller = CameraController(
      widget.cameras[0],
      ResolutionPreset.medium,
      enableAudio: false,
    );
    _initializeControllerFuture = _controller.initialize().then((_) {
      // Renk tespiti başlasın
      _startColorDetection();
    });
  }

  void _startColorDetection() {
    _controller.startImageStream((CameraImage image) {
      if (!isDetecting) {
        isDetecting = true;
        // Kameradan alınan görüntüyü işleyelim
        _detectColor(image);
      }
    });
  }

  void _detectColor(CameraImage image) async {
    try {
      // RGB formatına çeviriyoruz
      final img.Image convertedImage = _convertCameraImage(image);

      final List<int> color = _detectColorInCenter(convertedImage);
      final String colorName =
          _getColorNameFromRGB(color[0], color[1], color[2]);

      setState(() {
        detectedColorName = colorName;
      });

      isDetecting = false; // Sonraki kareyi işlemek için hazır
    } catch (e) {
      setState(() {
        detectedColorName = "Renk tespiti hatası";
      });
      isDetecting = false;
    }
  }

  img.Image _convertCameraImage(CameraImage image) {
    // Uçuşta kameradan gelen YUV formatını RGB formatına çeviriyoruz
    final int width = image.width;
    final int height = image.height;

    var imgBytes = Uint8List(width * height * 3); // RGB için
    int bufferIndex = 0;

    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        final int uvIndex = (y >> 1) * (width >> 1) + (x >> 1);
        final int yValue = image.planes[0].bytes[y * width + x];
        final int uValue = image.planes[1].bytes[uvIndex] - 128;
        final int vValue = image.planes[2].bytes[uvIndex] - 128;

        // YUV -> RGB çevirme formülü
        int r = (yValue + 1.370705 * vValue).clamp(0, 255).toInt();
        int g = (yValue - 0.337633 * uValue - 0.698001 * vValue)
            .clamp(0, 255)
            .toInt();
        int b = (yValue + 1.732446 * uValue).clamp(0, 255).toInt();

        imgBytes[bufferIndex++] = r;
        imgBytes[bufferIndex++] = g;
        imgBytes[bufferIndex++] = b;
      }
    }

    return img.Image.fromBytes(width, height, imgBytes);
  }

  List<int> _detectColorInCenter(img.Image image) {
    final int centerX = image.width ~/ 2;
    final int centerY = image.height ~/ 2;
    final int squareSize = 100;
    final List<int> pixelColors = [];

    for (int y = centerY - squareSize ~/ 2;
        y < centerY + squareSize ~/ 2;
        y++) {
      for (int x = centerX - squareSize ~/ 2;
          x < centerX + squareSize ~/ 2;
          x++) {
        pixelColors.add(image.getPixel(x, y));
      }
    }

    int red = 0, green = 0, blue = 0;
    for (int color in pixelColors) {
      red += img.getRed(color);
      green += img.getGreen(color);
      blue += img.getBlue(color);
    }

    int pixelCount = pixelColors.length;
    return [red ~/ pixelCount, green ~/ pixelCount, blue ~/ pixelCount];
  }

  String _getColorNameFromRGB(int r, int g, int b) {
    if (r >= 200 && g < 100 && b < 100) return "Kırmızı";
    if (r >= 150 && r < 200 && g < 100 && b < 100) return "Açık Kırmızı";

    if (r < 100 && g >= 200 && b < 100) return "Yeşil";
    if (r < 100 && g >= 150 && g < 200 && b < 100) return "Açık Yeşil";

    if (r < 100 && g < 100 && b >= 200) return "Mavi";
    if (r < 100 && g < 100 && b >= 150 && b < 200) return "Açık Mavi";

    if (r >= 200 && g >= 200 && b < 100) return "Sarı";
    if (r >= 150 && r < 200 && g >= 150 && g < 200 && b < 100)
      return "Açık Sarı";

    if (r >= 200 && g < 100 && b >= 200) return "Pembe";
    if (r >= 150 && r < 200 && g < 100 && b >= 150 && b < 200)
      return "Açık Pembe";

    if (r >= 200 && g >= 150 && b >= 150) return "Beyaz";
    if (r < 100 && g < 100 && b < 100) return "Siyah";
    if (r >= 100 && g >= 100 && b >= 100 && r < 200 && g < 200 && b < 200)
      return "Gri";

    if (r >= 150 && g >= 100 && b < 100) return "Turuncu";
    if (r >= 100 && g >= 150 && b < 100) return "Lime Yeşili";

    return "Bilinmeyen Renk";
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
                Center(
                  child: Container(
                    width: 100,
                    height: 100,
                    decoration: BoxDecoration(
                      border: Border.all(color: Colors.white, width: 2),
                    ),
                  ),
                ),
                Positioned(
                  bottom: 20,
                  left: 20,
                  child: Container(
                    padding: EdgeInsets.all(10),
                    color: Colors.white.withOpacity(0.8),
                    child: Text(
                      detectedColorName,
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
