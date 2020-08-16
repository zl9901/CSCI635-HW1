


import numpy as np
import time

class invert():

    def __init__(self):
        self.flag=0

    """
    experiment 1 is used to create numpy.random.rand(10,10)
    """
    def experiment1(self):
        array=[]
        start=time.time()
        for _ in range(10000):
            self.flag=0
            """
            try catch clause here is to detect the exception
            when there is a matrix that can not be inverted
            """
            try:
                matrix = np.random.rand(10, 10)
                inv_matrix = np.linalg.inv(matrix)
            except np.linalg.LinAlgError as err:
                if 'Singular matrix' in str(err):
                    self.flag=1
                else:
                    raise
            if self.flag==0:
                array.append(1)
            else:
                array.append(0)
        """
        array is used to calculate the mean and standard deviation
        """
        end=time.time()
        mean=float(sum(array))/10000
        tmp=0.0
        for val in array:
            tmp+=(val-mean)**2
        dev=(tmp/9999)**0.5
        print('total number of invertible matrices is ' + str(sum(array)))
        print('standard deviation is '+str(dev))
        print('mean value is '+str(mean))
        print('elapsed time is '+str(end-start))
        print()


    """
    experiment 2 is used to create numpy.random.randint(2,size=(10,10))
    """
    def experiment2(self):
        array=[]
        start=time.time()
        for _  in range(10000):
            self.flag=0
            """
            try catch clause here is to detect the exception
            when there is a matrix that can not be inverted
            """
            try:
                matrix = np.random.randint(2, size=(10, 10))
                inv_matrix = np.linalg.inv(matrix)
            except np.linalg.LinAlgError as err:
                if 'Singular matrix' in str(err):
                    self.flag=1
                else:
                    raise
            if self.flag == 0:
                array.append(1)
            else:
                array.append(0)
        """
        array is used to calculate the mean and standard deviation
        """
        end=time.time()
        mean = float(sum(array)) / 10000
        tmp = 0.0
        for val in array:
            tmp += (val - mean) ** 2
        dev = (tmp / 9999) ** 0.5
        print('total number of invertible matrices is ' + str(sum(array)))
        print('standard deviation is ' + str(dev))
        print('mean value is ' + str(mean))
        print('elapsed time is ' + str(end - start))
        print()

    """
    experiment 3 is used to create matrices that there should be a 75% chance that
    each entry is 0 and 25% chance that the entry is 1
    """
    def experiment3(self):
        array=[]
        start=time.time()
        for _ in range(10000):
            self.flag=0
            """
            we need to traverse the matrix
            so that we can determine the possibility of each entry
            """
            matrix = np.random.rand(10, 10)
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i,j]>=0.75:
                        matrix[i,j]=1
                    else:
                        matrix[i,j]=0
            """
            try catch clause here is to detect the exception
            when there is a matrix that can not be inverted
            """
            try:
                inv_matrix = np.linalg.inv(matrix)
            except np.linalg.LinAlgError as err:
                if 'Singular matrix' in str(err):
                    self.flag=1
                else:
                    raise
            if self.flag == 0:
                array.append(1)
            else:
                array.append(0)
        """
        array is used to calculate the mean and standard deviation
        """
        end=time.time()
        mean = float(sum(array)) / 10000
        tmp = 0.0
        for val in array:
            tmp += (val - mean) ** 2
        dev = (tmp / 9999) ** 0.5
        print('total number of invertible matrices is ' + str(sum(array)))
        print('standard deviation is ' + str(dev))
        print('mean value is ' + str(mean))
        print('elapsed time is ' + str(end - start))
        print()

    """
    experiment 4 is used to create matrices that there should be a 75% chance that
    each entry is 0 and 25% chance that the entry is a floating point number uniformly distributed
    between 0 and 1
    """
    def experiment4(self):
        array=[]
        start=time.time()
        for _ in range(10000):
            self.flag=0
            """
            we need to traverse the matrix
            so that we can determine the possibility of each entry
            """
            matrix = np.random.rand(10, 10)
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i,j]>=0.75:
                        matrix[i,j]=np.random.uniform(0,1)
                    else:
                        matrix[i,j]=0
            """
            try catch clause here is to detect the exception
            when there is a matrix that can not be inverted
            """
            try:
                inv_matrix = np.linalg.inv(matrix)
            except np.linalg.LinAlgError as err:
                if 'Singular matrix' in str(err):
                    self.flag=1
                else:
                    raise
            if self.flag == 0:
                array.append(1)
            else:
                array.append(0)
        """
        array is used to calculate the mean and standard deviation
        """
        end=time.time()
        mean = float(sum(array)) / 10000
        tmp = 0.0
        for val in array:
            tmp += (val - mean) ** 2
        dev = (tmp / 9999) ** 0.5
        print('total number of invertible matrices is ' + str(sum(array)))
        print('standard deviation is ' + str(dev))
        print('mean value is ' + str(mean))
        print('elapsed time is ' + str(end - start))


obj=invert()
obj.experiment1()
obj.experiment2()
obj.experiment3()
obj.experiment4()



