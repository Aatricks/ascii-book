# CLI Contract

This document defines the command-line interface for the `ascii-book` tool.

## Command

```bash
python -m ascii_art_generator.main <input_path> <output_path> [options]
```

## Positional Arguments

| Name | Description |
|---|---|
| `input_path` | The path to the source image file (PNG, JPG). |
| `output_path` | The path to save the generated ASCII art image. |

## Options

| Flag | Argument | Description | Default |
|---|---|---|---|
| `-w`, `--width` | integer | The desired width of the output image in characters. | 120 |
| `-m`, `--minimalistic` | - | Enables minimalistic mode for subject isolation. | `False` |
| `--bg-removal-method` | `simple` or `ml` | The method for background removal in minimalistic mode. | `simple` |
| `-h`, `--help` | - | Show the help message and exit. | - |
