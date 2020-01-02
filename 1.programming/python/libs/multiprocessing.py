
n_jobs = -1
N = 17_070

if n_jobs == -1: n_jobs = cpu_count()

#N_each = N // n_jobs
#N_first = N_each + N % n_jobs
#N_list = [N_first] + [N_each]*(n_jobs-1)

f=200
N_list = [f]*(N//f)+[N%f]

print([N_list[0] , N_list[1] , sum(N_list) , N , len(N_list) ] )

data_list=[]
with Pool(processes=8) as pool:
    for i,data in enumerate(pool.imap_unordered(my_data_gen,N_list) , 1):
        sys.stderr.write('\rdone {:.2%}  time : {} min , {} s '.format( i/len(N_list) , int(time.time()-t)//60 , int(time.time()-t)%60 ))
        data_list += [data]

data=pd.concat(data_list)
print('')



