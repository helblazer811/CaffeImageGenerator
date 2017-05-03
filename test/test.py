import image

gen=image.ImageGenerator("../caffe/examples/cifar10_copy/cifar10_full_iter_70000.caffemodel.h5","../caffe/examples/cifar10_copy/cifar10_full.prototxt","data","ip1","prob")

gen.generate_probable_image(32,32,.9999999,8,"output.jpg")
