import matplotlib.pyplot as plt
############################################################
plt.plot(x,y,marker='o',markersize=4,c='r')
plt.scatter(x,y,c='r',s=4) c=color = 'g','green'
#####
plt.suptitle('sth')
plt.title('sth')
plt.xlabel('sth')
plt.ylabel('sth')
plt.legend()
############################################################
fig , ax = plt.subplots(2,3,figsize=() )
fig.suptitle()
#####
ax[0].plot(x,y)
ax[1].scatter(x,y)
ax[1].set_title()
ax[0].set_xlabel()
ax[0].set_ylabel()
ax[1].legend()
############################################################
fig = plt.figure() # a ploter object
ax = fig.add_subplot(lll,xlabel=s1, ylabel=s2, title=s3)
ax.plot(x,y)
############################################################
plt.show()
