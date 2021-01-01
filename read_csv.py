# import required package
import csv


# function to read data
def read_data(dataset):
    datas = []      # initialize list to store csv content
    with open(dataset, 'rt')as f:   # open csv
        content = csv.reader(f)     # read csv content
        for rows in content:        # read each row
            tem = []                # tem. list to store each row
            for cols in rows:       # read attributes(each column values) in rows
                tem.append(cols)    # append data to tem(data will be read as string, for integer value use int(cols))
            datas.append(tem)       # append row data to datas
    return datas        # return the csv content


# main
data = read_data("sample.csv")  # read data from sample.csv file
print(data)     # print data
