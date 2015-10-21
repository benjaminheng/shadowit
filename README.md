# Shadowit

Shadow it! A no-fuss way to apply drop shadows to images.

Adding shadows to your images is a quick way to give some flair to your website, blog, or project repository. Shadowit allows you to easily and flexibly shadow your images. Check out some [examples](examples/examples.md) of Shadowit in action!

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [ImageMagick](http://www.imagemagick.org/script/binary-releases.php)

## Usage

```bash
$ python shadowit.py <input_file> [options...]
```

**Changing defaults**

Have your favorite configuration? Easily modify the default parameters by changing the values at the top of `shadowit.py`!

## Options

Option                      | Description
---                         | ---
**`-h`**                    | View help
**`INPUT`**                 | Input file name **(required)**
**`-o, --output FILE`**     | Output file name *(default: output.png)*
**`--exe FILE`**            | Path to ImageMagick's `convert` executable
**`--opacity OPACITY`**     | Opacity of shadow *(default: 100)*
**`--color COLOR`**         | Color of shadow *(default: #444444)*
**`--size SIZE`**           | Size of shadow *(default: 22)*
**`-x, --xOffset X`**       | X offset of shadow *(default: 0)*
**`-y, --yOffset Y`**       | Y offset of shadow *(default: 20)*
**`--imageBgColor COLOR`**  | Color of output image's background *(default: none)*

## License

MIT license
