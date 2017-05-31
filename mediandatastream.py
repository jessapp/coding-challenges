# Find the median in an ever-changing data stream
# If there are an even amount of numbers in the data stream, return the sorted middle
# Otherwise, return the average of the two middle numbers 

class DataStream(object):

    def __init__(self):
        self.datastream = []

    def add(self, num):
        self.datastream.append(num)

    def get_median(self):

        # sort data stream

        ds = self.datastream

        if ds == []:
            return []

        if len(ds) == 1:
            return ds.pop()

        for i in range(1, len(ds)):

            j = i - 1

            while j >= 0 and ds[j] > ds[i]:
                j -= 1
            j += 1

            if j != i:
                ds[j:i + 1] = ds[i: i+1] + ds[j:i]

        if len(ds) % 2 != 0:
            mid = len(ds) / 2
            return ds[mid]
        else:
            mid = len(ds) / 2
            return (ds[mid] + ds[mid-1]) / 2