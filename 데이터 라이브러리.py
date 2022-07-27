data=np,loadtxt('movies/rating,dat',delimiter="::", dtype=np.int64)
data[:5,:]

data.shape

mean_rating_total=data[:,2].mean()
mean_rating_total

user_ids=np.unique(data[:,0])
print(user_ids)
print(len(user_ids))

mean_values=[]
for user_id in user_ids:
    data_for_user=data[data[:,0]==user_id,:]
    value=data_for_user[:,2].mean()
    mean_values.append([user_id,value])

    mean_values[:5]



    mean_array=np.array(mean_values, dtype=np.float32)
    print(mean_array[:5])
    print(mean_arry.shape)

    np.savetxt('movies/result1.csv',mean_array,fmt='%.1f',deli,iter=',')



    movie_ids=np.umiqe(data[:,1])
    print(movie_ids)
    print(len(movie_ids))



    movie_values=[]
    for movie_id in movie_ids:
        data_for_movie=data[data[:,1]==movie_id,:]
        valus=data-for_movie[:,2].mean()
        movie_values.append([movie_id,valus])

movie_values[:5]



mean_array = np.array(mean_values, dtype=np.float32)
print(mean_array[:5])
print(mean_arry.shape)
