import pandas as pd
tot_size=1100000
chunk = tot_size * .1
filepath = 'data\events_anomalydetection.h5'
def generator(filename, chunksize= chunk,total_size = tot_size):
    i = 0
    while True:
        yield pd.read_hdf(filename,start=i*chunksize, stop=(i+1)*chunksize)
        i+=1
        if (i+1)*chunksize > total_size:
            i=0


for i in range(0,int(tot_size/chunk)):
    gen = generator(filepath)
    next(gen).to_hdf('small_events_anomalydetection_' + str(i) +'.h5', key='data', mode='w')