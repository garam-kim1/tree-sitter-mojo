// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "TreeSitterMojo",
    defaultLocalization: "en",
    products: [
        .library(name: "TreeSitterMojo", targets: ["TreeSitterMojo"]),
    ],
    dependencies: [
        .package(url: "https://github.com/ChimeHQ/SwiftTreeSitter", from: "0.8.0"),
    ],
    targets: [
        .target(
            name: "TreeSitterMojo",
            dependencies: [],
            path: ".",
            sources: [
                "src/parser.c",
                "src/scanner.c",
            ],
            resources: [
                .copy("queries")
            ],
            publicHeadersPath: "bindings/swift",
            cSettings: [.headerSearchPath("src")]
        ),
        .testTarget(
            name: "TreeSitterMojoTests",
            dependencies: [
                "SwiftTreeSitter",
                "TreeSitterMojo",
            ],
            path: "bindings/swift/TreeSitterMojoTests"
        )
    ],
    cLanguageStandard: .c11
)
