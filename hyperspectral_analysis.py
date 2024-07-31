import numpy as np
import spectral.io.envi as envi


class data_handling:
    
    def envi_to_npz(self, dat, fname):
        self.dat = dat
        img = envi.open(self.dat).load()
        np.savez(fname, data=img)
        return print("saved as: {fname}.npz")

    def envi_to_csv:
        ''' code to conver to csv'''
        return print("saved as: {fname}.csv")

    def envi_to_pickle:
        ''' code to convert to pickle '''       `
        return print("saved as: {fname}.pkl")

class analysis:
    """ read hyperspectral data and KMeans labels """
    
 #   def __init__(self):
  #      return

    def findspec(self, region):
        """ find the average spectral profile of specified region """
        # hyperspectral data of isolated region
        self.region = region
        prof = self.region

        # temporary array for holding average spectral profile of region                                                                                                                              
        temp_arr0 = np.zeros((len(prof[0][0])))

        # loop for calculating average intensity for each wavelength                                                                                                                                              
        for i in range(len(prof[0][0])):
            temp_list = []
            for j in range(len(prof[0])):
                    for k in range(len(prof)):
                        if prof[k][j].max()!= 0:
                            temp_list.append(prof[k][j][i]/prof[k][j].max())
            temp_arr0[i] += np.average(temp_list)
        return temp_arr0

    def compare(self, dat1, dat2):

        # some algorithm for comparison
        pass
 
class kmeans:

    def __init__(self, og_data, km_data):
        """ og_data = hyperspectral data
        km_data = KMeans labels """

        self.og_data = og_data
        self.km_data = km_data

    def findregion(self, region):
        """" Define region by a range of Kmeans labels, region=[Lower_bound, Upper_bound]
             default: region=None """
        # temporary array to hold KMeans labels of cholesterol region                                                                                       
        self.region = region
        temp = np.zeros((self.km_data.shape))

        # temporary array to hold spectral data of cholesterol region                                                                                                                                              
        temp_prof = np.zeros((self.og_data.shape))


        # loop through labels and data to isolate cholesterol region                                                                                                                                               
        for i in range(len(self.km_data)):
            for j in range(len(self.km_data[i])):
                if (self.km_data[i][j] <= (self.region[1])) and (self.km_data[i][j] >= (self.region[0])):
                    temp[i][j] += self.km_data[i][j]
                    temp_prof[i][j] += self.og_data[i][j]
        return temp_prof, temp


    def findpercentage(self, region, labels, lower_bound):
        """ calculates the percentage of the vesicle that is a specified region """    
        # temporary array to hold hyperspectral data of full vesicle 
        temp_vesicle = np.zeros((self.og_data.shape))

        # temporary array to hold KMeans labels of full vesicle
        temp_km = np.zeros((self.km_data.shape))

        self.region = region
        prof = self.region 

        self.labels = labels
        ch = labels

        self.lower_bound = lower_bound
        pl = self.lower_bound

        if pl!=None:
            # loop to isolate the vesicle
            for i in range(len(self.km_data)):
                for j in range(len(self.km_data[i])):
                    if self.km_data[i][j] >= pl:
                        temp_km[i][j] += self.km_data[i][j]
                        temp_vesicle[i][j] += self.og_data[i][j]
        else:
            temp_km = self.km_data
            temp_vesicle = self.og_data
        # removes zeros / non-vesicle data
        temp_km = temp_km[temp_km!=0]

        # removes zeros / non-cholesterol data
        ch = ch[ch!=0]

        # calculates the percentage of vesicle that is cholesterol
        chol_per = (len(ch)/len(temp_km))*100

        return chol_per    



class help:
    def __init__(self):
        x = """
        This is a program to help analyze hyperspectral data and its associated kmeans data.
        
        
        hyperspectral_analysis.analysis() is for analyzing specified hyperspectral data
        
        findspec(region) takes in hyperspectral data and returns a spectral profile
        
        findav(region) averages the wavelengths pixel by pixel, useful for visualization


        hyperspectral_analysis.kmeans(og_data, km_data) is for analyzing hyperspectral data using its kmeans labels 

        hyperspectral_analysis.kmeans(og_data, km_data).findregion(region) takes in lower and upper kmeans label bounds to isolate particular regions of the hyperspectral data  
        region=[Lower_bound, Upper_bound]

        hyperspectral_analysis.kmeans(og_data, km_data).findpercentage(self, region, labels, self.lower_bound) will find the percentage of the image that is made up of a specified region
        """
        return print(x)
    
