# Video Resolution and Format Converter

This Python script can reduce the resolution of one or more video files and change their video format. It provides a command-line interface for easy usage.

## Prerequisites

- Python 3.x installed on your system.

## Usage

### Installation

1. Clone or download the repository to your local machine.
2. Ensure you have the required Python dependencies installed by running:
   ```bash
   pip install -r requirements.txt
   ```

### Command-line Arguments

- `filepaths`: Path to the file(s) to process. You can specify multiple files.
- `-o, --output`: The output file to convert to.
- `-format, --videoformat`: The format to use. Available choices are mp4, mov, avi, mkv, webm, and ogv.
- `-r, --resolution`: Choose a (two) resolution to resize to. Example: `-r 1920 1080`

### Example Usage

#### Single File Conversion

To convert a single video file with specified resolution and output format:

```bash
python video_converter.py path/to/input_video.mp4 -o path/to/output_video.mp4 -r 1280 720 -format mp4
```

#### Multiple Files Conversion

To convert multiple video files with a common resolution and output format:

```bash
python video_converter.py path/to/input_video1.mp4 path/to/input_video2.mov -r 1920 1080 -format mov
```

## Notes

- If you provide a resolution, ensure it is in the format: `-r width height`.
- Output filename will be automatically generated for multiple files based on the input filename and chosen resolution.

## License

This project is licensed under the [MIT License](LICENSE).
