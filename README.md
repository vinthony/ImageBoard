# ImageBoard

This framework contains a simple UI for image comaprsion between different methods.

![image](https://user-images.githubusercontent.com/4397546/64908430-d85fbb80-d732-11e9-9bf2-68279382a405.png)

### Requirements

- Flask
- jinja2

### Usage

1. clone this repo by `git clone https://github.com/vinthony/ImageBoard.git`
2. Put the image with ***SAME NAME*** under the folder like : 
`static/dataset1/method1/1.png`,
`static/dataset1/method2/1.png`,
...
`static/dataset1/methodN/1.png`.
(Each dataset must contains **input** folder as reference.
Some examples can be found in `static/_SBU/`.)

3. run `python run.py` in the root dir of this project and open your favourite browser to `0.0.0.0:5000`.

### UI function

- [x] adjust the image size.
- [x] only compare certain images (remember or only in current page).
- [x] Pagination
- [ ] config file for port and dir
- [ ] install via pip
