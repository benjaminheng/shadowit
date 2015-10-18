# Shadowit

Shadow it! A no-fuss way to apply a drop shadow to an image.

Check out some [examples](examples/examples.md) of Shadowit in action!

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [ImageMagick](http://www.imagemagick.org/script/binary-releases.php)

## Quick Start

```bash
$ python shadowit.py <input_file> [options...]
```

## Options

Option                      | Description
---                         | ---
**`-h`**                    | View help
**`INPUT`**                 | Input file name **(required)**
**`-o, --output FILE`**     | Output file name *(default: output.png)*
**`--exe FILE`**            | Path to ImageMagick's `convert` executable
**`--opacity OPACITY`**     | Opacity of shadow *(default: 65)*
**`--color COLOR`**         | Color of shadow *(default: #555555)*
**`--size SIZE`**           | Size of shadow *(default: 9)*
**`-x, --xOffset X`**       | X offset of shadow *(default: 0)*
**`-y, --yOffset Y`**       | Y offset of shadow *(default: 10)*
**`--borderSize SIZE`**     | Size of image border *(default: 0)*
**`--borderColor COLOR`**   | Color of image border *(default: none)*
**`--imageBgColor COLOR`**  | Color of output image's background *(default: none)*

## License

MIT license
