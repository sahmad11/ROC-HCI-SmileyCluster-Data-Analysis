from zipfile import ZipFile
import os
import re
import glob
import pandas as pd


def getID(name,df,zp,colName):
	temp_df=pd.DataFrame(pd.read_csv(zp))
	rich=temp_df['taxonID'].nunique()
	ind=df.index[df['NEON_Site']== name]
	df.at[ind,colName]=rich
	
def extractFiles(df,file,colName):
	s=glob.glob(r"*2018-07*")
	for i in s:
		name=i[9:13]
		firstPart=i[0:28]
		if ".zip" in i:
			with ZipFile(i, 'r') as zipObj:
				listOfFileNames = zipObj.namelist()
				for fileName in listOfFileNames:
					if firstPart+file in fileName:
						zp=zipObj.extract(fileName)
						getID(name,df,zp,colName)
						break

def main():
	df=pd.DataFrame(pd.read_csv("Sheet 11.csv"))
	print("Select one of the following options for which you want to calculate richness: \n", "1- Beetles \n", "2- Birds \n", "3- Mammals \n")
	choice=int(input(" Enter a number: \n"))

	file=" "
	col=" "
	if(choice==1):
		file='bet_parataxonomistID'
		col='Beetles-Richness (July 2018)' 
	elif choice==2:
		file="brd_countdata"
		col="Bird-Richness (July 2018)"
	elif choice==3:
		file="mam_pertrapnight"
		col="Mammal-Richness (July 2018)"
	else:
		print("Invalid input")
		exit()

	if col not in df.columns:
			df.insert(len(df.columns),"Mammal-Richness (July 2018)","")

	extractFiles(df,file,col)
	df.to_csv(r'Sheet 11.csv',index=False,header=True)

if __name__ == '__main__':
	main()



