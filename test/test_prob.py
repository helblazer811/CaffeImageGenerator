import image
import os
gen=image.ImageGenerator("caffe/models/bvlc_googlenet/bvlc_googlenet.caffemodel","caffe/models/bvlc_googlenet/deploy.prototxt","data","loss3/classifier","prob")

for file in os.listdir("imagenet"):
    print file
    print gen.image_probability("imagenet/"+file,1)
