# MicroCV
_Petri dish OpenCV blob detection_

## Installation

Assuming python/pip are installed, run 
`python -m pip install -r requirements.txt` to set up the necessary requirements. replace `python` with your own python installation alias.

## Usage

From the command line, run `python main.py IMAGE_FILENAME`, where `IMAGE_FILENAME` is the petri dish image to analyze (e.g. example1.png).

The provided sliders may be used to refine the feature detection parameters. The sliders correspond to the following parameters:

- min_dist: Minimum distance between detected centers.
- edge_threshold: Upper threshold for the internal Canny edge detector.
- centre_threshold: Threshold for center detection.
- min_radius: Minimum radius to be detected. If unknown, put zero as default.
- max_radius: Maximum radius to be detected. If unknown, put zero as default.

Quit the python window by pressing `q`, or quitting the process from the command line.

>*Note that even with optimal settings, some features may not be detected. MicroCV is a tool intended to _aid_ microbial 
growth enumeration -- not automate it entirely. It is your responsibility to manually add false negatives / remove false positives from your tally.*    
