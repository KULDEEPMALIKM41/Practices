import pyRAPL

pyRAPL.setup()

csv_output = pyRAPL.outputs.CSVOutput('result.csv')

@pyRAPL.measure(output=csv_output)
def foo():
	# Instructions to be evaluated.
	pass
for _ in range(100):
	foo()
	
csv_output.save()