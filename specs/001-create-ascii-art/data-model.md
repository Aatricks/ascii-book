# Data Model

This document defines the key data entities for the ASCII Art Generator.

## 1. ConversionConfiguration

Represents the set of parameters that control a single ASCII art conversion process.

**Fields**:

| Name | Type | Description | Validation Rules |
|---|---|---|---|
| `input_path` | string (path) | The absolute or relative path to the source image. | Must be a valid path to a readable file. Must be a supported image format (PNG, JPG). |
| `output_path` | string (path) | The path where the generated ASCII art image will be saved. | The directory must exist and be writable. |
| `width` | integer | The desired width of the output image in characters. The height will be scaled proportionally. | Optional. Must be a positive integer. Defaults to a reasonable value (e.g., 120). |
| `minimalistic` | boolean | A flag to enable or disable minimalistic mode. | Defaults to `false`. |
| `bg_removal_method` | string (enum) | The method to use for background removal in minimalistic mode. | Optional. Must be one of `simple` or `ml`. Defaults to `simple`. |

**State Transitions**:

A `ConversionConfiguration` object is created at the start of the CLI tool's execution, based on the user-provided arguments. It is immutable for the duration of the conversion process.
