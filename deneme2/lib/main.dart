import 'package:camera/camera.dart';
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
      home: CameraPage(),
    ));

class CameraPage extends StatefulWidget {
  @override
  _CameraPageState createState() => _CameraPageState();
}

class _CameraPageState extends State<CameraPage> {
  late CameraController _controller;
  late List<CameraDescription> cameras;
  Future<void>? _initializeControllerFuture; // Nullable olarak tanımlandı

  @override
  void initState() {
    super.initState();
    _initializeCamera();
  }

  Future<void> _initializeCamera() async {
    cameras = await availableCameras();
    _controller = CameraController(
      cameras[0], // İlk mevcut kamerayı seçer (genellikle arka kamera)
      ResolutionPreset.high,
    );

    _initializeControllerFuture = _controller.initialize();
    setState(() {});
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Kamera')),
      body: _initializeControllerFuture == null
          ? Center(
              child:
                  CircularProgressIndicator()) // Future null ise yükleme göstergesi göster
          : FutureBuilder<void>(
              future: _initializeControllerFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  // Kamera başlatıldığında görüntü
                  return CameraPreview(_controller);
                } else {
                  // Kamera başlatılırken yükleme göstergesi
                  return Center(child: CircularProgressIndicator());
                }
              },
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async {
          try {
            await _initializeControllerFuture;
            final image = await _controller.takePicture();
            // Burada resmi işle veya göster
            print('Resim çekildi: ${image.path}');
          } catch (e) {
            print(e);
          }
        },
        child: Icon(Icons.camera),
      ),
    );
  }
}
