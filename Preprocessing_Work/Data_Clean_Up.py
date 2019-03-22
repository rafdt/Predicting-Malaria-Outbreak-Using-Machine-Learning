def getOutbreakHashMap():
    outbreaks = dict()
    file = open("/Users/ashleytran/Desktop/Outbreak Data.csv", mode = "r")
    lines = file.readlines()
    for i in range(1, len(lines)):
        values = lines[i].strip("\n").split(",")
        if values[3] in outbreaks.keys():
            outbreaks[values[3]].append(values[2])
        else:
            outbreaks[values[3]] = list()
            outbreaks[values[3]].append(values[2])
    return outbreaks

def main():
    outbreaks = getOutbreakHashMap()
    teenFile = open("/Users/ashleytran/Desktop/Teen Dataset - NIS-Teen Trend-MMR 2017 Data.csv", mode="r", encoding = "utf-8")
    childFile = open("/Users/ashleytran/Desktop/Child Dataset - NIS-Child Trend-MMR 2017 Data.csv", mode="r", encoding= "utf-8")
    cleanedFile = open("/Users/ashleytran/Desktop/Aggregated_Data.csv", mode = "w")
    cleanedFile.write("STATE,AGE,YEAR,VACC RATE,LL,UL,CI,SAMPLE SIZE,OUTBREAK\n")
    teenLines = teenFile.readlines()
    childLines = childFile.readlines()
    teenYears = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
             2016, 2017]
    childYears = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
                  2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
                  2014, 2015, 2016, 2017]
    for i in range(1, len(childLines)):
        values = childLines[i].strip("\n").split(",")
        state = values[0]
        for j in range(0, len(childYears)):
            datapoint = str(i) + ",0," +  str(childYears[j]) + "," + values[(j*5)+1] + \
            "," + values[(j*5)+2] + "," + values[(j*5)+3]
            confidence = values[(j*5)+4].strip("(").strip(")").strip("±")
            datapoint = datapoint + "," + confidence + "," + values[(j*5)+5]
            if (str(childYears[j]) in outbreaks.keys()):
                if (state in outbreaks[str(childYears[j])]):
                    datapoint = datapoint + ",1\n"
                else:
                    datapoint = datapoint + ",0\n"
            else:
                datapoint = datapoint + ",0\n"
            cleanedFile.write(datapoint)
    for i in range(1, len(teenLines)):
        values = teenLines[i].strip("\n").split(",")
        state = values[0]
        for j in range(0, len(teenYears)):
            datapoint = str(i) + ",1,"  + str(teenYears[j]) + "," + values[(j*5)+1] + \
            "," + values[(j*5)+2] + "," + values[(j*5)+3]
            confidence = values[(j*5)+4].strip("(").strip(")").strip("±")
            datapoint = datapoint + "," + confidence + "," + values[(j*5)+5]
            if (str(teenYears[j]) in outbreaks.keys()):
                if (state in outbreaks[str(teenYears[j])]):
                    datapoint = datapoint + ",1\n"
                else:
                    datapoint = datapoint + ",0\n"
            else:
                datapoint = datapoint + ",0\n"
            cleanedFile.write(datapoint)
    childFile.close()
    teenFile.close()
    cleanedFile.close()


if __name__ == "__main__":
    main()
