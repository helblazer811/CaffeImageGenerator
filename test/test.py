import image

gen=image.ImageGenerator("../caffe/examples/cifar10_copy/cifar10_full_iter_70000.caffemodel.h5","../caffe/examples/cifar10_copy/cifar10_full.prototxt","data","ip1","prob")

gen.generate_probable_image(64,64,.999,8,"output.jpg",8)
