# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:26:03 2023

@author: GPZ1100
"""
import requests
import cv2
import numpy as np
from numpy import random
import os

#FINAL STEP: ITERATE OVER ALL IMAGES IN FOLDER
for i in range(TOTALNUMBEROFIMAGES):
    
    #Uploads Image to model server
    headers = {
        # requests won't add a boundary if this header is set when you pass files=
        #'Content-Type': 'multipart/form-data',
        'apikey': 'ENTERYOURAPIKEY',
        'apisecret': 'ENTERYOURAPISECRET',
    }
    
    params = {
        'endpoint_id': 'ENTERYOURENDPOINTID',
    }
    
    #Protip: You can Ctrl+A, right click, and rename the first image to "1" to rename all scans to a number we can iterate on

    files = {
            'file': open(r'ENTERYOURIMAGEDIRECTORY\1 (%s).jpg'%(i+1), 'rb'),
    } 
    resp = requests.post('https://predict.app.landing.ai/inference/v1/predict', params=params, headers=headers, files=files)
    data = resp.json() # Check the JSON Response
    
    #Extracts model predictions
    List = [value for value in data['backbonepredictions'].values()]
    j = len(List)
    newList = []
    
    #Delete weak predictions
    for c in range(j):   
        if List[c]['score'] > 0.5:
            newList.append(List[c])
                   
    k = len(newList)   
    cropXmin = np.zeros(k)
    cropYmin = np.zeros(k)
    cropXmax = np.zeros(k)
    cropYmax = np.zeros(k)
    
    #Extracts coordinates of crops
    for v in range(k):
              cropXmin[v] = List[v]['coordinates']['xmin']
              cropYmin[v] = List[v]['coordinates']['ymin']
              cropXmax[v] = List[v]['coordinates']['xmax']
              cropYmax[v] = List[v]['coordinates']['ymax']
    
    #Crops image at coordinates
    
    mainImg = cv2.imread(r'ENTERYOURIMAGEDIRECTORY\1 (%s).jpg'%(i+1))
    crop_image = []
    for b in range(k):
        crop_image.append(mainImg[ int(cropYmin[b]) : int(cropYmax[b]), int(cropXmin[b]) : int(cropXmax[b]) ])
        
        
    #Resizes Image into rectangle and upscales
    
    
    
    
    
    
    #Saves cropped images
    os.chdir(r'ENTERYOUROUTPUTDIRECTORY')
    for n in range(k):
        p = random.randint(100000000)
        filename = 'Img{}{}.jpg'.format(i,p)
        cv2.imwrite(filename, crop_image[n])





