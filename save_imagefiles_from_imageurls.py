#!/usr/bin/python3
# Code name: save_imagefiles_from_imageurls.py 
# Brief Description: Simple code to download image files from an input url and 
# save them to file using request.urlretrieve from urllib. The trick is in 
# defining the mapping you want between the input image url and the output 
# image file names.  In general, this involves the concatenation of various 
# string variables, with one or more lists that need to be iterated through.
# The following example demonstrates how to download two types of sun images 
# from the spaceweather website: http://spaceweather.com
# Each image url pair is located in a folder identified by a date value in a 
# particular format as seen below
# The input image url pairs are comprised of a "coronal hole" image and a 
# "sunspot" image (e.g. "hmi1898").  Many different formats can be downloaded.
# The output image file pairs are obtained by concatenating the image path and
# file name.  Note that both images are written in one format, which has many
# options (see requests.urlretrieve man page)
# Code References:
# urllib.request.urlretrieve use follows forum reply by Liquid_Fire on 11/27/11
# see http://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-
# using-python-whose-url-address-i-already-know
# Created on: September 2, 2016
# Written by: Frederick D. Pearce
# Code version: 0.1 on 09/02/2016 - Original version used to setup github repo

# Copyright 2016 Frederick D. Pearce

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

## I) Import modules, all available via pip install
import urllib.request

## II) Define functions
def get_spaceweather_imageurl(iu_address, iu_date, iu_filename, iu_extension, \
        verbose):
    """Returns a complete image url string tailored to the spaceweather site by 
    concatenating the input image url (iu) strings that define the
    address, the date folder, the filename root, and the filename extension.
    If verbose is truthy, then print the returned image url string
    """
    sw_imageurl = iu_address + iu_date + "/" + iu_filename + iu_extension
    if verbose:
        print("Input image file URL: \n{}".format(sw_imageurl))
    return sw_imageurl

def get_spaceweather_imagefile(if_path, if_date, if_filename, if_extension, \
        verbose):
    """Returns a complete image filename string tailored to the spaceweather 
    site string by concatenating the input image filename (if) strings that 
    define the path, date, filename root, and the filename extension
    If verbose is truthy, then print the returned image filename string
    """
    sw_imagefile = if_path + if_date + "_" + if_filename + if_extension
    if verbose:
        print("Output image file full path: \n{}\n".format(sw_imagefile))
    return sw_imagefile

def save_spaceweather_images_to_file(input_data, output_data):
    """Save images to file from their urls on the Spaceweather website.
    This is a three step process that requires two loops, one over the folder 
    date values, inp_date, and the other over the url files contained within 
    each folder:
        1) Get the image urls specified in the input_data dict using the 
           website specific function get_*_imageurl() (e.g. spaceweather)
        2) Get the image file name specified in the output_data dict using 
           the user specified function get_*_imagefile()
        3) Download each image from its url and save it to its image file name
           using urllib.request.urlretrieve
      Warning: the ['file']['name'] list in input_data MUST be the same length as 
      the ['file']['name'] list in output_data!!!
    """
    print("\n**** Saving image files from input URLs ****\n")
    for inp_date in input_data['url']['folder']['date']['values']:
        for inp_fnind, inp_fname in enumerate(input_data['url']['file']['name']):
            input_imageurl = get_spaceweather_imageurl( \
                    input_data['url']['address'], inp_date, inp_fname, \
                    input_data['url']['file']['ext'][inp_fnind], \
                    output_data['verbose']
            )
            output_imagefile = get_spaceweather_imagefile( \
                    output_data['image']['path'], inp_date, \
                    output_data['image']['file']['name'][inp_fnind], \
                    output_data['image']['file']['ext'], \
                    output_data['verbose']
            )
            urllib.request.urlretrieve(input_imageurl, output_imagefile)
    if output_data['verbose']:
        print("**** Finished saving images to file ****\n")

## III) If this file is run from command line, execute script below
if __name__ == "__main__":
    ## Run script
    # input_data dict values are used to define image url names
    # output_data dict values are used to define image file names
    #   output_data['image']['path'] MUST exist! 
    #   output_data['verbose'] = True prints details to screen
    # The input file name extensions can be anything supported by 
    # request.urlretrieve, while the output image files are saved in a single 
    # format defined by the image file extension
    # ToDo: give option to create image path if it doesn't exist already
    input_data = { \
        'url': { \
            'address': "http://spaceweather.com/images2016/", \
            'folder': { \
                'date': { \
                    'values': ["12aug16", "13aug16"], \
                    'format': "%d%b%y"
                }
            }, \
            'file': { \
                'name': ["coronalhole_sdo_blank", "hmi1898"], \
                'ext': [".jpg", ".gif"]
            }
        }
    }
    output_data = { \
        'image': { \
            'path': \
                "/Users/frederickpearce/Documents/PythonProjects/save_imagefiles_from_imageurls/sun_images/", \
            'file': { \
                'name': ["coronalhole", "sunspot"], \
                'ext': ".jpg"
            }
        }, 
        'verbose': True
    }
    # Save images to file from their urls on the Spaceweather website: 
    # http://spaceweather.com.  It loops over folder and image file values
    # downloading images from each of the input url address+folder+filenames
    # and saving them to each of the image path+filenames
    # Warning: the ['file']['name'] list in input_data MUST be the same length as 
    # the ['file']['name'] list in output_data!!!
    save_spaceweather_images_to_file(input_data, output_data) 

