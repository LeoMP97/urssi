import numpy as np
import spectral.io.envi as envi
import pandas as pd

# adding a change to my code for review

class data_handling:
    def __init__(self, dat, fname):
        self.dat = dat
        self.fname = fname

    def envi_to_npz(self):
        img = envi.open(self.dat).load()
        return np.savez(self.fname, data=img), \
                print("saved as: {self.fname}.npz")

    def envi_to_csv():
        """code to conver to csv"""
        df = pd.Dataframe(self.dat)
        df.to_csv("{self.fname}.csv")
        return print("saved as: {self.fname}.csv")

    def envi_to_pickle():
        df = pd.Dataframe(self.dat)
        df.to_pickle("{self.fname}.pkl")

        """code to convert to pickle"""
        return print("saved as: {self.fname}.pkl")


class analysis:
    """read hyperspectral data and KMeans labels"""

    def findspec(self, region):
        """find the average spectral profile of specified region"""
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
                    if prof[k][j].max() != 0:
                        temp_list.append(prof[k][j][i] / prof[k][j].max())
            temp_arr0[i] += np.average(temp_list)
        return temp_arr0

    def compare(self, dat1, dat2):
        # some algorithm for comparison
        return


class kmeans:
    def __init__(self, og_data, km_data):
        """og_data = hyperspectral data
        km_data = KMeans labels"""

        self.og_data = og_data
        self.km_data = km_data

    def findregion(self, region):
        """ " Define region by a range of Kmeans labels, region=[Lower_bound, Upper_bound]
        default: region=None"""
        # temporary array to hold KMeans labels of cholesterol region
        self.region = region
        temp = np.zeros((self.km_data.shape))

        # temporary array to hold spectral data of cholesterol region
        temp_prof = np.zeros((self.og_data.shape))

        # loop through labels and data to isolate cholesterol region
        for i in range(len(self.km_data)):
            for j in range(len(self.km_data[i])):
                if (self.km_data[i][j] <= (self.region[1])) and (
                    self.km_data[i][j] >= (self.region[0])
                ):
                    temp[i][j] += self.km_data[i][j]
                    temp_prof[i][j] += self.og_data[i][j]
        return temp_prof, temp

    def findpercentage(self, region, labels, lower_bound):
        """calculates the percentage of the vesicle that is a specified region"""
        # temporary array to hold hyperspectral data of full vesicle
        temp_vesicle = np.zeros((self.og_data.shape))

        # temporary array to hold KMeans labels of full vesicle
        temp_km = np.zeros((self.km_data.shape))

        self.region = region

        self.labels = labels
        ch = labels

        self.lower_bound = lower_bound
        pl = self.lower_bound

        if pl is not None:
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
        temp_km = temp_km[temp_km != 0]

        # removes zeros / non-cholesterol data
        ch = ch[ch != 0]

        # calculates the percentage of vesicle that is cholesterol
        chol_per = (len(ch) / len(temp_km)) * 100

        return chol_per
