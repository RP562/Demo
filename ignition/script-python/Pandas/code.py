def newdataset(my_var):
	import pandas
	mydataset = {cars:["BMW", "Volvo", "Ford"],passings: [3, 7, 2]}
	my_var = pandas.DataFrame(mydataset)
	return my_var
