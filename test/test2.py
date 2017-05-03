import image

gen=image.ImageGenerator("caffe/examples/cifar10_copy/cifar10_full_iter_70000.caffemodel.h5","caffe/examples/cifar10_copy/cifar10_full.prototxt","data","ip1","prob")

gen.generate_number_image(32,32,1000,8,"ouput.jpg")

