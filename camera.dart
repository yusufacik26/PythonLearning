import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'dart:typed_data';

class CameraScreen extends StatefulWidget {
  @override
  _CameraScreenState createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen> {
  CameraController? _controller;
  late Future<void> _initializeControllerFuture;

  @override
  void initState() {
    super.initState();
    initializeCamera();
  }

  Future<void> initializeCamera() async {
    final cameras = await availableCameras();
    _controller = CameraController(cameras[0], ResolutionPreset.medium);
    _initializeControllerFuture = _controller!.initialize();
    setState(() {});
  }

  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }

  Future<void> captureImage() async {
    try {
      await _initializeControllerFuture;
      final image = await _controller?.takePicture();
      if (image != null) {
        Uint8List imageData = await image.readAsBytes();
        detectColor(imageData); // Renk tespiti fonksiyonunu çağır
      }
    } catch (e) {
      print(e);
    }
  }

  void detectColor(Uint8List imageData) {
    // Renk tespiti fonksiyonunu burada uygulayacağız
  }

  @override
  Widget build(BuildContext context) {
    if (_controller == null || !_controller!.value.isInitialized) {
      return Center(child: CircularProgressIndicator());
    }

    return Scaffold(
      appBar: AppBar(title: Text('Kamera ile Renk Tespiti')),
      body: CameraPreview(_controller!),
      floatingActionButton: FloatingActionButton(
        onPressed: captureImage,
        child: Icon(Icons.camera),
      ),
    );
  }
}
