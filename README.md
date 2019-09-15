# ImageBoard  <img height="25px" src="https://user-images.githubusercontent.com/4397546/64920384-ae1d0500-d7e9-11e9-8aed-308f81088e8c.png"> 


This framework contains a simple UI for image comaprsion between different methods.

![image](https://user-images.githubusercontent.com/4397546/64920210-3d74e900-d7e7-11e9-9033-010b497a8d7d.png)


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

3. run `python app.py` in the root dir of this project and open your favourite browser to `0.0.0.0:5000`.

### UI function

- [x] adjust the image size.
- [x] only compare certain images (remember or only in current page).
- [x] Pagination
- [ ] config file for port and dir
- [ ] install via pip
