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


## III) If this file is run from command line, execute script below
if __name__ == "__main__":
    ## Run script
    # input_data dict is used to define image url names
    # output_data dict is used to define image file names
    #   output_data['image']['path'] MUST exist! 
    #   output_data['verbose'] = True prints details to screen
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
    # Download image file from image file at input_data['url']['address'] +
    # input_data['url']['folder']['date']['values'] +
    # input_data['url']['file']['name'] + 
    # input_data['url']['file']['ext']
    # Then, write image file to directory/filename defined by
    # output_data['image']['path'] + output_data['image']['file']['name'] +
    # output_data['image']['file']['ext']
    # The ['file']['name'] list value in input_data MUST be the same length as 
    # the ['file']['name'] list value in  output_data!!!
    print("\n**** Saving image files from input URLs ****\n")
    for inp_date in input_data['url']['folder']['date']['values']:
        for inp_fnind, inp_fname in enumerate(input_data['url']['file']['name']):
            input_url = input_data['url']['address'] + inp_date + "/" + \
                    inp_fname + input_data['url']['file']['ext'][inp_fnind]
            if output_data['verbose']:
                print("Input image file URL: \n{}".format(input_url))
            output_imagefile = output_data['image']['path'] + \
                    "_".join((inp_date, \
                            output_data['image']['file']['name'][inp_fnind])) + \
                    output_data['image']['file']['ext']
            if output_data['verbose']:
                print("Output image file path: \n{}\n".format(output_imagefile))
            urllib.request.urlretrieve(input_url, output_imagefile)
    if output_data['verbose']:
        print("")

