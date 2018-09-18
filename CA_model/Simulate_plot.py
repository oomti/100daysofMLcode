#Run the simulation
arraysize = 5000, stepnumber= 10000000
results=simulate(arraysize = 5000, stepnumber= 10000000)

#Plot out the results
arraysize = 5000
stepnumber= 10000000
fig, ax = mpl.pyplot.subplots(2,2,figsize=(10,10))
title="The results with " + str(arraysize) + " participants, and " + str(stepnumber) + " steps"
fig.suptitle(title)

hist=ax[0,0].hist(results[0], bins=100)
ax[0,0].set_title("Histogram")
ax[0,0].set_xlabel("Inherent value")
ax[0,0].set_ylabel("Participant count")

ax[0,1].stem(hist[1][0:-1],np.multiply(hist[0],hist[1][0:-1]))
ax[0,1].set_title("Summed value in every bin")
ax[0,1].set_ylabel("Summed Inherent value")
ax[0,1].set_xlabel("Inherent Value")

ax[1,0].plot(sorted(results[0]))
ax[1,0].set_title("Ordered list of participants")
ax[1,0].set_ylabel("Inherent value")
ax[1,0].set_xlabel("Order")

ax[1,1].plot(sorted(results[0]))
ax[1,1].set_title("Log scale Ordered list of participants")
ax[1,1].set_ylabel("Log(Inherent value)")
ax[1,1].set_xlabel("Order")

ax[1,1].set_yscale('log')
