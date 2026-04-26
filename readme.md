# Image splitter

A simple desktop tool to sort images into *yes* or *no* bins—useful when preparing a dataset from a large folder of raw images.

I built this because I kept manually opening and closing image files in a folder, getting tired of it. It’s not fancy, but it gets the job done.

## Usage

- Select a source folder (all images in that folder load into the queue).
- Click **Yes** or **No** to sort each image into its bin folder.
- Bins are created automatically as subfolders (`yes/` and `no/`) next to the source folder.

> Tip: Avoid huge folders—everything loads into memory at startup. I’ve used it comfortably with ~5k 1080p images.

## Tech stack

- Python 3.8+
- `tkinter` (bundled)
- `Pillow` (for image handling)

## Setup & run

1. Install dependencies with `pipenv`:  
   ```bash
   pipenv install pillow
   ```
2. Run:  
   ```bash
   pipenv run python imagesplitter.py
   ```

## Notes

- No folder structure required—just point it at a flat directory of images.
- No class hierarchy—single-script implementation. Just `imagesplitter.py`.

## More from Karelseaat

For more projects and experiments, visit my GitHub Pages site: [karelseaat.github.io](https://karelseaat.github.io/)
