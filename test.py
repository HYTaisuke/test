import numpy as np
class StandardScale:
    def __init__(self):
        self.mean_=None
        self.scale_=None
    def fit(self,X):
        '''根据测试数据X获得数据的均值和误差'''
        assert  X.ndim==2 ,'训练数据为二维的'
        self.mean_=np.array([np.mean(X[:,i]) for i in range(X.shape[1])])
        self.scale_=np.array([np.std(X[:,i]) for i in range(X.shape[1])])
        return self
    def transform(self,X):
        '''将输入的X根据已经得出的均值和方差求得归一化后的数据'''
        assert X.ndim==2
        assert self.mean_ is not None and self.scale_ is not None
        assert X.shape[1] == len(self.mean_)

        resX = np.empty(shape=X.shape,dtype=float)
        for col in rnage(X.shape[1]):
            resX[:,col]=(X[:col]-self.mean_[col])/self.scale_[col]
        return resX
      """加油"""
