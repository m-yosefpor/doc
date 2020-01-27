min_w = sp.optimize.minimize( ( lambda w: loss(x,y,np.array([	[w[0],w[1]],[w[2],w[3]]]) , w[4] ) ) , [0.1,0.1,0.1,0.1,0.1] )
print(min_w.x)



sp.linalg.expm(A) # matrix e^A like in quantum mechanics
sp.linalg.sinm(A)
sp.linalg.cosm(A)


