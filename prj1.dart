import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
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
      title: 'Local Color Detection',
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
    // Periyodik olarak renk tespiti yap
    Timer.periodic(Duration(seconds: 2), (timer) async {
      await _detectColor();
    });
  }

  Future<void> _detectColor() async {
    try {
      // Görüntü yakala
      final image = await _controller.takePicture();
      final bytes = await image.readAsBytes();

      // `image` paketini kullanarak görüntüyü işliyoruz
      img.Image? capturedImage = img.decodeImage(bytes);

      if (capturedImage != null) {
        // Görüntünün ortasındaki 100x100 piksellik kareyi tespit et
        int centerX = capturedImage.width ~/ 2;
        int centerY = capturedImage.height ~/ 2;
        int squareSize = 100;

        img.Image croppedImage = img.copyCrop(
            capturedImage,
            centerX - squareSize ~/ 2,
            centerY - squareSize ~/ 2,
            squareSize,
            squareSize);

        // Ortalama rengi hesapla
        int red = 0, green = 0, blue = 0;
        int pixelCount = squareSize * squareSize;

        for (int y = 0; y < croppedImage.height; y++) {
          for (int x = 0; x < croppedImage.width; x++) {
            int pixel = croppedImage.getPixel(x, y);
            red += img.getRed(pixel);
            green += img.getGreen(pixel);
            blue += img.getBlue(pixel);
          }
        }

        red ~/= pixelCount;
        green ~/= pixelCount;
        blue ~/= pixelCount;

        setState(() {
          detectedColor = "R: $red, G: $green, B: $blue";
        });
      } else {
        setState(() {
          detectedColor = "Görüntü işlenemedi";
        });
      }
    } catch (e) {
      setState(() {
        detectedColor = "Hata: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Local Color Detection'),
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
