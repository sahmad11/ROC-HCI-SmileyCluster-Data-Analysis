import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing


def main():

# Elbow method to compute the average score of the k-means on different k values in the range [1,10]
#The visualization generated helps in selecting the best k value.
	wcss = []
	for i in range(1, 11):
		kmeans = KMeans(n_clusters=i, init='k-means++')
		kmeans.fit(df)
		wcss.append(kmeans.inertia_)
	plt.plot(range(1, 11), wcss)
	plt.title('Elbow Method')
	plt.xlabel('Number of clusters')
	plt.ylabel('WCSS')
	plt.show()

#Used PCA to select the most influencial attributes from the dataset to visualize the clustering results on the best k-value.

	df=pd.DataFrame(pd.read_csv("winequality_white.csv"))
	#df=df.drop(columns=["id","Mammal_Richness"],axis=1)
	kmeans=KMeans(n_clusters=3,init='k-means++').fit(df)
	centroids=kmeans.cluster_centers_
	pca=PCA(2)
	pca.fit(df)
	pca_data=pd.DataFrame(pca.transform(df))
	pca.fit(centroids)
	pca_cen=pd.DataFrame(pca.transform(centroids))
	print(pca_data.head())
	plt.scatter(pca_data[0], pca_data[1], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
	plt.scatter(pca_cen[0], pca_cen[1], c='red', s=50)
	plt.show()

main()

