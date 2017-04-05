# svg2png
This is a simple wrapper that converts SVG files to PNG using Inkscape.

## Usage
```
svg2png.py -i <src_folder> -s <output_size_array> [-o <output_folder>]
    -i        source folder that contains the svg files
    -s        target size array
    -o        output folder
              [Optional]if not provided, output is set to current folder where
              this script locates
    -h        print this help
```

## Example
`python svg2png.py -i /path/to/icon/folder/ -s 100,200,300 -o .`

Above command reads all svg files from folder /Users/shiyun/iconlibrary, convert into 3 different target dimensions and save into separate folders. 
Target folders(./100/, ./200/ and ./300/) are created under current folder(.)

## Prerequisite - Inkscape
This script requires **Inkscape** to do the real conversion. Please install **Inkscape** before running this script.

HOW-TO install 'inkscape' by Homebrew. 

    `brew install caskformula/caskformula/inkscape`
### Note

- Brew installation of 'Inkscape' might take 20 min for downloading and building, so please be patient.
- More detail for **Inkscape** installation, check [Inkscape Official Website](https://inkscape.org/en/download/mac-os/)

    
