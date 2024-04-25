import numpy as np
import cv2
import matplotlib.pyplot as plt

def load_image(image_path):
    image_path = image_path.strip()
    return cv2.imread(image_path)

def save_image(image, path):
    cv2.imwrite(path, image)

def show_image(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image

def search_cv2(function_name):
    try:
        return getattr(cv2, function_name)
    except AttributeError:
        return None
    
def gen_matrix(a,b,*args):
    s = np.array(args)
    return s.reshape(int(a), int(b))

def gen_vector(*args):
    s = np.array(args)
    return s

def multiplot_show(nrows, ncols, *args):
    
    if( type(nrows) is float):
        nrows = int(nrows)
    if( type(ncols) is float):
        ncols = int(ncols)
        
    
    args_i = 0
    for i in range(1,nrows+1):
        for j in range(1,ncols+1):
            if(args_i < len(args)):
                plt.subplot(nrows,ncols,args_i+1)
                red = args[args_i][:,:,2].copy()
                args[args_i][:,:,2] = args[args_i][:,:,0] 
                args[args_i][:,:,0] = red
                
                plt.imshow(args[args_i] )
                plt.title(f'img_{args_i}')
                args_i += 1
    
    plt.show()
    plt.close()


# histogram visualization with opencv
def histogram_visualization(image):
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([image],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
    plt.close()

# grabcut segmentation, for the image input it's important
# to have an image that contains the mask of the wanted object
# and the same image without that specification
def grabcut_segmentation(image):
    # in this line we are creating a mask
    mask = np.zeros(image.shape[:2],np.uint8)

    # these are the background and foreground models
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (50,50,450,290)

    # opencv grabcut function, that will segment the image
    cv2.grabCut(image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

    # this line will create a mask2
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

    # this line will multiply the mask2 with the original image
    # and segment the image
    image = image*mask2[:,:,np.newaxis]

    return image

# numpy 9 functions
def numpy_sin(x):
    return np.sin(x)

def numpy_cos(x):
    return np.cos(x)

def numpy_tan(x):
    return np.tan(x)

def numpy_arcsin(x):
    return np.arcsin(x)

def numpy_arccos(x):
    return np.arccos(x)

def numpy_arctan(x):
    return np.arctan(x)

def numpy_sinh(x):
    return np.sinh(x)

def numpy_cosh(x):
    return np.cosh(x)

def numpy_tanh(x):
    return np.tanh(x)