import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def DataPrepping(dataset):
    dataset['MSZoning'] = dataset['MSZoning'].map({'RL' : 1, 'RM' : 2, 'C (all)' : 3, 'FV' : 4, 'RH' : 5})

    dataset['LotFrontage'] = dataset['LotFrontage'].fillna(0)

    dataset['Street'] = dataset['Street'].map({'Pave':2, 'Grvl':1})

    dataset['Alley'] = dataset['Alley'].fillna('NA')
    dataset['Alley'] = dataset['Alley'].map({'NA':0, 'Grvl':1, 'Pave':2})

    dataset['LotShape'] = dataset['LotShape'].map({'Reg':4, 'IR1':3, 'IR2':2, 'IR3':1})

    dataset['LandContour'] = dataset['LandContour'].map({'Lvl':4, 'Bnk':3, 'Low':1, 'HLS':2})

    dataset['Utilities'] = dataset['Utilities'].map({'AllPub':1, 'NoSeWa':0})

    dataset['LandSlope'] = dataset['LandSlope'].map({'Gtl':0, 'Mod':1, 'Sev':2})

    dataset['Condition1'] = dataset['Condition1'].map({'Norm':3, 'Feedr':2, 'PosN':4, 'Artery':2, 'RRAe':1, 'RRNn':1, 'RRAn':1, 'PosA':4, 'RRNe':2})

    dataset['Condition2'] = dataset['Condition2'].map({'Norm':3, 'Feedr':2, 'PosN':4, 'Artery':2, 'RRAe':1, 'RRNn':1, 'RRAn':1, 'PosA':4, 'RRNe':2})

    dataset['BldgType'] = dataset['BldgType'].map({'1Fam':1, '2fmCon':2, 'Duplex':2, 'TwnhsE':3, 'Twnhs':3})

    dataset['HouseStyle'] = dataset['HouseStyle'].map({'2Story':2, '1Story':1, '1.5Fin':1.5, '1.5Unf':1.5, 'SFoyer':2, 'SLvl':2, '2.5Unf':2.5,'2.5Fin':2.5})

    dataset['MasVnrArea'] = dataset['MasVnrArea'].fillna(0)

    dataset['ExterQual'] = dataset['ExterQual'].map({'Gd':4, 'TA':3, 'Ex':5, 'Fa':2})

    dataset['ExterCond'] = dataset['ExterCond'].map({'Gd':4, 'TA':3, 'Ex':5, 'Fa':2, 'Po':1})

    dataset['Foundation'] = dataset['Foundation'].map({'PConc':6, 'CBlock':3, 'BrkTil':4, 'Wood':1, 'Slab':5, 'Stone':2})

    dataset['BsmtQual'] = dataset['BsmtQual'].fillna('NA')
    dataset['BsmtQual'] = dataset['BsmtQual'].map({'Gd':4, 'TA':3, 'Ex':5, 'NA':0, 'Fa':2})

    dataset['BsmtCond'] = dataset['BsmtCond'].fillna('NA')
    dataset['BsmtCond'] = dataset['BsmtCond'].map({'Gd':4, 'TA':3, 'Po':1, 'NA':0, 'Fa':2})

    dataset['BsmtExposure'] = dataset['BsmtExposure'].fillna('NA')
    dataset['BsmtExposure'] = dataset['BsmtExposure'].map({'No':0, 'Gd':4, 'Mn':2, 'Av':3, 'NA':0})

    dataset['BsmtFinType1'] = dataset['BsmtFinType1'].fillna('NA')
    dataset['BsmtFinType1'] = dataset['BsmtFinType1'].map({'GLQ':5, 'ALQ':4, 'Unf':0, 'Rec':2, 'BLQ':3, 'NA':0, 'LwQ':1})

    dataset['BsmtFinType2'] = dataset['BsmtFinType2'].fillna('NA')
    dataset['BsmtFinType2'] = dataset['BsmtFinType2'].map({'Unf':0, 'BLQ':3, 'NA':0, 'ALQ':4, 'Rec':2, 'LwQ':1, 'GLQ':5})

    dataset['HeatingQC'] = dataset['HeatingQC'].map({'Ex':5, 'Gd':4, 'TA':3, 'Fa':2, 'Po':1})

    dataset['CentralAir'] = dataset['CentralAir'].map({'Y':1, 'N':0})

    dataset['KitchenQual'] = dataset['KitchenQual'].map({'Gd':4, 'TA':3, 'Ex':5, 'Fa':2})

    dataset['FireplaceQu'] = dataset['FireplaceQu'].fillna('NA')
    dataset['FireplaceQu'] = dataset['FireplaceQu'].map({'NA':0, 'TA':3, 'Gd':4, 'Fa':2, 'Ex':5, 'Po':1})

    dataset['GarageYrBlt'] = dataset['GarageYrBlt'].fillna(0)

    dataset['GarageQual'] = dataset['GarageQual'].fillna('NA')
    dataset['GarageQual'] = dataset['GarageQual'].map({'NA':0, 'TA':3, 'Gd':4, 'Fa':2, 'Ex':5, 'Po':1})

    dataset['GarageCond'] = dataset['GarageCond'].fillna('NA')
    dataset['GarageCond'] = dataset['GarageCond'].map({'NA':0, 'TA':3, 'Gd':4, 'Fa':2, 'Ex':5, 'Po':1})

    dataset['PavedDrive'] = dataset['PavedDrive'].map({'Y':1, 'P':1, 'N':0})

    dataset['PoolQC'] = dataset['PoolQC'].fillna('NA')
    dataset['PoolQC'] = dataset['PoolQC'].map({'NA':0, 'TA':2, 'Gd':3, 'Fa':1, 'Ex':4})

    dataset['Fence'] = dataset['Fence'].fillna('NA')
    dataset['Fence'] = dataset['Fence'].map({'NA':0, 'MnPrv':3, 'GdWo':2, 'GdPrv':4, 'MnWw':1})

    dataset['MiscFeature'] = dataset['MiscFeature'].fillna('NA')
    dataset['MiscFeature'] = dataset['MiscFeature'].map({'NA':0, 'Shed':3, 'Gar2':2, 'Othr':1, 'TenC':5})

    dataset['SaleType'] = dataset['SaleType'].map({'WD':8, 'New':9, 'COD':1, 'ConLD':2, 'ConLI':3, 'CWD':6, 'ConLw':4, 'Con':5, 'Oth':1})

    dataset['SaleCondition'] = dataset['SaleCondition'].map({'Normal':6, 'Abnorml':5, 'Partial':1, 'AdjLand':4, 'Alloca':2, 'Family':3})
    
    dataset = dataset.drop(columns=['LotConfig', 'Neighborhood', 'GarageType', 'GarageFinish', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'Heating', 'Electrical', 'Functional'])
