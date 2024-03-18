# Video Resolution and Format Converter

This Python script can change the resolution and change the format of one or more video files.

## Prerequisites

- Python 3.x installed on your system.

## Usage

### Installation

1. Clone or download the repository to your local machine:
```bash
git clone https://github.com/iamvetle/VideoConvertor
```
2. Ensure you have the required Python dependencies installed by running:
```bash
pip install -r requirements.txt
```

### Command-line Arguments

- `FILES`: One or more paths to the video files you want to process.
- `-o, --output` OUTPUT_FILE: (Optional) The name of the output file to create. If not specified, the output file will have a modified name based on the original file and applied changes.
- `-format, --videoformat` VIDEOFORMAT: (Optional) The desired output video format. Supported formats: mp4, mov, avi, mkv, webm, ogv. **Required** when processing multiple files.
- `-r, --resolution` RESOLUTION_WIDTH RESOLUTION_HEIGHT: (Optional) The desired output resolution in the format width height (e.g., 1280 720 for 720p).


### Example Usage

``` bash
python main.py [-o OUTPUT_FILE] [-format VIDEOFORMAT] [-r RESOLUTION_WIDTH RESOLUTION_HEIGHT] FILES
```

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

- When processing multiple files:
    - The `-o` option cannot be used. Output filenames will be generated based on the original filenames and applied changes.
    - The `-format` option is **required**.
- When processing a single file with only a change in format:
    - The `-format` option is **not needed**, as the format will be inferred from the output filename.