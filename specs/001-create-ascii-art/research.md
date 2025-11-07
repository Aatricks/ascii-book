# Research & Decisions

This document records the technical decisions made during the planning phase for the ASCII Art Generator.

## Technology Selection

| Component | Technology | Rationale | Alternatives Considered |
|---|---|---|---|
| Language | Python 3.11 | A modern, stable version of Python with wide library support for image processing. | - |
| Image Manipulation | Pillow | The de-facto standard for image processing in Python. It's feature-rich and easy to use. | - |
| Numerical Operations | NumPy | Required by OpenCV and useful for efficient array manipulation of image data. | - |
| Advanced Image Ops | OpenCV | Provides robust implementations of edge detection (Canny, Sobel) and potentially more advanced segmentation algorithms for minimalistic mode. | Scikit-image (another good option, but OpenCV is more common for this type of task). |
| CLI Framework | argparse | Part of the Python standard library, making it a lightweight and dependency-free choice for creating the CLI. | Click, Typer (both are excellent, but add an external dependency). |
| Testing | pytest | A powerful and flexible testing framework for Python, with a rich ecosystem of plugins. | unittest (standard library, but more verbose). |

## Key Decisions

- **Minimalistic Mode Implementation**: The decision to support both a simple color-based segmentation and a more advanced ML-based method provides a good balance of simplicity and power for the user. The initial implementation will focus on the color-based approach, with the ML model being a future enhancement.
- **Project Structure**: A single, package-based structure (`src/ascii_art_generator`) was chosen for its simplicity and suitability for a self-contained CLI tool.
