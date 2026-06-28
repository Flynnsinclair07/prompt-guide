// vision_ocr.swift — macOS Vision OCR helper.
//
// Usage:  swift vision_ocr.swift /path/to/image.jpg
// Prints recognized text, one line per detected line, to stdout.
//
// Uses Apple's Vision framework (on-device, no network, no API key). Requires the
// Xcode Command Line Tools (`xcode-select --install`). prep_receipts.py calls this
// when `swift` is available and falls back to pytesseract otherwise.
import Foundation
import Vision
import AppKit

guard CommandLine.arguments.count > 1 else {
    FileHandle.standardError.write("usage: swift vision_ocr.swift <image>\n".data(using: .utf8)!)
    exit(64)
}

let path = CommandLine.arguments[1]
guard let image = NSImage(contentsOfFile: path),
      let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    FileHandle.standardError.write("could not load image: \(path)\n".data(using: .utf8)!)
    exit(65)
}

let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
do {
    try handler.perform([request])
    guard let observations = request.results else { exit(0) }
    for obs in observations {
        if let candidate = obs.topCandidates(1).first {
            print(candidate.string)
        }
    }
} catch {
    FileHandle.standardError.write("OCR failed: \(error)\n".data(using: .utf8)!)
    exit(66)
}
